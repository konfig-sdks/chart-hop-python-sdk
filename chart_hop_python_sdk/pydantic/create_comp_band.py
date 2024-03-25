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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from chart_hop_python_sdk.pydantic.enum_value import EnumValue
from chart_hop_python_sdk.pydantic.money import Money

class CreateCompBand(BaseModel):
    # human-readable name of content
    label: str = Field(alias='label')

    # hex color associated with the band level
    color: str = Field(alias='color')

    base_interval: EnumValue = Field(alias='baseInterval')

    # job level associated with the comp band
    job_level: str = Field(alias='jobLevel')

    base_comp_max: typing.Optional[Money] = Field(None, alias='baseCompMax')

    base_comp_mid: typing.Optional[Money] = Field(None, alias='baseCompMid')

    base_comp_min: typing.Optional[Money] = Field(None, alias='baseCompMin')

    # spread percent used to calculate base comp from the midpoint
    base_spread: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseSpread')

    base_target_pay: typing.Optional[Money] = Field(None, alias='baseTargetPay')

    # base target pay associated with open jobs at this band level, as a percentile
    base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseTargetPayPercentile')

    # target equity for the band, in shares
    equity_target_shares: typing.Optional[typing.Union[int, float]] = Field(None, alias='equityTargetShares')

    # target equity for the band, as a percentage of base
    equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = Field(None, alias='equityTargetPercentOfBase')

    # target equity for the band, as a monetary value, in the same currency as the base
    equity_target_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='equityTargetValue')

    variable_value: typing.Optional[Money] = Field(None, alias='variableValue')

    # variable compensation for the band, specified as a percentage of base
    variable_percent_of_base: typing.Optional[typing.Union[int, float]] = Field(None, alias='variablePercentOfBase')

    # first job tier associated with the comp band
    job_tier_one_field: typing.Optional[str] = Field(None, alias='jobTierOneField')

    # second job tier associated with the comp band
    job_tier_two_field: typing.Optional[str] = Field(None, alias='jobTierTwoField')

    # third job tier associated with the comp band
    job_tier_three_field: typing.Optional[str] = Field(None, alias='jobTierThreeField')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
