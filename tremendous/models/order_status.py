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


class OrderStatus(str, Enum):
    """
    Execution status of a given order  <table>   <thead>     <tr>       <th>         Status       </th>       <th>         Description       </th>     </tr>   </thead>   <tbody>     <tr>       <td>         <code>           CANCELED         </code>       </td>       <td>         The order and all of its rewards were canceled.       </td>     </tr>     <tr>       <td>         <code>           CART         </code>       </td>       <td>         The order has been created, but hasn't yet been processed.       </td>     </tr>     <tr>       <td>         <code>           EXECUTED         </code>       </td>       <td>         The order has been executed. Payment has been handled and rewards are being delivered (if applicable).       </td>     </tr>     <tr>       <td>         <code>           FAILED         </code>       </td>       <td>         The order could not be processed due to an error. E.g. due to insufficient funds in the account.       </td>     </tr>     <tr>       <td>         <code>           PENDING APPROVAL         </code>       </td>       <td>         The order has been created but needs approval to be executed.       </td>     </tr>     <tr>       <td>         <code>           PENDING INTERNAL PAYMENT APPROVAL         </code>       </td>       <td>         The order has been created but it is under review and requires approval from our team.       </td>     </tr>    </tbody> </table> 
    """

    """
    allowed enum values
    """
    CANCELED = 'CANCELED'
    CART = 'CART'
    EXECUTED = 'EXECUTED'
    FAILED = 'FAILED'
    PENDING_APPROVAL = 'PENDING APPROVAL'
    PENDING_INTERNAL_PAYMENT_APPROVAL = 'PENDING INTERNAL PAYMENT APPROVAL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderStatus from a JSON string"""
        return cls(json.loads(json_str))

