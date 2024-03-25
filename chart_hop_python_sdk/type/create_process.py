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

from chart_hop_python_sdk.type.create_process_results import CreateProcessResults
from chart_hop_python_sdk.type.log_data import LogData

class RequiredCreateProcess(TypedDict):
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

    # options passed to the process
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalCreateProcess(TypedDict, total=False):
    # data file path
    filePath: str

    # process id of parent process
    parentProcessId: str

    # status or error message
    message: str

    # percent progress so far
    progress: typing.Union[int, float]

    # internal-only error message
    internalError: str

    results: CreateProcessResults

    # list of log data that occurred during running of this process
    logDataList: typing.List[LogData]

    # process-specific state data
    state: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # app id of the process
    appId: str

    # unique ID of the process at queue time
    uuid: str

class CreateProcess(RequiredCreateProcess, OptionalCreateProcess):
    pass
