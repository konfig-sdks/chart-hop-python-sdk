# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from chart_hop_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from chart_hop_python_sdk.api_response import AsyncGeneratorResponse
from chart_hop_python_sdk import api_client, exceptions
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

from chart_hop_python_sdk.model.process_create_pending_process_request import ProcessCreatePendingProcessRequest as ProcessCreatePendingProcessRequestSchema

from chart_hop_python_sdk.type.process_create_pending_process_request import ProcessCreatePendingProcessRequest

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.process_create_pending_process_request import ProcessCreatePendingProcessRequest as ProcessCreatePendingProcessRequestPydantic

# Query params
TypeSchema = schemas.StrSchema
MaxRowsSchema = schemas.Int32Schema
MinColumnsSchema = schemas.Int32Schema
IsSyncSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'type': typing.Union[TypeSchema, str, ],
        'maxRows': typing.Union[MaxRowsSchema, decimal.Decimal, int, ],
        'minColumns': typing.Union[MinColumnsSchema, decimal.Decimal, int, ],
        'isSync': typing.Union[IsSyncSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_max_rows = api_client.QueryParameter(
    name="maxRows",
    style=api_client.ParameterStyle.FORM,
    schema=MaxRowsSchema,
    explode=True,
)
request_query_min_columns = api_client.QueryParameter(
    name="minColumns",
    style=api_client.ParameterStyle.FORM,
    schema=MinColumnsSchema,
    explode=True,
)
request_query_is_sync = api_client.QueryParameter(
    name="isSync",
    style=api_client.ParameterStyle.FORM,
    schema=IsSyncSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_org_id = api_client.PathParameter(
    name="orgId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrgIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyMultipartFormData = ProcessCreatePendingProcessRequestSchema


request_body_process_create_pending_process_request = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


class BaseApi(api_client.Api):

    def _create_pending_process_mapped_args(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if file is not None:
            _body["file"] = file
        if state is not None:
            _body["state"] = state
        args.body = _body
        if type is not None:
            _query_params["type"] = type
        if max_rows is not None:
            _query_params["maxRows"] = max_rows
        if min_columns is not None:
            _query_params["minColumns"] = min_columns
        if is_sync is not None:
            _query_params["isSync"] = is_sync
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_pending_process_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Creates a new process in the pending state
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_max_rows,
            request_query_min_columns,
            request_query_is_sync,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/process/self-serve',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_process_create_pending_process_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_pending_process_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Creates a new process in the pending state
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_type,
            request_query_max_rows,
            request_query_min_columns,
            request_query_is_sync,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/process/self-serve',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_process_create_pending_process_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreatePendingProcessRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_pending_process(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_pending_process_mapped_args(
            org_id=org_id,
            type=type,
            max_rows=max_rows,
            min_columns=min_columns,
            is_sync=is_sync,
            file=file,
            state=state,
        )
        return await self._acreate_pending_process_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_pending_process(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_pending_process_mapped_args(
            org_id=org_id,
            type=type,
            max_rows=max_rows,
            min_columns=min_columns,
            is_sync=is_sync,
            file=file,
            state=state,
        )
        return self._create_pending_process_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class CreatePendingProcess(BaseApi):

    async def acreate_pending_process(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_pending_process(
            org_id=org_id,
            type=type,
            max_rows=max_rows,
            min_columns=min_columns,
            is_sync=is_sync,
            file=file,
            state=state,
            **kwargs,
        )
    
    
    def create_pending_process(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_pending_process(
            org_id=org_id,
            type=type,
            max_rows=max_rows,
            min_columns=min_columns,
            is_sync=is_sync,
            file=file,
            state=state,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_pending_process_mapped_args(
            org_id=org_id,
            type=type,
            max_rows=max_rows,
            min_columns=min_columns,
            is_sync=is_sync,
            file=file,
            state=state,
        )
        return await self._acreate_pending_process_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        org_id: str,
        type: typing.Optional[str] = None,
        max_rows: typing.Optional[int] = None,
        min_columns: typing.Optional[int] = None,
        is_sync: typing.Optional[bool] = None,
        file: typing.Optional[typing.IO] = None,
        state: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_pending_process_mapped_args(
            org_id=org_id,
            type=type,
            max_rows=max_rows,
            min_columns=min_columns,
            is_sync=is_sync,
            file=file,
            state=state,
        )
        return self._create_pending_process_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

