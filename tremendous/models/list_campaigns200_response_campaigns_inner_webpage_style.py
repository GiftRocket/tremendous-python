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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ListCampaigns200ResponseCampaignsInnerWebpageStyle(BaseModel):
    """
    Definition of the webpage style
    """ # noqa: E501
    headline: Optional[StrictStr] = Field(default=None, description="Headline for the reward page")
    message: Optional[StrictStr] = Field(default=None, description="Message for the reward page")
    logo_image_url: Optional[StrictStr] = Field(default=None, description="URL of a publicly-accessible image (png, jpeg, jpg, gif, or svg). This image will be copied to our storage location.")
    logo_image_height_px: Optional[StrictInt] = Field(default=None, description="Image height in pixels")
    logo_background_color: Optional[StrictStr] = Field(default=None, description="Logo backgrond color code (hex, rgb, or rgba)")
    background_color: Optional[StrictStr] = Field(default=None, description="Backgrond color code (hex, rgb, or rgba)")
    __properties: ClassVar[List[str]] = ["headline", "message", "logo_image_url", "logo_image_height_px", "logo_background_color", "background_color"]

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
        """Create an instance of ListCampaigns200ResponseCampaignsInnerWebpageStyle from a JSON string"""
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
        # set to None if headline (nullable) is None
        # and model_fields_set contains the field
        if self.headline is None and "headline" in self.model_fields_set:
            _dict['headline'] = None

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

        # set to None if background_color (nullable) is None
        # and model_fields_set contains the field
        if self.background_color is None and "background_color" in self.model_fields_set:
            _dict['background_color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListCampaigns200ResponseCampaignsInnerWebpageStyle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "headline": obj.get("headline"),
            "message": obj.get("message"),
            "logo_image_url": obj.get("logo_image_url"),
            "logo_image_height_px": obj.get("logo_image_height_px"),
            "logo_background_color": obj.get("logo_background_color"),
            "background_color": obj.get("background_color")
        })
        return _obj


