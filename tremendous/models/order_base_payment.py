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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from tremendous.models.payment_details_refund import PaymentDetailsRefund
from typing import Optional, Set
from typing_extensions import Self

class OrderBasePayment(BaseModel):
    """
    Cost breakdown of the order (cost of rewards + fees). Cost and fees are always denominated in USD, independent from the currency of the ordered rewards. Note that this property will only appear for processed orders (`status` is `EXECUTED`).
    """ # noqa: E501
    subtotal: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Total price of the order before fees (in USD)")
    total: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Total price of the order including fees (in USD)")
    fees: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Fees for the order (in USD)")
    refund: Optional[PaymentDetailsRefund] = None
    channel: Optional[StrictStr] = Field(default=None, description="Name of the channel in which the order was created")
    __properties: ClassVar[List[str]] = ["subtotal", "total", "fees", "refund", "channel"]

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
        """Create an instance of OrderBasePayment from a JSON string"""
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
            "subtotal",
            "total",
            "fees",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of refund
        if self.refund:
            _dict['refund'] = self.refund.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderBasePayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subtotal": obj.get("subtotal"),
            "total": obj.get("total"),
            "fees": obj.get("fees"),
            "refund": PaymentDetailsRefund.from_dict(obj["refund"]) if obj.get("refund") is not None else None,
            "channel": obj.get("channel")
        })
        return _obj


