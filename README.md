# Playwright Python SauceDemo QA Framework

## Project Overview
This project demonstrates a complete QA workflow using the SauceDemo application as the system under test.

The objective of this project is to showcase:
- Manual QA analysis
- Test scenario identification
- Detailed test case design
- Automation feasibility analysis
- UI test automation using Playwright with Python
- CI/CD integration using GitHub Actions

This repository is being developed following a real-world QA process rather than focusing only on automation scripts.

---

## Application Under Test
- Website: https://www.saucedemo.com/

---

## Tech Stack
- Python
- Playwright
- Pytest
- GitHub Actions
- Page Object Model (POM)

---

## CI/CD Integration

This project uses GitHub Actions for Continuous Integration (CI).

### Workflow Features
- Automated test execution on push and pull requests
- Cross-browser Playwright support
- HTML test report generation
- Artifact upload for test execution reports

---

## Current Project Status
### Completed
- Project setup
- Test scenarios documentation
- Login module test cases
- Product module test cases
- Cart module test cases
- Checkout module test cases
- Playwright framework setup
- Login module automation
- Product module automation
- Cart module automation
- Checkout module automation
- CI/CD pipeline integration
- HTML reporting
- Screenshot Capture on Failure


### In Progress


### Planned GitHub Actions Features
- parallel browser execution
- Slack/MS Teams notifications

---

## Repository Structure

```text
saucedemo-playwright-python-qa-framework/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   ├── __init__.py
│   └── config.py
│
├── .github/
│   └── workflows/
│       └── playwright.yml
|
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
---

## QA Process Followed
1. Requirement understanding
2. Test scenario identification
3. Test case preparation
4. Automation feasibility analysis
5. Automation framework implementation
6. CI/CD integration

---

## Author
Richa