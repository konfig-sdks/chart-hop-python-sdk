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

from chart_hop_python_sdk.pydantic.process_event_entity_data import ProcessEventEntityData
from chart_hop_python_sdk.pydantic.process_event_update import ProcessEventUpdate

class ProcessEvent(BaseModel):
    type: Literal["HIRE", "UPDATE", "CREATE_PERSON", "ERROR", "INBOUND", "CHANGE", "OUTBOUND_CREATE", "OUTBOUND_UPDATE", "OUTBOUND_DELETE", "INITIATING_CREATE", "INITIATING_UPDATE", "INITIATING_DELETE"] = Field(alias='type')

    updates: typing.List[ProcessEventUpdate] = Field(alias='updates')

    at: int = Field(alias='at')

    id: typing.Optional[str] = Field(None, alias='id')

    entity_data: typing.Optional[ProcessEventEntityData] = Field(None, alias='entityData')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
