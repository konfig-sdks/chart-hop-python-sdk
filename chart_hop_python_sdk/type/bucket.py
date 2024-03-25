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

from chart_hop_python_sdk.type.bucket_approver_map import BucketApproverMap

class RequiredBucket(TypedDict):
    bucket: typing.Union[int, float]

    approverMap: BucketApproverMap

class OptionalBucket(TypedDict, total=False):
    pass

class Bucket(RequiredBucket, OptionalBucket):
    pass
