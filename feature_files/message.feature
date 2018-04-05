Feature: One

Background:
	Given Set BaseURI as "http://api.plivo.com/v1/"

Scenario: Use numbers api to get any two numbers.
  Given Set Numbers api endpoint as "Account/MAODUZYTQ0Y2FMYJBLOW/Number/"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Set Empty Query params
	And Raise GET HTTP request for numbers
  Then Valid HTTP response should be received from numbers API
	And Response http code should be 200 from numbers API
	And Response HEADER content type should be "application/json" from numbers API
	And Response BODY should not be null or empty from numbers API
	And Retrieve two numbers from response

  Scenario: Use message api to send an sms from a number to another number
    Given Set Message api endpoint as "Account/MAODUZYTQ0Y2FMYJBLOW/Message"
    When Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Set message to send as "Hello"
	And Raise POST HTTP request for sending message
    Then Valid HTTP response should be received from message API
	And Response HEADER content type should be "application/json" from message API
   	And Response BODY should not be null or empty from message API
	And Retrieve message uuid for the message

  Scenario: Using message uuid get the details of the message using details api.
    Given Set message details api endpoint as "Account/MAODUZYTQ0Y2FMYJBLOW/Message/"
    When Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
	And Raise GET HTTP request for message details
    Then Valid HTTP response should be received from message details API
	And Response http code should be 200 from message details API
	And Response HEADER content type should be "application/json" from message details API
   	And Response BODY should not be null or empty from message details API
	Then Retrieve message details

Scenario: Use pricing api to determine the rate of the message which is outbound rate under message object
    Given Set pricing details api endpoint as "Account/MAODUZYTQ0Y2FMYJBLOW/Pricing"
    When Set HEADER param request content type as "application/json"
	And Set country iso code as params "US"
    And Set HEADER param response accept type as "application/json"
	And Raise GET HTTP request for pricing details
    Then Valid HTTP response should be received from pricing API
	And Response http code should be 200 from pricing API
	And Response HEADER content type should be "application/json" from pricing API
   	And Response BODY should not be null or empty from pricing API
	Then Retrieve pricing details

Scenario: Verify the rate and the price deducted for the sending message, should be same
	When Rate and price deducted for the sending message is compared with pricing
	Then Rates and price should match

Scenario: And finally after sending message, using account details api, account cash credit should be less than by the deducted amount.
	Given Set account details api endpoint as "Account/MAODUZYTQ0Y2FMYJBLOW"
    When Set HEADER param request content type as "application/json"
	And Set Empty Query params
    And Set HEADER param response accept type as "application/json"
	And Raise GET HTTP request for account details
    Then Valid HTTP response should be received from account details API
	And Response http code should be 200 from account details API
	And Response HEADER content type should be "application/json" from account details API
   	And Response BODY should not be null or empty from account details API
	Then Verify account cash credit