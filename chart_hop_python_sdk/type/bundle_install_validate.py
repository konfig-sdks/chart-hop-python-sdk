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

from chart_hop_python_sdk.type.bundle_install_entity import BundleInstallEntity
from chart_hop_python_sdk.type.bundle_install_validate_errors import BundleInstallValidateErrors

class RequiredBundleInstallValidate(TypedDict):
    ok: bool

class OptionalBundleInstallValidate(TypedDict, total=False):
    duplicateEntities: typing.List[BundleInstallEntity]

    errors: BundleInstallValidateErrors

class BundleInstallValidate(RequiredBundleInstallValidate, OptionalBundleInstallValidate):
    pass
