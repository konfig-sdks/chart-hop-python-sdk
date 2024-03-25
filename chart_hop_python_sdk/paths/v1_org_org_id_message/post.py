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

from chart_hop_python_sdk.model.partial_message import PartialMessage as PartialMessageSchema
from chart_hop_python_sdk.model.message import Message as MessageSchema

from chart_hop_python_sdk.type.partial_message import PartialMessage
from chart_hop_python_sdk.type.message import Message

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.message import Message as MessagePydantic
from chart_hop_python_sdk.pydantic.partial_message import PartialMessage as PartialMessagePydantic

from . import path

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
SchemaForRequestBodyApplicationJson = PartialMessageSchema


request_body_partial_message = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = MessageSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Message


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Message


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_message_mapped_args(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if id is not None:
            _body["id"] = id
        if org_id is not None:
            _body["orgId"] = org_id
        if type is not None:
            _body["type"] = type
        if notification_type is not None:
            _body["notificationType"] = notification_type
        if user_id is not None:
            _body["userId"] = user_id
        if content is not None:
            _body["content"] = content
        if message_url is not None:
            _body["messageUrl"] = message_url
        if key is not None:
            _body["key"] = key
        if read_at is not None:
            _body["readAt"] = read_at
        if seen_at is not None:
            _body["seenAt"] = seen_at
        if create_id is not None:
            _body["createId"] = create_id
        if create_at is not None:
            _body["createAt"] = create_at
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.path = _path_params
        return args

    async def _acreate_new_message_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new message
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/v1/org/{orgId}/message',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_partial_message.serialize(body, content_type)
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


    def _create_new_message_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new message
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/v1/org/{orgId}/message',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_partial_message.serialize(body, content_type)
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


class CreateNewMessageRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_message(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_message_mapped_args(
            org_id=org_id,
            title=title,
            id=id,
            org_id=org_id,
            type=type,
            notification_type=notification_type,
            user_id=user_id,
            content=content,
            message_url=message_url,
            key=key,
            read_at=read_at,
            seen_at=seen_at,
            create_id=create_id,
            create_at=create_at,
        )
        return await self._acreate_new_message_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_message(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_message_mapped_args(
            org_id=org_id,
            title=title,
            id=id,
            org_id=org_id,
            type=type,
            notification_type=notification_type,
            user_id=user_id,
            content=content,
            message_url=message_url,
            key=key,
            read_at=read_at,
            seen_at=seen_at,
            create_id=create_id,
            create_at=create_at,
        )
        return self._create_new_message_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateNewMessage(BaseApi):

    async def acreate_new_message(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> MessagePydantic:
        raw_response = await self.raw.acreate_new_message(
            org_id=org_id,
            title=title,
            id=id,
            org_id=org_id,
            type=type,
            notification_type=notification_type,
            user_id=user_id,
            content=content,
            message_url=message_url,
            key=key,
            read_at=read_at,
            seen_at=seen_at,
            create_id=create_id,
            create_at=create_at,
            **kwargs,
        )
        if validate:
            return MessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(MessagePydantic, raw_response.body)
    
    
    def create_new_message(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
        validate: bool = False,
    ) -> MessagePydantic:
        raw_response = self.raw.create_new_message(
            org_id=org_id,
            title=title,
            id=id,
            org_id=org_id,
            type=type,
            notification_type=notification_type,
            user_id=user_id,
            content=content,
            message_url=message_url,
            key=key,
            read_at=read_at,
            seen_at=seen_at,
            create_id=create_id,
            create_at=create_at,
        )
        if validate:
            return MessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(MessagePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_message_mapped_args(
            org_id=org_id,
            title=title,
            id=id,
            org_id=org_id,
            type=type,
            notification_type=notification_type,
            user_id=user_id,
            content=content,
            message_url=message_url,
            key=key,
            read_at=read_at,
            seen_at=seen_at,
            create_id=create_id,
            create_at=create_at,
        )
        return await self._acreate_new_message_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        notification_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        message_url: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        read_at: typing.Optional[str] = None,
        seen_at: typing.Optional[str] = None,
        create_id: typing.Optional[str] = None,
        create_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_message_mapped_args(
            org_id=org_id,
            title=title,
            id=id,
            org_id=org_id,
            type=type,
            notification_type=notification_type,
            user_id=user_id,
            content=content,
            message_url=message_url,
            key=key,
            read_at=read_at,
            seen_at=seen_at,
            create_id=create_id,
            create_at=create_at,
        )
        return self._create_new_message_oapg(
            body=args.body,
            path_params=args.path,
        )

