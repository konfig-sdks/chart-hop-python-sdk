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

from chart_hop_python_sdk.model.get_visualizations_options_change_ids import GetVisualizationsOptionsChangeIds as GetVisualizationsOptionsChangeIdsSchema
from chart_hop_python_sdk.model.get_visualizations_options import GetVisualizationsOptions as GetVisualizationsOptionsSchema
from chart_hop_python_sdk.model.comp_review_visualizations import CompReviewVisualizations as CompReviewVisualizationsSchema

from chart_hop_python_sdk.type.get_visualizations_options import GetVisualizationsOptions
from chart_hop_python_sdk.type.get_visualizations_options_change_ids import GetVisualizationsOptionsChangeIds
from chart_hop_python_sdk.type.comp_review_visualizations import CompReviewVisualizations

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.get_visualizations_options import GetVisualizationsOptions as GetVisualizationsOptionsPydantic
from chart_hop_python_sdk.pydantic.get_visualizations_options_change_ids import GetVisualizationsOptionsChangeIds as GetVisualizationsOptionsChangeIdsPydantic
from chart_hop_python_sdk.pydantic.comp_review_visualizations import CompReviewVisualizations as CompReviewVisualizationsPydantic

from . import path

# Query params
ViewJobIdSchema = schemas.StrSchema
PreviewSchema = schemas.BoolSchema
IncludeAllRequestsSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'viewJobId': typing.Union[ViewJobIdSchema, str, ],
        'preview': typing.Union[PreviewSchema, bool, ],
        'includeAllRequests': typing.Union[IncludeAllRequestsSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_view_job_id = api_client.QueryParameter(
    name="viewJobId",
    style=api_client.ParameterStyle.FORM,
    schema=ViewJobIdSchema,
    explode=True,
)
request_query_preview = api_client.QueryParameter(
    name="preview",
    style=api_client.ParameterStyle.FORM,
    schema=PreviewSchema,
    explode=True,
)
request_query_include_all_requests = api_client.QueryParameter(
    name="includeAllRequests",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeAllRequestsSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
CompReviewIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'compReviewId': typing.Union[CompReviewIdSchema, str, ],
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
request_path_comp_review_id = api_client.PathParameter(
    name="compReviewId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompReviewIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = GetVisualizationsOptionsSchema


request_body_get_visualizations_options = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = CompReviewVisualizationsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CompReviewVisualizations


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CompReviewVisualizations


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

    def _create_visualization_data_mapped_args(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if change_ids is not None:
            _body["changeIds"] = change_ids
        if view_in_currency is not None:
            _body["viewInCurrency"] = view_in_currency
        if include_collaborators is not None:
            _body["includeCollaborators"] = include_collaborators
        if is_collabicient_view is not None:
            _body["isCollabicientView"] = is_collabicient_view
        args.body = _body
        if view_job_id is not None:
            _query_params["viewJobId"] = view_job_id
        if preview is not None:
            _query_params["preview"] = preview
        if include_all_requests is not None:
            _query_params["includeAllRequests"] = include_all_requests
        if org_id is not None:
            _path_params["orgId"] = org_id
        if comp_review_id is not None:
            _path_params["compReviewId"] = comp_review_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_visualization_data_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get data for visualizations for a comp review
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
            request_path_comp_review_id,
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
            request_query_view_job_id,
            request_query_preview,
            request_query_include_all_requests,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/comp-review/{compReviewId}/visualizations',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_get_visualizations_options.serialize(body, content_type)
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


    def _create_visualization_data_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get data for visualizations for a comp review
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
            request_path_comp_review_id,
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
            request_query_view_job_id,
            request_query_preview,
            request_query_include_all_requests,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/comp-review/{compReviewId}/visualizations',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_get_visualizations_options.serialize(body, content_type)
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


class CreateVisualizationDataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_visualization_data(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_visualization_data_mapped_args(
            is_collabicient_view=is_collabicient_view,
            org_id=org_id,
            comp_review_id=comp_review_id,
            change_ids=change_ids,
            view_in_currency=view_in_currency,
            include_collaborators=include_collaborators,
            view_job_id=view_job_id,
            preview=preview,
            include_all_requests=include_all_requests,
        )
        return await self._acreate_visualization_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_visualization_data(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_visualization_data_mapped_args(
            is_collabicient_view=is_collabicient_view,
            org_id=org_id,
            comp_review_id=comp_review_id,
            change_ids=change_ids,
            view_in_currency=view_in_currency,
            include_collaborators=include_collaborators,
            view_job_id=view_job_id,
            preview=preview,
            include_all_requests=include_all_requests,
        )
        return self._create_visualization_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class CreateVisualizationData(BaseApi):

    async def acreate_visualization_data(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> CompReviewVisualizationsPydantic:
        raw_response = await self.raw.acreate_visualization_data(
            is_collabicient_view=is_collabicient_view,
            org_id=org_id,
            comp_review_id=comp_review_id,
            change_ids=change_ids,
            view_in_currency=view_in_currency,
            include_collaborators=include_collaborators,
            view_job_id=view_job_id,
            preview=preview,
            include_all_requests=include_all_requests,
            **kwargs,
        )
        if validate:
            return CompReviewVisualizationsPydantic(**raw_response.body)
        return api_client.construct_model_instance(CompReviewVisualizationsPydantic, raw_response.body)
    
    
    def create_visualization_data(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> CompReviewVisualizationsPydantic:
        raw_response = self.raw.create_visualization_data(
            is_collabicient_view=is_collabicient_view,
            org_id=org_id,
            comp_review_id=comp_review_id,
            change_ids=change_ids,
            view_in_currency=view_in_currency,
            include_collaborators=include_collaborators,
            view_job_id=view_job_id,
            preview=preview,
            include_all_requests=include_all_requests,
        )
        if validate:
            return CompReviewVisualizationsPydantic(**raw_response.body)
        return api_client.construct_model_instance(CompReviewVisualizationsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_visualization_data_mapped_args(
            is_collabicient_view=is_collabicient_view,
            org_id=org_id,
            comp_review_id=comp_review_id,
            change_ids=change_ids,
            view_in_currency=view_in_currency,
            include_collaborators=include_collaborators,
            view_job_id=view_job_id,
            preview=preview,
            include_all_requests=include_all_requests,
        )
        return await self._acreate_visualization_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        is_collabicient_view: bool,
        org_id: str,
        comp_review_id: str,
        change_ids: typing.Optional[GetVisualizationsOptionsChangeIds] = None,
        view_in_currency: typing.Optional[str] = None,
        include_collaborators: typing.Optional[bool] = None,
        view_job_id: typing.Optional[str] = None,
        preview: typing.Optional[bool] = None,
        include_all_requests: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_visualization_data_mapped_args(
            is_collabicient_view=is_collabicient_view,
            org_id=org_id,
            comp_review_id=comp_review_id,
            change_ids=change_ids,
            view_in_currency=view_in_currency,
            include_collaborators=include_collaborators,
            view_job_id=view_job_id,
            preview=preview,
            include_all_requests=include_all_requests,
        )
        return self._create_visualization_data_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )
