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

from chart_hop_python_sdk.model.results_data import ResultsData as ResultsDataSchema

from chart_hop_python_sdk.type.results_data import ResultsData

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.results_data import ResultsData as ResultsDataPydantic

from . import path

# Query params
ScenarioIdSchema = schemas.StrSchema
DateSchema = schemas.DateSchema
StartDateSchema = schemas.DateSchema
EndDateSchema = schemas.DateSchema
QSchema = schemas.StrSchema
ModelFromSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
FieldsSchema = schemas.StrSchema


class FieldsListSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsListSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
IncludeAllSchema = schemas.BoolSchema
FormatSchema = schemas.StrSchema
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
        'startDate': typing.Union[StartDateSchema, str, date, ],
        'endDate': typing.Union[EndDateSchema, str, date, ],
        'q': typing.Union[QSchema, str, ],
        'from': typing.Union[ModelFromSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'fields': typing.Union[FieldsSchema, str, ],
        'fieldsList': typing.Union[FieldsListSchema, list, tuple, ],
        'includeAll': typing.Union[IncludeAllSchema, bool, ],
        'format': typing.Union[FormatSchema, str, ],
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
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_fields_list = api_client.QueryParameter(
    name="fieldsList",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsListSchema,
    explode=True,
)
request_query_include_all = api_client.QueryParameter(
    name="includeAll",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeAllSchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
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
SchemaFor200ResponseBodyApplicationJson = ResultsDataSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultsData


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultsData


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
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
    '202': _response_for_202,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _find_in_organization_mapped_args(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if scenario_id is not None:
            _query_params["scenarioId"] = scenario_id
        if date is not None:
            _query_params["date"] = date
        if start_date is not None:
            _query_params["startDate"] = start_date
        if end_date is not None:
            _query_params["endDate"] = end_date
        if q is not None:
            _query_params["q"] = q
        if _from is not None:
            _query_params["from"] = _from
        if limit is not None:
            _query_params["limit"] = limit
        if fields is not None:
            _query_params["fields"] = fields
        if fields_list is not None:
            _query_params["fieldsList"] = fields_list
        if include_all is not None:
            _query_params["includeAll"] = include_all
        if format is not None:
            _query_params["format"] = format
        if return_access is not None:
            _query_params["returnAccess"] = return_access
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _afind_in_organization_oapg(
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
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Find persons in the organization
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
            request_query_start_date,
            request_query_end_date,
            request_query_q,
            request_query__from,
            request_query_limit,
            request_query_fields,
            request_query_fields_list,
            request_query_include_all,
            request_query_format,
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
            path_template='/v2/org/{orgId}/person',
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


    def _find_in_organization_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Find persons in the organization
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
            request_query_start_date,
            request_query_end_date,
            request_query_q,
            request_query__from,
            request_query_limit,
            request_query_fields,
            request_query_fields_list,
            request_query_include_all,
            request_query_format,
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
            path_template='/v2/org/{orgId}/person',
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


class FindInOrganizationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_in_organization(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_in_organization_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            start_date=start_date,
            end_date=end_date,
            q=q,
            _from=_from,
            limit=limit,
            fields=fields,
            fields_list=fields_list,
            include_all=include_all,
            format=format,
            return_access=return_access,
        )
        return await self._afind_in_organization_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def find_in_organization(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_in_organization_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            start_date=start_date,
            end_date=end_date,
            q=q,
            _from=_from,
            limit=limit,
            fields=fields,
            fields_list=fields_list,
            include_all=include_all,
            format=format,
            return_access=return_access,
        )
        return self._find_in_organization_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class FindInOrganization(BaseApi):

    async def afind_in_organization(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultsDataPydantic:
        raw_response = await self.raw.afind_in_organization(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            start_date=start_date,
            end_date=end_date,
            q=q,
            _from=_from,
            limit=limit,
            fields=fields,
            fields_list=fields_list,
            include_all=include_all,
            format=format,
            return_access=return_access,
            **kwargs,
        )
        if validate:
            return ResultsDataPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsDataPydantic, raw_response.body)
    
    
    def find_in_organization(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ResultsDataPydantic:
        raw_response = self.raw.find_in_organization(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            start_date=start_date,
            end_date=end_date,
            q=q,
            _from=_from,
            limit=limit,
            fields=fields,
            fields_list=fields_list,
            include_all=include_all,
            format=format,
            return_access=return_access,
        )
        if validate:
            return ResultsDataPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsDataPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_in_organization_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            start_date=start_date,
            end_date=end_date,
            q=q,
            _from=_from,
            limit=limit,
            fields=fields,
            fields_list=fields_list,
            include_all=include_all,
            format=format,
            return_access=return_access,
        )
        return await self._afind_in_organization_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        start_date: typing.Optional[date] = None,
        end_date: typing.Optional[date] = None,
        q: typing.Optional[str] = None,
        _from: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        fields_list: typing.Optional[typing.List[str]] = None,
        include_all: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        return_access: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_in_organization_mapped_args(
            org_id=org_id,
            scenario_id=scenario_id,
            date=date,
            start_date=start_date,
            end_date=end_date,
            q=q,
            _from=_from,
            limit=limit,
            fields=fields,
            fields_list=fields_list,
            include_all=include_all,
            format=format,
            return_access=return_access,
        )
        return self._find_in_organization_oapg(
            query_params=args.query,
            path_params=args.path,
        )
