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

from chart_hop_python_sdk.pydantic.money import Money

class CompensationBandsConfig(BaseModel):
    # whether annualized salaries are used
    annualized_salaries: bool = Field(alias='annualizedSalaries')

    # whether hourly salaries are used
    hourly_salaries: bool = Field(alias='hourlySalaries')

    # how many hours per week to use when calculating comp bands
    hours_per_week: typing.Union[int, float] = Field(alias='hoursPerWeek')

    # how many weeks per year to use when calculating comp bands
    weeks_per_year: typing.Union[int, float] = Field(alias='weeksPerYear')

    # target salary within a comp band
    has_target_salary: bool = Field(alias='hasTargetSalary')

    # whether the org's location data is used as multipliers
    has_location_multiplier: bool = Field(alias='hasLocationMultiplier')

    # currency rounding settings in the UI
    currency_rounding: typing.List[Money] = Field(alias='currencyRounding')

    # how annualized salaries are represented
    annualized_salaries_type: typing.Optional[str] = Field(None, alias='annualizedSalariesType')

    # how hourly salaries are represented
    hourly_salaries_type: typing.Optional[str] = Field(None, alias='hourlySalariesType')

    # how target salaries are represented
    target_salary_type: typing.Optional[str] = Field(None, alias='targetSalaryType')

    # equity format
    equity_format: typing.Optional[str] = Field(None, alias='equityFormat')

    # variable bonus format
    variable_bonus_format: typing.Optional[str] = Field(None, alias='variableBonusFormat')

    # whether or not the tiers are mapped to fields. after we migrate all the tiers to be mapped, this flag can be removed
    tiers_not_mapped_to_codes: typing.Optional[bool] = Field(None, alias='tiersNotMappedToCodes')

    # the org's first tier for their comp bands
    first_tier: typing.Optional[str] = Field(None, alias='firstTier')

    # the org's second tier for their comp bands
    second_tier: typing.Optional[str] = Field(None, alias='secondTier')

    # the org's third tier for their comp bands
    third_tier: typing.Optional[str] = Field(None, alias='thirdTier')

    # the source for the band job levels
    job_level_source: typing.Optional[str] = Field(None, alias='jobLevelSource')

    # comparable market job level system
    market_job_level_system: typing.Optional[str] = Field(None, alias='marketJobLevelSystem')

    # has migrated V1 bands
    has_migrated_bands: typing.Optional[bool] = Field(None, alias='hasMigratedBands')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
