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
from chart_hop_python_sdk.type.money import Money

class RequiredCreateCompBand(TypedDict):
    # human-readable name of content
    label: str

    # hex color associated with the band level
    color: str

    baseInterval: EnumValue

    # job level associated with the comp band
    jobLevel: str

class OptionalCreateCompBand(TypedDict, total=False):
    baseCompMax: Money

    baseCompMid: Money

    baseCompMin: Money

    # spread percent used to calculate base comp from the midpoint
    baseSpread: typing.Union[int, float]

    baseTargetPay: Money

    # base target pay associated with open jobs at this band level, as a percentile
    baseTargetPayPercentile: typing.Union[int, float]

    # target equity for the band, in shares
    equityTargetShares: typing.Union[int, float]

    # target equity for the band, as a percentage of base
    equityTargetPercentOfBase: typing.Union[int, float]

    # target equity for the band, as a monetary value, in the same currency as the base
    equityTargetValue: typing.Union[int, float]

    variableValue: Money

    # variable compensation for the band, specified as a percentage of base
    variablePercentOfBase: typing.Union[int, float]

    # first job tier associated with the comp band
    jobTierOneField: str

    # second job tier associated with the comp band
    jobTierTwoField: str

    # third job tier associated with the comp band
    jobTierThreeField: str

class CreateCompBand(RequiredCreateCompBand, OptionalCreateCompBand):
    pass
