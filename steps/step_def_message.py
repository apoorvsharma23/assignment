from behave import given, when, then, step
import requests

global_general_variables = {}
http_auth = ['MAODUZYTQ0Y2FMYJBLOW','Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1']
http_request_header = {}
http_request_url_query_param = {}
numbers = []
numbers_to_call = {}
message_uuids = []
message_details = {}
rate_details = {}

@given(u'Set BaseURI as "{base_URI}"')
def step_impl(context, base_URI):
    global_general_variables['base_URI'] = base_URI

@given(u'Set Numbers api endpoint as "{numbers_api_endpoint}"')
def step_impl(context, numbers_api_endpoint):
    global_general_variables['numbers_api_endpoint'] = numbers_api_endpoint

@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type

@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type

@when(u'Set Empty Query params')
def step_impl(context):
        http_request_url_query_param.clear()

@when(u'Raise GET HTTP request for numbers')
def step_impl(context):
    url_temp = global_general_variables['base_URI']
    url_temp += global_general_variables['numbers_api_endpoint']
    global_general_variables['number_api_response'] = requests.get(url_temp,auth=(http_auth[0],http_auth[1]),headers=http_request_header)


@then(u'Valid HTTP response should be received from numbers API')
def step_impl(context):
    if None in global_general_variables['number_api_response']:
        assert False, 'Null response received'

@then(u'Response http code should be {numbers_expected_response_code:d} from numbers API')
def step_impl(context, numbers_expected_response_code):
    global_general_variables['numbers_expected_response_code'] = numbers_expected_response_code
    actual_response_code = global_general_variables['number_api_response'].status_code
    if str(actual_response_code) not in str(numbers_expected_response_code):
        print (str(global_general_variables['number_api_response'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response HEADER content type should be "{numbers_expected_response_content_type}" from numbers API')
def step_impl(context, numbers_expected_response_content_type):
    global_general_variables['numbers_expected_response_content_type'] = numbers_expected_response_content_type
    actual_response_content_type = global_general_variables['number_api_response'].headers['Content-Type']
    if numbers_expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty from numbers API')
def step_impl(context):
    if None in global_general_variables['number_api_response']:
        assert False, '***ERROR:  Null or none response body received'

@then(u'Retrieve two numbers from response')
def step_impl(context):
    current_json = global_general_variables['number_api_response'].json()
    for obj in current_json["objects"]:
            numbers.append(obj.get("number"))
    numbers_to_call['number_from'] = numbers[1]
    print (numbers_to_call['number_from'])
    numbers_to_call['number_to'] = numbers[2]
    print (numbers_to_call['number_to'])


@given(u'Set Message api endpoint as "{message_api_endpoint}"')
def step_impl(context, message_api_endpoint):
    global_general_variables['message_api_endpoint'] = message_api_endpoint

@when(u'Set message to send as "{query_param1}"')
def step_impl(context, query_param1):
        http_request_url_query_param.clear()
        http_request_url_query_param['src'] = numbers_to_call['number_from']
        http_request_url_query_param['dst'] = numbers_to_call['number_to']
        http_request_url_query_param['text'] = query_param1

@when(u'Raise POST HTTP request for sending message')
def step_impl(context):
    url_temp = global_general_variables['base_URI']
    url_temp += global_general_variables['message_api_endpoint']
    global_general_variables['message_api_response'] = requests.post(url_temp,auth=(http_auth[0], http_auth[1]),headers=http_request_header,params=http_request_url_query_param)

@then(u'Valid HTTP response should be received from message API')
def step_impl(context):
    if None in global_general_variables['message_api_response']:
        assert False, 'Null response received'

@then(u'Response http code should be {message_expected_response_code:d} from message API')
def step_impl(context, message_expected_response_code):
    global_general_variables['message_expected_response_code'] = message_expected_response_code
    actual_response_code = global_general_variables['message_expected_response_code'].status_code
    if str(actual_response_code) not in str(message_expected_response_code):
        print (str(global_general_variables['message_api_response'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response HEADER content type should be "{message_expected_response_content_type}" from message API')
def step_impl(context, message_expected_response_content_type):
    global_general_variables['message_expected_response_content_type'] = message_expected_response_content_type
    actual_response_content_type = global_general_variables['message_api_response'].headers['Content-Type']
    if message_expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type

@then(u'Response BODY should not be null or empty from message API')
def step_impl(context):
    if None in global_general_variables['message_api_response']:
        assert False, '***ERROR:  Null or none response body received'

@then(u'Retrieve message uuid for the message')
def step_impl(context):
        current_json = global_general_variables['message_api_response'].json()
        message_uuids.append(current_json.get("message_uuid"))
        message_details['message_uuid'] = message_uuids[0]
        print (message_details['message_uuid'])


@given(u'Set message details api endpoint as "{message_details_api_endpoint}"')
def step_impl(context, message_details_api_endpoint):
    global_general_variables['message_details_api_endpoint'] = message_details_api_endpoint

@when(u'Raise GET HTTP request for message details')
def step_impl(context):
    url_temp = global_general_variables['base_URI']
    url_temp += global_general_variables['message_details_api_endpoint']
    url_temp += message_details['message_uuid']
    global_general_variables['message_details_response'] = requests.get(url_temp,auth=(http_auth[0], http_auth[1]),headers=http_request_header)

@then(u'Valid HTTP response should be received from message details API')
def step_impl(context):
    if None in global_general_variables['message_details_response']:
        assert False, 'Null response received'


@then(u'Response http code should be {expected_response_code:d} from message details API')
def step_impl(context, expected_response_code):
    global_general_variables['message_details_expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['message_details_response'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['message_details_response'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response http code should be {message_details_expected_response_code:d} from message API')
def step_impl(context, message_details_expected_response_code):
    global_general_variables['message_details_expected_response_code'] = message_details_expected_response_code
    actual_response_code = global_general_variables['message_details_response'].status_code
    if str(actual_response_code) not in str(message_details_expected_response_code):
        print (str(global_general_variables['message_api_response'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response HEADER content type should be "{message_details_expected_response_content_type}" from message details API')
def step_impl(context, message_details_expected_response_content_type):
    global_general_variables['message_details_expected_response_content_type'] = message_details_expected_response_content_type
    actual_response_content_type = global_general_variables['message_details_response'].headers['Content-Type']
    if message_details_expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type

@then(u'Response BODY should not be null or empty from message details API')
def step_impl(context):
    if None in global_general_variables['message_details_response']:
        assert False, '***ERROR:  Null or none response body received'

@then(u'Retrieve message details')
def step_impl(context):
    current_json = global_general_variables['message_details_response'].json()
    message_details['total_rate']=current_json.get("total_rate")
    print message_details['total_rate']
    message_details['total_amount']=current_json.get("total_amount")
    print message_details['total_amount']

@given(u'Set pricing details api endpoint as "{pricing_details_api_endpoint}"')
def step_impl(context, pricing_details_api_endpoint):
    global_general_variables['Pricing_api_endpoint'] = pricing_details_api_endpoint

@when(u'Set country iso code as params "{query_param1}"')
def step_impl(context, query_param1):
        http_request_url_query_param.clear()
        http_request_url_query_param['country_iso'] = query_param1


@when(u'Raise GET HTTP request for pricing details')
def step_impl(context):
        url_temp = global_general_variables['base_URI']
        url_temp += global_general_variables['Pricing_api_endpoint']
        global_general_variables['pricing_api_response'] = requests.get(url_temp,auth=(http_auth[0], http_auth[1]),headers=http_request_header,params=http_request_url_query_param)
@then(u'Valid HTTP response should be received from pricing API')
def step_impl(context):
    if None in global_general_variables['pricing_api_response']:
        assert False, 'Null response received'


@then(u'Response http code should be {expected_response_code:d} from pricing API')
def step_impl(context, expected_response_code):
    global_general_variables['pricing_expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['pricing_api_response'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['pricing_api_response'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{pricing_details_expected_response_content_type}" from pricing API')
def step_impl(context, pricing_details_expected_response_content_type):
    global_general_variables['message_details_expected_response_content_type'] = pricing_details_expected_response_content_type
    actual_response_content_type = global_general_variables['pricing_api_response'].headers['Content-Type']
    if pricing_details_expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type

@then(u'Response BODY should not be null or empty from pricing API')
def step_impl(context):
    if None in global_general_variables['pricing_api_response']:
        assert False, '***ERROR:  Null or none response body received'


@then(u'Retrieve pricing details')
def step_impl(context):
        current_json = global_general_variables['pricing_api_response'].json()
        rate_details['outbound_rate'] = current_json.get("message").get("outbound").get("rate")
        print rate_details['outbound_rate']

@when(u'Rate and price deducted for the sending message is compared with pricing')
def step_impl(context):
        print "Comparing rate with price deducted for sending message"

@then(u'Rates and price should match')
def step_impl(context):
    assert (rate_details['outbound_rate'] == message_details['total_rate']), 'Rates Not matching'

@given(u'Set account details api endpoint as "{account_details_api_endpoint}"')
def step_impl(context, account_details_api_endpoint):
    global_general_variables['account_details_api_endpoint'] = account_details_api_endpoint

@when(u'Raise GET HTTP request for account details')
def step_impl(context):
    url_temp = global_general_variables['base_URI']
    url_temp += global_general_variables['account_details_api_endpoint']
    global_general_variables['account_details_response'] = requests.get(url_temp,auth=(http_auth[0], http_auth[1]),headers=http_request_header)

@then(u'Valid HTTP response should be received from account details API')
def step_impl(context):
    if None in global_general_variables['account_details_response']:
        assert False, 'Null response received'

@then(u'Response http code should be {account_expected_response_code:d} from account details API')
def step_impl(context, account_expected_response_code):
    global_general_variables['numbers_expected_response_code'] = account_expected_response_code
    actual_response_code = global_general_variables['account_details_response'].status_code
    if str(actual_response_code) not in str(account_expected_response_code):
        print (str(global_general_variables['account_details_response'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@then(u'Response HEADER content type should be "{account_expected_response_content_type}" from account details API')
def step_impl(context, account_expected_response_content_type):
    global_general_variables['account_expected_response_content_type'] = account_expected_response_content_type
    actual_response_content_type = global_general_variables['account_details_response'].headers['Content-Type']
    if account_expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty from account details API')
def step_impl(context):
    if None in global_general_variables['account_details_response']:
        assert False, '***ERROR:  Null or none response body received'

@then(u'Verify account cash credit')
def step_impl(context):
    current_json = global_general_variables['account_details_response'].json()
    rate_details['cash_credits'] = current_json.get("cash_credits")
    print rate_details['cash_credits']
    if rate_details['cash_credits']>=message_details['total_amount']:
        assert False, 'Cash credits is not less than deducted amount'
