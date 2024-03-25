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

from chart_hop_python_sdk.model.results_change import ResultsChange as ResultsChangeSchema

from chart_hop_python_sdk.type.results_change import ResultsChange

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.results_change import ResultsChange as ResultsChangePydantic

from . import path

# Query params
ScenarioIdSchema = schemas.StrSchema
DateSchema = schemas.DateSchema
EndDateSchema = schemas.DateSchema
TypeSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema
PersonIdSchema = schemas.StrSchema
JobIdSchema = schemas.StrSchema
IncludeBackfillSchema = schemas.BoolSchema
RefsSchema = schemas.StrSchema
QSchema = schemas.StrSchema
ModelFromSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema


class OpenSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "FILLED": "FILLED",
            "OPEN": "OPEN",
        }
    
    @schemas.classproperty
    def FILLED(cls):
        return cls("FILLED")
    
    @schemas.classproperty
    def OPEN(cls):
        return cls("OPEN")
DescSchema = schemas.BoolSchema
ScenarioOnlySchema = schemas.BoolSchema
ParentOnlySchema = schemas.BoolSchema
IncludeGrantScheduleSchema = schemas.BoolSchema
ExcludeAtsRecruitingFieldsSchema = schemas.BoolSchema
IncludeStruckSchema = schemas.BoolSchema
StatusSchema = schemas.StrSchema
StripUpdatesSchema = schemas.BoolSchema
FormatSchema = schemas.StrSchema
FieldEntityTypesSchema = schemas.StrSchema
ReturnAccessSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'scenarioId': typing.Union[ScenarioIdSchema, str, ],
        'date': typing.Union[DateSchema, str, date, ],
        'endDate': typing.Union[EndDateSchema, str, date, ],
        'type': typing.Union[TypeSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
        'personId': typing.Union[PersonIdSchema, str, ],
        'jobId': typing.Union[JobIdSchema, str, ],
        'includeBackfill': typing.Union[IncludeBackfillSchema, bool, ],
        'refs': typing.Union[RefsSchema, str, ],
        'q': typing.Union[QSchema, str, ],
        'from': typing.Union[ModelFromSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'open': typing.Union[OpenSchema, str, ],
        'desc': typing.Union[DescSchema, bool, ],
        'scenarioOnly': typing.Union[ScenarioOnlySchema, bool, ],
        'parentOnly': typing.Union[ParentOnlySchema, bool, ],
        'includeGrantSchedule': typing.Union[IncludeGrantScheduleSchema, bool, ],
        'excludeAtsRecruitingFields': typing.Union[ExcludeAtsRecruitingFieldsSchema, bool, ],
        'includeStruck': typing.Union[IncludeStruckSchema, bool, ],
        'status': typing.Union[StatusSchema, str, ],
        'stripUpdates': typing.Union[StripUpdatesSchema, bool, ],
        'format': typing.Union[FormatSchema, str, ],
        'fieldEntityTypes': typing.Union[FieldEntityTypesSchema, str, ],
        'returnAccess': typing.Union[ReturnAccessSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
request_query_end_date = api_client.QueryParameter(
    name="endDate",
    style=api_client.ParameterStyle.FORM,
    schema=EndDateSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_person_id = api_client.QueryParameter(
    name="personId",
    style=api_client.ParameterStyle.FORM,
    schema=PersonIdSchema,
    explode=True,
)
request_query_job_id = api_client.QueryParameter(
    name="jobId",
    style=api_client.ParameterStyle.FORM,
    schema=JobIdSchema,
    explode=True,
)
request_query_include_backfill = api_client.QueryParameter(
    name="includeBackfill",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeBackfillSchema,
    explode=True,
)
request_query_refs = api_client.QueryParameter(
    name="refs",
    style=api_client.ParameterStyle.FORM,
    schema=RefsSchema,
    explode=True,
)
request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
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
request_query_open = api_client.QueryParameter(
    name="open",
    style=api_client.ParameterStyle.FORM,
    schema=OpenSchema,
    explode=True,
)
request_query_desc = api_client.QueryParameter(
    name="desc",
    style=api_client.ParameterStyle.FORM,
    schema=DescSchema,
    explode=True,
)
request_query_scenario_only = api_client.QueryParameter(
    name="scenarioOnly",
    style=api_client.ParameterStyle.FORM,
    schema=ScenarioOnlySchema,
    explode=True,
)
request_query_parent_only = api_client.QueryParameter(
    name="parentOnly",
    style=api_client.ParameterStyle.FORM,
    schema=ParentOnlySchema,
    explode=True,
)
request_query_include_grant_schedule = api_client.QueryParameter(
    name="includeGrantSchedule",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeGrantScheduleSchema,
    explode=True,
)
request_query_exclude_ats_recruiting_fields = api_client.QueryParameter(
    name="excludeAtsRecruitingFields",
    style=api_client.ParameterStyle.FORM,
    schema=ExcludeAtsRecruitingFieldsSchema,
    explode=True,
)
request_query_include_struck = api_client.QueryParameter(
    name="includeStruck",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeStruckSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_strip_updates = api_client.QueryParameter(
    name="stripUpdates",
    style=api_client.ParameterStyle.FORM,
    schema=StripUpdatesSchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
request_query_field_entity_types = api_client.QueryParameter(
    name="fieldEntityTypes",
    style=api_client.ParameterStyle.FORM,
    schema=FieldEntityTypesSchema,
    explode=True,
)
request_query_return_access = api_client.QueryParameter(
    name="returnAccess",
    style=api_client.ParameterStyle.FORM,
    schema=ReturnAccessSchema,
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
SchemaFor200ResponseBodyApplicationJson = ResultsChangeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultsChange


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultsChange


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

    def _get_recent_changes_mapped_args(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if scenario_id is not None:
            _query_params["scenarioId"] = scenario_id
        if date is not None:
            _query_params["date"] = date
        if end_date is not None:
            _query_params["endDate"] = end_date
        if type is not None:
            _query_params["type"] = type
        if fields is not None:
            _query_params["fields"] = fields
        if person_id is not None:
            _query_params["personId"] = person_id
        if job_id is not None:
            _query_params["jobId"] = job_id
        if include_backfill is not None:
            _query_params["includeBackfill"] = include_backfill
        if refs is not None:
            _query_params["refs"] = refs
        if q is not None:
            _query_params["q"] = q
        if _from is not None:
            _query_params["from"] = _from
        if limit is not None:
            _query_params["limit"] = limit
        if open is not None:
            _query_params["open"] = open
        if desc is not None:
            _query_params["desc"] = desc
        if scenario_only is not None:
            _query_params["scenarioOnly"] = scenario_only
        if parent_only is not None:
            _query_params["parentOnly"] = parent_only
        if include_grant_schedule is not None:
            _query_params["includeGrantSchedule"] = include_grant_schedule
        if exclude_ats_recruiting_fields is not None:
            _query_params["excludeAtsRecruitingFields"] = exclude_ats_recruiting_fields
        if include_struck is not None:
            _query_params["includeStruck"] = include_struck
        if status is not None:
            _query_params["status"] = status
        if strip_updates is not None:
            _query_params["stripUpdates"] = strip_updates
        if format is not None:
            _query_params["format"] = format
        if field_entity_types is not None:
            _query_params["fieldEntityTypes"] = field_entity_types
        if return_access is not None:
            _query_params["returnAccess"] = return_access
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_recent_changes_oapg(
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
        Return recent changes across an org, or for a particular person or job
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
            request_query_scenario_id,
            request_query_date,
            request_query_end_date,
            request_query_type,
            request_query_fields,
            request_query_person_id,
            request_query_job_id,
            request_query_include_backfill,
            request_query_refs,
            request_query_q,
            request_query__from,
            request_query_limit,
            request_query_open,
            request_query_desc,
            request_query_scenario_only,
            request_query_parent_only,
            request_query_include_grant_schedule,
            request_query_exclude_ats_recruiting_fields,
            request_query_include_struck,
            request_query_status,
            request_query_strip_updates,
            request_query_format,
            request_query_field_entity_types,
            request_query_return_access,
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
            path_template='/v1/org/{orgId}/change',
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


    def _get_recent_changes_oapg(
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
        Return recent changes across an org, or for a particular person or job
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
            request_query_scenario_id,
            request_query_date,
            request_query_end_date,
            request_query_type,
            request_query_fields,
            request_query_person_id,
            request_query_job_id,
            request_query_include_backfill,
            request_query_refs,
            request_query_q,
            request_query__from,
            request_query_limit,
            request_query_open,
            request_query_desc,
            request_query_scenario_only,
            request_query_parent_only,
            request_query_include_grant_schedule,
            request_query_exclude_ats_recruiting_fields,
            request_query_include_struck,
            request_query_status,
            request_query_strip_updates,
            request_query_format,
            request_query_field_entity_types,
            request_query_return_access,
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
            path_template='/v1/org/{orgId}/change',
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


class GetRecentChangesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_recent_changes(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_recent_changes_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            end_date=end_date,
            type=type,
            fields=fields,
            person_id=person_id,
            job_id=job_id,
            include_backfill=include_backfill,
            refs=refs,
            q=q,
            _from=_from,
            limit=limit,
            open=open,
            desc=desc,
            scenario_only=scenario_only,
            parent_only=parent_only,
            include_grant_schedule=include_grant_schedule,
            exclude_ats_recruiting_fields=exclude_ats_recruiting_fields,
            include_struck=include_struck,
            status=status,
            strip_updates=strip_updates,
            format=format,
            field_entity_types=field_entity_types,
            return_access=return_access,
        )
        return await self._aget_recent_changes_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_recent_changes(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_recent_changes_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            end_date=end_date,
            type=type,
            fields=fields,
            person_id=person_id,
            job_id=job_id,
            include_backfill=include_backfill,
            refs=refs,
            q=q,
            _from=_from,
            limit=limit,
            open=open,
            desc=desc,
            scenario_only=scenario_only,
            parent_only=parent_only,
            include_grant_schedule=include_grant_schedule,
            exclude_ats_recruiting_fields=exclude_ats_recruiting_fields,
            include_struck=include_struck,
            status=status,
            strip_updates=strip_updates,
            format=format,
            field_entity_types=field_entity_types,
            return_access=return_access,
        )
        return self._get_recent_changes_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetRecentChanges(BaseApi):

    async def aget_recent_changes(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultsChangePydantic:
        raw_response = await self.raw.aget_recent_changes(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            end_date=end_date,
            type=type,
            fields=fields,
            person_id=person_id,
            job_id=job_id,
            include_backfill=include_backfill,
            refs=refs,
            q=q,
            _from=_from,
            limit=limit,
            open=open,
            desc=desc,
            scenario_only=scenario_only,
            parent_only=parent_only,
            include_grant_schedule=include_grant_schedule,
            exclude_ats_recruiting_fields=exclude_ats_recruiting_fields,
            include_struck=include_struck,
            status=status,
            strip_updates=strip_updates,
            format=format,
            field_entity_types=field_entity_types,
            return_access=return_access,
            **kwargs,
        )
        if validate:
            return ResultsChangePydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsChangePydantic, raw_response.body)
    
    
    def get_recent_changes(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ResultsChangePydantic:
        raw_response = self.raw.get_recent_changes(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            end_date=end_date,
            type=type,
            fields=fields,
            person_id=person_id,
            job_id=job_id,
            include_backfill=include_backfill,
            refs=refs,
            q=q,
            _from=_from,
            limit=limit,
            open=open,
            desc=desc,
            scenario_only=scenario_only,
            parent_only=parent_only,
            include_grant_schedule=include_grant_schedule,
            exclude_ats_recruiting_fields=exclude_ats_recruiting_fields,
            include_struck=include_struck,
            status=status,
            strip_updates=strip_updates,
            format=format,
            field_entity_types=field_entity_types,
            return_access=return_access,
        )
        if validate:
            return ResultsChangePydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsChangePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_recent_changes_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            end_date=end_date,
            type=type,
            fields=fields,
            person_id=person_id,
            job_id=job_id,
            include_backfill=include_backfill,
            refs=refs,
            q=q,
            _from=_from,
            limit=limit,
            open=open,
            desc=desc,
            scenario_only=scenario_only,
            parent_only=parent_only,
            include_grant_schedule=include_grant_schedule,
            exclude_ats_recruiting_fields=exclude_ats_recruiting_fields,
            include_struck=include_struck,
            status=status,
            strip_updates=strip_updates,
            format=format,
            field_entity_types=field_entity_types,
            return_access=return_access,
        )
        return await self._aget_recent_changes_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        include_backfill: typing.Optional[bool] = None,
        refs: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        open: typing.Optional[str] = None,
        desc: typing.Optional[bool] = None,
        scenario_only: typing.Optional[bool] = None,
        parent_only: typing.Optional[bool] = None,
        include_grant_schedule: typing.Optional[bool] = None,
        exclude_ats_recruiting_fields: typing.Optional[bool] = None,
        include_struck: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        strip_updates: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        field_entity_types: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_recent_changes_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            end_date=end_date,
            type=type,
            fields=fields,
            person_id=person_id,
            job_id=job_id,
            include_backfill=include_backfill,
            refs=refs,
            q=q,
            _from=_from,
            limit=limit,
            open=open,
            desc=desc,
            scenario_only=scenario_only,
            parent_only=parent_only,
            include_grant_schedule=include_grant_schedule,
            exclude_ats_recruiting_fields=exclude_ats_recruiting_fields,
            include_struck=include_struck,
            status=status,
            strip_updates=strip_updates,
            format=format,
            field_entity_types=field_entity_types,
            return_access=return_access,
        )
        return self._get_recent_changes_oapg(
            query_params=args.query,
            path_params=args.path,
        )

