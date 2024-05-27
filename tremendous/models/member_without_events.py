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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MemberWithoutEvents(BaseModel):
    """
    Each organization has one or more users that can access and manage that organization. These users are called members.  Members can take actions via the Tremendous web dashboard directly.  These actions include adding funding sources to the organization, creating Campaigns, and more. 
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    email: StrictStr = Field(description="Email address of the member")
    name: Optional[StrictStr] = Field(description="Full name of the member")
    active: Optional[StrictBool] = Field(default=None, description="Is this member currently active in the organization. If `false`, the member will not be able to access the organization. ")
    role: StrictStr = Field(description="Role of the member within the organization.  <table>   <thead>     <tr>       <th>Role</th>       <th>Description</th>     </tr>   </thead>     <tr>       <td><code>MEMBER</code></td>       <td>Limited permissions. Can view their own reward and order histories only.</td>     </tr>     <tr>       <td><code>ADMIN</code></td>       <td>Update organization settings, invite other members to the organization, and view all member order and reward histories within their organization.</td>     </tr>   <tbody>   </tbody> </table> ")
    status: StrictStr = Field(description="Current status of the member's account.  When creating a member it starts out in the status `INVITED`. As soon as that member open the invitation link and registers an account, the status switches to `REGISTERED`. ")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp when this member was created.  The `created_at` timestamp is **NOT** returned when retrieving a member (but is part of the response when listing or creating members). ")
    last_login_at: Optional[datetime] = Field(default=None, description="Timestamp when this member most recently logged into the dashboard of the organization associated with this API key. ")
    __properties: ClassVar[List[str]] = ["id", "email", "name", "active", "role", "status", "created_at", "last_login_at"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MEMBER', 'ADMIN']):
            raise ValueError("must be one of enum values ('MEMBER', 'ADMIN')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['REGISTERED', 'INVITED']):
            raise ValueError("must be one of enum values ('REGISTERED', 'INVITED')")
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
        """Create an instance of MemberWithoutEvents from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "status",
            "created_at",
            "last_login_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if last_login_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_login_at is None and "last_login_at" in self.model_fields_set:
            _dict['last_login_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberWithoutEvents from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "name": obj.get("name"),
            "active": obj.get("active"),
            "role": obj.get("role"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "last_login_at": obj.get("last_login_at")
        })
        return _obj


