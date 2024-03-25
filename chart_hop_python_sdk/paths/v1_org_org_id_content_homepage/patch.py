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

from chart_hop_python_sdk.model.content_block import ContentBlock as ContentBlockSchema
from chart_hop_python_sdk.model.share_access import ShareAccess as ShareAccessSchema
from chart_hop_python_sdk.model.update_content import UpdateContent as UpdateContentSchema

from chart_hop_python_sdk.type.share_access import ShareAccess
from chart_hop_python_sdk.type.content_block import ContentBlock
from chart_hop_python_sdk.type.update_content import UpdateContent

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.update_content import UpdateContent as UpdateContentPydantic
from chart_hop_python_sdk.pydantic.share_access import ShareAccess as ShareAccessPydantic
from chart_hop_python_sdk.pydantic.content_block import ContentBlock as ContentBlockPydantic

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
SchemaForRequestBodyApplicationJson = UpdateContentSchema


request_body_update_content = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
)
_status_code_to_response = {
    'default': _response_for_default,
}


class BaseApi(api_client.Api):

    def _update_homepage_content_mapped_args(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if parent_content_id is not None:
            _body["parentContentId"] = parent_content_id
        if path is not None:
            _body["path"] = path
        if blocks is not None:
            _body["blocks"] = blocks
        if image_path is not None:
            _body["imagePath"] = image_path
        if emoji is not None:
            _body["emoji"] = emoji
        if cover_image_path is not None:
            _body["coverImagePath"] = cover_image_path
        if sensitive is not None:
            _body["sensitive"] = sensitive
        if share_access is not None:
            _body["shareAccess"] = share_access
        if status is not None:
            _body["status"] = status
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.path = _path_params
        return args

    async def _aupdate_homepage_content_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update the homepage content
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/content/homepage',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_content.serialize(body, content_type)
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
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


    def _update_homepage_content_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update the homepage content
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/content/homepage',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_content.serialize(body, content_type)
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateHomepageContentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_homepage_content(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_homepage_content_mapped_args(
            org_id=org_id,
            title=title,
            parent_content_id=parent_content_id,
            path=path,
            blocks=blocks,
            image_path=image_path,
            emoji=emoji,
            cover_image_path=cover_image_path,
            sensitive=sensitive,
            share_access=share_access,
            status=status,
        )
        return await self._aupdate_homepage_content_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_homepage_content(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_homepage_content_mapped_args(
            org_id=org_id,
            title=title,
            parent_content_id=parent_content_id,
            path=path,
            blocks=blocks,
            image_path=image_path,
            emoji=emoji,
            cover_image_path=cover_image_path,
            sensitive=sensitive,
            share_access=share_access,
            status=status,
        )
        return self._update_homepage_content_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateHomepageContent(BaseApi):

    async def aupdate_homepage_content(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_homepage_content(
            org_id=org_id,
            title=title,
            parent_content_id=parent_content_id,
            path=path,
            blocks=blocks,
            image_path=image_path,
            emoji=emoji,
            cover_image_path=cover_image_path,
            sensitive=sensitive,
            share_access=share_access,
            status=status,
            **kwargs,
        )
    
    
    def update_homepage_content(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_homepage_content(
            org_id=org_id,
            title=title,
            parent_content_id=parent_content_id,
            path=path,
            blocks=blocks,
            image_path=image_path,
            emoji=emoji,
            cover_image_path=cover_image_path,
            sensitive=sensitive,
            share_access=share_access,
            status=status,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_homepage_content_mapped_args(
            org_id=org_id,
            title=title,
            parent_content_id=parent_content_id,
            path=path,
            blocks=blocks,
            image_path=image_path,
            emoji=emoji,
            cover_image_path=cover_image_path,
            sensitive=sensitive,
            share_access=share_access,
            status=status,
        )
        return await self._aupdate_homepage_content_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        title: typing.Optional[str] = None,
        parent_content_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        blocks: typing.Optional[typing.List[ContentBlock]] = None,
        image_path: typing.Optional[str] = None,
        emoji: typing.Optional[str] = None,
        cover_image_path: typing.Optional[str] = None,
        sensitive: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_homepage_content_mapped_args(
            org_id=org_id,
            title=title,
            parent_content_id=parent_content_id,
            path=path,
            blocks=blocks,
            image_path=image_path,
            emoji=emoji,
            cover_image_path=cover_image_path,
            sensitive=sensitive,
            share_access=share_access,
            status=status,
        )
        return self._update_homepage_content_oapg(
            body=args.body,
            path_params=args.path,
        )

