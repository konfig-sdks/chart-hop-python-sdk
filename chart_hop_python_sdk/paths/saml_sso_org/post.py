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

from chart_hop_python_sdk.model.saml_perform_sso_assertion_request import SamlPerformSsoAssertionRequest as SamlPerformSsoAssertionRequestSchema

from chart_hop_python_sdk.type.saml_perform_sso_assertion_request import SamlPerformSsoAssertionRequest

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.saml_perform_sso_assertion_request import SamlPerformSsoAssertionRequest as SamlPerformSsoAssertionRequestPydantic

from . import path

# Path params
OrgSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'org': typing.Union[OrgSchema, str, ],
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


request_path_org = api_client.PathParameter(
    name="org",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrgSchema,
    required=True,
)
# Cookie params
TokenSchema = schemas.StrSchema
RequestRequiredCookieParams = typing_extensions.TypedDict(
    'RequestRequiredCookieParams',
    {
    }
)
RequestOptionalCookieParams = typing_extensions.TypedDict(
    'RequestOptionalCookieParams',
    {
        'token': typing.Union[TokenSchema, str, ],
    },
    total=False
)


class RequestCookieParams(RequestRequiredCookieParams, RequestOptionalCookieParams):
    pass


request_cookie_token = api_client.CookieParameter(
    name="token",
    style=api_client.ParameterStyle.FORM,
    schema=TokenSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = SamlPerformSsoAssertionRequestSchema


request_body_saml_perform_sso_assertion_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
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

    def _perform_sso_assertion_0_mapped_args(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _cookie_params = {}
        _body = {}
        if saml_response is not None:
            _body["SAMLResponse"] = saml_response
        if relay_state is not None:
            _body["RelayState"] = relay_state
        args.body = _body
        if org is not None:
            _path_params["org"] = org
        if token is not None:
            _cookie_params["token"] = token
        args.path = _path_params
        args.cookie = _cookie_params
        return args

    async def _aperform_sso_assertion_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
            cookie_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Single sign on URL, where SAML assertion is perform
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        self._verify_typed_dict_inputs_oapg(RequestCookieParams, cookie_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/saml/sso/{org}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_saml_perform_sso_assertion_request.serialize(body, content_type)
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


    def _perform_sso_assertion_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
            cookie_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Single sign on URL, where SAML assertion is perform
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        self._verify_typed_dict_inputs_oapg(RequestCookieParams, cookie_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/saml/sso/{org}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_saml_perform_sso_assertion_request.serialize(body, content_type)
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


class PerformSsoAssertion0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aperform_sso_assertion_0(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._perform_sso_assertion_0_mapped_args(
            org=org,
            token=token,
            saml_response=saml_response,
            relay_state=relay_state,
        )
        return await self._aperform_sso_assertion_0_oapg(
            body=args.body,
            path_params=args.path,
            cookie_params=args.cookie,
            **kwargs,
        )
    
    def perform_sso_assertion_0(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._perform_sso_assertion_0_mapped_args(
            org=org,
            token=token,
            saml_response=saml_response,
            relay_state=relay_state,
        )
        return self._perform_sso_assertion_0_oapg(
            body=args.body,
            path_params=args.path,
            cookie_params=args.cookie,
        )

class PerformSsoAssertion0(BaseApi):

    async def aperform_sso_assertion_0(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aperform_sso_assertion_0(
            org=org,
            token=token,
            saml_response=saml_response,
            relay_state=relay_state,
            **kwargs,
        )
    
    
    def perform_sso_assertion_0(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.perform_sso_assertion_0(
            org=org,
            token=token,
            saml_response=saml_response,
            relay_state=relay_state,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._perform_sso_assertion_0_mapped_args(
            org=org,
            token=token,
            saml_response=saml_response,
            relay_state=relay_state,
        )
        return await self._aperform_sso_assertion_0_oapg(
            body=args.body,
            path_params=args.path,
            cookie_params=args.cookie,
            **kwargs,
        )
    
    def post(
        self,
        org: str,
        token: typing.Optional[str] = None,
        saml_response: typing.Optional[str] = None,
        relay_state: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._perform_sso_assertion_0_mapped_args(
            org=org,
            token=token,
            saml_response=saml_response,
            relay_state=relay_state,
        )
        return self._perform_sso_assertion_0_oapg(
            body=args.body,
            path_params=args.path,
            cookie_params=args.cookie,
        )

