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

from chart_hop_python_sdk.model.form_render import FormRender as FormRenderSchema

from chart_hop_python_sdk.type.form_render import FormRender

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.form_render import FormRender as FormRenderPydantic

# Query params
TargetIdSchema = schemas.StrSchema


class TargetTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def NONE(cls):
        return cls("NONE")
    
    @schemas.classproperty
    def PERSON(cls):
        return cls("PERSON")
FormResponseIdSchema = schemas.StrSchema
FormResponseChangeIdSchema = schemas.StrSchema
FormVersionIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'targetId': typing.Union[TargetIdSchema, str, ],
        'targetType': typing.Union[TargetTypeSchema, str, ],
        'formResponseId': typing.Union[FormResponseIdSchema, str, ],
        'formResponseChangeId': typing.Union[FormResponseChangeIdSchema, str, ],
        'formVersionId': typing.Union[FormVersionIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_target_id = api_client.QueryParameter(
    name="targetId",
    style=api_client.ParameterStyle.FORM,
    schema=TargetIdSchema,
    explode=True,
)
request_query_target_type = api_client.QueryParameter(
    name="targetType",
    style=api_client.ParameterStyle.FORM,
    schema=TargetTypeSchema,
    explode=True,
)
request_query_form_response_id = api_client.QueryParameter(
    name="formResponseId",
    style=api_client.ParameterStyle.FORM,
    schema=FormResponseIdSchema,
    explode=True,
)
request_query_form_response_change_id = api_client.QueryParameter(
    name="formResponseChangeId",
    style=api_client.ParameterStyle.FORM,
    schema=FormResponseChangeIdSchema,
    explode=True,
)
request_query_form_version_id = api_client.QueryParameter(
    name="formVersionId",
    style=api_client.ParameterStyle.FORM,
    schema=FormVersionIdSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
FormIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'formId': typing.Union[FormIdSchema, str, ],
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
request_path_form_id = api_client.PathParameter(
    name="formId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FormIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = FormRenderSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FormRender


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FormRender


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _render_for_display_mapped_args(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if target_id is not None:
            _query_params["targetId"] = target_id
        if target_type is not None:
            _query_params["targetType"] = target_type
        if form_response_id is not None:
            _query_params["formResponseId"] = form_response_id
        if form_response_change_id is not None:
            _query_params["formResponseChangeId"] = form_response_change_id
        if form_version_id is not None:
            _query_params["formVersionId"] = form_version_id
        if org_id is not None:
            _path_params["orgId"] = org_id
        if form_id is not None:
            _path_params["formId"] = form_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _arender_for_display_oapg(
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
        Render a form for display
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
            request_path_form_id,
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
            request_query_target_id,
            request_query_target_type,
            request_query_form_response_id,
            request_query_form_response_change_id,
            request_query_form_version_id,
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
            path_template='/v1/org/{orgId}/form/{formId}/render',
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


    def _render_for_display_oapg(
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
        Render a form for display
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
            request_path_form_id,
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
            request_query_target_id,
            request_query_target_type,
            request_query_form_response_id,
            request_query_form_response_change_id,
            request_query_form_version_id,
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
            path_template='/v1/org/{orgId}/form/{formId}/render',
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


class RenderForDisplayRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arender_for_display(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._render_for_display_mapped_args(
            org_id=org_id,
            form_id=form_id,
            target_id=target_id,
            target_type=target_type,
            form_response_id=form_response_id,
            form_response_change_id=form_response_change_id,
            form_version_id=form_version_id,
        )
        return await self._arender_for_display_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def render_for_display(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._render_for_display_mapped_args(
            org_id=org_id,
            form_id=form_id,
            target_id=target_id,
            target_type=target_type,
            form_response_id=form_response_id,
            form_response_change_id=form_response_change_id,
            form_version_id=form_version_id,
        )
        return self._render_for_display_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class RenderForDisplay(BaseApi):

    async def arender_for_display(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FormRenderPydantic:
        raw_response = await self.raw.arender_for_display(
            org_id=org_id,
            form_id=form_id,
            target_id=target_id,
            target_type=target_type,
            form_response_id=form_response_id,
            form_response_change_id=form_response_change_id,
            form_version_id=form_version_id,
            **kwargs,
        )
        if validate:
            return FormRenderPydantic(**raw_response.body)
        return api_client.construct_model_instance(FormRenderPydantic, raw_response.body)
    
    
    def render_for_display(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FormRenderPydantic:
        raw_response = self.raw.render_for_display(
            org_id=org_id,
            form_id=form_id,
            target_id=target_id,
            target_type=target_type,
            form_response_id=form_response_id,
            form_response_change_id=form_response_change_id,
            form_version_id=form_version_id,
        )
        if validate:
            return FormRenderPydantic(**raw_response.body)
        return api_client.construct_model_instance(FormRenderPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._render_for_display_mapped_args(
            org_id=org_id,
            form_id=form_id,
            target_id=target_id,
            target_type=target_type,
            form_response_id=form_response_id,
            form_response_change_id=form_response_change_id,
            form_version_id=form_version_id,
        )
        return await self._arender_for_display_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        form_id: str,
        target_id: typing.Optional[str] = None,
        target_type: typing.Optional[str] = None,
        form_response_id: typing.Optional[str] = None,
        form_response_change_id: typing.Optional[str] = None,
        form_version_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._render_for_display_mapped_args(
            org_id=org_id,
            form_id=form_id,
            target_id=target_id,
            target_type=target_type,
            form_response_id=form_response_id,
            form_response_change_id=form_response_change_id,
            form_version_id=form_version_id,
        )
        return self._render_for_display_oapg(
            query_params=args.query,
            path_params=args.path,
        )

