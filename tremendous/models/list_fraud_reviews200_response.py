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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from tremendous.models.list_fraud_reviews200_response_fraud_reviews_inner import ListFraudReviews200ResponseFraudReviewsInner
from typing import Optional, Set
from typing_extensions import Self

class ListFraudReviews200Response(BaseModel):
    """
    ListFraudReviews200Response
    """ # noqa: E501
    fraud_reviews: List[ListFraudReviews200ResponseFraudReviewsInner]
    total_count: StrictInt = Field(description="The total number of fraud reviews")
    __properties: ClassVar[List[str]] = ["fraud_reviews", "total_count"]

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
        """Create an instance of ListFraudReviews200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fraud_reviews (list)
        _items = []
        if self.fraud_reviews:
            for _item in self.fraud_reviews:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fraud_reviews'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListFraudReviews200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fraud_reviews": [ListFraudReviews200ResponseFraudReviewsInner.from_dict(_item) for _item in obj["fraud_reviews"]] if obj.get("fraud_reviews") is not None else None,
            "total_count": obj.get("total_count")
        })
        return _obj


