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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tremendous.models.balance_transaction_order import BalanceTransactionOrder
from typing import Optional, Set
from typing_extensions import Self

class BalanceTransaction(BaseModel):
    """
    A balance transaction represents a specific movement or change in an account's balance. 
    """ # noqa: E501
    created_at: datetime = Field(description="Date that the transaction was created")
    amount: Union[StrictFloat, StrictInt] = Field(description="Amount of the transaction in USD")
    balance: Union[StrictFloat, StrictInt] = Field(description="The updated total after the transaction. Note that this running balance may be delayed and contain `null`.")
    action: StrictStr = Field(description="The action that was performed")
    description: StrictStr = Field(description="A brief description of the transaction")
    order: Optional[BalanceTransactionOrder] = None
    __properties: ClassVar[List[str]] = ["created_at", "amount", "balance", "action", "description", "order"]

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
        """Create an instance of BalanceTransaction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BalanceTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "amount": obj.get("amount"),
            "balance": obj.get("balance"),
            "action": obj.get("action"),
            "description": obj.get("description"),
            "order": BalanceTransactionOrder.from_dict(obj["order"]) if obj.get("order") is not None else None
        })
        return _obj


