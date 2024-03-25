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

from chart_hop_python_sdk.pydantic.log_data import LogData
from chart_hop_python_sdk.pydantic.process_results import ProcessResults

class Process(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

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

    # created by user id (user who requested the process run)
    create_id: str = Field(alias='createId')

    # created timestamp
    create_at: str = Field(alias='createAt')

    # options passed to the process
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='options')

    # data file path
    file_path: typing.Optional[str] = Field(None, alias='filePath')

    # data log path
    log_path: typing.Optional[str] = Field(None, alias='logPath')

    # process id of parent process
    parent_process_id: typing.Optional[str] = Field(None, alias='parentProcessId')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # started at timestamp
    start_at: typing.Optional[str] = Field(None, alias='startAt')

    # ended at timestamp
    end_at: typing.Optional[str] = Field(None, alias='endAt')

    # status or error message
    message: typing.Optional[str] = Field(None, alias='message')

    # percent progress so far
    progress: typing.Optional[typing.Union[int, float]] = Field(None, alias='progress')

    # internal-only error message
    internal_error: typing.Optional[str] = Field(None, alias='internalError')

    results: typing.Optional[ProcessResults] = Field(None, alias='results')

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
