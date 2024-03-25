# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from chart_hop_python_sdk.type.enum_value import EnumValue
from chart_hop_python_sdk.type.job_tier_field import JobTierField
from chart_hop_python_sdk.type.money import Money
from chart_hop_python_sdk.type.table_row_ref import TableRowRef

class RequiredCompBand(TypedDict):
    # globally unique id
    id: str

    # parent organization id
    orgId: str

    # human-readable name of content
    label: str

    # hex color associated with the band level
    color: str

    baseInterval: EnumValue

class OptionalCompBand(TypedDict, total=False):
    baseCompMax: Money

    baseCompMid: Money

    baseCompMin: Money

    # spread percent used to calculate base comp from the midpoint
    baseSpread: typing.Union[int, float]

    baseTargetPay: Money

    # target pay associated with open jobs at this band level, specified as a percentile of [min,max]
    baseTargetPayPercentile: typing.Union[int, float]

    jobTierOneField: JobTierField

    jobTierTwoField: JobTierField

    jobTierThreeField: JobTierField

    jobLevel: TableRowRef

    # target equity for the band, in shares
    equityTargetShares: typing.Union[int, float]

    # target equity for the band, as a percentage of base
    equityTargetPercentOfBase: typing.Union[int, float]

    # target equity for the band, as a monetary value, in the same currency as the base
    equityTargetValue: typing.Union[int, float]

    variableValue: Money

    # variable compensation for the band, specified as a percentage of base
    variablePercentOfBase: typing.Union[int, float]

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class CompBand(RequiredCompBand, OptionalCompBand):
    pass
