
# Custom Header Signature



Documentation for accessing and setting credentials for RapidAPI-Key.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| X-RapidAPI-Key | `str` | This is an API key from RapidAPI. | `x_rapid_api_key` |



**Note:** Auth credentials can be set using `CustomHeaderAuthenticationCredentials` object, passed in as named parameter `custom_header_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = WordsapiClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials()
)
```


