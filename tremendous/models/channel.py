# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Channel(str, Enum):
    """
    Name of the channel in which the order was created
    """

    """
    allowed enum values
    """
    UI = 'UI'
    API = 'API'
    EMBED = 'EMBED'
    DECIPHER = 'DECIPHER'
    QUALTRICS = 'QUALTRICS'
    TYPEFORM = 'TYPEFORM'
    SURVEY_MONKEY = 'SURVEY MONKEY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Channel from a JSON string"""
        return cls(json.loads(json_str))

