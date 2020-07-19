import requests
import pytest

# API is a bridge between server and client machines to exchange information
# APIs are implemented in REST, SOAP format
# We will start with REST format as it is more popularly used
# API responses can be in various formats, most popular format is json
# API consists of a protocol which will be either "http://" or "https://"
# API consists of a 'base url' or server address
# API can optionally have a version number
# API consists of an "endpoint"
# API can have optional parameters or data to be sent with API call, which can include authentication parameters and endpoint parameters
# API authentication can optionally have parameters like username, password, api_key, etc
# API will have request type, which will be http/https verbs, which include get, post, delete, update

# API FUNCTIONAL TEST CASES:
# Verify that api call can be made only with allowed protocol http/https
# If applicable, if authentication is required, then verify ONLY authenticated users are able to make ONLY allowed aPI calls
# Verify that server returns meaningful error message when api call is made with 'expired' api_key
# Verify that server returns meaningful error message when api call is made with 'invalid' api_key
# Verify that server returns meaningful error message when api call is made with 'valid' api_key which does not have the required permission
# verify that server returns meaningful error message when api call is made with restricted request method (hhtp verbs: get, post, update, delete, patch, etc)
# Verify that server returns meaningful error message when api call is made with invalid data / parameters
# Verify that server returns meaningful error message when api call is made with missing required data / parameters
# Verify that server returns valid response when valid api call is made with correct authentication and required data parameters
# Verify that server returns valid response when valid api call is made with correct authentication and required and optional data parameters
# Verify that server returns response in valid format (json, xml, text, etc)
# Verify that server returns response in valida json schema - it is called schema validation
# Verify that server returns response with "correct data" (from database) - it is called data validation or data integrity testing
# Verify that server returns correct response status code
# Verify that server returns correct headers
# Verify that server returns correct content
# Verify that server returns correct cookies
# verify that server returns correct encoding
# verify that server returns correct 'apparent encoding'
# verify that server response history is correct
# verify that server response returns correct permanent redirect status
# verify that server response returns correct redirect status
# verify that server response returns correct reason for status code

# API PERFORMANCE TEST CASE:
# Verify that server response time is within expected range (for e.g 2 milisecond)
# Verify that server response time does not increase when number of requests per second increases to very high numbers
# Verify that server does not timeout without meaningful error message
# Verify that server request does not get ghosted - meaning it never returns a response

Api_Key = "7aebafc56fad6766a234d4f63e1a96b0"
city = "London"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, Api_Key)

response = requests.get(url)

print("response.status_code:")
print("\t" + str(response.status_code))
expected_status_code = 200
assert expected_status_code == response.status_code
assert '200' in str(response.status_code)


print("response.request: ")
print("\t" + str(response.request))
expected_request = "<PreparedRequest [GET]>"
assert expected_request == str(response.request)
assert "<PreparedRequest [GET]>" in str(response.request)


print(response.text)
expected_text = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"},{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":15.07,"feels_like":13.81,"temp_min":14.44,"temp_max":15.56,"pressure":1017,"humidity":87},"visibility":5000,"wind":{"speed":3.1,"deg":350},"rain":{"1h":0.25},"clouds":{"all":90},"dt":1595150862,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1595131572,"sunset":1595189225},"timezone":3600,"id":2643743,"name":"London","cod":200}

