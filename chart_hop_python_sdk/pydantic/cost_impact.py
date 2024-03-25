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

from chart_hop_python_sdk.pydantic.cost_impact_months import CostImpactMonths

class CostImpact(BaseModel):
    # total annual run-rate impact
    annual: typing.Union[int, float] = Field(alias='annual')

    # first month to be affected
    first_month: str = Field(alias='firstMonth')

    months: CostImpactMonths = Field(alias='months')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
