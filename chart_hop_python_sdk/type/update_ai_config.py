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

from chart_hop_python_sdk.type.ai_model_config import AiModelConfig

class RequiredUpdateAiConfig(TypedDict):
    pass

class OptionalUpdateAiConfig(TypedDict, total=False):
    formResponseSummaryConfig: AiModelConfig

    formResponseCombineSummaryConfig: AiModelConfig

    reportResultSummaryConfig: AiModelConfig

class UpdateAiConfig(RequiredUpdateAiConfig, OptionalUpdateAiConfig):
    pass
