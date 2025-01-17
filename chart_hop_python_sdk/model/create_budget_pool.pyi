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


class CreateBudgetPool(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "sourceField",
            "appliedField",
            "basisType",
            "compReviewId",
            "label",
        }
        
        class properties:
            compReviewId = schemas.StrSchema
            label = schemas.StrSchema
            appliedField = schemas.StrSchema
            sourceField = schemas.StrSchema
            
            
            class basisType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("CUSTOM")
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("FIXED")
                
                @schemas.classproperty
                def CUSTOM_FIXED(cls):
                    return cls("CUSTOM_FIXED")
                
                @schemas.classproperty
                def PERCENTAGE(cls):
                    return cls("PERCENTAGE")
                
                @schemas.classproperty
                def CUSTOM_PERCENTAGE(cls):
                    return cls("CUSTOM_PERCENTAGE")
            participantsExpr = schemas.StrSchema
        
            @staticmethod
            def fixedAmount() -> typing.Type['Money']:
                return Money
            fixedValue = schemas.NumberSchema
        
            @staticmethod
            def basisFieldMatrix() -> typing.Type['BasisFieldMatrix']:
                return BasisFieldMatrix
        
            @staticmethod
            def fixedBudgetMap() -> typing.Type['CreateBudgetPoolFixedBudgetMap']:
                return CreateBudgetPoolFixedBudgetMap
            basisExpr = schemas.StrSchema
            defaultCurrency = schemas.StrSchema
            __annotations__ = {
                "compReviewId": compReviewId,
                "label": label,
                "appliedField": appliedField,
                "sourceField": sourceField,
                "basisType": basisType,
                "participantsExpr": participantsExpr,
                "fixedAmount": fixedAmount,
                "fixedValue": fixedValue,
                "basisFieldMatrix": basisFieldMatrix,
                "fixedBudgetMap": fixedBudgetMap,
                "basisExpr": basisExpr,
                "defaultCurrency": defaultCurrency,
            }
    
    sourceField: MetaOapg.properties.sourceField
    appliedField: MetaOapg.properties.appliedField
    basisType: MetaOapg.properties.basisType
    compReviewId: MetaOapg.properties.compReviewId
    label: MetaOapg.properties.label
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compReviewId"]) -> MetaOapg.properties.compReviewId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appliedField"]) -> MetaOapg.properties.appliedField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceField"]) -> MetaOapg.properties.sourceField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basisType"]) -> MetaOapg.properties.basisType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participantsExpr"]) -> MetaOapg.properties.participantsExpr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixedAmount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixedValue"]) -> MetaOapg.properties.fixedValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basisFieldMatrix"]) -> 'BasisFieldMatrix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixedBudgetMap"]) -> 'CreateBudgetPoolFixedBudgetMap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basisExpr"]) -> MetaOapg.properties.basisExpr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultCurrency"]) -> MetaOapg.properties.defaultCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["compReviewId", "label", "appliedField", "sourceField", "basisType", "participantsExpr", "fixedAmount", "fixedValue", "basisFieldMatrix", "fixedBudgetMap", "basisExpr", "defaultCurrency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compReviewId"]) -> MetaOapg.properties.compReviewId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appliedField"]) -> MetaOapg.properties.appliedField: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceField"]) -> MetaOapg.properties.sourceField: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basisType"]) -> MetaOapg.properties.basisType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participantsExpr"]) -> typing.Union[MetaOapg.properties.participantsExpr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixedAmount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixedValue"]) -> typing.Union[MetaOapg.properties.fixedValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basisFieldMatrix"]) -> typing.Union['BasisFieldMatrix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixedBudgetMap"]) -> typing.Union['CreateBudgetPoolFixedBudgetMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basisExpr"]) -> typing.Union[MetaOapg.properties.basisExpr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultCurrency"]) -> typing.Union[MetaOapg.properties.defaultCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["compReviewId", "label", "appliedField", "sourceField", "basisType", "participantsExpr", "fixedAmount", "fixedValue", "basisFieldMatrix", "fixedBudgetMap", "basisExpr", "defaultCurrency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sourceField: typing.Union[MetaOapg.properties.sourceField, str, ],
        appliedField: typing.Union[MetaOapg.properties.appliedField, str, ],
        basisType: typing.Union[MetaOapg.properties.basisType, str, ],
        compReviewId: typing.Union[MetaOapg.properties.compReviewId, str, ],
        label: typing.Union[MetaOapg.properties.label, str, ],
        participantsExpr: typing.Union[MetaOapg.properties.participantsExpr, str, schemas.Unset] = schemas.unset,
        fixedAmount: typing.Union['Money', schemas.Unset] = schemas.unset,
        fixedValue: typing.Union[MetaOapg.properties.fixedValue, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        basisFieldMatrix: typing.Union['BasisFieldMatrix', schemas.Unset] = schemas.unset,
        fixedBudgetMap: typing.Union['CreateBudgetPoolFixedBudgetMap', schemas.Unset] = schemas.unset,
        basisExpr: typing.Union[MetaOapg.properties.basisExpr, str, schemas.Unset] = schemas.unset,
        defaultCurrency: typing.Union[MetaOapg.properties.defaultCurrency, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateBudgetPool':
        return super().__new__(
            cls,
            *args,
            sourceField=sourceField,
            appliedField=appliedField,
            basisType=basisType,
            compReviewId=compReviewId,
            label=label,
            participantsExpr=participantsExpr,
            fixedAmount=fixedAmount,
            fixedValue=fixedValue,
            basisFieldMatrix=basisFieldMatrix,
            fixedBudgetMap=fixedBudgetMap,
            basisExpr=basisExpr,
            defaultCurrency=defaultCurrency,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.basis_field_matrix import BasisFieldMatrix
from chart_hop_python_sdk.model.create_budget_pool_fixed_budget_map import CreateBudgetPoolFixedBudgetMap
from chart_hop_python_sdk.model.money import Money
