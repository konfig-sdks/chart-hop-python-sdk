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

from chart_hop_python_sdk.type.money import Money

class RequiredCompensationBandsConfig(TypedDict):
    # whether annualized salaries are used
    annualizedSalaries: bool

    # whether hourly salaries are used
    hourlySalaries: bool

    # how many hours per week to use when calculating comp bands
    hoursPerWeek: typing.Union[int, float]

    # how many weeks per year to use when calculating comp bands
    weeksPerYear: typing.Union[int, float]

    # target salary within a comp band
    hasTargetSalary: bool

    # whether the org's location data is used as multipliers
    hasLocationMultiplier: bool

    # currency rounding settings in the UI
    currencyRounding: typing.List[Money]

class OptionalCompensationBandsConfig(TypedDict, total=False):
    # how annualized salaries are represented
    annualizedSalariesType: str

    # how hourly salaries are represented
    hourlySalariesType: str

    # how target salaries are represented
    targetSalaryType: str

    # equity format
    equityFormat: str

    # variable bonus format
    variableBonusFormat: str

    # whether or not the tiers are mapped to fields. after we migrate all the tiers to be mapped, this flag can be removed
    tiersNotMappedToCodes: bool

    # the org's first tier for their comp bands
    firstTier: str

    # the org's second tier for their comp bands
    secondTier: str

    # the org's third tier for their comp bands
    thirdTier: str

    # the source for the band job levels
    jobLevelSource: str

    # comparable market job level system
    marketJobLevelSystem: str

    # has migrated V1 bands
    hasMigratedBands: bool

class CompensationBandsConfig(RequiredCompensationBandsConfig, OptionalCompensationBandsConfig):
    pass
