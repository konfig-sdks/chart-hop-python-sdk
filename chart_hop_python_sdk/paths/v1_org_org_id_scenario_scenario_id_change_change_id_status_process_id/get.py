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

from chart_hop_python_sdk.model.change_status_response import ChangeStatusResponse as ChangeStatusResponseSchema

from chart_hop_python_sdk.type.change_status_response import ChangeStatusResponse

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.change_status_response import ChangeStatusResponse as ChangeStatusResponsePydantic

from . import path

# Path params
OrgIdSchema = schemas.StrSchema
ScenarioIdSchema = schemas.StrSchema
ChangeIdSchema = schemas.StrSchema
ProcessIdSchema = schemas.Int32Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'scenarioId': typing.Union[ScenarioIdSchema, str, ],
        'changeId': typing.Union[ChangeIdSchema, str, ],
        'processId': typing.Union[ProcessIdSchema, decimal.Decimal, int, ],
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
request_path_process_id = api_client.PathParameter(
    name="processId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProcessIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ChangeStatusResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ChangeStatusResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ChangeStatusResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_status_mapped_args(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if org_id is not None:
            _path_params["orgId"] = org_id
        if scenario_id is not None:
            _path_params["scenarioId"] = scenario_id
        if change_id is not None:
            _path_params["changeId"] = change_id
        if process_id is not None:
            _path_params["processId"] = process_id
        args.path = _path_params
        return args

    async def _aget_status_oapg(
        self,
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
        Get the status of a running change within a scenario
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_scenario_id,
            request_path_change_id,
            request_path_process_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}/status/{processId}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_status_oapg(
        self,
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
        Get the status of a running change within a scenario
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_scenario_id,
            request_path_change_id,
            request_path_process_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v1/org/{orgId}/scenario/{scenarioId}/change/{changeId}/status/{processId}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetStatusRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_status(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_status_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            process_id=process_id,
        )
        return await self._aget_status_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_status(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_status_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            process_id=process_id,
        )
        return self._get_status_oapg(
            path_params=args.path,
        )

class GetStatus(BaseApi):

    async def aget_status(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
        validate: bool = False,
        **kwargs,
    ) -> ChangeStatusResponsePydantic:
        raw_response = await self.raw.aget_status(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            process_id=process_id,
            **kwargs,
        )
        if validate:
            return ChangeStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ChangeStatusResponsePydantic, raw_response.body)
    
    
    def get_status(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
        validate: bool = False,
    ) -> ChangeStatusResponsePydantic:
        raw_response = self.raw.get_status(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            process_id=process_id,
        )
        if validate:
            return ChangeStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ChangeStatusResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_status_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            process_id=process_id,
        )
        return await self._aget_status_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        scenario_id: str,
        change_id: str,
        process_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_status_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            change_id=change_id,
            process_id=process_id,
        )
        return self._get_status_oapg(
            path_params=args.path,
        )

