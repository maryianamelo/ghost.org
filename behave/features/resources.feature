Feature: Resources

Background: SETUP
    Given I click in "Resources" tab grid


Scenario: Search for create new blog
    Given I click on "Start here" page
    When  I search for "create new blog"
    And   I click in the "10" th result
    Then  I verify that the article title is correct
