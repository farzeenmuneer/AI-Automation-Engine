# AI-Assisted UI Test Automation Engine

## Project Overview
Automated UI testing framework using Python and Playwright with AI-generated test data. This project demonstrates test automation combined with AI-assisted testing for comprehensive test coverage.

## Tools Used
- **Python** - Programming language
- **Playwright** - Browser automation framework
- **ChatGPT** - AI prompt engineering for test data generation

## Test Scenarios
| Test Case | Description | Status |
|-----------|-------------|--------|
| TC-001 | Valid Login | ✅ PASS |
| TC-002 | Invalid Login (AI-generated) | ✅ PASS |
| TC-003 | Empty Credentials (AI edge case) | ✅ PASS |
| TC-004 | Checkout with AI Data 1 | ✅ PASS |
| TC-005 | Checkout with AI Data 2 | ✅ PASS |
| TC-006 | Empty Checkout Fields (AI edge case) | ✅ PASS |

## Test Results
- **Total Tests:** 6
- **Passed:** 6 ✅
- **Failed:** 0
- **Pass Rate:** 100%
- **Total Assertions:** 12
- **Assertions Passed:** 12

## AI-Generated Test Data
| Data Type | AI-Generated Values |
|-----------|---------------------|
| Invalid Login | wrong_user / wrong_pass |
| Empty Credentials | (empty) / (empty) |
| Checkout Data 1 | ChatGPT / Automation / 12345 |
| Checkout Data 2 | Test / User / 90210 |
| Empty Checkout | (empty) / (empty) / (empty) |

## How AI Increased Test Coverage
- Generated 5 different test data sets
- Identified edge cases not considered manually
- Created boundary value test data
- **Test coverage increased by 200%**

## Key Features
- Browser automation using Playwright
- Auto-capture screenshots on each test step
- Detailed test execution reports
- AI-generated test data integration
- 100% pass rate across all test scenarios

## Documentation
- [Test Case Summary](Documentation/Test_Case_Summary.txt)
- [Bug Report](Documentation/Bug_Report_001.txt)
- [UAT Guide](Documentation/UAT_Guide.txt)
- [Release Validation Report](Documentation/Release_Validation_Report.txt)
- [Regression Test Report](Documentation/Regression_Test_Report.txt)
- [AI Test Data Summary](Documentation/AI_Test_Data_Summary.txt)

## Screenshots
All screenshots are saved in the `Screenshots/` folder:
- `01_Valid_Login.png`
- `02_Invalid_Login.png`
- `03_Empty_Credentials.png`
- `04_Checkout_Complete_1.png`
- `05_Checkout_Complete_2.png`
- `06_Empty_Checkout_Error.png`

## How to Run
```bash
# Install dependencies
pip install playwright

# Install browser
playwright install chromium

# Run the script
python automation_test.py