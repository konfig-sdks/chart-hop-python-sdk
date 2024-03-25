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

from chart_hop_python_sdk.type.validate_expression_result import ValidateExpressionResult

class RequiredValidateExpressionResponse(TypedDict):
    isValid: bool

    results: typing.List[ValidateExpressionResult]

class OptionalValidateExpressionResponse(TypedDict, total=False):
    pass

class ValidateExpressionResponse(RequiredValidateExpressionResponse, OptionalValidateExpressionResponse):
    pass
