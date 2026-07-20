## Assignment 8 – cypress issue troubleshooting

---

### Scenario

### A Cypress automation script fails with the following observations:

-  Login page opens successfully.
-  Username and password are entered.
-  Login button is clicked.
-  Dashboard is not displayed.
-  Backend API returns HTTP 500 Internal Server Error.

---

#### 1. Is the issue likely in the UI or the backend?

The issue is in the backend. the `HTTP 500 Internal Server Error` reports a backend server error.

---

#### 2. Which Cypress feature would help confirm your conclusion?

- cy.intercept() – To intercept an API request in a web page

---

#### 3. What evidence would you collect before reporting the issue?

Intercept logs (status, body), request payload, browser console logs, screenshots, video, server logs, and environment details.

---
