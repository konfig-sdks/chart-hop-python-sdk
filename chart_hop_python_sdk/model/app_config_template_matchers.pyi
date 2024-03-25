# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from chart_hop_python_sdk import schemas  # noqa: F401


class AppConfigTemplateMatchers(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    template field matchers defined by a user
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['AppConfigTemplateMatchersItem']:
            return AppConfigTemplateMatchersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['AppConfigTemplateMatchersItem'], typing.List['AppConfigTemplateMatchersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AppConfigTemplateMatchers':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AppConfigTemplateMatchersItem':
        return super().__getitem__(i)

from chart_hop_python_sdk.model.app_config_template_matchers_item import AppConfigTemplateMatchersItem
