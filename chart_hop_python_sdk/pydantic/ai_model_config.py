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


class AiModelConfig(BaseModel):
    model_id: str = Field(alias='modelId')

    prompt_before: str = Field(alias='promptBefore')

    prompt_after: str = Field(alias='promptAfter')

    max_tokens: int = Field(alias='maxTokens')

    temperature: typing.Union[int, float] = Field(alias='temperature')

    top_p: int = Field(alias='topP')

    max_string_length: int = Field(alias='maxStringLength')

    stop_sequences: typing.Optional[str] = Field(None, alias='stopSequences')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
