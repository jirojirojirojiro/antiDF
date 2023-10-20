import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# JavaScript code to detect login forms
DETECT_LOGIN_FORM_SCRIPT = """
function detectLoginForm() {
    var form = null;
  
    // recursively navigate to find parent form
    function findForm(elm) {
        if (elm !== null) {
            if (elm.tagName === 'FORM') {
                return elm;
            }
            return findForm(elm.parentNode);
        } else {
            return elm;
        }
    }
    
    var passwdInput = document.querySelectorAll('input[type="password"]');

    // no password fields
    if (passwdInput.length === 0) {
        return null;
    }

    // there might be more than one password field. In that case, the form to be returned 
    // will be the form with ONE and ONLY ONE visible, empty field, that is not 
    // the password field itself
    if (passwdInput.length >= 1) {
        Array.prototype.slice.call(passwdInput, 0).every(function(passwdField) {
            var passwdForm = findForm(passwdField);
            var inputs = passwdForm.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
            var otherVisibleFields = [];
            [].forEach.call(
                inputs,
                function(input) {
                    if (passwdField !== input) {
                        // form is visible and is empty
                        if (input.offsetWidth > 0 && input.offsetHeight > 0 && input.value === '') {
                            otherVisibleFields.push(input);
                        }
                    }
                }
            );

            // there is one visible field additional to a visible password field
            if (otherVisibleFields.length === 1 && passwdField.offsetWidth > 0 && passwdField.offsetHeight > 0) {
                form = passwdForm;
                return false; // found the right form, breaks the loop
            }

            return true; // continues the loop
        });
    }

    return form;
};
"""

def detect_login_panels(urls, proxies, useragent):
    login_urls = []

    for url, proxy, headers in zip(urls, proxies, useragent):

        try:
            req = requests.get(url, headers=headers, proxies=proxy, verify=False, timeout=8, allow_redirects=True)
            response = str(req.content)
            soup = BeautifulSoup(response, "html.parser")
            form_elements = soup.find_all("form")
            action = form_elements[0].attrs.get("action") if form_elements else ""

            if not action or action == "?":
                action = ""
            elif action[0] == "/":
                action = action[1:]

            check = re.search("login", str(req.url))

            if not check:
                action = ""

            if req.status_code == 200:
                for login in LoginDetectionSettings.LOGN_INPUTS:  # Use LoginDetectionSettings
                    try:
                        find = re.compile(login).search(str(response))
                        if find:
                            login_urls.append(req.url + str(action))
                            print(colored("[+] Login panel found! [{}] - {}", "green").format(req.url, req.status_code))
                            break
                    except IndexError:
                        pass

        except IOError:
            pass
        except IndexError:
            pass
        except KeyboardInterrupt:
            print("\nStopped")
            exit(0)

    return login_urls

def detect_and_test_login_forms(urls, payloads, regex_patterns):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = ChromeService(executable_path=settings.CHROMEDRIVER_PATH)  # Use the path from config
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for url in urls:
            driver.get(url)
            login_form = driver.execute_script(DETECT_LOGIN_FORM_SCRIPT)

            if login_form:
                for payload in payloads:
                    username_field = driver.find_element_by_css_selector('input[type="text"]')
                    password_field = driver.find_element_by_css_selector('input[type="password"]')

                    if username_field and password_field:
                        username_field.clear()
                        password_field.clear()

                        username_field.send_keys(payload)
                        password_field.send_keys(payload)

                        # Assume your form has a submit button of type "submit"
                        submit_button = driver.find_element_by_css_selector('input[type="submit"]')
                        submit_button.click()

                        response = driver.page_source

                        if any(re.search(pattern, response) for pattern in regex_patterns):
                            print(f"Payload '{payload}' resulted in a possible error.")
    finally:
        driver.quit()
