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

from chart_hop_python_sdk.model.update_assessment import UpdateAssessment as UpdateAssessmentSchema
from chart_hop_python_sdk.model.share_access import ShareAccess as ShareAccessSchema

from chart_hop_python_sdk.type.share_access import ShareAccess
from chart_hop_python_sdk.type.update_assessment import UpdateAssessment

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.update_assessment import UpdateAssessment as UpdateAssessmentPydantic
from chart_hop_python_sdk.pydantic.share_access import ShareAccess as ShareAccessPydantic

# Query params
SilentSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'silent': typing.Union[SilentSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_silent = api_client.QueryParameter(
    name="silent",
    style=api_client.ParameterStyle.FORM,
    schema=SilentSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
AssessmentIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'assessmentId': typing.Union[AssessmentIdSchema, str, ],
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
request_path_assessment_id = api_client.PathParameter(
    name="assessmentId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AssessmentIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateAssessmentSchema


request_body_update_assessment = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
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


class BaseApi(api_client.Api):

    def _update_existing_assessment_mapped_args(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if label is not None:
            _body["label"] = label
        if slug is not None:
            _body["slug"] = slug
        if type is not None:
            _body["type"] = type
        if fields is not None:
            _body["fields"] = fields
        if share_access is not None:
            _body["shareAccess"] = share_access
        if sensitive is not None:
            _body["sensitive"] = sensitive
        if color is not None:
            _body["color"] = color
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if status is not None:
            _body["status"] = status
        if done_at is not None:
            _body["doneAt"] = done_at
        if task_count is not None:
            _body["taskCount"] = task_count
        if task_done_count is not None:
            _body["taskDoneCount"] = task_done_count
        if people_included_count is not None:
            _body["peopleIncludedCount"] = people_included_count
        if query is not None:
            _body["query"] = query
        args.body = _body
        if silent is not None:
            _query_params["silent"] = silent
        if org_id is not None:
            _path_params["orgId"] = org_id
        if assessment_id is not None:
            _path_params["assessmentId"] = assessment_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_existing_assessment_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update an existing assessment
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
            request_path_assessment_id,
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
            request_query_silent,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/assessment/{assessmentId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_assessment.serialize(body, content_type)
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


    def _update_existing_assessment_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update an existing assessment
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
            request_path_assessment_id,
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
            request_query_silent,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/assessment/{assessmentId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_assessment.serialize(body, content_type)
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


class UpdateExistingAssessmentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_existing_assessment(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_assessment_mapped_args(
            org_id=org_id,
            assessment_id=assessment_id,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            share_access=share_access,
            sensitive=sensitive,
            color=color,
            start_date=start_date,
            end_date=end_date,
            status=status,
            done_at=done_at,
            task_count=task_count,
            task_done_count=task_done_count,
            people_included_count=people_included_count,
            query=query,
            silent=silent,
        )
        return await self._aupdate_existing_assessment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_existing_assessment(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_assessment_mapped_args(
            org_id=org_id,
            assessment_id=assessment_id,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            share_access=share_access,
            sensitive=sensitive,
            color=color,
            start_date=start_date,
            end_date=end_date,
            status=status,
            done_at=done_at,
            task_count=task_count,
            task_done_count=task_done_count,
            people_included_count=people_included_count,
            query=query,
            silent=silent,
        )
        return self._update_existing_assessment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateExistingAssessment(BaseApi):

    async def aupdate_existing_assessment(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_existing_assessment(
            org_id=org_id,
            assessment_id=assessment_id,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            share_access=share_access,
            sensitive=sensitive,
            color=color,
            start_date=start_date,
            end_date=end_date,
            status=status,
            done_at=done_at,
            task_count=task_count,
            task_done_count=task_done_count,
            people_included_count=people_included_count,
            query=query,
            silent=silent,
            **kwargs,
        )
    
    
    def update_existing_assessment(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_existing_assessment(
            org_id=org_id,
            assessment_id=assessment_id,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            share_access=share_access,
            sensitive=sensitive,
            color=color,
            start_date=start_date,
            end_date=end_date,
            status=status,
            done_at=done_at,
            task_count=task_count,
            task_done_count=task_done_count,
            people_included_count=people_included_count,
            query=query,
            silent=silent,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_assessment_mapped_args(
            org_id=org_id,
            assessment_id=assessment_id,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            share_access=share_access,
            sensitive=sensitive,
            color=color,
            start_date=start_date,
            end_date=end_date,
            status=status,
            done_at=done_at,
            task_count=task_count,
            task_done_count=task_done_count,
            people_included_count=people_included_count,
            query=query,
            silent=silent,
        )
        return await self._aupdate_existing_assessment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        assessment_id: str,
        label: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        status: typing.Optional[str] = None,
        done_at: typing.Optional[str] = None,
        task_count: typing.Optional[int] = None,
        task_done_count: typing.Optional[int] = None,
        people_included_count: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        silent: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_assessment_mapped_args(
            org_id=org_id,
            assessment_id=assessment_id,
            label=label,
            slug=slug,
            type=type,
            fields=fields,
            share_access=share_access,
            sensitive=sensitive,
            color=color,
            start_date=start_date,
            end_date=end_date,
            status=status,
            done_at=done_at,
            task_count=task_count,
            task_done_count=task_done_count,
            people_included_count=people_included_count,
            query=query,
            silent=silent,
        )
        return self._update_existing_assessment_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

