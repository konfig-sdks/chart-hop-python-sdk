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


class CompReviewReviewerWorkbook(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "columns",
        }
        
        class properties:
            
            
            class columns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CompReviewWorkbookColumn']:
                        return CompReviewWorkbookColumn
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CompReviewWorkbookColumn'], typing.List['CompReviewWorkbookColumn']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columns':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CompReviewWorkbookColumn':
                    return super().__getitem__(i)
            numFrozenColumns = schemas.Int32Schema
            moreInfoUrl = schemas.StrSchema
            moreInfoLabel = schemas.StrSchema
            isEdited = schemas.BoolSchema
            __annotations__ = {
                "columns": columns,
                "numFrozenColumns": numFrozenColumns,
                "moreInfoUrl": moreInfoUrl,
                "moreInfoLabel": moreInfoLabel,
                "isEdited": isEdited,
            }
    
    columns: MetaOapg.properties.columns
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numFrozenColumns"]) -> MetaOapg.properties.numFrozenColumns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moreInfoUrl"]) -> MetaOapg.properties.moreInfoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moreInfoLabel"]) -> MetaOapg.properties.moreInfoLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEdited"]) -> MetaOapg.properties.isEdited: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["columns", "numFrozenColumns", "moreInfoUrl", "moreInfoLabel", "isEdited", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numFrozenColumns"]) -> typing.Union[MetaOapg.properties.numFrozenColumns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moreInfoUrl"]) -> typing.Union[MetaOapg.properties.moreInfoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moreInfoLabel"]) -> typing.Union[MetaOapg.properties.moreInfoLabel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEdited"]) -> typing.Union[MetaOapg.properties.isEdited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["columns", "numFrozenColumns", "moreInfoUrl", "moreInfoLabel", "isEdited", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        columns: typing.Union[MetaOapg.properties.columns, list, tuple, ],
        numFrozenColumns: typing.Union[MetaOapg.properties.numFrozenColumns, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        moreInfoUrl: typing.Union[MetaOapg.properties.moreInfoUrl, str, schemas.Unset] = schemas.unset,
        moreInfoLabel: typing.Union[MetaOapg.properties.moreInfoLabel, str, schemas.Unset] = schemas.unset,
        isEdited: typing.Union[MetaOapg.properties.isEdited, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompReviewReviewerWorkbook':
        return super().__new__(
            cls,
            *args,
            columns=columns,
            numFrozenColumns=numFrozenColumns,
            moreInfoUrl=moreInfoUrl,
            moreInfoLabel=moreInfoLabel,
            isEdited=isEdited,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.comp_review_workbook_column import CompReviewWorkbookColumn