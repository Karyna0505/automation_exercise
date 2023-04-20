## Automation Exercise

This repository contains automated tests written in Python using the Playwright library for testing test cases at https://www.automationexercise.com/test_cases.
The project uses Allure as a test result report, and Slack to automatically send test result notifications. The project is also configured to run tests in parallel on different browsers using CLI arguments and deploy test results to GitHub Pages using GitHub Actions.

### Installation

1.To run the tests, you need to install Python 3.x and the Playwright library.
Clone and checkout the github project:

    git clone https://github.com/Karyna0505/automation_exercise.git
2.To install the Playwright library. Go to the terminal and execute inside the checked out folder, run the following command:

    npm install playwright
3.Install the required dependencies:

    pip install -r requirements.txt
4.Install Playwright and the browser of your choice. For example, to install Chromium:

    python -m playwright install chromium

### How to run the tests
Running a single test file

    pytest tests/test_search_product.py

Running tests in parallel 

     pytest -n 2 --browser chromium
Run the tests with the following command:

    pytest --browser=<browser> --alluredir=<path-to-allure-results-directory>
Replace <browser> with the name of the browser you want to run the tests on, for example, chromium, firefox, or webkit. Replace <path-to-allure-results-directory> with the path to the directory where you want to store the Allure results.

More details how to run on the link https://playwright.dev/python/docs/running-tests
### Allure Report

The reports can be obtained using this command:

    pytest --alluredir=./reports --clean-alluredir
After the tests have run to see the reports use another command

    allure serve reports


        
