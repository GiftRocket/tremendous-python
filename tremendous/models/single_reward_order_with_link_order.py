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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tremendous.models.order_base_payment import OrderBasePayment
from tremendous.models.order_with_link_rewards_inner import OrderWithLinkRewardsInner
from typing import Optional, Set
from typing_extensions import Self

class SingleRewardOrderWithLinkOrder(BaseModel):
    """
    An order wraps around the fulfilment of one or more rewards.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="Tremendous ID of the order")
    external_id: Optional[StrictStr] = Field(default=None, description="Reference for this order, supplied by the customer.  When set, `external_id` makes order idempotent. All requests that use the same `external_id` after the initial order creation, will result in a response that returns the data of the initially created order. The response will have a `201` response code. These responses **fail** to create any further orders.  It also allows for retrieving by `external_id` instead of `id` only. ")
    campaign_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="ID of the campaign in your account, that defines the available products (different gift cards, charity, etc.) that the recipient can choose from. ")
    created_at: datetime = Field(description="Date the order has been created")
    status: StrictStr = Field(description="Execution status of a given order  <table>   <thead>     <tr>       <th>         Status       </th>       <th>         Description       </th>     </tr>   </thead>   <tbody>     <tr>       <td>         <code>           CANCELED         </code>       </td>       <td>         The order and all of its rewards were canceled.       </td>     </tr>     <tr>       <td>         <code>           CART         </code>       </td>       <td>         The order has been created, but hasn't yet been processed.       </td>     </tr>     <tr>       <td>         <code>           EXECUTED         </code>       </td>       <td>         The order has been executed. Payment has been handled and rewards are being delivered (if applicable).       </td>     </tr>     <tr>       <td>         <code>           FAILED         </code>       </td>       <td>         The order could not be processed due to an error. E.g. due to insufficient funds in the account.       </td>     </tr>     <tr>       <td>         <code>           PENDING APPROVAL         </code>       </td>       <td>         The order has been created but needs approval to be executed.       </td>     </tr>     <tr>       <td>         <code>           PENDING INTERNAL PAYMENT APPROVAL         </code>       </td>       <td>         The order has been created but it is under review and requires approval from our team.       </td>     </tr>    </tbody> </table> ")
    channel: Optional[StrictStr] = Field(default=None, description="Name of the channel in which the order was created")
    payment: Optional[OrderBasePayment] = None
    invoice_id: Optional[StrictStr] = Field(default=None, description="The ID for the invoice associated with this order")
    rewards: Optional[List[OrderWithLinkRewardsInner]] = None
    __properties: ClassVar[List[str]] = ["id", "external_id", "campaign_id", "created_at", "status", "channel", "payment", "invoice_id", "rewards"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('campaign_id')
    def campaign_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CANCELED', 'CART', 'EXECUTED', 'FAILED', 'PENDING APPROVAL', 'PENDING INTERNAL PAYMENT APPROVAL']):
            raise ValueError("must be one of enum values ('CANCELED', 'CART', 'EXECUTED', 'FAILED', 'PENDING APPROVAL', 'PENDING INTERNAL PAYMENT APPROVAL')")
        return value

    @field_validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UI', 'API', 'EMBED', 'DECIPHER', 'QUALTRICS', 'TYPEFORM', 'SURVEY MONKEY']):
            raise ValueError("must be one of enum values ('UI', 'API', 'EMBED', 'DECIPHER', 'QUALTRICS', 'TYPEFORM', 'SURVEY MONKEY')")
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
        """Create an instance of SingleRewardOrderWithLinkOrder from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "campaign_id",
            "created_at",
            "status",
            "channel",
            "invoice_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rewards (list)
        _items = []
        if self.rewards:
            for _item in self.rewards:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rewards'] = _items
        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaign_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SingleRewardOrderWithLinkOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "external_id": obj.get("external_id"),
            "campaign_id": obj.get("campaign_id"),
            "created_at": obj.get("created_at"),
            "status": obj.get("status"),
            "channel": obj.get("channel"),
            "payment": OrderBasePayment.from_dict(obj["payment"]) if obj.get("payment") is not None else None,
            "invoice_id": obj.get("invoice_id"),
            "rewards": [OrderWithLinkRewardsInner.from_dict(_item) for _item in obj["rewards"]] if obj.get("rewards") is not None else None
        })
        return _obj


