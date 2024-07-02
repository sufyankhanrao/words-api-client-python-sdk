# -*- coding: utf-8 -*-

"""
wordsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class CustomHeaderAuthentication(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in CustomHeaderAuthentication

        """
        return "CustomHeaderAuthentication: X-RapidAPI-Key is undefined."

    def __init__(self, custom_header_authentication_credentials):
        auth_params = {}
        if custom_header_authentication_credentials is not None \
                and custom_header_authentication_credentials.x_rapid_api_key is not None:
            auth_params["X-RapidAPI-Key"] = custom_header_authentication_credentials.x_rapid_api_key
        super().__init__(auth_params=auth_params)


class CustomHeaderAuthenticationCredentials:

    @property
    def x_rapid_api_key(self):
        return self._x_rapid_api_key

    def __init__(self, x_rapid_api_key):
        if x_rapid_api_key is None:
            raise ValueError('x_rapid_api_key cannot be None')
        self._x_rapid_api_key = x_rapid_api_key

    def clone_with(self, x_rapid_api_key=None):
        return CustomHeaderAuthenticationCredentials(
            x_rapid_api_key or self.x_rapid_api_key)
