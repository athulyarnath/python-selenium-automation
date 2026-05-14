Feature: Q1 Update Target product search test case and add Behave variables

  Scenario: Target Single Product Search
    Given Open Target Home page in browser
    When Sign in for the best experience popup is open
    Then Close the popup
    When Search for tea from results page
    Then Verify search results for tea is displayed
    Then Verify products are listing with name and image

  Scenario Outline: Target Product Search for multiple products
    Given Open Target Home page in browser
    When Sign in for the best experience popup is open
    Then Close the popup
    When Search for <product> from main page
    Then Verify search results for <expected_product> is shown
    Examples:
      | product | expected_product |
      | Coffee  | Coffee           |
      | Tea     | Tea              |
      | Mouse   | Mouse            |


  Scenario: Q3-Target Product Search for wireless mouse
    Given Open Target Home page in browser
    When Sign in for the best experience popup is open
    Then Close the popup
    When Search for Wireless Mouse from product search
    Then Verify search results for Wireless Mouse is shown from product search
    When Add first wireliess mouse to cart by clicking add to cart button
    Then Choose options Navigation bar will be shown
    When Click on Add to Cart from Navigation bar
    Then Added to cart option will be shown in Navigation bar
    When Click on View Cart button from navigation bar
    Then Cart option will be shown on the screen

  Scenario: Selecting multiple options
    Given Open target Product details page
    Then User can click different color options from details page
    Then User can click on fulfillment options

# Scenarios for Lesson 6 Homeworks
  Scenario: Target Single Product Search with POM
    Given Open Target main page
    When Best experience sign in popup is open
    Then Close best experience popup
    When Search for coffe from header
    Then Verify search results displays coffee
    Then Verify coffees are showing with name and image

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target main page
    When Click on Cart Icon from header
    Then Verify 'Your cart is empty' is shown