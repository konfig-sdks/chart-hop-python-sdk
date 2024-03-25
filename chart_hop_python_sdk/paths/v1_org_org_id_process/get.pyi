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

from chart_hop_python_sdk.model.results_process import ResultsProcess as ResultsProcessSchema

from chart_hop_python_sdk.type.results_process import ResultsProcess

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.results_process import ResultsProcess as ResultsProcessPydantic

# Query params
IsAppProcessSchema = schemas.BoolSchema
AppIdSchema = schemas.StrSchema
ParentProcessIdSchema = schemas.StrSchema
TypeSchema = schemas.StrSchema
CompletedAtStartSchema = schemas.Int64Schema
CompletedAtEndSchema = schemas.Int64Schema
StatusesSchema = schemas.StrSchema
IsParentProcessSchema = schemas.BoolSchema
ProcessTypesSchema = schemas.StrSchema
SearchValueSchema = schemas.StrSchema
ModelFromSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
SyncDirectionsSchema = schemas.StrSchema
SyncCausesSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'isAppProcess': typing.Union[IsAppProcessSchema, bool, ],
        'appId': typing.Union[AppIdSchema, str, ],
        'parentProcessId': typing.Union[ParentProcessIdSchema, str, ],
        'type': typing.Union[TypeSchema, str, ],
        'completedAtStart': typing.Union[CompletedAtStartSchema, decimal.Decimal, int, ],
        'completedAtEnd': typing.Union[CompletedAtEndSchema, decimal.Decimal, int, ],
        'statuses': typing.Union[StatusesSchema, str, ],
        'isParentProcess': typing.Union[IsParentProcessSchema, bool, ],
        'processTypes': typing.Union[ProcessTypesSchema, str, ],
        'searchValue': typing.Union[SearchValueSchema, str, ],
        'from': typing.Union[ModelFromSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'syncDirections': typing.Union[SyncDirectionsSchema, str, ],
        'syncCauses': typing.Union[SyncCausesSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_is_app_process = api_client.QueryParameter(
    name="isAppProcess",
    style=api_client.ParameterStyle.FORM,
    schema=IsAppProcessSchema,
    explode=True,
)
request_query_app_id = api_client.QueryParameter(
    name="appId",
    style=api_client.ParameterStyle.FORM,
    schema=AppIdSchema,
    explode=True,
)
request_query_parent_process_id = api_client.QueryParameter(
    name="parentProcessId",
    style=api_client.ParameterStyle.FORM,
    schema=ParentProcessIdSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_completed_at_start = api_client.QueryParameter(
    name="completedAtStart",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedAtStartSchema,
    explode=True,
)
request_query_completed_at_end = api_client.QueryParameter(
    name="completedAtEnd",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedAtEndSchema,
    explode=True,
)
request_query_statuses = api_client.QueryParameter(
    name="statuses",
    style=api_client.ParameterStyle.FORM,
    schema=StatusesSchema,
    explode=True,
)
request_query_is_parent_process = api_client.QueryParameter(
    name="isParentProcess",
    style=api_client.ParameterStyle.FORM,
    schema=IsParentProcessSchema,
    explode=True,
)
request_query_process_types = api_client.QueryParameter(
    name="processTypes",
    style=api_client.ParameterStyle.FORM,
    schema=ProcessTypesSchema,
    explode=True,
)
request_query_search_value = api_client.QueryParameter(
    name="searchValue",
    style=api_client.ParameterStyle.FORM,
    schema=SearchValueSchema,
    explode=True,
)
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
request_query_sync_directions = api_client.QueryParameter(
    name="syncDirections",
    style=api_client.ParameterStyle.FORM,
    schema=SyncDirectionsSchema,
    explode=True,
)
request_query_sync_causes = api_client.QueryParameter(
    name="syncCauses",
    style=api_client.ParameterStyle.FORM,
    schema=SyncCausesSchema,
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
SchemaFor200ResponseBodyApplicationJson = ResultsProcessSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultsProcess


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultsProcess


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
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_previously_run_processes_mapped_args(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if is_app_process is not None:
            _query_params["isAppProcess"] = is_app_process
        if app_id is not None:
            _query_params["appId"] = app_id
        if parent_process_id is not None:
            _query_params["parentProcessId"] = parent_process_id
        if type is not None:
            _query_params["type"] = type
        if completed_at_start is not None:
            _query_params["completedAtStart"] = completed_at_start
        if completed_at_end is not None:
            _query_params["completedAtEnd"] = completed_at_end
        if statuses is not None:
            _query_params["statuses"] = statuses
        if is_parent_process is not None:
            _query_params["isParentProcess"] = is_parent_process
        if process_types is not None:
            _query_params["processTypes"] = process_types
        if search_value is not None:
            _query_params["searchValue"] = search_value
        if _from is not None:
            _query_params["from"] = _from
        if limit is not None:
            _query_params["limit"] = limit
        if sync_directions is not None:
            _query_params["syncDirections"] = sync_directions
        if sync_causes is not None:
            _query_params["syncCauses"] = sync_causes
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_previously_run_processes_oapg(
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
        Retrieve a number of previously run processes
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
            request_query_is_app_process,
            request_query_app_id,
            request_query_parent_process_id,
            request_query_type,
            request_query_completed_at_start,
            request_query_completed_at_end,
            request_query_statuses,
            request_query_is_parent_process,
            request_query_process_types,
            request_query_search_value,
            request_query__from,
            request_query_limit,
            request_query_sync_directions,
            request_query_sync_causes,
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
            path_template='/v1/org/{orgId}/process',
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


    def _get_previously_run_processes_oapg(
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
        Retrieve a number of previously run processes
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
            request_query_is_app_process,
            request_query_app_id,
            request_query_parent_process_id,
            request_query_type,
            request_query_completed_at_start,
            request_query_completed_at_end,
            request_query_statuses,
            request_query_is_parent_process,
            request_query_process_types,
            request_query_search_value,
            request_query__from,
            request_query_limit,
            request_query_sync_directions,
            request_query_sync_causes,
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
            path_template='/v1/org/{orgId}/process',
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


class GetPreviouslyRunProcessesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_previously_run_processes(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_previously_run_processes_mapped_args(
            org_id=org_id,
            is_app_process=is_app_process,
            app_id=app_id,
            parent_process_id=parent_process_id,
            type=type,
            completed_at_start=completed_at_start,
            completed_at_end=completed_at_end,
            statuses=statuses,
            is_parent_process=is_parent_process,
            process_types=process_types,
            search_value=search_value,
            _from=_from,
            limit=limit,
            sync_directions=sync_directions,
            sync_causes=sync_causes,
        )
        return await self._aget_previously_run_processes_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_previously_run_processes(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_previously_run_processes_mapped_args(
            org_id=org_id,
            is_app_process=is_app_process,
            app_id=app_id,
            parent_process_id=parent_process_id,
            type=type,
            completed_at_start=completed_at_start,
            completed_at_end=completed_at_end,
            statuses=statuses,
            is_parent_process=is_parent_process,
            process_types=process_types,
            search_value=search_value,
            _from=_from,
            limit=limit,
            sync_directions=sync_directions,
            sync_causes=sync_causes,
        )
        return self._get_previously_run_processes_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetPreviouslyRunProcesses(BaseApi):

    async def aget_previously_run_processes(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultsProcessPydantic:
        raw_response = await self.raw.aget_previously_run_processes(
            org_id=org_id,
            is_app_process=is_app_process,
            app_id=app_id,
            parent_process_id=parent_process_id,
            type=type,
            completed_at_start=completed_at_start,
            completed_at_end=completed_at_end,
            statuses=statuses,
            is_parent_process=is_parent_process,
            process_types=process_types,
            search_value=search_value,
            _from=_from,
            limit=limit,
            sync_directions=sync_directions,
            sync_causes=sync_causes,
            **kwargs,
        )
        if validate:
            return ResultsProcessPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsProcessPydantic, raw_response.body)
    
    
    def get_previously_run_processes(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ResultsProcessPydantic:
        raw_response = self.raw.get_previously_run_processes(
            org_id=org_id,
            is_app_process=is_app_process,
            app_id=app_id,
            parent_process_id=parent_process_id,
            type=type,
            completed_at_start=completed_at_start,
            completed_at_end=completed_at_end,
            statuses=statuses,
            is_parent_process=is_parent_process,
            process_types=process_types,
            search_value=search_value,
            _from=_from,
            limit=limit,
            sync_directions=sync_directions,
            sync_causes=sync_causes,
        )
        if validate:
            return ResultsProcessPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsProcessPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_previously_run_processes_mapped_args(
            org_id=org_id,
            is_app_process=is_app_process,
            app_id=app_id,
            parent_process_id=parent_process_id,
            type=type,
            completed_at_start=completed_at_start,
            completed_at_end=completed_at_end,
            statuses=statuses,
            is_parent_process=is_parent_process,
            process_types=process_types,
            search_value=search_value,
            _from=_from,
            limit=limit,
            sync_directions=sync_directions,
            sync_causes=sync_causes,
        )
        return await self._aget_previously_run_processes_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        is_app_process: typing.Optional[bool] = None,
        app_id: typing.Optional[str] = None,
        parent_process_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        completed_at_start: typing.Optional[int] = None,
        completed_at_end: typing.Optional[int] = None,
        statuses: typing.Optional[str] = None,
        is_parent_process: typing.Optional[bool] = None,
        process_types: typing.Optional[str] = None,
        search_value: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sync_directions: typing.Optional[str] = None,
        sync_causes: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_previously_run_processes_mapped_args(
            org_id=org_id,
            is_app_process=is_app_process,
            app_id=app_id,
            parent_process_id=parent_process_id,
            type=type,
            completed_at_start=completed_at_start,
            completed_at_end=completed_at_end,
            statuses=statuses,
            is_parent_process=is_parent_process,
            process_types=process_types,
            search_value=search_value,
            _from=_from,
            limit=limit,
            sync_directions=sync_directions,
            sync_causes=sync_causes,
        )
        return self._get_previously_run_processes_oapg(
            query_params=args.query,
            path_params=args.path,
        )
