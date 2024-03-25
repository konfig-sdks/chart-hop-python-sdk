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

from chart_hop_python_sdk.type.action_step_http_headers import ActionStepHttpHeaders

class RequiredActionStep(TypedDict):
    # The type of action to run
    type: str

class OptionalActionStep(TypedDict, total=False):
    # unique id for action step
    stepId: str

    # If the action is FORM, the id of the form to fill out
    formId: str

    # If the action is MESSAGE, the target to send the message to. If the action is FORM/TASK, the person who should have the form filled out on/complete the task
    target: str

    # If the action is FORM/TASK, the user who should fill out the form/complete the task (default is, same as target)
    assignee: str

    # The message that will be sent -- supports CQLT templates
    message: str

    # The email subject line that will be used -- supports CQLT templates. If not provided, will use 'Notification'
    emailSubject: str

    # whether to run with access to sensitive events or not - if this is left blank, will default to the sensitive setting of the Action
    sensitive: bool

    # If the action is HTTP, the url that will receive the HTTP request
    httpUrl: str

    # If the action is HTTP, the method used by the HTTP request (defaults to POST)
    httpMethod: str

    httpHeaders: ActionStepHttpHeaders

    # If the action is HTTP, the payload contained in the HTTP request
    httpContent: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class ActionStep(RequiredActionStep, OptionalActionStep):
    pass
