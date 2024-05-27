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
import json
from enum import Enum
from typing_extensions import Self


class DeliveryMethod(str, Enum):
    """
    How to deliver the reward to the recipient.  <table>   <thead>     <tr>       <th>Delivery Method</th>       <th>Description</th>     </tr>   </thead>   <tbody>     <tr>       <td><code>EMAIL</code></td>       <td>Deliver the reward to the recipient by email</td>     </tr>     <tr>       <td><code>LINK</code></td>       <td>         <p>Deliver the reward to the recipient via a link.</p>         <p>The link can be retrieved on a successfully ordered reward via the <code>/rewards</code> or <code>/rewards/{id}</code> endpoint. That link must then be  delivered to the recipient out-of-band.</p>       </td>     </tr>     <tr>       <td><code>PHONE</code></td>       <td>Deliver the reward to the recipient by SMS</td>     </tr>   </tbody> </table> 
    """

    """
    allowed enum values
    """
    EMAIL = 'EMAIL'
    LINK = 'LINK'
    PHONE = 'PHONE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeliveryMethod from a JSON string"""
        return cls(json.loads(json_str))


