# Test Cases — SauceDemo

# Login Module Test Cases

| Test Case Name | Precondition | Description | Test Steps | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|---|
| TC_LOGIN_001 | User is on login page | Verify successful login with valid credentials | 1. Enter valid username <br> 2. Enter valid password <br> 3. Click Login button | User redirected to inventory page | High | Automated |
| TC_LOGIN_002 | User is on login page | Verify login with invalid credentials | 1. Enter invalid username <br> 2. Enter invalid password <br> 3. Click Login button | Error message displayed | High | Automated |
| TC_LOGIN_003 | User is on login page | Verify login with empty username | 1. Leave username empty <br> 2. Enter password <br> 3. Click Login button | Validation message displayed | Medium | Automated |
| TC_LOGIN_004 | User is on login page | Verify login with empty password | 1. Enter username <br> 2. Leave password empty <br> 3. Click Login button | Validation message displayed | Medium | Automated |
| TC_LOGIN_005 | User is on login page | Verify locked user cannot login | 1. Enter locked user credentials <br> 2. Click Login button | Locked user error message displayed | High | Automated |
| TC_LOGIN_006 | User is on login page | Verify username field visibility | 1. Open login page <br> 2. Observe username field | Username field visible | Low | Automated |
| TC_LOGIN_007 | User is on login page | Verify password field visibility | 1. Open login page <br> 2. Observe password field | Password field visible | Low | Automated |
| TC_LOGIN_008 | User is on login page | Verify login button visibility | 1. Open login page <br> 2. Observe login button | Login button visible and enabled | Low | Automated |
| TC_LOGIN_009 | User is on login page | Verify error message cleared after successful login | 1. Login with invalid credentials <br> 2. Verify error displayed <br> 3. Login with valid credentials | User logged in successfully and error removed | Medium | Automated |
| TC_LOGIN_010 | User is on login page | Verify password field is masked | 1. Enter password in password field | Password characters hidden/masked | Low | Automated |

---

# Product Module Test Cases

| Test Case Name | Precondition | Description | Test Steps | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|---|
| TC_PRODUCT_001 | User logged into application | Verify product list displayed successfully | 1. Login with valid credentials <br> 2. Observe inventory page | Product list displayed correctly | High | Automated |
| TC_PRODUCT_002 | User logged into application | Verify product details displayed correctly | 1. Login to application <br> 2. Verify product name, image, description, and price | Product details displayed correctly | Medium | Automated |
| TC_PRODUCT_003 | User logged into application | Verify product sorting by name | 1. Login to application <br> 2. Select sorting option "Name (A to Z)" | Products sorted alphabetically | Medium | Automated |
| TC_PRODUCT_004 | User logged into application | Verify product sorting by price | 1. Login to application <br> 2. Select sorting option "Price (Low to High)" | Products sorted by ascending price | Medium | Automated |
| TC_PRODUCT_005 | User logged into application | Verify product details page opens correctly | 1. Login to application <br> 2. Click on a product name | Product details page displayed | Medium | Automated |
| TC_PRODUCT_007 | User logged into application | Verify all product images load successfully | 1. Login to application <br> 2. Observe all product images on inventory page | All product images displayed correctly | Medium | Automated |
| TC_PRODUCT_008 | User logged into application | Verify product count remains unchanged after sorting | 1. Login to application <br> 2. Capture initial product count <br> 3. Apply sorting option <br> 4. Capture updated product count | Product count remains unchanged | Medium | Automated |
| TC_PRODUCT_009 | User logged into application | Verify sorting products by price high to low | 1. Login to application <br> 2. Select sorting option "Price (High to Low)" | Products sorted by descending price | Medium | Automated |
| TC_PRODUCT_010 | User logged into application | Verify sorting products by name Z to A | 1. Login to application <br> 2. Select sorting option "Name (Z to A)" | Products sorted in reverse alphabetical order | Medium | Automated |

---

# Cart Module Test Cases

| Test Case Name | Precondition | Description | Test Steps | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|---|
| TC_CART_001 | User logged into application | Verify user can add product to cart | 1. Login to application <br> 2. Click Add to Cart button for a product | Product added successfully to cart | High | Automated |
| TC_CART_002 | Product already added to cart | Verify user can remove product from cart | 1. Navigate to cart page <br> 2. Click Remove button | Product removed from cart | High | Automated |
| TC_CART_003 | User logged into application | Verify cart badge count updates correctly | 1. Add product to cart <br> 2. Observe cart badge count | Cart badge count updated correctly | Medium | Automated |
| TC_CART_004 | Product added to cart | Verify products displayed correctly in cart page | 1. Add product to cart <br> 2. Open cart page | Correct products displayed in cart | High | Automated |
| TC_CART_005 | User on cart page | Verify Continue Shopping button functionality | 1. Open cart page <br> 2. Click Continue Shopping button | User redirected to inventory page | Low | Automated |

---

# Checkout Module Test Cases

| Test Case Name | Precondition | Description | Test Steps | Expected Result | Priority | Automation Status |
|---|---|---|---|---|---|---|
| TC_CHECKOUT_001 | Product added to cart | Verify successful checkout process | 1. Add product to cart <br> 2. Open cart <br> 3. Click Checkout <br> 4. Enter checkout information <br> 5. Complete checkout | Order completed successfully | High | Automated |
| TC_CHECKOUT_002 | Product added to cart | Verify validation for empty first name | 1. Open checkout page <br> 2. Leave first name empty <br> 3. Enter remaining details <br> 4. Click Continue | Validation message displayed | Medium | Automated |
| TC_CHECKOUT_003 | Product added to cart | Verify validation for empty last name | 1. Open checkout page <br> 2. Leave last name empty <br> 3. Enter remaining details <br> 4. Click Continue | Validation message displayed | Medium | Automated |
| TC_CHECKOUT_004 | Product added to cart | Verify validation for empty postal code | 1. Open checkout page <br> 2. Leave postal code empty <br> 3. Click Continue | Validation message displayed | Medium | Automated |
| TC_CHECKOUT_005 | User on checkout page | Verify checkout cancellation | 1. Start checkout process <br> 2. Click Cancel button | User redirected to cart or inventory page | Low | Automated |
| TC_CHECKOUT_006 | User on checkout overview page | Verify checkout summary information | 1. Complete checkout information <br> 2. Open checkout overview page | Correct order summary displayed | Medium | Automated |