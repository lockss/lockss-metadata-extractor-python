# lockss_metadata_extractor.MdupdatesApi

All URIs are relative to *https://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mdupdates**](MdupdatesApi.md#delete_mdupdates) | **DELETE** /mdupdates | Delete all of the currently queued and active jobs
[**delete_mdupdates_jobid**](MdupdatesApi.md#delete_mdupdates_jobid) | **DELETE** /mdupdates/{jobid} | Delete a job
[**get_mdupdates**](MdupdatesApi.md#get_mdupdates) | **GET** /mdupdates | Get a list of currently active jobs
[**get_mdupdates_jobid**](MdupdatesApi.md#get_mdupdates_jobid) | **GET** /mdupdates/{jobid} | Get a job
[**post_mdupdates**](MdupdatesApi.md#post_mdupdates) | **POST** /mdupdates | Perform an AU metadata update operation


# **delete_mdupdates**
> int delete_mdupdates()

Delete all of the currently queued and active jobs

Delete all of the currently queued and active jobs

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
api_instance = lockss_metadata_extractor.MdupdatesApi(lockss_metadata_extractor.ApiClient(configuration))

try:
    # Delete all of the currently queued and active jobs
    api_response = api_instance.delete_mdupdates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdupdatesApi->delete_mdupdates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mdupdates_jobid**
> Job delete_mdupdates_jobid(jobid)

Delete a job

Delete a job given the job identifier, stopping any current processing, if necessary

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
api_instance = lockss_metadata_extractor.MdupdatesApi(lockss_metadata_extractor.ApiClient(configuration))
jobid = 'jobid_example' # str | The identifier of the job to be deleted

try:
    # Delete a job
    api_response = api_instance.delete_mdupdates_jobid(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdupdatesApi->delete_mdupdates_jobid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| The identifier of the job to be deleted | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mdupdates**
> JobPageInfo get_mdupdates(limit=limit, continuation_token=continuation_token)

Get a list of currently active jobs

Get a list of all currently active jobs or a pageful of the list defined by the continuation token and size

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
api_instance = lockss_metadata_extractor.MdupdatesApi(lockss_metadata_extractor.ApiClient(configuration))
limit = 50 # int | The number of jobs per page (optional) (default to 50)
continuation_token = 'continuation_token_example' # str | The continuation token of the next page of jobs to be returned (optional)

try:
    # Get a list of currently active jobs
    api_response = api_instance.get_mdupdates(limit=limit, continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdupdatesApi->get_mdupdates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of jobs per page | [optional] [default to 50]
 **continuation_token** | **str**| The continuation token of the next page of jobs to be returned | [optional] 

### Return type

[**JobPageInfo**](JobPageInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mdupdates_jobid**
> Status get_mdupdates_jobid(jobid)

Get a job

Get a job given the job identifier

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
api_instance = lockss_metadata_extractor.MdupdatesApi(lockss_metadata_extractor.ApiClient(configuration))
jobid = 'jobid_example' # str | The identifier of the requested job

try:
    # Get a job
    api_response = api_instance.get_mdupdates_jobid(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdupdatesApi->get_mdupdates_jobid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| The identifier of the requested job | 

### Return type

[**Status**](Status.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mdupdates**
> Job post_mdupdates(metadata_update_spec)

Perform an AU metadata update operation

Perform an AU metadata update operation given the update specification

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
api_instance = lockss_metadata_extractor.MdupdatesApi(lockss_metadata_extractor.ApiClient(configuration))
metadata_update_spec = lockss_metadata_extractor.MetadataUpdateSpec() # MetadataUpdateSpec | The information defining the AU metadata update operation

try:
    # Perform an AU metadata update operation
    api_response = api_instance.post_mdupdates(metadata_update_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdupdatesApi->post_mdupdates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_update_spec** | [**MetadataUpdateSpec**](MetadataUpdateSpec.md)| The information defining the AU metadata update operation | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

