Feature: MASH Login

    Background: A user is on the login page and is entering an email and password.
        Given a user is on the MASH login page
    
    Scenario: A user is logging in with correct credentials.
        When the user pushes the login button
        Then the user is redirected to the dashboard of the associated employee or manager

    Scenario: A user is logging in with correct credentials.
        When the user pushes the ENTER button
        Then the user is redirected to the dashboard of the associated employee or manager
    
    Scenario: A user is logging in with incorrect credentials.
        When the user pushes the login button
        Then the user is redirected to the login page
    
    Scenario: A user is logging in with incorrect credentials.
        When the user pushes the ENTER button
        Then the user is redirected to the login page