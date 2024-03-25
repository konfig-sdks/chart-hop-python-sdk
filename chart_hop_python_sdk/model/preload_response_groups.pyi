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


class PreloadResponseGroups(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PreloadResponseGroupsItem']:
            return PreloadResponseGroupsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PreloadResponseGroupsItem'], typing.List['PreloadResponseGroupsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PreloadResponseGroups':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PreloadResponseGroupsItem':
        return super().__getitem__(i)

from chart_hop_python_sdk.model.preload_response_groups_item import PreloadResponseGroupsItem
