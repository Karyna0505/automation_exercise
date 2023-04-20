## Automation Exercise

This repository contains automated tests written in Python using the Playwright library for testing test cases at https://www.automationexercise.com/test_cases.
The project uses Allure as a test result report, and Slack to automatically send test result notifications. The project is also configured to run tests in parallel on different browsers using CLI arguments and deploy test results to GitHub Pages using GitHub Actions.

### Installation

1.To run the tests, you need to install Python 3.x and the Playwright library.
Clone and checkout the github project:

    git clone https://github.com/Karyna0505/automation_exercise.git
2.To install the Playwright library. Go to the terminal and execute inside the checked out folder, run the following command:

   python -m pip install --upgrade pip
   
   pip install pipenv
   
   pipenv install --system
   
   playwright install chromium
   
3.Install Playwright and the browser of your choice. For example, to install Chromium:

    python -m playwright install chromium

### How to run the tests
Running a single test file

    pytest tests/test_search_product.py

Running tests in parallel 

     pytest -n 2 

More details how to run on the link https://playwright.dev/python/docs/running-tests
### Allure Report

After the tests have run to see the reports use command

    allure serve reports


        
