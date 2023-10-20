
# Anti-DF: Web Security Toolkit 🔒

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Login Panel Detection](#running-login-panel-detection)
  - [Running SQL Injection Testing](#running-sql-injection-testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction 🚀

Anti-DF is a powerful web security toolkit designed to help you detect and assess security vulnerabilities in web applications. Whether you're a security professional or a developer, this tool provides a comprehensive set of features to enhance the security of your web applications.

## Features 🛡️

- **Login Panel Detection:** Detect potential login panels on web pages.
- **SQL Injection Testing:** Test web forms for SQL injection vulnerabilities.
- **Concurrency:** Perform tasks with high parallelism for faster scanning.
- **Customization:** Configure User-Agent, proxies, and more.
- **Detailed Logging:** Log and monitor scan results.

## Getting Started 🏁

### Prerequisites 📋

- Python 3.9 or higher
- Chrome browser (for login panel detection)

### Installation 💽

1. Clone the repository:

   ```bash
   git clone https://github.com/jirojirojirojiro/anti-df.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

### Running Login Panel Detection 🔍

To detect login panels on a target URL, run the following command:

```bash
python main.py --url <target_url> --login
```

### Running SQL Injection Testing 💉

To perform SQL injection testing, use the following command:

```bash
python main.py --url <target_url> --sqli --category <payload_category> --inputname <username_input>
```

## Contributing 🤝

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Special thanks to the open-source community for their valuable contributions.
- Inspired by web security professionals and researchers.


