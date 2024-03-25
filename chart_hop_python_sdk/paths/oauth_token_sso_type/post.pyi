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

from chart_hop_python_sdk.model.access_token_response import AccessTokenResponse as AccessTokenResponseSchema
from chart_hop_python_sdk.model.access_token_request import AccessTokenRequest as AccessTokenRequestSchema

from chart_hop_python_sdk.type.access_token_request import AccessTokenRequest
from chart_hop_python_sdk.type.access_token_response import AccessTokenResponse

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.access_token_response import AccessTokenResponse as AccessTokenResponsePydantic
from chart_hop_python_sdk.pydantic.access_token_request import AccessTokenRequest as AccessTokenRequestPydantic

# Query params
CreateOrgSchema = schemas.BoolSchema


class SignupSourceSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ADP_MARKETPLACE(cls):
        return cls("ADP_MARKETPLACE")
    
    @schemas.classproperty
    def SELF_SERVE(cls):
        return cls("SELF_SERVE")
    
    @schemas.classproperty
    def SELF_SERVE_TEST(cls):
        return cls("SELF_SERVE_TEST")
    
    @schemas.classproperty
    def SEQUOIA_ONE(cls):
        return cls("SEQUOIA_ONE")
    
    @schemas.classproperty
    def CONNECT(cls):
        return cls("CONNECT")
UtmParamsSchema = schemas.StrSchema
EmailSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'createOrg': typing.Union[CreateOrgSchema, bool, ],
        'signupSource': typing.Union[SignupSourceSchema, str, ],
        'utmParams': typing.Union[UtmParamsSchema, str, ],
        'email': typing.Union[EmailSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_create_org = api_client.QueryParameter(
    name="createOrg",
    style=api_client.ParameterStyle.FORM,
    schema=CreateOrgSchema,
    explode=True,
)
request_query_signup_source = api_client.QueryParameter(
    name="signupSource",
    style=api_client.ParameterStyle.FORM,
    schema=SignupSourceSchema,
    explode=True,
)
request_query_utm_params = api_client.QueryParameter(
    name="utmParams",
    style=api_client.ParameterStyle.FORM,
    schema=UtmParamsSchema,
    explode=True,
)
request_query_email = api_client.QueryParameter(
    name="email",
    style=api_client.ParameterStyle.FORM,
    schema=EmailSchema,
    explode=True,
)
# Path params
TypeSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'type': typing.Union[TypeSchema, str, ],
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


request_path_type = api_client.PathParameter(
    name="type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TypeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = AccessTokenRequestSchema


request_body_access_token_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = AccessTokenResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AccessTokenResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AccessTokenResponse


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _generate_bearer_token_from_sso_mapped_args(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if id_token is not None:
            _body["idToken"] = id_token
        if scope is not None:
            _body["scope"] = scope
        if from_token is not None:
            _body["fromToken"] = from_token
        args.body = _body
        if create_org is not None:
            _query_params["createOrg"] = create_org
        if signup_source is not None:
            _query_params["signupSource"] = signup_source
        if utm_params is not None:
            _query_params["utmParams"] = utm_params
        if email is not None:
            _query_params["email"] = email
        if type is not None:
            _path_params["type"] = type
        args.query = _query_params
        args.path = _path_params
        return args

    async def _agenerate_bearer_token_from_sso_oapg(
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
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Return an Oauth2 Authorization bearer token, given a SSO id token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_type,
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
            request_query_create_org,
            request_query_signup_source,
            request_query_utm_params,
            request_query_email,
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
            path_template='/oauth/token/sso/{type}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_access_token_request.serialize(body, content_type)
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


    def _generate_bearer_token_from_sso_oapg(
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
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Return an Oauth2 Authorization bearer token, given a SSO id token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_type,
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
            request_query_create_org,
            request_query_signup_source,
            request_query_utm_params,
            request_query_email,
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
            path_template='/oauth/token/sso/{type}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_access_token_request.serialize(body, content_type)
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


class GenerateBearerTokenFromSsoRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_bearer_token_from_sso(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_bearer_token_from_sso_mapped_args(
            id_token=id_token,
            scope=scope,
            type=type,
            from_token=from_token,
            create_org=create_org,
            signup_source=signup_source,
            utm_params=utm_params,
            email=email,
        )
        return await self._agenerate_bearer_token_from_sso_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def generate_bearer_token_from_sso(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_bearer_token_from_sso_mapped_args(
            id_token=id_token,
            scope=scope,
            type=type,
            from_token=from_token,
            create_org=create_org,
            signup_source=signup_source,
            utm_params=utm_params,
            email=email,
        )
        return self._generate_bearer_token_from_sso_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class GenerateBearerTokenFromSso(BaseApi):

    async def agenerate_bearer_token_from_sso(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AccessTokenResponsePydantic:
        raw_response = await self.raw.agenerate_bearer_token_from_sso(
            id_token=id_token,
            scope=scope,
            type=type,
            from_token=from_token,
            create_org=create_org,
            signup_source=signup_source,
            utm_params=utm_params,
            email=email,
            **kwargs,
        )
        if validate:
            return AccessTokenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AccessTokenResponsePydantic, raw_response.body)
    
    
    def generate_bearer_token_from_sso(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AccessTokenResponsePydantic:
        raw_response = self.raw.generate_bearer_token_from_sso(
            id_token=id_token,
            scope=scope,
            type=type,
            from_token=from_token,
            create_org=create_org,
            signup_source=signup_source,
            utm_params=utm_params,
            email=email,
        )
        if validate:
            return AccessTokenResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AccessTokenResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_bearer_token_from_sso_mapped_args(
            id_token=id_token,
            scope=scope,
            type=type,
            from_token=from_token,
            create_org=create_org,
            signup_source=signup_source,
            utm_params=utm_params,
            email=email,
        )
        return await self._agenerate_bearer_token_from_sso_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        id_token: str,
        scope: str,
        type: str,
        from_token: typing.Optional[str] = None,
        create_org: typing.Optional[bool] = None,
        signup_source: typing.Optional[str] = None,
        utm_params: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_bearer_token_from_sso_mapped_args(
            id_token=id_token,
            scope=scope,
            type=type,
            from_token=from_token,
            create_org=create_org,
            signup_source=signup_source,
            utm_params=utm_params,
            email=email,
        )
        return self._generate_bearer_token_from_sso_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )
