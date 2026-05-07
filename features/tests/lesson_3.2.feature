Feature: test cases and using Behavior-Driven Development (BDD)

  Scenario: Cart option shows “Your cart is empty” message is shown in target.com
    Given Open Target Home page
    When Click on Cart Icon
    Then Verify 'Your cart is empty' is displayed

  Scenario: Logged out user can navigate to Sign In page from target.com
    Given Open Target Home page
    When Click Sign In
    Then Verify navigation menu opened on right side
    When Click Sign In from Navigation menu
    Then Verify Sign In form opened


