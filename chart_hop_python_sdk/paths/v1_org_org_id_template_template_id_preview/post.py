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

from chart_hop_python_sdk.model.template_preview_request import TemplatePreviewRequest as TemplatePreviewRequestSchema
from chart_hop_python_sdk.model.template_render_response import TemplateRenderResponse as TemplateRenderResponseSchema

from chart_hop_python_sdk.type.template_render_response import TemplateRenderResponse
from chart_hop_python_sdk.type.template_preview_request import TemplatePreviewRequest

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.template_preview_request import TemplatePreviewRequest as TemplatePreviewRequestPydantic
from chart_hop_python_sdk.pydantic.template_render_response import TemplateRenderResponse as TemplateRenderResponsePydantic

from . import path

# Query params
JobIdSchema = schemas.StrSchema
ScenarioIdSchema = schemas.StrSchema
DateSchema = schemas.DateSchema


class FormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "TEXT": "TEXT",
            "PDF": "PDF",
        }
    
    @schemas.classproperty
    def TEXT(cls):
        return cls("TEXT")
    
    @schemas.classproperty
    def PDF(cls):
        return cls("PDF")


class ChangeGroupingTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "PRIMARY": "PRIMARY",
            "SCENARIO": "SCENARIO",
            "COMP_REVIEW": "COMP_REVIEW",
        }
    
    @schemas.classproperty
    def PRIMARY(cls):
        return cls("PRIMARY")
    
    @schemas.classproperty
    def SCENARIO(cls):
        return cls("SCENARIO")
    
    @schemas.classproperty
    def COMP_REVIEW(cls):
        return cls("COMP_REVIEW")
ChangeGroupingIdSchema = schemas.StrSchema
UseScenarioChangesSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'jobId': typing.Union[JobIdSchema, str, ],
        'scenarioId': typing.Union[ScenarioIdSchema, str, ],
        'date': typing.Union[DateSchema, str, date, ],
        'format': typing.Union[FormatSchema, str, ],
        'changeGroupingType': typing.Union[ChangeGroupingTypeSchema, str, ],
        'changeGroupingId': typing.Union[ChangeGroupingIdSchema, str, ],
        'useScenarioChanges': typing.Union[UseScenarioChangesSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_job_id = api_client.QueryParameter(
    name="jobId",
    style=api_client.ParameterStyle.FORM,
    schema=JobIdSchema,
    explode=True,
)
request_query_scenario_id = api_client.QueryParameter(
    name="scenarioId",
    style=api_client.ParameterStyle.FORM,
    schema=ScenarioIdSchema,
    explode=True,
)
request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
request_query_change_grouping_type = api_client.QueryParameter(
    name="changeGroupingType",
    style=api_client.ParameterStyle.FORM,
    schema=ChangeGroupingTypeSchema,
    explode=True,
)
request_query_change_grouping_id = api_client.QueryParameter(
    name="changeGroupingId",
    style=api_client.ParameterStyle.FORM,
    schema=ChangeGroupingIdSchema,
    explode=True,
)
request_query_use_scenario_changes = api_client.QueryParameter(
    name="useScenarioChanges",
    style=api_client.ParameterStyle.FORM,
    schema=UseScenarioChangesSchema,
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
SchemaForRequestBodyApplicationJson = TemplatePreviewRequestSchema


request_body_template_preview_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor204ResponseBodyApplicationJson = TemplateRenderResponseSchema


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: TemplateRenderResponse


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: TemplateRenderResponse


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor204ResponseBodyApplicationJson),
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
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
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
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _generate_template_preview_mapped_args(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if content is not None:
            _body["content"] = content
        if stylesheet is not None:
            _body["stylesheet"] = stylesheet
        args.body = _body
        if job_id is not None:
            _query_params["jobId"] = job_id
        if scenario_id is not None:
            _query_params["scenarioId"] = scenario_id
        if date is not None:
            _query_params["date"] = date
        if format is not None:
            _query_params["format"] = format
        if change_grouping_type is not None:
            _query_params["changeGroupingType"] = change_grouping_type
        if change_grouping_id is not None:
            _query_params["changeGroupingId"] = change_grouping_id
        if use_scenario_changes is not None:
            _query_params["useScenarioChanges"] = use_scenario_changes
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _agenerate_template_preview_oapg(
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
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Preview template content without saving it
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
            request_query_job_id,
            request_query_scenario_id,
            request_query_date,
            request_query_format,
            request_query_change_grouping_type,
            request_query_change_grouping_id,
            request_query_use_scenario_changes,
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
            path_template='/v1/org/{orgId}/template/{templateId}/preview',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_template_preview_request.serialize(body, content_type)
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


    def _generate_template_preview_oapg(
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
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Preview template content without saving it
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
            request_query_job_id,
            request_query_scenario_id,
            request_query_date,
            request_query_format,
            request_query_change_grouping_type,
            request_query_change_grouping_id,
            request_query_use_scenario_changes,
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
            path_template='/v1/org/{orgId}/template/{templateId}/preview',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_template_preview_request.serialize(body, content_type)
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


class GenerateTemplatePreviewRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_template_preview(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_template_preview_mapped_args(
            content=content,
            org_id=org_id,
            stylesheet=stylesheet,
            job_id=job_id,
            scenario_id=scenario_id,
            date=date,
            format=format,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            use_scenario_changes=use_scenario_changes,
        )
        return await self._agenerate_template_preview_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def generate_template_preview(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_template_preview_mapped_args(
            content=content,
            org_id=org_id,
            stylesheet=stylesheet,
            job_id=job_id,
            scenario_id=scenario_id,
            date=date,
            format=format,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            use_scenario_changes=use_scenario_changes,
        )
        return self._generate_template_preview_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class GenerateTemplatePreview(BaseApi):

    async def agenerate_template_preview(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> TemplateRenderResponsePydantic:
        raw_response = await self.raw.agenerate_template_preview(
            content=content,
            org_id=org_id,
            stylesheet=stylesheet,
            job_id=job_id,
            scenario_id=scenario_id,
            date=date,
            format=format,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            use_scenario_changes=use_scenario_changes,
            **kwargs,
        )
        if validate:
            return TemplateRenderResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplateRenderResponsePydantic, raw_response.body)
    
    
    def generate_template_preview(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> TemplateRenderResponsePydantic:
        raw_response = self.raw.generate_template_preview(
            content=content,
            org_id=org_id,
            stylesheet=stylesheet,
            job_id=job_id,
            scenario_id=scenario_id,
            date=date,
            format=format,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            use_scenario_changes=use_scenario_changes,
        )
        if validate:
            return TemplateRenderResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplateRenderResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_template_preview_mapped_args(
            content=content,
            org_id=org_id,
            stylesheet=stylesheet,
            job_id=job_id,
            scenario_id=scenario_id,
            date=date,
            format=format,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            use_scenario_changes=use_scenario_changes,
        )
        return await self._agenerate_template_preview_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        content: str,
        org_id: str,
        stylesheet: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        format: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        use_scenario_changes: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_template_preview_mapped_args(
            content=content,
            org_id=org_id,
            stylesheet=stylesheet,
            job_id=job_id,
            scenario_id=scenario_id,
            date=date,
            format=format,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            use_scenario_changes=use_scenario_changes,
        )
        return self._generate_template_preview_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

