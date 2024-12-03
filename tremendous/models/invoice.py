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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Invoice(BaseModel):
    """
    Invoices are instruments to fund your Tremendous account's balance.  Invoices can be created by your organization programatically. Once we receive your payment, the invoice is marked as `PAID` and we add the respective funds to your account's balance. 
    """ # noqa: E501
    id: StrictStr = Field(description="The invoice number")
    po_number: Optional[StrictStr] = Field(default=None, description="Reference to the purchase order number within your organization")
    amount: Union[StrictFloat, StrictInt] = Field(description="Amount of the invoice in USD")
    international: Optional[StrictBool] = None
    status: StrictStr = Field(description="Status of this invoice  <table>   <thead>     <tr>       <th>Status</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>DELETED</code></td>       <td>Invoice has been deleted by your organization</td>     </tr>     <tr>       <td><code>PAID</code></td>       <td>Invoice has been paid by your organization</td>     </tr>     <tr>       <td><code>OPEN</code></td>       <td>Invoice has been created by your organization but has not been paid, yet</td>     </tr>   </tbody> </table> ")
    orders: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="List of orders related to the invoice (it doesn't apply to prefunding)")
    rewards: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="List of rewards related to the invoice (it doesn't apply to prefunding)")
    created_at: datetime = Field(description="Timestamp of when the invoice has been created. ")
    paid_at: Optional[datetime] = Field(description="Timestamp of when the invoice has been paid. ")
    __properties: ClassVar[List[str]] = ["id", "po_number", "amount", "international", "status", "orders", "rewards", "created_at", "paid_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DELETED', 'PAID', 'OPEN', 'MARKED_AS_PAID']):
            raise ValueError("must be one of enum values ('DELETED', 'PAID', 'OPEN', 'MARKED_AS_PAID')")
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
        """Create an instance of Invoice from a JSON string"""
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
        # set to None if po_number (nullable) is None
        # and model_fields_set contains the field
        if self.po_number is None and "po_number" in self.model_fields_set:
            _dict['po_number'] = None

        # set to None if paid_at (nullable) is None
        # and model_fields_set contains the field
        if self.paid_at is None and "paid_at" in self.model_fields_set:
            _dict['paid_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Invoice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "po_number": obj.get("po_number"),
            "amount": obj.get("amount"),
            "international": obj.get("international"),
            "status": obj.get("status"),
            "orders": obj.get("orders"),
            "rewards": obj.get("rewards"),
            "created_at": obj.get("created_at"),
            "paid_at": obj.get("paid_at")
        })
        return _obj


