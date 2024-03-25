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

from chart_hop_python_sdk.pydantic.deviation import Deviation
from chart_hop_python_sdk.pydantic.guideline_calculation_fields import GuidelineCalculationFields

class GuidelineCalculation(BaseModel):
    guideline_id: str = Field(alias='guidelineId')

    job_id: str = Field(alias='jobId')

    comp_review_id: str = Field(alias='compReviewId')

    guideline_label: str = Field(alias='guidelineLabel')

    applied_field: str = Field(alias='appliedField')

    flag_mode: Literal["DEVIATION_THRESHOLD", "NONE"] = Field(alias='flagMode')

    is_deviated: bool = Field(alias='isDeviated')

    deviation: Deviation = Field(alias='deviation')

    fields: GuidelineCalculationFields = Field(alias='fields')

    budget_pool_id: typing.Optional[str] = Field(None, alias='budgetPoolId')

    min: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='min')

    max: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='max')

    target: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='target')

    flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = Field(None, alias='flagDeviationThreshold')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
