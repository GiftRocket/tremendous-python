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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from tremendous.models.allow_email1 import AllowEmail1
from tremendous.models.allow_ip1 import AllowIp1
from tremendous.models.review_country1 import ReviewCountry1
from tremendous.models.review_email1 import ReviewEmail1
from tremendous.models.review_ip1 import ReviewIp1
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

UPDATEFRAUDRULELISTREQUESTCONFIG_ANY_OF_SCHEMAS = ["AllowEmail1", "AllowIp1", "ReviewCountry1", "ReviewEmail1", "ReviewIp1"]

class UpdateFraudRuleListRequestConfig(BaseModel):
    """
    The configuration associated with the rule. The properties allowed depend on the type of rule.
    """

    # data type: ReviewCountry1
    anyof_schema_1_validator: Optional[ReviewCountry1] = None
    # data type: ReviewIp1
    anyof_schema_2_validator: Optional[ReviewIp1] = None
    # data type: ReviewEmail1
    anyof_schema_3_validator: Optional[ReviewEmail1] = None
    # data type: AllowIp1
    anyof_schema_4_validator: Optional[AllowIp1] = None
    # data type: AllowEmail1
    anyof_schema_5_validator: Optional[AllowEmail1] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[AllowEmail1, AllowIp1, ReviewCountry1, ReviewEmail1, ReviewIp1]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "AllowEmail1", "AllowIp1", "ReviewCountry1", "ReviewEmail1", "ReviewIp1" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = UpdateFraudRuleListRequestConfig.model_construct()
        error_messages = []
        # validate data type: ReviewCountry1
        if not isinstance(v, ReviewCountry1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewCountry1`")
        else:
            return v

        # validate data type: ReviewIp1
        if not isinstance(v, ReviewIp1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewIp1`")
        else:
            return v

        # validate data type: ReviewEmail1
        if not isinstance(v, ReviewEmail1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewEmail1`")
        else:
            return v

        # validate data type: AllowIp1
        if not isinstance(v, AllowIp1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AllowIp1`")
        else:
            return v

        # validate data type: AllowEmail1
        if not isinstance(v, AllowEmail1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AllowEmail1`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in UpdateFraudRuleListRequestConfig with anyOf schemas: AllowEmail1, AllowIp1, ReviewCountry1, ReviewEmail1, ReviewIp1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ReviewCountry1] = None
        try:
            instance.actual_instance = ReviewCountry1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ReviewIp1] = None
        try:
            instance.actual_instance = ReviewIp1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[ReviewEmail1] = None
        try:
            instance.actual_instance = ReviewEmail1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[AllowIp1] = None
        try:
            instance.actual_instance = AllowIp1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[AllowEmail1] = None
        try:
            instance.actual_instance = AllowEmail1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateFraudRuleListRequestConfig with anyOf schemas: AllowEmail1, AllowIp1, ReviewCountry1, ReviewEmail1, ReviewIp1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AllowEmail1, AllowIp1, ReviewCountry1, ReviewEmail1, ReviewIp1]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


