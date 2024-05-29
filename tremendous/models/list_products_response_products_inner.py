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
from tremendous.models.list_products_response_products_inner_countries_inner import ListProductsResponseProductsInnerCountriesInner
from tremendous.models.list_products_response_products_inner_images_inner import ListProductsResponseProductsInnerImagesInner
from tremendous.models.list_products_response_products_inner_skus_inner import ListProductsResponseProductsInnerSkusInner
from typing import Optional, Set
from typing_extensions import Self

class ListProductsResponseProductsInner(BaseModel):
    """
    A product represents one way to payout a reward to it's recipient. Think:  * Amazon.com gift card (ID: `OKMHM2X2OHYV`) * Donations to Save the Children (ID: `ESRNAD533W5A`) * Virtual Visa debit card (ID: `Q24BD9EZ332JT`)  each of which is one specific product on Tremendous.  > 📘 All available products > > See this [list](https://www.tremendous.com/catalog)  Products can be limited in their availability to recipients by  * geography (field `countries`) * currency (field `currencies`) * amount of the reward (field `skus`)   * e.g. adidas gift cards accept any amount between 5 and 200 USD.  See the description of each respective parameter for further details. 
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    name: StrictStr = Field(description="Name of the product")
    description: StrictStr = Field(description="Detailed description of the product. Mostly used for products with a `category` of `charities`.")
    category: StrictStr = Field(description="The category of this product  <table>   <thead>     <tr>       <th>Category</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>ach</code></td>       <td>Bank transfer to the recipient</td>     </tr>     <tr>       <td><code>charity</code></td>       <td>Donations to a charity</td>     </tr>     <tr>       <td><code>merchant_card</code></td>       <td>A gift card for a certain merchant (e.g. Amazon)</td>     </tr>     <tr>       <td><code>paypal</code></td>       <td>Payout via PayPal</td>     </tr>     <tr>       <td><code>venmo</code></td>       <td>Payout via Venmo</td>     </tr>     <tr>       <td><code>visa_card</code></td>       <td>Payout in form of a Visa debit card</td>     </tr>   </tbody> </table> ")
    disclosure: StrictStr = Field(description="Legal disclosures for this product. Can be in HTML format.")
    skus: Optional[List[ListProductsResponseProductsInnerSkusInner]] = Field(default=None, description="Products may are restricted in their usage based on the amount of the reward. The `skus` array defines bands of denominations in which this product may be used for payouts. ")
    currency_codes: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="Available currencies for this product")
    countries: Annotated[List[ListProductsResponseProductsInnerCountriesInner], Field(min_length=1)] = Field(description="List of countries in which this product is available to recipients.")
    images: Annotated[List[ListProductsResponseProductsInnerImagesInner], Field(min_length=0)] = Field(description="List of product images associated with this product (e.g. logos or images of the gift cards)")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "category", "disclosure", "skus", "currency_codes", "countries", "images"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[A-Z0-9]{4,20}", value):
            raise ValueError(r"must validate the regular expression /[A-Z0-9]{4,20}/")
        return value

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ach', 'charity', 'merchant_card', 'paypal', 'venmo', 'visa_card']):
            raise ValueError("must be one of enum values ('ach', 'charity', 'merchant_card', 'paypal', 'venmo', 'visa_card')")
        return value

    @field_validator('currency_codes')
    def currency_codes_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['USD', 'CAD', 'EUR', 'AED', 'AFN', 'ALL', 'AMD', 'ARS', 'AUD', 'AZN', 'BAM', 'BDT', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BRL', 'BWP', 'BYR', 'BZD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'GBP', 'GEL', 'GHS', 'GNF', 'GTQ', 'HKD', 'HNL', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KHR', 'KRW', 'KWD', 'KZT', 'LBP', 'LKR', 'LTL', 'LVL', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MOP', 'MUR', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SDG', 'SEK', 'SGD', 'SOS', 'SYP', 'THB', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VEF', 'VND', 'XAF', 'XOF', 'YER', 'ZAR', 'ZMK']):
                raise ValueError("each list item must be one of ('USD', 'CAD', 'EUR', 'AED', 'AFN', 'ALL', 'AMD', 'ARS', 'AUD', 'AZN', 'BAM', 'BDT', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BRL', 'BWP', 'BYR', 'BZD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'GBP', 'GEL', 'GHS', 'GNF', 'GTQ', 'HKD', 'HNL', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KHR', 'KRW', 'KWD', 'KZT', 'LBP', 'LKR', 'LTL', 'LVL', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MOP', 'MUR', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SDG', 'SEK', 'SGD', 'SOS', 'SYP', 'THB', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VEF', 'VND', 'XAF', 'XOF', 'YER', 'ZAR', 'ZMK')")
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
        """Create an instance of ListProductsResponseProductsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in skus (list)
        _items = []
        if self.skus:
            for _item in self.skus:
                if _item:
                    _items.append(_item.to_dict())
            _dict['skus'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in countries (list)
        _items = []
        if self.countries:
            for _item in self.countries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['countries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListProductsResponseProductsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "category": obj.get("category"),
            "disclosure": obj.get("disclosure"),
            "skus": [ListProductsResponseProductsInnerSkusInner.from_dict(_item) for _item in obj["skus"]] if obj.get("skus") is not None else None,
            "currency_codes": obj.get("currency_codes"),
            "countries": [ListProductsResponseProductsInnerCountriesInner.from_dict(_item) for _item in obj["countries"]] if obj.get("countries") is not None else None,
            "images": [ListProductsResponseProductsInnerImagesInner.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None
        })
        return _obj

