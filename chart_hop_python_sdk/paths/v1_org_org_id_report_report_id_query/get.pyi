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

from chart_hop_python_sdk.model.report_get_all_report_charts_response import ReportGetAllReportChartsResponse as ReportGetAllReportChartsResponseSchema

from chart_hop_python_sdk.type.report_get_all_report_charts_response import ReportGetAllReportChartsResponse

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.report_get_all_report_charts_response import ReportGetAllReportChartsResponse as ReportGetAllReportChartsResponsePydantic

# Query params
StartDateSchema = schemas.StrSchema
EndDateSchema = schemas.StrSchema


class IntervalSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DAY(cls):
        return cls("DAY")
    
    @schemas.classproperty
    def WEEK(cls):
        return cls("WEEK")
    
    @schemas.classproperty
    def MONTH(cls):
        return cls("MONTH")
    
    @schemas.classproperty
    def QUARTER(cls):
        return cls("QUARTER")
    
    @schemas.classproperty
    def FISCAL_QUARTER(cls):
        return cls("FISCAL_QUARTER")
    
    @schemas.classproperty
    def YEAR(cls):
        return cls("YEAR")
    
    @schemas.classproperty
    def FISCAL_YEAR(cls):
        return cls("FISCAL_YEAR")
ScenarioIdSchema = schemas.StrSchema
ProjectHiresSchema = schemas.BoolSchema
FilterSchema = schemas.StrSchema


class ChangeGroupingTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
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
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'startDate': typing.Union[StartDateSchema, str, ],
        'endDate': typing.Union[EndDateSchema, str, ],
        'interval': typing.Union[IntervalSchema, str, ],
        'scenarioId': typing.Union[ScenarioIdSchema, str, ],
        'projectHires': typing.Union[ProjectHiresSchema, bool, ],
        'filter': typing.Union[FilterSchema, str, ],
        'changeGroupingType': typing.Union[ChangeGroupingTypeSchema, str, ],
        'changeGroupingId': typing.Union[ChangeGroupingIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_start_date = api_client.QueryParameter(
    name="startDate",
    style=api_client.ParameterStyle.FORM,
    schema=StartDateSchema,
    explode=True,
)
request_query_end_date = api_client.QueryParameter(
    name="endDate",
    style=api_client.ParameterStyle.FORM,
    schema=EndDateSchema,
    explode=True,
)
request_query_interval = api_client.QueryParameter(
    name="interval",
    style=api_client.ParameterStyle.FORM,
    schema=IntervalSchema,
    explode=True,
)
request_query_scenario_id = api_client.QueryParameter(
    name="scenarioId",
    style=api_client.ParameterStyle.FORM,
    schema=ScenarioIdSchema,
    explode=True,
)
request_query_project_hires = api_client.QueryParameter(
    name="projectHires",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectHiresSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
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
# Path params
OrgIdSchema = schemas.StrSchema
ReportIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'reportId': typing.Union[ReportIdSchema, str, ],
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
request_path_report_id = api_client.PathParameter(
    name="reportId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ReportIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ReportGetAllReportChartsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReportGetAllReportChartsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReportGetAllReportChartsResponse


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

    def _get_all_report_charts_mapped_args(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if start_date is not None:
            _query_params["startDate"] = start_date
        if end_date is not None:
            _query_params["endDate"] = end_date
        if interval is not None:
            _query_params["interval"] = interval
        if scenario_id is not None:
            _query_params["scenarioId"] = scenario_id
        if project_hires is not None:
            _query_params["projectHires"] = project_hires
        if filter is not None:
            _query_params["filter"] = filter
        if change_grouping_type is not None:
            _query_params["changeGroupingType"] = change_grouping_type
        if change_grouping_id is not None:
            _query_params["changeGroupingId"] = change_grouping_id
        if org_id is not None:
            _path_params["orgId"] = org_id
        if report_id is not None:
            _path_params["reportId"] = report_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_all_report_charts_oapg(
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
        Query all the charts in a report
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
            request_path_report_id,
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
            request_query_start_date,
            request_query_end_date,
            request_query_interval,
            request_query_scenario_id,
            request_query_project_hires,
            request_query_filter,
            request_query_change_grouping_type,
            request_query_change_grouping_id,
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
            path_template='/v1/org/{orgId}/report/{reportId}/query',
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


    def _get_all_report_charts_oapg(
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
        Query all the charts in a report
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
            request_path_report_id,
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
            request_query_start_date,
            request_query_end_date,
            request_query_interval,
            request_query_scenario_id,
            request_query_project_hires,
            request_query_filter,
            request_query_change_grouping_type,
            request_query_change_grouping_id,
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
            path_template='/v1/org/{orgId}/report/{reportId}/query',
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


class GetAllReportChartsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_report_charts(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_report_charts_mapped_args(
            org_id=org_id,
            report_id=report_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            scenario_id=scenario_id,
            project_hires=project_hires,
            filter=filter,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return await self._aget_all_report_charts_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_all_report_charts(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_report_charts_mapped_args(
            org_id=org_id,
            report_id=report_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            scenario_id=scenario_id,
            project_hires=project_hires,
            filter=filter,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return self._get_all_report_charts_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAllReportCharts(BaseApi):

    async def aget_all_report_charts(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReportGetAllReportChartsResponsePydantic:
        raw_response = await self.raw.aget_all_report_charts(
            org_id=org_id,
            report_id=report_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            scenario_id=scenario_id,
            project_hires=project_hires,
            filter=filter,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            **kwargs,
        )
        if validate:
            return RootModel[ReportGetAllReportChartsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ReportGetAllReportChartsResponsePydantic, raw_response.body)
    
    
    def get_all_report_charts(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ReportGetAllReportChartsResponsePydantic:
        raw_response = self.raw.get_all_report_charts(
            org_id=org_id,
            report_id=report_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            scenario_id=scenario_id,
            project_hires=project_hires,
            filter=filter,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        if validate:
            return RootModel[ReportGetAllReportChartsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ReportGetAllReportChartsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_report_charts_mapped_args(
            org_id=org_id,
            report_id=report_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            scenario_id=scenario_id,
            project_hires=project_hires,
            filter=filter,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return await self._aget_all_report_charts_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        report_id: str,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        project_hires: typing.Optional[bool] = None,
        filter: typing.Optional[str] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_report_charts_mapped_args(
            org_id=org_id,
            report_id=report_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            scenario_id=scenario_id,
            project_hires=project_hires,
            filter=filter,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return self._get_all_report_charts_oapg(
            query_params=args.query,
            path_params=args.path,
        )
