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


class ProductFeatures(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    set of features this product has access to
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def ATS_SYNC(cls):
                return cls("ATS_SYNC")
            
            @schemas.classproperty
            def COMPENSATION_REVIEW(cls):
                return cls("COMPENSATION_REVIEW")
            
            @schemas.classproperty
            def CUSTOM_FIELD(cls):
                return cls("CUSTOM_FIELD")
            
            @schemas.classproperty
            def CUSTOM_FIELD_READONLY(cls):
                return cls("CUSTOM_FIELD_READONLY")
            
            @schemas.classproperty
            def CUSTOM_FORM(cls):
                return cls("CUSTOM_FORM")
            
            @schemas.classproperty
            def CUSTOM_PROFILE_TAB(cls):
                return cls("CUSTOM_PROFILE_TAB")
            
            @schemas.classproperty
            def CUSTOM_ROLE(cls):
                return cls("CUSTOM_ROLE")
            
            @schemas.classproperty
            def MULTI_PAYROLL(cls):
                return cls("MULTI_PAYROLL")
            
            @schemas.classproperty
            def PERFORMANCE_REVIEW(cls):
                return cls("PERFORMANCE_REVIEW")
            
            @schemas.classproperty
            def REPORT(cls):
                return cls("REPORT")
            
            @schemas.classproperty
            def REPORT_READONLY(cls):
                return cls("REPORT_READONLY")
            
            @schemas.classproperty
            def SCENARIO(cls):
                return cls("SCENARIO")
            
            @schemas.classproperty
            def SURVEY(cls):
                return cls("SURVEY")
            
            @schemas.classproperty
            def TABLE(cls):
                return cls("TABLE")
            
            @schemas.classproperty
            def TEMPLATE(cls):
                return cls("TEMPLATE")
            
            @schemas.classproperty
            def WORKDAY_ADAPTIVE(cls):
                return cls("WORKDAY_ADAPTIVE")
            
            @schemas.classproperty
            def PAYROLL_OUTBOUND(cls):
                return cls("PAYROLL_OUTBOUND")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProductFeatures':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
