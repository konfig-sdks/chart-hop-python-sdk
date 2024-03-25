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


class UpdateProcess(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PENDING": "PENDING",
                        "RUNNING": "RUNNING",
                        "DONE": "DONE",
                        "ERROR": "ERROR",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("DONE")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
            filePath = schemas.StrSchema
            message = schemas.StrSchema
            progress = schemas.Float64Schema
            internalError = schemas.StrSchema
            options = schemas.DictSchema
        
            @staticmethod
            def results() -> typing.Type['UpdateProcessResults']:
                return UpdateProcessResults
            
            
            class logDataList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LogData']:
                        return LogData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LogData'], typing.List['LogData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'logDataList':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LogData':
                    return super().__getitem__(i)
            state = schemas.DictSchema
            appId = schemas.StrSchema
            __annotations__ = {
                "status": status,
                "filePath": filePath,
                "message": message,
                "progress": progress,
                "internalError": internalError,
                "options": options,
                "results": results,
                "logDataList": logDataList,
                "state": state,
                "appId": appId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filePath"]) -> MetaOapg.properties.filePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalError"]) -> MetaOapg.properties.internalError: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> 'UpdateProcessResults': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logDataList"]) -> MetaOapg.properties.logDataList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "filePath", "message", "progress", "internalError", "options", "results", "logDataList", "state", "appId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filePath"]) -> typing.Union[MetaOapg.properties.filePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress"]) -> typing.Union[MetaOapg.properties.progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalError"]) -> typing.Union[MetaOapg.properties.internalError, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union['UpdateProcessResults', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logDataList"]) -> typing.Union[MetaOapg.properties.logDataList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> typing.Union[MetaOapg.properties.appId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "filePath", "message", "progress", "internalError", "options", "results", "logDataList", "state", "appId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        filePath: typing.Union[MetaOapg.properties.filePath, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        progress: typing.Union[MetaOapg.properties.progress, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        internalError: typing.Union[MetaOapg.properties.internalError, str, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        results: typing.Union['UpdateProcessResults', schemas.Unset] = schemas.unset,
        logDataList: typing.Union[MetaOapg.properties.logDataList, list, tuple, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        appId: typing.Union[MetaOapg.properties.appId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateProcess':
        return super().__new__(
            cls,
            *args,
            status=status,
            filePath=filePath,
            message=message,
            progress=progress,
            internalError=internalError,
            options=options,
            results=results,
            logDataList=logDataList,
            state=state,
            appId=appId,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.log_data import LogData
from chart_hop_python_sdk.model.update_process_results import UpdateProcessResults