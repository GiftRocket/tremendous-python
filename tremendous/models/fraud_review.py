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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tremendous.models.get_fraud_review200_response_fraud_review_geo import GetFraudReview200ResponseFraudReviewGeo
from tremendous.models.get_fraud_review200_response_fraud_review_related_rewards import GetFraudReview200ResponseFraudReviewRelatedRewards
from tremendous.models.order_without_link_rewards_inner import OrderWithoutLinkRewardsInner
from typing import Optional, Set
from typing_extensions import Self

class FraudReview(BaseModel):
    """
    The fraud review associated with a reward.
    """ # noqa: E501
    status: Optional[StrictStr] = Field(default=None, description="The current status of the fraud review:  * `flagged` - The reward has been flagged for and waiting manual review. * `blocked` - The reward was reviewed and blocked. * `released` - The reward was reviewed and released. ")
    reasons: Optional[List[StrictStr]] = Field(default=None, description="The array may contain multiple reasons, depending on which rule(s) flagged the reward for review. Reasons can be any of the following:  * `Disallowed IP` * `Disallowed email` * `Disallowed country` * `Over reward dollar limit` * `Over reward count limit` * `VPN detected` * `Device related to multiple emails` * `Device or account related to multiple emails` * `IP on a Tremendous fraud list` * `Bank account on a Tremendous fraud list` * `Fingerprint on a Tremendous fraud list` * `Email on a Tremendous fraud list` * `Phone on a Tremendous fraud list` * `IP related to a blocked reward` * `Bank account related to a blocked reward` * `Fingerprint related to a blocked reward` * `Email related to a blocked reward` * `Phone related to a blocked reward` * `Allowed IP` * `Allowed email` ")
    reviewed_by: Optional[StrictStr] = Field(default=None, description="The name of the person who reviewed the reward, or `Automatic Review` if the reward was blocked automatically. Rewards can be automatically blocked if they remain in the flagged fraud queue for more than 30 days.  This field is only present if the status is not `flagged`. ")
    reviewed_at: Optional[datetime] = Field(default=None, description="When the reward was blocked or released following fraud review.  This field is only present if the status is not `flagged`. ")
    related_rewards: Optional[GetFraudReview200ResponseFraudReviewRelatedRewards] = None
    device_id: Optional[StrictStr] = Field(default=None, description="The device fingerprint, if known.")
    redemption_method: Optional[StrictStr] = Field(default=None, description="The product selected to claim the reward")
    redeemed_at: Optional[datetime] = Field(default=None, description="Date the reward was redeemed")
    geo: Optional[GetFraudReview200ResponseFraudReviewGeo] = None
    reward: Optional[OrderWithoutLinkRewardsInner] = None
    __properties: ClassVar[List[str]] = ["status", "reasons", "reviewed_by", "reviewed_at", "related_rewards", "device_id", "redemption_method", "redeemed_at", "geo", "reward"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['flagged', 'blocked', 'released']):
            raise ValueError("must be one of enum values ('flagged', 'blocked', 'released')")
        return value

    @field_validator('reasons')
    def reasons_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Disallowed IP', 'Disallowed email', 'Disallowed country', 'Over reward dollar limit', 'Over reward count limit', 'VPN detected', 'Device related to multiple emails', 'Device or account related to multiple emails', 'IP on a Tremendous fraud list', 'Bank account on a Tremendous fraud list', 'Fingerprint on a Tremendous fraud list', 'Email on a Tremendous fraud list', 'Phone on a Tremendous fraud list', 'IP related to a blocked reward', 'Bank account related to a blocked reward', 'Fingerprint related to a blocked reward', 'Email related to a blocked reward', 'Phone related to a blocked reward', 'Allowed IP', 'Allowed email']):
                raise ValueError("each list item must be one of ('Disallowed IP', 'Disallowed email', 'Disallowed country', 'Over reward dollar limit', 'Over reward count limit', 'VPN detected', 'Device related to multiple emails', 'Device or account related to multiple emails', 'IP on a Tremendous fraud list', 'Bank account on a Tremendous fraud list', 'Fingerprint on a Tremendous fraud list', 'Email on a Tremendous fraud list', 'Phone on a Tremendous fraud list', 'IP related to a blocked reward', 'Bank account related to a blocked reward', 'Fingerprint related to a blocked reward', 'Email related to a blocked reward', 'Phone related to a blocked reward', 'Allowed IP', 'Allowed email')")
        return value

    @field_validator('redemption_method')
    def redemption_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['paypal', 'bank', 'merchant card', 'visa card', 'charity', 'venmo']):
            raise ValueError("must be one of enum values ('paypal', 'bank', 'merchant card', 'visa card', 'charity', 'venmo')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FraudReview from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "status",
            "reasons",
            "redemption_method",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of related_rewards
        if self.related_rewards:
            _dict['related_rewards'] = self.related_rewards.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo
        if self.geo:
            _dict['geo'] = self.geo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FraudReview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "reasons": obj.get("reasons"),
            "reviewed_by": obj.get("reviewed_by"),
            "reviewed_at": obj.get("reviewed_at"),
            "related_rewards": GetFraudReview200ResponseFraudReviewRelatedRewards.from_dict(obj["related_rewards"]) if obj.get("related_rewards") is not None else None,
            "device_id": obj.get("device_id"),
            "redemption_method": obj.get("redemption_method"),
            "redeemed_at": obj.get("redeemed_at"),
            "geo": GetFraudReview200ResponseFraudReviewGeo.from_dict(obj["geo"]) if obj.get("geo") is not None else None,
            "reward": OrderWithoutLinkRewardsInner.from_dict(obj["reward"]) if obj.get("reward") is not None else None
        })
        return _obj


