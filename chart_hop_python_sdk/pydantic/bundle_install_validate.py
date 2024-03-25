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

from chart_hop_python_sdk.pydantic.bundle_install_entity import BundleInstallEntity
from chart_hop_python_sdk.pydantic.bundle_install_validate_errors import BundleInstallValidateErrors

class BundleInstallValidate(BaseModel):
    ok: bool = Field(alias='ok')

    duplicate_entities: typing.Optional[typing.List[BundleInstallEntity]] = Field(None, alias='duplicateEntities')

    errors: typing.Optional[BundleInstallValidateErrors] = Field(None, alias='errors')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
