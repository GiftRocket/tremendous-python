# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and its members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FraudReviewReason(str, Enum):
    """
    FraudReviewReason
    """

    """
    allowed enum values
    """
    DISALLOWED_IP = 'Disallowed IP'
    DISALLOWED_EMAIL = 'Disallowed email'
    DISALLOWED_COUNTRY = 'Disallowed country'
    OVER_REWARD_DOLLAR_LIMIT = 'Over reward dollar limit'
    OVER_REWARD_COUNT_LIMIT = 'Over reward count limit'
    VPN_DETECTED = 'VPN detected'
    DEVICE_RELATED_TO_MULTIPLE_EMAILS = 'Device related to multiple emails'
    DEVICE_OR_ACCOUNT_RELATED_TO_MULTIPLE_EMAILS = 'Device or account related to multiple emails'
    IP_ON_A_TREMENDOUS_FRAUD_LIST = 'IP on a Tremendous fraud list'
    BANK_ACCOUNT_ON_A_TREMENDOUS_FRAUD_LIST = 'Bank account on a Tremendous fraud list'
    FINGERPRINT_ON_A_TREMENDOUS_FRAUD_LIST = 'Fingerprint on a Tremendous fraud list'
    EMAIL_ON_A_TREMENDOUS_FRAUD_LIST = 'Email on a Tremendous fraud list'
    PHONE_ON_A_TREMENDOUS_FRAUD_LIST = 'Phone on a Tremendous fraud list'
    IP_RELATED_TO_A_BLOCKED_REWARD = 'IP related to a blocked reward'
    DEVICE_RELATED_TO_A_BLOCKED_REWARD = 'Device related to a blocked reward'
    BANK_ACCOUNT_RELATED_TO_A_BLOCKED_REWARD = 'Bank account related to a blocked reward'
    FINGERPRINT_RELATED_TO_A_BLOCKED_REWARD = 'Fingerprint related to a blocked reward'
    EMAIL_RELATED_TO_A_BLOCKED_REWARD = 'Email related to a blocked reward'
    PHONE_RELATED_TO_A_BLOCKED_REWARD = 'Phone related to a blocked reward'
    ALLOWED_IP = 'Allowed IP'
    ALLOWED_EMAIL = 'Allowed email'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FraudReviewReason from a JSON string"""
        return cls(json.loads(json_str))


