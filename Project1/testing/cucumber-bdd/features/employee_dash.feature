Feature: Employee dashboard

    Background: A user is on the employee dashboard page
      Given a user is on the employee dashboard page

    Scenario: A user has not logged in
      When the user tries to access their dashboard without logging in
      Then the user is redirected to the login page

    Scenario: A user has logged in through the login page
      When a user has started an employee session
      Then the user is able to view the employee dashboard
