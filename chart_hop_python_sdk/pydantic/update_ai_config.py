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

from chart_hop_python_sdk.pydantic.ai_model_config import AiModelConfig

class UpdateAiConfig(BaseModel):
    form_response_summary_config: typing.Optional[AiModelConfig] = Field(None, alias='formResponseSummaryConfig')

    form_response_combine_summary_config: typing.Optional[AiModelConfig] = Field(None, alias='formResponseCombineSummaryConfig')

    report_result_summary_config: typing.Optional[AiModelConfig] = Field(None, alias='reportResultSummaryConfig')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
