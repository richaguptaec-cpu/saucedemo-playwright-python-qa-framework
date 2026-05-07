# Test Cases — SauceDemo

# Login Module Test Cases

| Test Case Name | Precondition | Description | Test Steps | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|---|
| TC_LOGIN_001 | User is on login page | Verify successful login with valid credentials | 1. Enter valid username <br> 2. Enter valid password <br> 3. Click Login button | User redirected to inventory page | High | Automated |
| TC_LOGIN_002 | User is on login page | Verify login with invalid credentials | 1. Enter invalid username <br> 2. Enter invalid password <br> 3. Click Login button | Error message displayed | High | Automated |
| TC_LOGIN_003 | User is on login page | Verify login with empty username | 1. Leave username empty <br> 2. Enter password <br> 3. Click Login button | Validation message displayed | Medium | Automated |
| TC_LOGIN_004 | User is on login page | Verify UI alignment of login page | 1. Open login page <br> 2. Verify logo and input alignment | UI elements aligned properly | Low | Manual |