# lockss_metadata_extractor.StatusApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Get the status of the service


# **get_status**
> ApiStatus get_status()

Get the status of the service

Get the status of the service

### Example
```python
from __future__ import print_function
import time
import lockss_metadata_extractor
from lockss_metadata_extractor.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = lockss_metadata_extractor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lockss_metadata_extractor.StatusApi(lockss_metadata_extractor.ApiClient(configuration))

try:
    # Get the status of the service
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiStatus**](ApiStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

