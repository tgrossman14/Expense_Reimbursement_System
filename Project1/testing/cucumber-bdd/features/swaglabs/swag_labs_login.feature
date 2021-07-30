# Cucumber-specific file containing scenarios written in Gherkin
# Gherkin- BDD language. Specifies requirements at a very high level.

# Feature- Basic keyword. Denotes what feature is being tested. Feature contains a collection of scenarios.
Feature: Swag Labs Login

    # Background- Used before scenarios, part of feature. Includes steps allowing shared context to all scenarios.
    Background: A user is on the home page and is entering correct username and password
        # Given- Before user has interacted w/ feature
        Given a user is on the home page of Swag Labs
        # And == But- Can break down steps even further
        And a user enters the correct username and the correct password

    # Scenario- Keyword. Denotes the use case scenario under test.
    # Use case- Details specific example of how an end user might engage with the application.
    Scenario: A user is on the home page of Swag Labs and would like to login with correct credentials.
        # Can detail specific steps a user would take using "Cucumber steps"
        # When- Specifies the action a user would take.
        When the user pushes the submit button
        # Then- Specifies the expected result of the user's action
        Then the user is redirected to the dashboard
    # Custom tags can be used for scenarios with @
    Scenario: A user is on the home page of Swag Labs and would like to log in with correct credentials.
        When the user pushes the enter button
        Then the user is redirected to the dashboard page anyway
