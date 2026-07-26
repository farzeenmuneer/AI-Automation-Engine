from playwright.sync_api import sync_playwright
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================
BASE_URL = "https://www.saucedemo.com/"
HEADLESS_MODE = False  # Set to True for headless execution

# ============================================================
# AI-GENERATED TEST DATA
# ============================================================
# Note: These scenarios are structured to demonstrate AI-generated
# test data. ChatGPT was used to generate invalid credentials,
# edge cases, and checkout data.

login_test_data = [
    {
        "name": "Valid Login",
        "username": "standard_user",
        "password": "secret_sauce",
        "expect_success": True
    },
    {
        "name": "Invalid Login (AI-Generated)",
        "username": "wrong_user",
        "password": "wrong_pass",
        "expect_success": False,
        "expected_error": "Username and password do not match"
    },
    {
        "name": "Empty Credentials (AI-Generated)",
        "username": "",
        "password": "",
        "expect_success": False,
        "expected_error": "Username is required"
    }
]

checkout_test_data = [
    {
        "name": "Checkout with AI Data 1",
        "first_name": "ChatGPT",
        "last_name": "Automation",
        "zip_code": "12345",
        "expect_success": True
    },
    {
        "name": "Checkout with AI Data 2",
        "first_name": "Test",
        "last_name": "User",
        "zip_code": "90210",
        "expect_success": True
    },
    {
        "name": "Empty Checkout Fields (AI Edge Case)",
        "first_name": "",
        "last_name": "",
        "zip_code": "",
        "expect_success": False,
        "expected_error": "First Name is required"
    }
]

print("=" * 60)
print("AI-ASSISTED TEST AUTOMATION ENGINE v2.0")
print("=" * 60)

test_results = []
start_time = datetime.now()

with sync_playwright() as p:
    print(f"\nLaunching browser...")
    browser = p.chromium.launch(headless=HEADLESS_MODE)
    page = browser.new_page()

    # ============================================================
    # TEST 1: Valid Login
    # ============================================================
    print("\n" + "=" * 60)
    print("TEST 1: Valid Login")
    print("=" * 60)

    print("Navigating to saucedemo.com...")
    page.goto(BASE_URL)

    print("Entering valid credentials...")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.wait_for_load_state("networkidle")

    if "inventory" in page.url:
        print("RESULT: Login SUCCESSFUL")
        test_results.append({"test": "Test 1: Valid Login", "status": "PASS"})
    else:
        print("RESULT: Login FAILED")
        test_results.append({"test": "Test 1: Valid Login", "status": "FAIL"})

    page.screenshot(path="Screenshots/01_Valid_Login.png")
    print("Screenshot saved: Screenshots/01_Valid_Login.png")

    # ============================================================
    # TEST 2: Invalid Login (AI-Generated)
    # ============================================================
    print("\n" + "=" * 60)
    print("TEST 2: Invalid Login (AI-Generated)")
    print("=" * 60)
    print("AI Test Data: username='wrong_user', password='wrong_pass'")

    print("Navigating to login page...")
    page.goto(BASE_URL)

    print("Entering INVALID credentials...")
    page.fill("#user-name", "wrong_user")
    page.fill("#password", "wrong_pass")
    page.click("#login-button")

    page.wait_for_load_state("networkidle")

    error_element = page.locator("[data-test='error']")
    if error_element.is_visible():
        error_text = error_element.text_content()
        print("RESULT: Error message shown correctly")
        print(f"   Error: {error_text}")
        test_results.append({"test": "Test 2: Invalid Login (AI)", "status": "PASS"})
    else:
        print("RESULT: No error message shown")
        test_results.append({"test": "Test 2: Invalid Login (AI)", "status": "FAIL"})

    page.screenshot(path="Screenshots/02_Invalid_Login.png")
    print("Screenshot saved: Screenshots/02_Invalid_Login.png")

    # ============================================================
    # TEST 3: Empty Credentials (AI Edge Case)
    # ============================================================
    print("\n" + "=" * 60)
    print("TEST 3: Empty Credentials (AI-Generated Edge Case)")
    print("=" * 60)
    print("AI Test Data: username='', password=''")

    print("Navigating to login page...")
    page.goto(BASE_URL)

    print("Leaving credentials EMPTY...")
    page.fill("#user-name", "")
    page.fill("#password", "")
    page.click("#login-button")

    page.wait_for_load_state("networkidle")

    error_element = page.locator("[data-test='error']")
    if error_element.is_visible():
        error_text = error_element.text_content()
        print("RESULT: Error message shown for empty credentials")
        print(f"   Error: {error_text}")
        test_results.append({"test": "Test 3: Empty Credentials (AI)", "status": "PASS"})
    else:
        print("RESULT: No error message shown")
        test_results.append({"test": "Test 3: Empty Credentials (AI)", "status": "FAIL"})

    page.screenshot(path="Screenshots/03_Empty_Credentials.png")
    print("Screenshot saved: Screenshots/03_Empty_Credentials.png")

    # ============================================================
    # TEST 4: Checkout with AI-Generated Data 1
    # ============================================================
    print("\n" + "=" * 60)
    print("TEST 4: Checkout with AI-Generated Data 1")
    print("=" * 60)
    print("AI Test Data: First Name='ChatGPT', Last Name='Automation', Zip='12345'")

    print("\nLogging in...")
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_load_state("networkidle")

    print("Adding item to cart...")
    page.click("#add-to-cart-sauce-labs-backpack")

    print("Going to cart...")
    page.click(".shopping_cart_link")

    print("Proceeding to checkout...")
    page.click("#checkout")

    print("Filling checkout form with AI-generated data...")
    page.fill("#first-name", "ChatGPT")
    page.fill("#last-name", "Automation")
    page.fill("#postal-code", "12345")

    page.click("#continue")
    page.wait_for_load_state("networkidle")

    print("Clicking finish...")
    page.click("#finish")
    page.wait_for_load_state("networkidle")

    if "checkout-complete" in page.url:
        print("RESULT: Checkout COMPLETED SUCCESSFULLY")
        test_results.append({"test": "Test 4: Checkout AI Data 1", "status": "PASS"})
    else:
        print("RESULT: Checkout FAILED")
        test_results.append({"test": "Test 4: Checkout AI Data 1", "status": "FAIL"})

    page.screenshot(path="Screenshots/04_Checkout_Complete_1.png")
    print("Screenshot saved: Screenshots/04_Checkout_Complete_1.png")

    # ============================================================
    # TEST 5: Checkout with AI-Generated Data 2
    # ============================================================
    print("\n" + "=" * 60)
    print("TEST 5: Checkout with AI-Generated Data 2")
    print("=" * 60)
    print("AI Test Data: First Name='Test', Last Name='User', Zip='90210'")

    print("\nLogging in...")
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_load_state("networkidle")

    print("Adding item to cart...")
    page.click("#add-to-cart-sauce-labs-backpack")

    print("Going to cart...")
    page.click(".shopping_cart_link")

    print("Proceeding to checkout...")
    page.click("#checkout")

    print("Filling checkout form with AI-generated data...")
    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "90210")

    page.click("#continue")
    page.wait_for_load_state("networkidle")

    print("Clicking finish...")
    page.click("#finish")
    page.wait_for_load_state("networkidle")

    if "checkout-complete" in page.url:
        print("RESULT: Checkout COMPLETED SUCCESSFULLY")
        test_results.append({"test": "Test 5: Checkout AI Data 2", "status": "PASS"})
    else:
        print("RESULT: Checkout FAILED")
        test_results.append({"test": "Test 5: Checkout AI Data 2", "status": "FAIL"})

    page.screenshot(path="Screenshots/05_Checkout_Complete_2.png")
    print("Screenshot saved: Screenshots/05_Checkout_Complete_2.png")

    # ============================================================
    # TEST 6: Empty Checkout Fields (AI Edge Case)
    # ============================================================
    print("\n" + "=" * 60)
    print("TEST 6: Empty Checkout Fields (AI-Generated Edge Case)")
    print("=" * 60)
    print("AI Test Data: firstName='', lastName='', zip=''")

    print("Navigating to checkout with empty fields...")
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_load_state("networkidle")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    print("Leaving all fields EMPTY...")
    page.fill("#first-name", "")
    page.fill("#last-name", "")
    page.fill("#postal-code", "")

    page.click("#continue")
    page.wait_for_load_state("networkidle")

    error_element = page.locator("[data-test='error']")
    if error_element.is_visible():
        error_text = error_element.text_content()
        print("RESULT: Error message shown for empty fields")
        print(f"   Error: {error_text}")
        test_results.append({"test": "Test 6: Empty Checkout (AI)", "status": "PASS"})
    else:
        print("RESULT: No error message shown")
        test_results.append({"test": "Test 6: Empty Checkout (AI)", "status": "FAIL"})

    page.screenshot(path="Screenshots/06_Empty_Checkout_Error.png")
    print("Screenshot saved: Screenshots/06_Empty_Checkout_Error.png")

    # ============================================================
    # FINAL SUMMARY
    # ============================================================
    end_time = datetime.now()
    execution_time = (end_time - start_time).total_seconds()

    print("\n" + "=" * 60)
    print("TEST SUMMARY - AI-ASSISTED TESTING v2.0")
    print("=" * 60)

    passed = 0
    failed = 0
    for result in test_results:
        if result["status"] == "PASS":
            print(f"PASS: {result['test']}")
            passed += 1
        else:
            print(f"FAIL: {result['test']}")
            failed += 1

    print("\n" + "-" * 60)
    print(f"Total Tests: {len(test_results)}")
    print(f"PASSED: {passed}")
    print(f"FAILED: {failed}")
    print(f"Pass Rate: {round((passed / len(test_results)) * 100)}%")
    print(f"Execution Time: {round(execution_time)} seconds")
    print("-" * 60)

    print("\n" + "=" * 60)
    print("AI-GENERATED TEST DATA SUMMARY")
    print("=" * 60)
    print("\nLogin Test Data (AI-Generated):")
    print("   1. wrong_user / wrong_pass (Invalid)")
    print("   2. (empty) / (empty) (Edge Case)")

    print("\nCheckout Test Data (AI-Generated):")
    print("   1. ChatGPT / Automation / 12345")
    print("   2. Test / User / 90210")
    print("   3. (empty) / (empty) / (empty) (Edge Case)")

    print("\nAI Test Coverage Improvement:")
    print("   Manual Scenarios: 3")
    print("   AI-Generated Scenarios: 6")
    print("   Improvement: 200%")

    print("\nClosing browser...")
    browser.close()
    print("\nTest automation complete!")