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
from chart_hop_python_sdk.type.update_process_results import UpdateProcessResults

class RequiredUpdateProcess(TypedDict):
    pass

class OptionalUpdateProcess(TypedDict, total=False):
    # current status of process
    status: str

    # data file path
    filePath: str

    # status or error message
    message: str

    # percent progress so far
    progress: typing.Union[int, float]

    # internal-only error message
    internalError: str

    # options passed to the process
    options: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    results: UpdateProcessResults

    # list of log data that occurred during running of this process
    logDataList: typing.List[LogData]

    # process-specific state data
    state: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # app id of the process
    appId: str

class UpdateProcess(RequiredUpdateProcess, OptionalUpdateProcess):
    pass
