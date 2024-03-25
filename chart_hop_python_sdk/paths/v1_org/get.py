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

from chart_hop_python_sdk.model.results_org import ResultsOrg as ResultsOrgSchema

from chart_hop_python_sdk.type.results_org import ResultsOrg

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.results_org import ResultsOrg as ResultsOrgPydantic

from . import path

# Query params
ModelFromSchema = schemas.StrSchema
QSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
CustomerIdSchema = schemas.StrSchema
RealOnlySchema = schemas.BoolSchema
LastCreateAtSchema = schemas.Int64Schema
LastActiveAtSchema = schemas.Int64Schema
InternalOptionsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'from': typing.Union[ModelFromSchema, str, ],
        'q': typing.Union[QSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'customerId': typing.Union[CustomerIdSchema, str, ],
        'realOnly': typing.Union[RealOnlySchema, bool, ],
        'lastCreateAt': typing.Union[LastCreateAtSchema, decimal.Decimal, int, ],
        'lastActiveAt': typing.Union[LastActiveAtSchema, decimal.Decimal, int, ],
        'internalOptions': typing.Union[InternalOptionsSchema, str, ],
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
request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_customer_id = api_client.QueryParameter(
    name="customerId",
    style=api_client.ParameterStyle.FORM,
    schema=CustomerIdSchema,
    explode=True,
)
request_query_real_only = api_client.QueryParameter(
    name="realOnly",
    style=api_client.ParameterStyle.FORM,
    schema=RealOnlySchema,
    explode=True,
)
request_query_last_create_at = api_client.QueryParameter(
    name="lastCreateAt",
    style=api_client.ParameterStyle.FORM,
    schema=LastCreateAtSchema,
    explode=True,
)
request_query_last_active_at = api_client.QueryParameter(
    name="lastActiveAt",
    style=api_client.ParameterStyle.FORM,
    schema=LastActiveAtSchema,
    explode=True,
)
request_query_internal_options = api_client.QueryParameter(
    name="internalOptions",
    style=api_client.ParameterStyle.FORM,
    schema=InternalOptionsSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ResultsOrgSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultsOrg


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultsOrg


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
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_visible_orgs_mapped_args(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if _from is not None:
            _query_params["from"] = _from
        if q is not None:
            _query_params["q"] = q
        if limit is not None:
            _query_params["limit"] = limit
        if customer_id is not None:
            _query_params["customerId"] = customer_id
        if real_only is not None:
            _query_params["realOnly"] = real_only
        if last_create_at is not None:
            _query_params["lastCreateAt"] = last_create_at
        if last_active_at is not None:
            _query_params["lastActiveAt"] = last_active_at
        if internal_options is not None:
            _query_params["internalOptions"] = internal_options
        args.query = _query_params
        return args

    async def _alist_visible_orgs_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Return all visible orgs, paginated by name
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_q,
            request_query_limit,
            request_query_customer_id,
            request_query_real_only,
            request_query_last_create_at,
            request_query_last_active_at,
            request_query_internal_options,
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
            path_template='/v1/org',
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


    def _list_visible_orgs_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Return all visible orgs, paginated by name
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_q,
            request_query_limit,
            request_query_customer_id,
            request_query_real_only,
            request_query_last_create_at,
            request_query_last_active_at,
            request_query_internal_options,
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
            path_template='/v1/org',
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


class ListVisibleOrgsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_visible_orgs(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_visible_orgs_mapped_args(
            _from=_from,
            q=q,
            limit=limit,
            customer_id=customer_id,
            real_only=real_only,
            last_create_at=last_create_at,
            last_active_at=last_active_at,
            internal_options=internal_options,
        )
        return await self._alist_visible_orgs_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_visible_orgs(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_visible_orgs_mapped_args(
            _from=_from,
            q=q,
            limit=limit,
            customer_id=customer_id,
            real_only=real_only,
            last_create_at=last_create_at,
            last_active_at=last_active_at,
            internal_options=internal_options,
        )
        return self._list_visible_orgs_oapg(
            query_params=args.query,
        )

class ListVisibleOrgs(BaseApi):

    async def alist_visible_orgs(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultsOrgPydantic:
        raw_response = await self.raw.alist_visible_orgs(
            _from=_from,
            q=q,
            limit=limit,
            customer_id=customer_id,
            real_only=real_only,
            last_create_at=last_create_at,
            last_active_at=last_active_at,
            internal_options=internal_options,
            **kwargs,
        )
        if validate:
            return ResultsOrgPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsOrgPydantic, raw_response.body)
    
    
    def list_visible_orgs(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ResultsOrgPydantic:
        raw_response = self.raw.list_visible_orgs(
            _from=_from,
            q=q,
            limit=limit,
            customer_id=customer_id,
            real_only=real_only,
            last_create_at=last_create_at,
            last_active_at=last_active_at,
            internal_options=internal_options,
        )
        if validate:
            return ResultsOrgPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsOrgPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_visible_orgs_mapped_args(
            _from=_from,
            q=q,
            limit=limit,
            customer_id=customer_id,
            real_only=real_only,
            last_create_at=last_create_at,
            last_active_at=last_active_at,
            internal_options=internal_options,
        )
        return await self._alist_visible_orgs_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        _from: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        real_only: typing.Optional[bool] = None,
        last_create_at: typing.Optional[int] = None,
        last_active_at: typing.Optional[int] = None,
        internal_options: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_visible_orgs_mapped_args(
            _from=_from,
            q=q,
            limit=limit,
            customer_id=customer_id,
            real_only=real_only,
            last_create_at=last_create_at,
            last_active_at=last_active_at,
            internal_options=internal_options,
        )
        return self._list_visible_orgs_oapg(
            query_params=args.query,
        )

