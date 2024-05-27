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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tremendous.models.list_funding_sources200_response_funding_sources_inner_meta import ListFundingSources200ResponseFundingSourcesInnerMeta
from typing import Optional, Set
from typing_extensions import Self

class ListFundingSources200ResponseFundingSourcesInner(BaseModel):
    """
    
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    method: StrictStr = Field(description="You can pay for rewards using different payment methods on Tremendous:  <table>   <thead>     <tr>       <th>Payment Method</th>       <th>Description</th>       </tr>   </thead>   <tbody>     <tr>       <td><code>balance</code></td>       <td>Pre-funded balance in your Tremendous account to draw funds from to send rewards to recipients.</td>     </tr>     <tr>       <td><code>bank_account</code></td>       <td>Bank account to draw funds from to send rewards to recipients.</td>     </tr>     <tr>       <td><code>credit_card</code></td>       <td>Credit card to draw funds from to send rewards to recipients.</td>     </tr>     <tr>       <td><code>invoice</code></td>       <td>Send rewards to recipients and pay by invoice.</td>     </tr>    </tbody> </table> ")
    type: Optional[StrictStr] = Field(default=None, description="**Only available when `method` is set to `invoice`.** ")
    meta: ListFundingSources200ResponseFundingSourcesInnerMeta
    __properties: ClassVar[List[str]] = ["id", "method", "type", "meta"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['balance', 'bank_account', 'credit_card', 'invoice']):
            raise ValueError("must be one of enum values ('balance', 'bank_account', 'credit_card', 'invoice')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['COMMERCIAL', 'PRO_FORMA', 'PREFUNDING_ONLY']):
            raise ValueError("must be one of enum values ('COMMERCIAL', 'PRO_FORMA', 'PREFUNDING_ONLY')")
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
        """Create an instance of ListFundingSources200ResponseFundingSourcesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListFundingSources200ResponseFundingSourcesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "method": obj.get("method"),
            "type": obj.get("type"),
            "meta": ListFundingSources200ResponseFundingSourcesInnerMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None
        })
        return _obj


