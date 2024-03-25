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


class RequiredAiModelConfig(TypedDict):
    modelId: str

    promptBefore: str

    promptAfter: str

    maxTokens: int

    temperature: typing.Union[int, float]

    topP: int

    maxStringLength: int

class OptionalAiModelConfig(TypedDict, total=False):
    stopSequences: str

class AiModelConfig(RequiredAiModelConfig, OptionalAiModelConfig):
    pass
