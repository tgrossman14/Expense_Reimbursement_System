Feature: New reimbursement

  Background: A user is on the employee dashboard page
    Given a user is on the employee dashboard page and in an employee session

  Scenario: A user is posting a new reimbursement with a valid amount and reason
    When a user has submitted a reimbursement with a valid dollar amount and a valid reason
    Then the reimbursement appears in their list of reimbursements
