Feature: Customer 
  As an admin
  I want to test custome page
  So that he can be use

   Scenario: create new costomer
    Given I am on the Saleor Dashboard in Customer page 
    When I create customer
    Then I should be redirected to the customer details page 

    
  Scenario: delete  costomer
    Given I am on the Saleor Dashboard in Customer page 
    When I delete customer
    Then He should disapear in the custommer list

  Scenario: view costomer
    Given I am on the Saleor Dashboard in Customer page 
    When I search for customer
    Then I sould see the customer 

  Scenario: update costomer
    Given I am on the Saleor Dashboard in Customer page 
    When I modifier customer
    Then I should see the modifications

