Feature: Change reimbursement approval

  Background: A user is on the manager dashboard page
    Given a user is on the manager dashboard page and a user is in a manager session

  Scenario: A user is changing reimbursement approval to "approved" before confirming
    When a user clicks the approve button
    Then the reimbursement's approval changes to "approved"

  Scenario: A user is changing the reimbursement approval to "denied" before confirming
    When a user clicks the deny button
    Then the reimbursement's approval changes to "denied"

  Scenario: A user is confirming their reimbursement approval changes
    When a user clicks the confirm approvals button
    Then all reimbursement approval changes are made
