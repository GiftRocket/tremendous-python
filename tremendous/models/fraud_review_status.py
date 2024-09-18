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


class FraudReviewStatus(str, Enum):
    """
    The current status of the fraud review:  * `flagged` - The reward has been flagged for and waiting manual review. * `blocked` - The reward was reviewed and blocked. * `released` - The reward was reviewed and released. 
    """

    """
    allowed enum values
    """
    FLAGGED = 'flagged'
    BLOCKED = 'blocked'
    RELEASED = 'released'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FraudReviewStatus from a JSON string"""
        return cls(json.loads(json_str))


