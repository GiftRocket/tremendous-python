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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tremendous.models.list_rewards200_response_rewards_inner_custom_fields_inner import ListRewards200ResponseRewardsInnerCustomFieldsInner
from tremendous.models.list_rewards200_response_rewards_inner_delivery import ListRewards200ResponseRewardsInnerDelivery
from tremendous.models.list_rewards200_response_rewards_inner_recipient import ListRewards200ResponseRewardsInnerRecipient
from tremendous.models.list_rewards200_response_rewards_inner_value import ListRewards200ResponseRewardsInnerValue
from typing import Optional, Set
from typing_extensions import Self

class ListRewards200ResponseRewardsInner(BaseModel):
    """
    A single reward, sent to a recipient. A reward is always part of an order.  Either `products` or `campaign_id` must be specified. 
    """ # noqa: E501
    id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Tremendous ID of the reward")
    order_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Tremendous ID of the order this reward is part of.")
    created_at: Optional[datetime] = Field(default=None, description="Date the reward was created")
    value: Optional[ListRewards200ResponseRewardsInnerValue] = None
    recipient: Optional[ListRewards200ResponseRewardsInnerRecipient] = None
    deliver_at: Optional[date] = Field(default=None, description="Timestamp of reward delivery within the next year. Note that if date-time is provided, the time values will be ignored.")
    custom_fields: Optional[List[ListRewards200ResponseRewardsInnerCustomFieldsInner]] = None
    delivery: Optional[ListRewards200ResponseRewardsInnerDelivery] = None
    __properties: ClassVar[List[str]] = ["id", "order_id", "created_at", "value", "recipient", "deliver_at", "custom_fields", "delivery"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('order_id')
    def order_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('deliver_at')
    def deliver_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"YYYY-MM-DD", value):
            raise ValueError(r"must validate the regular expression /YYYY-MM-DD/")
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
        """Create an instance of ListRewards200ResponseRewardsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['custom_fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of delivery
        if self.delivery:
            _dict['delivery'] = self.delivery.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListRewards200ResponseRewardsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "order_id": obj.get("order_id"),
            "created_at": obj.get("created_at"),
            "value": ListRewards200ResponseRewardsInnerValue.from_dict(obj["value"]) if obj.get("value") is not None else None,
            "recipient": ListRewards200ResponseRewardsInnerRecipient.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "deliver_at": obj.get("deliver_at"),
            "custom_fields": [ListRewards200ResponseRewardsInnerCustomFieldsInner.from_dict(_item) for _item in obj["custom_fields"]] if obj.get("custom_fields") is not None else None,
            "delivery": ListRewards200ResponseRewardsInnerDelivery.from_dict(obj["delivery"]) if obj.get("delivery") is not None else None
        })
        return _obj

