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

from chart_hop_python_sdk.type.log_data import LogData
from chart_hop_python_sdk.type.process_results import ProcessResults

class RequiredProcess(TypedDict):
    # globally unique id
    id: str

    # parent org id
    orgId: str

    # human-readable label that identifies this process
    label: str

    # process type
    type: str

    # current status of process
    status: str

    # user id who is running the process
    runUserId: str

    # created by user id (user who requested the process run)
    createId: str

    # created timestamp
    createAt: str

    # options passed to the process
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalProcess(TypedDict, total=False):
    # data file path
    filePath: str

    # data log path
    logPath: str

    # process id of parent process
    parentProcessId: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # started at timestamp
    startAt: str

    # ended at timestamp
    endAt: str

    # status or error message
    message: str

    # percent progress so far
    progress: typing.Union[int, float]

    # internal-only error message
    internalError: str

    results: ProcessResults

    # list of log data that occurred during running of this process
    logDataList: typing.List[LogData]

    # process-specific state data
    state: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # app id of the process
    appId: str

    # unique ID of the process at queue time
    uuid: str

class Process(RequiredProcess, OptionalProcess):
    pass
