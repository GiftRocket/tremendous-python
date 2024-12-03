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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ListCampaigns200ResponseCampaignsInnerEmailStyle(BaseModel):
    """
    Definition of the email style
    """ # noqa: E501
    sender_name: Optional[StrictStr] = Field(default=None, description="If sending via email, this is how the email will appear to be sent from")
    subject_line: Optional[StrictStr] = Field(default=None, description="Email subject line")
    logo_image_url: Optional[StrictStr] = Field(default=None, description="URL of a publicly-accessible image (png, jpeg, jpg, gif, or svg). This image will be copied to our storage location.")
    logo_image_height_px: Optional[StrictInt] = Field(default=None, description="Image height in pixels")
    logo_background_color: Optional[StrictStr] = Field(default=None, description="Logo background color code (hex, rgb, or rgba)")
    button_color: Optional[StrictStr] = Field(default=None, description="Button color code (hex, rgb, or rgba)")
    __properties: ClassVar[List[str]] = ["sender_name", "subject_line", "logo_image_url", "logo_image_height_px", "logo_background_color", "button_color"]

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
        """Create an instance of ListCampaigns200ResponseCampaignsInnerEmailStyle from a JSON string"""
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
        # set to None if sender_name (nullable) is None
        # and model_fields_set contains the field
        if self.sender_name is None and "sender_name" in self.model_fields_set:
            _dict['sender_name'] = None

        # set to None if subject_line (nullable) is None
        # and model_fields_set contains the field
        if self.subject_line is None and "subject_line" in self.model_fields_set:
            _dict['subject_line'] = None

        # set to None if logo_image_url (nullable) is None
        # and model_fields_set contains the field
        if self.logo_image_url is None and "logo_image_url" in self.model_fields_set:
            _dict['logo_image_url'] = None

        # set to None if logo_image_height_px (nullable) is None
        # and model_fields_set contains the field
        if self.logo_image_height_px is None and "logo_image_height_px" in self.model_fields_set:
            _dict['logo_image_height_px'] = None

        # set to None if logo_background_color (nullable) is None
        # and model_fields_set contains the field
        if self.logo_background_color is None and "logo_background_color" in self.model_fields_set:
            _dict['logo_background_color'] = None

        # set to None if button_color (nullable) is None
        # and model_fields_set contains the field
        if self.button_color is None and "button_color" in self.model_fields_set:
            _dict['button_color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListCampaigns200ResponseCampaignsInnerEmailStyle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sender_name": obj.get("sender_name"),
            "subject_line": obj.get("subject_line"),
            "logo_image_url": obj.get("logo_image_url"),
            "logo_image_height_px": obj.get("logo_image_height_px"),
            "logo_background_color": obj.get("logo_background_color"),
            "button_color": obj.get("button_color")
        })
        return _obj


