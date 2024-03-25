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

from chart_hop_python_sdk.model.change_amend_scenario_change_request import ChangeAmendScenarioChangeRequest as ChangeAmendScenarioChangeRequestSchema
from chart_hop_python_sdk.model.update_scenario_change_response import UpdateScenarioChangeResponse as UpdateScenarioChangeResponseSchema

from chart_hop_python_sdk.type.update_scenario_change_response import UpdateScenarioChangeResponse
from chart_hop_python_sdk.type.change_amend_scenario_change_request import ChangeAmendScenarioChangeRequest

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.change_amend_scenario_change_request import ChangeAmendScenarioChangeRequest as ChangeAmendScenarioChangeRequestPydantic
from chart_hop_python_sdk.pydantic.update_scenario_change_response import UpdateScenarioChangeResponse as UpdateScenarioChangeResponsePydantic

# Query params
FieldsSchema = schemas.StrSchema
IncludeUpdatedFieldsSchema = schemas.BoolSchema
FormatSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'fields': typing.Union[FieldsSchema, str, ],
        'includeUpdatedFields': typing.Union[IncludeUpdatedFieldsSchema, bool, ],
        'format': typing.Union[FormatSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_include_updated_fields = api_client.QueryParameter(
    name="includeUpdatedFields",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeUpdatedFieldsSchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
ScenarioIdSchema = schemas.StrSchema
ChangeIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'scenarioId': typing.Union[ScenarioIdSchema, str, ],
        'changeId': typing.Union[ChangeIdSchema, str, ],
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
request_path_scenario_id = api_client.PathParameter(
    name="scenarioId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ScenarioIdSchema,
    required=True,
)
request_path_change_id = api_client.PathParameter(
    name="changeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ChangeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ChangeAmendScenarioChangeRequestSchema


request_body_change_amend_scenario_change_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor204ResponseBodyApplicationJson = UpdateScenarioChangeResponseSchema


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: UpdateScenarioChangeResponse


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: UpdateScenarioChangeResponse


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

    def _amend_scenario_change_mapped_args(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        args.body = _body
        if fields is not None:
            _query_params["fields"] = fields
        if include_updated_fields is not None:
            _query_params["includeUpdatedFields"] = include_updated_fields
        if format is not None:
            _query_params["format"] = format
        if org_id is not None:
            _path_params["orgId"] = org_id
        if scenario_id is not None:
            _path_params["scenarioId"] = scenario_id
        if change_id is not None:
            _path_params["changeId"] = change_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aamend_scenario_change_oapg(
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
        Amend a change within a scenario, and potentially return the updated data
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
            request_path_scenario_id,
            request_path_change_id,
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
            request_query_fields,
            request_query_include_updated_fields,
            request_query_format,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_change_amend_scenario_change_request.serialize(body, content_type)
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


    def _amend_scenario_change_oapg(
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
        Amend a change within a scenario, and potentially return the updated data
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
            request_path_scenario_id,
            request_path_change_id,
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
            request_query_fields,
            request_query_include_updated_fields,
            request_query_format,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_change_amend_scenario_change_request.serialize(body, content_type)
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


class AmendScenarioChangeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aamend_scenario_change(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._amend_scenario_change_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            fields=fields,
            include_updated_fields=include_updated_fields,
            format=format,
        )
        return await self._aamend_scenario_change_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def amend_scenario_change(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._amend_scenario_change_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            fields=fields,
            include_updated_fields=include_updated_fields,
            format=format,
        )
        return self._amend_scenario_change_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class AmendScenarioChange(BaseApi):

    async def aamend_scenario_change(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UpdateScenarioChangeResponsePydantic:
        raw_response = await self.raw.aamend_scenario_change(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            fields=fields,
            include_updated_fields=include_updated_fields,
            format=format,
            **kwargs,
        )
        if validate:
            return UpdateScenarioChangeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UpdateScenarioChangeResponsePydantic, raw_response.body)
    
    
    def amend_scenario_change(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UpdateScenarioChangeResponsePydantic:
        raw_response = self.raw.amend_scenario_change(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            fields=fields,
            include_updated_fields=include_updated_fields,
            format=format,
        )
        if validate:
            return UpdateScenarioChangeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UpdateScenarioChangeResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._amend_scenario_change_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            fields=fields,
            include_updated_fields=include_updated_fields,
            format=format,
        )
        return await self._aamend_scenario_change_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        fields: typing.Optional[str] = None,
        include_updated_fields: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._amend_scenario_change_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            fields=fields,
            include_updated_fields=include_updated_fields,
            format=format,
        )
        return self._amend_scenario_change_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

