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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tremendous.models.create_organization_request_copy_settings import CreateOrganizationRequestCopySettings
from typing import Optional, Set
from typing_extensions import Self

class CreateOrganizationRequest(BaseModel):
    """
    CreateOrganizationRequest
    """ # noqa: E501
    name: StrictStr = Field(description="Name of the organization")
    website: StrictStr = Field(description="URL of the website of that organization")
    with_api_key: Optional[StrictBool] = Field(default=None, description="Default value is `false`. Set to true to also generate an API key associated to the new organization.")
    copy_settings: Optional[CreateOrganizationRequestCopySettings] = None
    phone: Optional[StrictStr] = Field(default=None, description="Phone number of the organization. For non-US phone numbers, specify the country code (prefixed with +).")
    __properties: ClassVar[List[str]] = ["name", "website", "with_api_key", "copy_settings", "phone"]

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
        """Create an instance of CreateOrganizationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of copy_settings
        if self.copy_settings:
            _dict['copy_settings'] = self.copy_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrganizationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "website": obj.get("website"),
            "with_api_key": obj.get("with_api_key"),
            "copy_settings": CreateOrganizationRequestCopySettings.from_dict(obj["copy_settings"]) if obj.get("copy_settings") is not None else None,
            "phone": obj.get("phone")
        })
        return _obj


