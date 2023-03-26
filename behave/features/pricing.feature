Feature: Pricing

Background: SETUP
    Given I click in "Pricing" tab

Scenario: Search for create new blog
    Given I click "8" times in a range
    Then  I verify that the audience number is defined as up to "20,000" members
    And  I verify that the plan prices is according to the ones below
         |plan    | price|
         |creator | 149  |
         |team    | 209  |
         |business| 269  |

