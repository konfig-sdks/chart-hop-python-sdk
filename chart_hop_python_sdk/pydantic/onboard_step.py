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


class OnboardStep(BaseModel):
    # customer facing description
    description: str = Field(alias='description')

    # unique id
    id: str = Field(alias='id')

    # unique string that briefly describes the onboard step
    name: str = Field(alias='name')

    # customer facing identifier
    label: str = Field(alias='label')

    # url for charthop docs that describe how to accomplish this step
    docs_url: str = Field(alias='docsUrl')

    # url for charthop page that where this step can be completed
    action_url: str = Field(alias='actionUrl')

    # text that shows up on the 'action button' of the card for this step
    action_text: str = Field(alias='actionText')

    # file name of the picture for the step (does not include path)
    picture_file_name: str = Field(alias='pictureFileName')

    # numerical position for which the step appears in relationship to other onboard steps
    sort: int = Field(alias='sort')

    # event type (in the format of <COLLECTION NAME>.<CHANGE TYPE>) that triggers the completion of this onboard step
    event_type: str = Field(alias='eventType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
