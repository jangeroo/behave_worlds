@mj
Feature: Cash withdrawal

  Scenario: Successful withdrawal from an account in credit
    Given I have deposited '$100' into my account
    When I withdraw '$20'
    Then '$20' should be dispensed
    And I should have '$80' left in my account
