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

from chart_hop_python_sdk.model.create_approval_chain import CreateApprovalChain as CreateApprovalChainSchema
from chart_hop_python_sdk.model.approval_chain import ApprovalChain as ApprovalChainSchema
from chart_hop_python_sdk.model.create_approval_chain_approval_notifier_user_ids import CreateApprovalChainApprovalNotifierUserIds as CreateApprovalChainApprovalNotifierUserIdsSchema

from chart_hop_python_sdk.type.approval_chain import ApprovalChain
from chart_hop_python_sdk.type.create_approval_chain_approval_notifier_user_ids import CreateApprovalChainApprovalNotifierUserIds
from chart_hop_python_sdk.type.create_approval_chain import CreateApprovalChain

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.create_approval_chain import CreateApprovalChain as CreateApprovalChainPydantic
from chart_hop_python_sdk.pydantic.create_approval_chain_approval_notifier_user_ids import CreateApprovalChainApprovalNotifierUserIds as CreateApprovalChainApprovalNotifierUserIdsPydantic
from chart_hop_python_sdk.pydantic.approval_chain import ApprovalChain as ApprovalChainPydantic

# Query params
CreateDefaultStagesSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'createDefaultStages': typing.Union[CreateDefaultStagesSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_create_default_stages = api_client.QueryParameter(
    name="createDefaultStages",
    style=api_client.ParameterStyle.FORM,
    schema=CreateDefaultStagesSchema,
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
SchemaForRequestBodyApplicationJson = CreateApprovalChainSchema


request_body_create_approval_chain = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = ApprovalChainSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ApprovalChain


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ApprovalChain


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_chain_mapped_args(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if entity_id is not None:
            _body["entityId"] = entity_id
        if entity_type is not None:
            _body["entityType"] = entity_type
        if name is not None:
            _body["name"] = name
        if is_preview is not None:
            _body["isPreview"] = is_preview
        if fallback_approver_job_id is not None:
            _body["fallbackApproverJobId"] = fallback_approver_job_id
        if fallback_approver_job_error is not None:
            _body["fallbackApproverJobError"] = fallback_approver_job_error
        if approval_notifier_user_ids is not None:
            _body["approvalNotifierUserIds"] = approval_notifier_user_ids
        args.body = _body
        if create_default_stages is not None:
            _query_params["createDefaultStages"] = create_default_stages
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_chain_oapg(
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
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create an approval chain
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
            request_query_create_default_stages,
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
            path_template='/v1/org/{orgId}/approval-chain',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_approval_chain.serialize(body, content_type)
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


    def _create_chain_oapg(
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
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create an approval chain
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
            request_query_create_default_stages,
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
            path_template='/v1/org/{orgId}/approval-chain',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_approval_chain.serialize(body, content_type)
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


class CreateChainRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_chain(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_chain_mapped_args(
            name=name,
            is_preview=is_preview,
            approval_notifier_user_ids=approval_notifier_user_ids,
            org_id=org_id,
            entity_id=entity_id,
            entity_type=entity_type,
            fallback_approver_job_id=fallback_approver_job_id,
            fallback_approver_job_error=fallback_approver_job_error,
            create_default_stages=create_default_stages,
        )
        return await self._acreate_chain_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_chain(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_chain_mapped_args(
            name=name,
            is_preview=is_preview,
            approval_notifier_user_ids=approval_notifier_user_ids,
            org_id=org_id,
            entity_id=entity_id,
            entity_type=entity_type,
            fallback_approver_job_id=fallback_approver_job_id,
            fallback_approver_job_error=fallback_approver_job_error,
            create_default_stages=create_default_stages,
        )
        return self._create_chain_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class CreateChain(BaseApi):

    async def acreate_chain(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ApprovalChainPydantic:
        raw_response = await self.raw.acreate_chain(
            name=name,
            is_preview=is_preview,
            approval_notifier_user_ids=approval_notifier_user_ids,
            org_id=org_id,
            entity_id=entity_id,
            entity_type=entity_type,
            fallback_approver_job_id=fallback_approver_job_id,
            fallback_approver_job_error=fallback_approver_job_error,
            create_default_stages=create_default_stages,
            **kwargs,
        )
        if validate:
            return ApprovalChainPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApprovalChainPydantic, raw_response.body)
    
    
    def create_chain(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ApprovalChainPydantic:
        raw_response = self.raw.create_chain(
            name=name,
            is_preview=is_preview,
            approval_notifier_user_ids=approval_notifier_user_ids,
            org_id=org_id,
            entity_id=entity_id,
            entity_type=entity_type,
            fallback_approver_job_id=fallback_approver_job_id,
            fallback_approver_job_error=fallback_approver_job_error,
            create_default_stages=create_default_stages,
        )
        if validate:
            return ApprovalChainPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApprovalChainPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_chain_mapped_args(
            name=name,
            is_preview=is_preview,
            approval_notifier_user_ids=approval_notifier_user_ids,
            org_id=org_id,
            entity_id=entity_id,
            entity_type=entity_type,
            fallback_approver_job_id=fallback_approver_job_id,
            fallback_approver_job_error=fallback_approver_job_error,
            create_default_stages=create_default_stages,
        )
        return await self._acreate_chain_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        is_preview: bool,
        approval_notifier_user_ids: CreateApprovalChainApprovalNotifierUserIds,
        org_id: str,
        entity_id: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        fallback_approver_job_id: typing.Optional[str] = None,
        fallback_approver_job_error: typing.Optional[str] = None,
        create_default_stages: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_chain_mapped_args(
            name=name,
            is_preview=is_preview,
            approval_notifier_user_ids=approval_notifier_user_ids,
            org_id=org_id,
            entity_id=entity_id,
            entity_type=entity_type,
            fallback_approver_job_id=fallback_approver_job_id,
            fallback_approver_job_error=fallback_approver_job_error,
            create_default_stages=create_default_stages,
        )
        return self._create_chain_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

