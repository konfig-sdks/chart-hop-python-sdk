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
from chart_hop_python_sdk.pydantic.job_tier_field import JobTierField
from chart_hop_python_sdk.pydantic.money import Money
from chart_hop_python_sdk.pydantic.table_row_ref import TableRowRef

class CompBand(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: str = Field(alias='orgId')

    # human-readable name of content
    label: str = Field(alias='label')

    # hex color associated with the band level
    color: str = Field(alias='color')

    base_interval: EnumValue = Field(alias='baseInterval')

    base_comp_max: typing.Optional[Money] = Field(None, alias='baseCompMax')

    base_comp_mid: typing.Optional[Money] = Field(None, alias='baseCompMid')

    base_comp_min: typing.Optional[Money] = Field(None, alias='baseCompMin')

    # spread percent used to calculate base comp from the midpoint
    base_spread: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseSpread')

    base_target_pay: typing.Optional[Money] = Field(None, alias='baseTargetPay')

    # target pay associated with open jobs at this band level, specified as a percentile of [min,max]
    base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = Field(None, alias='baseTargetPayPercentile')

    job_tier_one_field: typing.Optional[JobTierField] = Field(None, alias='jobTierOneField')

    job_tier_two_field: typing.Optional[JobTierField] = Field(None, alias='jobTierTwoField')

    job_tier_three_field: typing.Optional[JobTierField] = Field(None, alias='jobTierThreeField')

    job_level: typing.Optional[TableRowRef] = Field(None, alias='jobLevel')

    # target equity for the band, in shares
    equity_target_shares: typing.Optional[typing.Union[int, float]] = Field(None, alias='equityTargetShares')

    # target equity for the band, as a percentage of base
    equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = Field(None, alias='equityTargetPercentOfBase')

    # target equity for the band, as a monetary value, in the same currency as the base
    equity_target_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='equityTargetValue')

    variable_value: typing.Optional[Money] = Field(None, alias='variableValue')

    # variable compensation for the band, specified as a percentage of base
    variable_percent_of_base: typing.Optional[typing.Union[int, float]] = Field(None, alias='variablePercentOfBase')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
