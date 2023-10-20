import sys
import time
import logging
import coloredlogs
import click
import os
from concurrent.futures import ThreadPoolExecutor
from modules import login_detection
from config import settings
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

log_file = 'logs/activity.log'
log_dir = os.path.dirname(log_file)
os.makedirs(log_dir, exist_ok=True)

def get_brave_path():
    return '/usr/bin/brave-browser'

def create_brave_driver():
    brave_path = get_brave_path()
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    return driver

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] - %(message)s')
logger = logging.getLogger('my_security_tool')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
coloredlogs.install(level='DEBUG', logger=logger, fmt='%(asctime)s [%(levelname)s] - %(message)s')

@click.command()
@click.option('--url', help='Target URL')
@click.option('--file', help='Target hosts list file')
@click.option('--proxy', help='Proxy (e.g., http://127.0.0.1:8080)')
@click.option('--login', is_flag=True, help='Run only Login panel Detector')
@click.option('--sqli', is_flag=True, help='Run SQL Injection testing')
@click.option('--category', help='SQL Injection payload category (e.g., generic_sql_injection)')
@click.option('-n', '--inputname', help='Customize actual username input for SQLi scan (default "username")')
@click.option('-t', '--threads', type=int, help='Number of threads (default 30)')
def main(url, file, proxy, login, sqli, category, inputname, threads):
    try:
        if not (url or file):
            logger.error('You must specify either --url or --file.')
            return

        if not (login or sqli):
            logger.error('You must specify either --login or --sqli.')
            return

        user_agent = UserAgent().random

        with ThreadPoolExecutor(max_workers=threads) as executor:
            login_urls = []
            if login:
                login_results = executor.map(
                    login_detection.detect_login_panels,
                    [url],
                    [proxy],
                    [{'User-Agent': user_agent}]
                )

                # Filter out None values and flatten the list
                for sublist in login_results:
                    if sublist is not None:
                        for url in sublist:
                            login_urls.append(url)

            if sqli:
                # Implement SQL injection testing with concurrency
                pass

            if not login_urls:
                logger.warning('No login panels were detected.')

    except Exception as e:
        logger.exception(f'An error occurred: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()
