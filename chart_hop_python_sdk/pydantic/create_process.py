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

from chart_hop_python_sdk.pydantic.create_process_results import CreateProcessResults
from chart_hop_python_sdk.pydantic.log_data import LogData

class CreateProcess(BaseModel):
    # parent org id
    org_id: str = Field(alias='orgId')

    # human-readable label that identifies this process
    label: str = Field(alias='label')

    # process type
    type: str = Field(alias='type')

    # current status of process
    status: Literal["PENDING", "RUNNING", "DONE", "ERROR"] = Field(alias='status')

    # user id who is running the process
    run_user_id: str = Field(alias='runUserId')

    # options passed to the process
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='options')

    # data file path
    file_path: typing.Optional[str] = Field(None, alias='filePath')

    # process id of parent process
    parent_process_id: typing.Optional[str] = Field(None, alias='parentProcessId')

    # status or error message
    message: typing.Optional[str] = Field(None, alias='message')

    # percent progress so far
    progress: typing.Optional[typing.Union[int, float]] = Field(None, alias='progress')

    # internal-only error message
    internal_error: typing.Optional[str] = Field(None, alias='internalError')

    results: typing.Optional[CreateProcessResults] = Field(None, alias='results')

    # list of log data that occurred during running of this process
    log_data_list: typing.Optional[typing.List[LogData]] = Field(None, alias='logDataList')

    # process-specific state data
    state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='state')

    # app id of the process
    app_id: typing.Optional[str] = Field(None, alias='appId')

    # unique ID of the process at queue time
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
