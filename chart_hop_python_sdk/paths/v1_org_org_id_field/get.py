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

from chart_hop_python_sdk.model.results_field import ResultsField as ResultsFieldSchema

from chart_hop_python_sdk.type.results_field import ResultsField

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.results_field import ResultsField as ResultsFieldPydantic

from . import path

# Query params
ModelFromSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
IdsSchema = schemas.StrSchema
TableSchema = schemas.StrSchema
TableTypeSchema = schemas.StrSchema
FormSchema = schemas.StrSchema
BuiltinSchema = schemas.StrSchema
IncludeTtstSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'from': typing.Union[ModelFromSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'ids': typing.Union[IdsSchema, str, ],
        'table': typing.Union[TableSchema, str, ],
        'tableType': typing.Union[TableTypeSchema, str, ],
        'form': typing.Union[FormSchema, str, ],
        'builtin': typing.Union[BuiltinSchema, str, ],
        'includeTtst': typing.Union[IncludeTtstSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    explode=True,
)
request_query_table = api_client.QueryParameter(
    name="table",
    style=api_client.ParameterStyle.FORM,
    schema=TableSchema,
    explode=True,
)
request_query_table_type = api_client.QueryParameter(
    name="tableType",
    style=api_client.ParameterStyle.FORM,
    schema=TableTypeSchema,
    explode=True,
)
request_query_form = api_client.QueryParameter(
    name="form",
    style=api_client.ParameterStyle.FORM,
    schema=FormSchema,
    explode=True,
)
request_query_builtin = api_client.QueryParameter(
    name="builtin",
    style=api_client.ParameterStyle.FORM,
    schema=BuiltinSchema,
    explode=True,
)
request_query_include_ttst = api_client.QueryParameter(
    name="includeTtst",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeTtstSchema,
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
SchemaFor200ResponseBodyApplicationJson = ResultsFieldSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultsField


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultsField


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_all_paginated_mapped_args(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if _from is not None:
            _query_params["from"] = _from
        if limit is not None:
            _query_params["limit"] = limit
        if ids is not None:
            _query_params["ids"] = ids
        if table is not None:
            _query_params["table"] = table
        if table_type is not None:
            _query_params["tableType"] = table_type
        if form is not None:
            _query_params["form"] = form
        if builtin is not None:
            _query_params["builtin"] = builtin
        if include_ttst is not None:
            _query_params["includeTtst"] = include_ttst
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_all_paginated_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Return all fields in the organization paginated
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
            request_query__from,
            request_query_limit,
            request_query_ids,
            request_query_table,
            request_query_table_type,
            request_query_form,
            request_query_builtin,
            request_query_include_ttst,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/field',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_all_paginated_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Return all fields in the organization paginated
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
            request_query__from,
            request_query_limit,
            request_query_ids,
            request_query_table,
            request_query_table_type,
            request_query_form,
            request_query_builtin,
            request_query_include_ttst,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/field',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetAllPaginatedRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_paginated(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_paginated_mapped_args(
            org_id=org_id,
            _from=_from,
            limit=limit,
            ids=ids,
            table=table,
            table_type=table_type,
            form=form,
            builtin=builtin,
            include_ttst=include_ttst,
        )
        return await self._aget_all_paginated_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_all_paginated(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_paginated_mapped_args(
            org_id=org_id,
            _from=_from,
            limit=limit,
            ids=ids,
            table=table,
            table_type=table_type,
            form=form,
            builtin=builtin,
            include_ttst=include_ttst,
        )
        return self._get_all_paginated_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAllPaginated(BaseApi):

    async def aget_all_paginated(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultsFieldPydantic:
        raw_response = await self.raw.aget_all_paginated(
            org_id=org_id,
            _from=_from,
            limit=limit,
            ids=ids,
            table=table,
            table_type=table_type,
            form=form,
            builtin=builtin,
            include_ttst=include_ttst,
            **kwargs,
        )
        if validate:
            return ResultsFieldPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsFieldPydantic, raw_response.body)
    
    
    def get_all_paginated(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ResultsFieldPydantic:
        raw_response = self.raw.get_all_paginated(
            org_id=org_id,
            _from=_from,
            limit=limit,
            ids=ids,
            table=table,
            table_type=table_type,
            form=form,
            builtin=builtin,
            include_ttst=include_ttst,
        )
        if validate:
            return ResultsFieldPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsFieldPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_paginated_mapped_args(
            org_id=org_id,
            _from=_from,
            limit=limit,
            ids=ids,
            table=table,
            table_type=table_type,
            form=form,
            builtin=builtin,
            include_ttst=include_ttst,
        )
        return await self._aget_all_paginated_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        table: typing.Optional[str] = None,
        table_type: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        builtin: typing.Optional[str] = None,
        include_ttst: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_paginated_mapped_args(
            org_id=org_id,
            _from=_from,
            limit=limit,
            ids=ids,
            table=table,
            table_type=table_type,
            form=form,
            builtin=builtin,
            include_ttst=include_ttst,
        )
        return self._get_all_paginated_oapg(
            query_params=args.query,
            path_params=args.path,
        )

