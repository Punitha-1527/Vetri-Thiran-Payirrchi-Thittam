# Performance Testing

**Project:** EduGenie – Your Smart Budget & Recommendation Assistant  
**Team ID:** SWTID-2026-5933  
**Tested By:** Shameem S (with Punitha K, Madhan, Haridha)

> The target values below are acceptance limits. Replace them with the values you measure when you run the tests.

## Performance Parameters

| S.No | Parameter | Target Value |
|---|---|---|
| 1 | Page load time | Under 3 seconds |
| 2 | Expense categorisation accuracy | At least 85 percent on test data |
| 3 | Forecast error (MAPE) | Under 20 percent |
| 4 | Category prediction response time | Under 1 second |
| 5 | AI recommendation response time | Under 8 seconds |
| 6 | Login API response time | Under 1 second |
| 7 | Concurrent users supported | At least 20 |
| 8 | Error rate | Under 2 percent |

## Functional Test Cases

| Test Case ID | Feature | Test Scenario | Expected Result |
|---|---|---|---|
| TC-01 | Registration | Register with valid details | Account is created |
| TC-02 | Login | Log in with wrong password | Error message is shown |
| TC-03 | Expense Tracking | Add an expense of 250 for "Movie ticket" | Expense is saved and listed |
| TC-04 | Expense Tracking | Submit a negative amount | Validation message is shown |
| TC-05 | Auto Categorisation | Enter "Zomato dinner" | Category is predicted as Food |
| TC-06 | Budget Planner | Spend over 80 percent of a category limit | Alert is displayed |
| TC-07 | Spending Forecast | Open forecast with at least 3 months of data | Forecast chart is displayed |
| TC-08 | AI Recommendations | Request tips after adding expenses | Tips relate to the user's top categories |
| TC-09 | Budget Chat | Ask "Can I afford a 5000 purchase?" | Answer uses remaining budget |
| TC-10 | Security | Open a protected page without login | Access is denied |
