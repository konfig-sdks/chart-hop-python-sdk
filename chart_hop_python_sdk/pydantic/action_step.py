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

from chart_hop_python_sdk.pydantic.action_step_http_headers import ActionStepHttpHeaders

class ActionStep(BaseModel):
    # The type of action to run
    type: Literal["FORM", "MESSAGE", "HTTP", "TASK"] = Field(alias='type')

    # unique id for action step
    step_id: typing.Optional[str] = Field(None, alias='stepId')

    # If the action is FORM, the id of the form to fill out
    form_id: typing.Optional[str] = Field(None, alias='formId')

    # If the action is MESSAGE, the target to send the message to. If the action is FORM/TASK, the person who should have the form filled out on/complete the task
    target: typing.Optional[str] = Field(None, alias='target')

    # If the action is FORM/TASK, the user who should fill out the form/complete the task (default is, same as target)
    assignee: typing.Optional[str] = Field(None, alias='assignee')

    # The message that will be sent -- supports CQLT templates
    message: typing.Optional[str] = Field(None, alias='message')

    # The email subject line that will be used -- supports CQLT templates. If not provided, will use 'Notification'
    email_subject: typing.Optional[str] = Field(None, alias='emailSubject')

    # whether to run with access to sensitive events or not - if this is left blank, will default to the sensitive setting of the Action
    sensitive: typing.Optional[bool] = Field(None, alias='sensitive')

    # If the action is HTTP, the url that will receive the HTTP request
    http_url: typing.Optional[str] = Field(None, alias='httpUrl')

    # If the action is HTTP, the method used by the HTTP request (defaults to POST)
    http_method: typing.Optional[str] = Field(None, alias='httpMethod')

    http_headers: typing.Optional[ActionStepHttpHeaders] = Field(None, alias='httpHeaders')

    # If the action is HTTP, the payload contained in the HTTP request
    http_content: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='httpContent')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
