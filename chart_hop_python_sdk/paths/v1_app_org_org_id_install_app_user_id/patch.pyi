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

from chart_hop_python_sdk.model.update_user import UpdateUser as UpdateUserSchema
from chart_hop_python_sdk.model.org_access import OrgAccess as OrgAccessSchema
from chart_hop_python_sdk.model.user_email_setting import UserEmailSetting as UserEmailSettingSchema
from chart_hop_python_sdk.model.name import Name as NameSchema

from chart_hop_python_sdk.type.name import Name
from chart_hop_python_sdk.type.user_email_setting import UserEmailSetting
from chart_hop_python_sdk.type.update_user import UpdateUser
from chart_hop_python_sdk.type.org_access import OrgAccess

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.update_user import UpdateUser as UpdateUserPydantic
from chart_hop_python_sdk.pydantic.name import Name as NamePydantic
from chart_hop_python_sdk.pydantic.user_email_setting import UserEmailSetting as UserEmailSettingPydantic
from chart_hop_python_sdk.pydantic.org_access import OrgAccess as OrgAccessPydantic

# Query params
IncludeInactiveSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'includeInactive': typing.Union[IncludeInactiveSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_include_inactive = api_client.QueryParameter(
    name="includeInactive",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeInactiveSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
AppUserIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'appUserId': typing.Union[AppUserIdSchema, str, ],
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
request_path_app_user_id = api_client.PathParameter(
    name="appUserId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AppUserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateUserSchema


request_body_update_user = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
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


class BaseApi(api_client.Api):

    def _update_installed_app_mapped_args(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if app_id is not None:
            _body["appId"] = app_id
        if name is not None:
            _body["name"] = name
        if email is not None:
            _body["email"] = email
        if orgs is not None:
            _body["orgs"] = orgs
        if image_path is not None:
            _body["imagePath"] = image_path
        if status is not None:
            _body["status"] = status
        if options is not None:
            _body["options"] = options
        if internal_options is not None:
            _body["internalOptions"] = internal_options
        if secrets is not None:
            _body["secrets"] = secrets
        if email_settings is not None:
            _body["emailSettings"] = email_settings
        args.body = _body
        if include_inactive is not None:
            _query_params["includeInactive"] = include_inactive
        if org_id is not None:
            _path_params["orgId"] = org_id
        if app_user_id is not None:
            _path_params["appUserId"] = app_user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_installed_app_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update the settings of an installed app
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
            request_path_app_user_id,
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
            request_query_include_inactive,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/app/org/{orgId}/install/{appUserId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_user.serialize(body, content_type)
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


    def _update_installed_app_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update the settings of an installed app
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
            request_path_app_user_id,
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
            request_query_include_inactive,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/app/org/{orgId}/install/{appUserId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_user.serialize(body, content_type)
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


class UpdateInstalledAppRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_installed_app(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_installed_app_mapped_args(
            org_id=org_id,
            app_user_id=app_user_id,
            app_id=app_id,
            name=name,
            email=email,
            orgs=orgs,
            image_path=image_path,
            status=status,
            options=options,
            internal_options=internal_options,
            secrets=secrets,
            email_settings=email_settings,
            include_inactive=include_inactive,
        )
        return await self._aupdate_installed_app_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_installed_app(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_installed_app_mapped_args(
            org_id=org_id,
            app_user_id=app_user_id,
            app_id=app_id,
            name=name,
            email=email,
            orgs=orgs,
            image_path=image_path,
            status=status,
            options=options,
            internal_options=internal_options,
            secrets=secrets,
            email_settings=email_settings,
            include_inactive=include_inactive,
        )
        return self._update_installed_app_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateInstalledApp(BaseApi):

    async def aupdate_installed_app(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_installed_app(
            org_id=org_id,
            app_user_id=app_user_id,
            app_id=app_id,
            name=name,
            email=email,
            orgs=orgs,
            image_path=image_path,
            status=status,
            options=options,
            internal_options=internal_options,
            secrets=secrets,
            email_settings=email_settings,
            include_inactive=include_inactive,
            **kwargs,
        )
    
    
    def update_installed_app(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_installed_app(
            org_id=org_id,
            app_user_id=app_user_id,
            app_id=app_id,
            name=name,
            email=email,
            orgs=orgs,
            image_path=image_path,
            status=status,
            options=options,
            internal_options=internal_options,
            secrets=secrets,
            email_settings=email_settings,
            include_inactive=include_inactive,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_installed_app_mapped_args(
            org_id=org_id,
            app_user_id=app_user_id,
            app_id=app_id,
            name=name,
            email=email,
            orgs=orgs,
            image_path=image_path,
            status=status,
            options=options,
            internal_options=internal_options,
            secrets=secrets,
            email_settings=email_settings,
            include_inactive=include_inactive,
        )
        return await self._aupdate_installed_app_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        app_user_id: str,
        app_id: typing.Optional[str] = None,
        name: typing.Optional[Name] = None,
        email: typing.Optional[str] = None,
        orgs: typing.Optional[typing.List[OrgAccess]] = None,
        image_path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        internal_options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        secrets: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        email_settings: typing.Optional[typing.List[UserEmailSetting]] = None,
        include_inactive: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_installed_app_mapped_args(
            org_id=org_id,
            app_user_id=app_user_id,
            app_id=app_id,
            name=name,
            email=email,
            orgs=orgs,
            image_path=image_path,
            status=status,
            options=options,
            internal_options=internal_options,
            secrets=secrets,
            email_settings=email_settings,
            include_inactive=include_inactive,
        )
        return self._update_installed_app_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

