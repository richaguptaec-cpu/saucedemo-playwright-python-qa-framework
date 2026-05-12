# Test Scenarios — SauceDemo

## Login Module

### TS_LOGIN_001 — Successful Login
Verify user can login with valid credentials.

### TS_LOGIN_002 — Invalid Login
Verify error message appears when invalid credentials are entered.

### TS_LOGIN_003 — Empty Username
Verify validation message appears when username is empty.

### TS_LOGIN_004 — Empty Password
Verify validation message appears when password is empty.

### TS_LOGIN_005 — Locked User Login
Verify locked user cannot access the application.

### TS_LOGIN_006 — Verify Username Field Visibility
Verify username input field is visible on login page.

### TS_LOGIN_007 — Verify Password Field Visibility
Verify password input field is visible on login page.

### TS_LOGIN_008 — Verify Login Button Visibility
Verify login button is visible and enabled.

### TS_LOGIN_009 — Verify Error Message Disappears After Successful Login
Verify error message is cleared after entering valid credentials and logging in successfully.

### TS_LOGIN_010 — Verify Password Field Is Masked
Verify password field hides entered characters.

---

## Product Module

### TS_PRODUCT_001 — View Product List
Verify product list is displayed after successful login.

### TS_PRODUCT_002 — Verify Product Details
Verify product name, description, and price are displayed correctly.

### TS_PRODUCT_003 — Sort Products by Name
Verify products can be sorted alphabetically.

### TS_PRODUCT_004 — Sort Products by Price
Verify products can be sorted by price.

### TS_PRODUCT_005 — Open Product Details
Verify user can open individual product details page.

### TS_PRODUCT_007 — Verify Product Images Load Successfully
Verify all product images are displayed correctly on inventory page.

### TS_PRODUCT_008 — Verify Product Count After Sorting
Verify total number of displayed products remains unchanged after applying sorting options.

### TS_PRODUCT_009 — Sort Products by Price (High to Low)
Verify products can be sorted by descending price.

### TS_PRODUCT_010 — Sort Products by Name (Z to A)
Verify products can be sorted in reverse alphabetical order.

---

## Cart Module

### TS_CART_001 — Add Product to Cart
Verify user can add product to cart successfully.

### TS_CART_002 — Remove Product from Cart
Verify user can remove product from cart successfully.

### TS_CART_003 — Verify Cart Badge Count
Verify cart badge count updates correctly after adding products.

### TS_CART_004 — Verify Cart Page
Verify selected products are displayed correctly in cart page.

### TS_CART_005 — Continue Shopping
Verify user can navigate back to inventory page using Continue Shopping button.

---

## Checkout Module

### TS_CHECKOUT_001 — Successful Checkout
Verify user can complete checkout successfully.

### TS_CHECKOUT_002 — Checkout with Empty First Name
Verify validation message appears when first name is empty.

### TS_CHECKOUT_003 — Checkout with Empty Last Name
Verify validation message appears when last name is empty.

### TS_CHECKOUT_004 — Checkout with Empty Postal Code
Verify validation message appears when postal code is empty.

### TS_CHECKOUT_005 — Cancel Checkout
Verify user can cancel checkout process successfully.

### TS_CHECKOUT_006 — Verify Checkout Summary
Verify checkout overview page displays correct order information.

---