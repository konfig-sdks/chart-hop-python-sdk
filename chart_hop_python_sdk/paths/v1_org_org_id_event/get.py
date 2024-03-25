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

from chart_hop_python_sdk.model.results_event import ResultsEvent as ResultsEventSchema

from chart_hop_python_sdk.type.results_event import ResultsEvent

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.results_event import ResultsEvent as ResultsEventPydantic

from . import path

# Query params
UserIdSchema = schemas.StrSchema
EntityIdSchema = schemas.StrSchema


class EntityTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "ACTION": "ACTION",
            "AGREEMENT": "AGREEMENT",
            "APP": "APP",
            "APP_CONFIG": "APP_CONFIG",
            "APPROVAL_CHAIN": "APPROVAL_CHAIN",
            "APPROVAL_CHAIN_STAGE": "APPROVAL_CHAIN_STAGE",
            "APPROVAL_REQUEST": "APPROVAL_REQUEST",
            "ASSESSMENT": "ASSESSMENT",
            "BUDGET_POOL": "BUDGET_POOL",
            "BUNDLE": "BUNDLE",
            "CATEGORY": "CATEGORY",
            "CATEGORY_SORT": "CATEGORY_SORT",
            "CHANGE": "CHANGE",
            "COMMENT": "COMMENT",
            "COMP_BAND": "COMP_BAND",
            "COMP_REVIEW": "COMP_REVIEW",
            "CONTENT": "CONTENT",
            "CUSTOMER": "CUSTOMER",
            "DATA_VIEW": "DATA_VIEW",
            "EXCHANGE_RATE": "EXCHANGE_RATE",
            "EMAIL_TEMPLATE": "EMAIL_TEMPLATE",
            "FIELD": "FIELD",
            "FILE": "FILE",
            "FORM": "FORM",
            "FORM_DRAFT": "FORM_DRAFT",
            "FORM_RESPONSE": "FORM_RESPONSE",
            "GEOCODE": "GEOCODE",
            "GROUP": "GROUP",
            "GUIDELINE": "GUIDELINE",
            "JOB": "JOB",
            "JOB_LEVEL": "JOB_LEVEL",
            "MEDIA": "MEDIA",
            "MESSAGE": "MESSAGE",
            "MULTIPLIER": "MULTIPLIER",
            "ORG": "ORG",
            "ORG_CONFIG": "ORG_CONFIG",
            "PERSON": "PERSON",
            "PROFILE_TAB": "PROFILE_TAB",
            "POLICY": "POLICY",
            "POSITION": "POSITION",
            "PROCESS": "PROCESS",
            "PRODUCT": "PRODUCT",
            "QUERY_TOKEN": "QUERY_TOKEN",
            "QUESTION": "QUESTION",
            "REPORT": "REPORT",
            "REPORT_CHART": "REPORT_CHART",
            "ROLE": "ROLE",
            "SCENARIO": "SCENARIO",
            "STOCK_PRICE": "STOCK_PRICE",
            "TABLE": "TABLE",
            "TABLE_ROW": "TABLE_ROW",
            "TASK_CONFIG": "TASK_CONFIG",
            "TEMPLATE": "TEMPLATE",
            "TASK": "TASK",
            "TOKEN": "TOKEN",
            "TIMEOFF": "TIMEOFF",
            "TRACKED_GROUP": "TRACKED_GROUP",
            "USER": "USER",
        }
    
    @schemas.classproperty
    def ACTION(cls):
        return cls("ACTION")
    
    @schemas.classproperty
    def AGREEMENT(cls):
        return cls("AGREEMENT")
    
    @schemas.classproperty
    def APP(cls):
        return cls("APP")
    
    @schemas.classproperty
    def APP_CONFIG(cls):
        return cls("APP_CONFIG")
    
    @schemas.classproperty
    def APPROVAL_CHAIN(cls):
        return cls("APPROVAL_CHAIN")
    
    @schemas.classproperty
    def APPROVAL_CHAIN_STAGE(cls):
        return cls("APPROVAL_CHAIN_STAGE")
    
    @schemas.classproperty
    def APPROVAL_REQUEST(cls):
        return cls("APPROVAL_REQUEST")
    
    @schemas.classproperty
    def ASSESSMENT(cls):
        return cls("ASSESSMENT")
    
    @schemas.classproperty
    def BUDGET_POOL(cls):
        return cls("BUDGET_POOL")
    
    @schemas.classproperty
    def BUNDLE(cls):
        return cls("BUNDLE")
    
    @schemas.classproperty
    def CATEGORY(cls):
        return cls("CATEGORY")
    
    @schemas.classproperty
    def CATEGORY_SORT(cls):
        return cls("CATEGORY_SORT")
    
    @schemas.classproperty
    def CHANGE(cls):
        return cls("CHANGE")
    
    @schemas.classproperty
    def COMMENT(cls):
        return cls("COMMENT")
    
    @schemas.classproperty
    def COMP_BAND(cls):
        return cls("COMP_BAND")
    
    @schemas.classproperty
    def COMP_REVIEW(cls):
        return cls("COMP_REVIEW")
    
    @schemas.classproperty
    def CONTENT(cls):
        return cls("CONTENT")
    
    @schemas.classproperty
    def CUSTOMER(cls):
        return cls("CUSTOMER")
    
    @schemas.classproperty
    def DATA_VIEW(cls):
        return cls("DATA_VIEW")
    
    @schemas.classproperty
    def EXCHANGE_RATE(cls):
        return cls("EXCHANGE_RATE")
    
    @schemas.classproperty
    def EMAIL_TEMPLATE(cls):
        return cls("EMAIL_TEMPLATE")
    
    @schemas.classproperty
    def FIELD(cls):
        return cls("FIELD")
    
    @schemas.classproperty
    def FILE(cls):
        return cls("FILE")
    
    @schemas.classproperty
    def FORM(cls):
        return cls("FORM")
    
    @schemas.classproperty
    def FORM_DRAFT(cls):
        return cls("FORM_DRAFT")
    
    @schemas.classproperty
    def FORM_RESPONSE(cls):
        return cls("FORM_RESPONSE")
    
    @schemas.classproperty
    def GEOCODE(cls):
        return cls("GEOCODE")
    
    @schemas.classproperty
    def GROUP(cls):
        return cls("GROUP")
    
    @schemas.classproperty
    def GUIDELINE(cls):
        return cls("GUIDELINE")
    
    @schemas.classproperty
    def JOB(cls):
        return cls("JOB")
    
    @schemas.classproperty
    def JOB_LEVEL(cls):
        return cls("JOB_LEVEL")
    
    @schemas.classproperty
    def MEDIA(cls):
        return cls("MEDIA")
    
    @schemas.classproperty
    def MESSAGE(cls):
        return cls("MESSAGE")
    
    @schemas.classproperty
    def MULTIPLIER(cls):
        return cls("MULTIPLIER")
    
    @schemas.classproperty
    def ORG(cls):
        return cls("ORG")
    
    @schemas.classproperty
    def ORG_CONFIG(cls):
        return cls("ORG_CONFIG")
    
    @schemas.classproperty
    def PERSON(cls):
        return cls("PERSON")
    
    @schemas.classproperty
    def PROFILE_TAB(cls):
        return cls("PROFILE_TAB")
    
    @schemas.classproperty
    def POLICY(cls):
        return cls("POLICY")
    
    @schemas.classproperty
    def POSITION(cls):
        return cls("POSITION")
    
    @schemas.classproperty
    def PROCESS(cls):
        return cls("PROCESS")
    
    @schemas.classproperty
    def PRODUCT(cls):
        return cls("PRODUCT")
    
    @schemas.classproperty
    def QUERY_TOKEN(cls):
        return cls("QUERY_TOKEN")
    
    @schemas.classproperty
    def QUESTION(cls):
        return cls("QUESTION")
    
    @schemas.classproperty
    def REPORT(cls):
        return cls("REPORT")
    
    @schemas.classproperty
    def REPORT_CHART(cls):
        return cls("REPORT_CHART")
    
    @schemas.classproperty
    def ROLE(cls):
        return cls("ROLE")
    
    @schemas.classproperty
    def SCENARIO(cls):
        return cls("SCENARIO")
    
    @schemas.classproperty
    def STOCK_PRICE(cls):
        return cls("STOCK_PRICE")
    
    @schemas.classproperty
    def TABLE(cls):
        return cls("TABLE")
    
    @schemas.classproperty
    def TABLE_ROW(cls):
        return cls("TABLE_ROW")
    
    @schemas.classproperty
    def TASK_CONFIG(cls):
        return cls("TASK_CONFIG")
    
    @schemas.classproperty
    def TEMPLATE(cls):
        return cls("TEMPLATE")
    
    @schemas.classproperty
    def TASK(cls):
        return cls("TASK")
    
    @schemas.classproperty
    def TOKEN(cls):
        return cls("TOKEN")
    
    @schemas.classproperty
    def TIMEOFF(cls):
        return cls("TIMEOFF")
    
    @schemas.classproperty
    def TRACKED_GROUP(cls):
        return cls("TRACKED_GROUP")
    
    @schemas.classproperty
    def USER(cls):
        return cls("USER")
ParentEntityIdSchema = schemas.StrSchema
ScenarioIdSchema = schemas.StrSchema
ProcessIdSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema
CodeSchema = schemas.StrSchema
ModelFromSchema = schemas.Int64Schema
LimitSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'userId': typing.Union[UserIdSchema, str, ],
        'entityId': typing.Union[EntityIdSchema, str, ],
        'entityType': typing.Union[EntityTypeSchema, str, ],
        'parentEntityId': typing.Union[ParentEntityIdSchema, str, ],
        'scenarioId': typing.Union[ScenarioIdSchema, str, ],
        'processId': typing.Union[ProcessIdSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
        'code': typing.Union[CodeSchema, str, ],
        'from': typing.Union[ModelFromSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_user_id = api_client.QueryParameter(
    name="userId",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    explode=True,
)
request_query_entity_id = api_client.QueryParameter(
    name="entityId",
    style=api_client.ParameterStyle.FORM,
    schema=EntityIdSchema,
    explode=True,
)
request_query_entity_type = api_client.QueryParameter(
    name="entityType",
    style=api_client.ParameterStyle.FORM,
    schema=EntityTypeSchema,
    explode=True,
)
request_query_parent_entity_id = api_client.QueryParameter(
    name="parentEntityId",
    style=api_client.ParameterStyle.FORM,
    schema=ParentEntityIdSchema,
    explode=True,
)
request_query_scenario_id = api_client.QueryParameter(
    name="scenarioId",
    style=api_client.ParameterStyle.FORM,
    schema=ScenarioIdSchema,
    explode=True,
)
request_query_process_id = api_client.QueryParameter(
    name="processId",
    style=api_client.ParameterStyle.FORM,
    schema=ProcessIdSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_code = api_client.QueryParameter(
    name="code",
    style=api_client.ParameterStyle.FORM,
    schema=CodeSchema,
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
SchemaFor200ResponseBodyApplicationJson = ResultsEventSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultsEvent


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultsEvent


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

    def _get_past_events_mapped_args(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if user_id is not None:
            _query_params["userId"] = user_id
        if entity_id is not None:
            _query_params["entityId"] = entity_id
        if entity_type is not None:
            _query_params["entityType"] = entity_type
        if parent_entity_id is not None:
            _query_params["parentEntityId"] = parent_entity_id
        if scenario_id is not None:
            _query_params["scenarioId"] = scenario_id
        if process_id is not None:
            _query_params["processId"] = process_id
        if fields is not None:
            _query_params["fields"] = fields
        if code is not None:
            _query_params["code"] = code
        if _from is not None:
            _query_params["from"] = _from
        if limit is not None:
            _query_params["limit"] = limit
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_past_events_oapg(
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
        Return past events, paginated, without payloads present
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
            request_query_user_id,
            request_query_entity_id,
            request_query_entity_type,
            request_query_parent_entity_id,
            request_query_scenario_id,
            request_query_process_id,
            request_query_fields,
            request_query_code,
            request_query__from,
            request_query_limit,
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
            path_template='/v1/org/{orgId}/event',
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


    def _get_past_events_oapg(
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
        Return past events, paginated, without payloads present
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
            request_query_user_id,
            request_query_entity_id,
            request_query_entity_type,
            request_query_parent_entity_id,
            request_query_scenario_id,
            request_query_process_id,
            request_query_fields,
            request_query_code,
            request_query__from,
            request_query_limit,
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
            path_template='/v1/org/{orgId}/event',
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


class GetPastEventsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_past_events(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_past_events_mapped_args(
            org_id=org_id,
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            parent_entity_id=parent_entity_id,
            scenario_id=scenario_id,
            process_id=process_id,
            fields=fields,
            code=code,
            _from=_from,
            limit=limit,
        )
        return await self._aget_past_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_past_events(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_past_events_mapped_args(
            org_id=org_id,
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            parent_entity_id=parent_entity_id,
            scenario_id=scenario_id,
            process_id=process_id,
            fields=fields,
            code=code,
            _from=_from,
            limit=limit,
        )
        return self._get_past_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetPastEvents(BaseApi):

    async def aget_past_events(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultsEventPydantic:
        raw_response = await self.raw.aget_past_events(
            org_id=org_id,
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            parent_entity_id=parent_entity_id,
            scenario_id=scenario_id,
            process_id=process_id,
            fields=fields,
            code=code,
            _from=_from,
            limit=limit,
            **kwargs,
        )
        if validate:
            return ResultsEventPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsEventPydantic, raw_response.body)
    
    
    def get_past_events(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ResultsEventPydantic:
        raw_response = self.raw.get_past_events(
            org_id=org_id,
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            parent_entity_id=parent_entity_id,
            scenario_id=scenario_id,
            process_id=process_id,
            fields=fields,
            code=code,
            _from=_from,
            limit=limit,
        )
        if validate:
            return ResultsEventPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultsEventPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_past_events_mapped_args(
            org_id=org_id,
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            parent_entity_id=parent_entity_id,
            scenario_id=scenario_id,
            process_id=process_id,
            fields=fields,
            code=code,
            _from=_from,
            limit=limit,
        )
        return await self._aget_past_events_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        user_id: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        parent_entity_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        _from: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_past_events_mapped_args(
            org_id=org_id,
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            parent_entity_id=parent_entity_id,
            scenario_id=scenario_id,
            process_id=process_id,
            fields=fields,
            code=code,
            _from=_from,
            limit=limit,
        )
        return self._get_past_events_oapg(
            query_params=args.query,
            path_params=args.path,
        )

