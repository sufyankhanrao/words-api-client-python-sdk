# -*- coding: utf-8 -*-

"""
wordsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from wordsapi.api_helper import APIHelper


class SynonymsResponse(object):

    """Implementation of the 'SynonymsResponse' model.

    This custom type contains response for synonyms endpoint.

    Attributes:
        word (str): The word that is searched.
        synonyms (List[str]): The synonyms of the searched word.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "word": 'word',
        "synonyms": 'synonyms'
    }

    _optionals = [
        'word',
        'synonyms',
    ]

    _nullables = [
        'word',
        'synonyms',
    ]

    def __init__(self,
                 word=APIHelper.SKIP,
                 synonyms=APIHelper.SKIP):
        """Constructor for the SynonymsResponse class"""

        # Initialize members of the class
        if word is not APIHelper.SKIP:
            self.word = word 
        if synonyms is not APIHelper.SKIP:
            self.synonyms = synonyms 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        word = dictionary.get("word") if "word" in dictionary.keys() else APIHelper.SKIP
        synonyms = dictionary.get("synonyms") if "synonyms" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(word,
                   synonyms)
