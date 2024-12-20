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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeliveryDetailsWithLink(BaseModel):
    """
    Details on how the reward is delivered to the recipient. 
    """ # noqa: E501
    method: StrictStr = Field(description="How to deliver the reward to the recipient.  <table>   <thead>     <tr>       <th>Delivery Method</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>EMAIL</code></td>       <td>Deliver the reward to the recipient by email</td>     </tr>     <tr>       <td><code>LINK</code></td>       <td>         <p>Deliver the reward to the recipient via a link.</p>         <p>The link can be retrieved on a successfully ordered reward via the <code>/rewards</code> or <code>/rewards/{id}</code> endpoint. That link must then be  delivered to the recipient out-of-band.</p>       </td>     </tr>     <tr>       <td><code>PHONE</code></td>       <td>Deliver the reward to the recipient by SMS</td>     </tr>   </tbody> </table> ")
    status: StrictStr = Field(description="Current status of the delivery of the reward:  * `SCHEDULED` - Reward is scheduled for delivery and will be delivered soon. * `FAILED` - Delivery of reward failed (e.g. email bounced). * `SUCCEEDED` - Reward was successfully delivered (email or text message delivered or reward link active). * `PENDING` - Delivery is pending but not yet scheduled. ")
    link: Optional[StrictStr] = Field(default=None, description="Link to redeem the reward at. You need to deliver this link to the recipient. ")
    __properties: ClassVar[List[str]] = ["method", "status", "link"]

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['EMAIL', 'LINK', 'PHONE']):
            raise ValueError("must be one of enum values ('EMAIL', 'LINK', 'PHONE')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SCHEDULED', 'FAILED', 'SUCCEEDED', 'PENDING']):
            raise ValueError("must be one of enum values ('SCHEDULED', 'FAILED', 'SUCCEEDED', 'PENDING')")
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
        """Create an instance of DeliveryDetailsWithLink from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "status",
            "link",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryDetailsWithLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "method": obj.get("method"),
            "status": obj.get("status"),
            "link": obj.get("link")
        })
        return _obj


