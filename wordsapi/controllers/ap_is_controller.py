# -*- coding: utf-8 -*-

"""
wordsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from wordsapi.api_helper import APIHelper
from wordsapi.configuration import Server
from wordsapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from wordsapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from wordsapi.models.synonyms_response import SynonymsResponse
from wordsapi.models.word_response import WordResponse
from wordsapi.models.examples_response import ExamplesResponse
from wordsapi.models.frequency_response import FrequencyResponse
from wordsapi.models.definitions_response import DefinitionsResponse
from wordsapi.models.pronunciation_response import PronunciationResponse


class APIsController(BaseController):

    """A Controller to access Endpoints in the wordsapi API."""
    def __init__(self, config):
        super(APIsController, self).__init__(config)

    def synonyms(self,
                 word):
        """Does a GET request to /words/{word}/synonyms.

        Get synonyms of a word.

        Args:
            word (str): The word to search synonyms for.

        Returns:
            SynonymsResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/words/{word}/synonyms')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('word')
                            .value(word)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('RapidAPI-Key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SynonymsResponse.from_dictionary)
        ).execute()

    def word(self,
             word):
        """Does a GET request to /words/{word}.

        Retrieve information about a word. Results can include definitions,
        part of speech, synonyms, related words, syllables, and pronunciation.
        This method is useful to see which relationships are attached to which
        definition and part of speech of a word.

        Args:
            word (str): This is a template parameter that is used to provide
                the word, about which the information is being fetched.

        Returns:
            WordResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/words/{word}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('word')
                            .value(word)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('RapidAPI-Key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WordResponse.from_dictionary)
        ).execute()

    def examples(self,
                 word):
        """Does a GET request to /words/{word}/examples.

        Get examples of how the word is used.

        Args:
            word (str): The word to search the examples for.

        Returns:
            ExamplesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/words/{word}/examples')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('word')
                            .value(word)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('RapidAPI-Key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ExamplesResponse.from_dictionary)
        ).execute()

    def frequency(self,
                  word):
        """Does a GET request to /words/{word}/frequency.

        Expands upon the frequency score returned by the main /words/{word}
        endpoint. Returns zipf, a score indicating how common the word is in
        the English language, with a range of 1 to 7; per Million, the number
        of times the word is likely to appear in a corpus of one million
        English words; and diversity, a 0-1 scale the shows the likelihood of
        the word appearing in an English document that is part of a corpus.

        Args:
            word (str): The word to search frequency for.

        Returns:
            FrequencyResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/words/{word}/frequency')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('word')
                            .value(word)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('RapidAPI-Key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FrequencyResponse.from_dictionary)
        ).execute()

    def definitions(self,
                    word):
        """Does a GET request to /words/{word}/definitions.

        Get definitions of a word, including the part of speech.

        Args:
            word (str): The word to search the definitions for.

        Returns:
            DefinitionsResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/words/{word}/definitions')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('word')
                            .value(word)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('RapidAPI-Key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DefinitionsResponse.from_dictionary)
        ).execute()

    def pronunciation(self,
                      word):
        """Does a GET request to /words/{word}/pronunciation.

        How to pronounce a word, according to the International Phonetic
        Alphabet. May include multiple results if the word is pronounced
        differently depending on its part of speech.

        Args:
            word (str): The word to search pronunciation for.

        Returns:
            PronunciationResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/words/{word}/pronunciation')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('word')
                            .value(word)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('RapidAPI-Key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PronunciationResponse.from_dictionary)
        ).execute()
