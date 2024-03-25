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


class CompReviewEligibleEmployeesExcludedEmploymentStatuses(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Exclude these employment types if specified
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def FULL(cls):
                return cls("FULL")
            
            @schemas.classproperty
            def PART(cls):
                return cls("PART")
            
            @schemas.classproperty
            def TEMP(cls):
                return cls("TEMP")
            
            @schemas.classproperty
            def CONTRACT(cls):
                return cls("CONTRACT")
            
            @schemas.classproperty
            def INTERN(cls):
                return cls("INTERN")
            
            @schemas.classproperty
            def EXPAT(cls):
                return cls("EXPAT")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CompReviewEligibleEmployeesExcludedEmploymentStatuses':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
