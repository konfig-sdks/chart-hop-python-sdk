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

from chart_hop_python_sdk.model.update_app_config_disabled_field_mappers import UpdateAppConfigDisabledFieldMappers as UpdateAppConfigDisabledFieldMappersSchema
from chart_hop_python_sdk.model.update_app_config_enabled_outbound_field_mappers import UpdateAppConfigEnabledOutboundFieldMappers as UpdateAppConfigEnabledOutboundFieldMappersSchema
from chart_hop_python_sdk.model.field_mapper import FieldMapper as FieldMapperSchema
from chart_hop_python_sdk.model.update_app_config_template_matchers import UpdateAppConfigTemplateMatchers as UpdateAppConfigTemplateMatchersSchema
from chart_hop_python_sdk.model.outbound_field_mapper import OutboundFieldMapper as OutboundFieldMapperSchema
from chart_hop_python_sdk.model.update_app_config import UpdateAppConfig as UpdateAppConfigSchema

from chart_hop_python_sdk.type.update_app_config_enabled_outbound_field_mappers import UpdateAppConfigEnabledOutboundFieldMappers
from chart_hop_python_sdk.type.outbound_field_mapper import OutboundFieldMapper
from chart_hop_python_sdk.type.field_mapper import FieldMapper
from chart_hop_python_sdk.type.update_app_config_disabled_field_mappers import UpdateAppConfigDisabledFieldMappers
from chart_hop_python_sdk.type.update_app_config_template_matchers import UpdateAppConfigTemplateMatchers
from chart_hop_python_sdk.type.update_app_config import UpdateAppConfig

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.outbound_field_mapper import OutboundFieldMapper as OutboundFieldMapperPydantic
from chart_hop_python_sdk.pydantic.update_app_config import UpdateAppConfig as UpdateAppConfigPydantic
from chart_hop_python_sdk.pydantic.field_mapper import FieldMapper as FieldMapperPydantic
from chart_hop_python_sdk.pydantic.update_app_config_disabled_field_mappers import UpdateAppConfigDisabledFieldMappers as UpdateAppConfigDisabledFieldMappersPydantic
from chart_hop_python_sdk.pydantic.update_app_config_enabled_outbound_field_mappers import UpdateAppConfigEnabledOutboundFieldMappers as UpdateAppConfigEnabledOutboundFieldMappersPydantic
from chart_hop_python_sdk.pydantic.update_app_config_template_matchers import UpdateAppConfigTemplateMatchers as UpdateAppConfigTemplateMatchersPydantic

# Path params
AppIdSchema = schemas.StrSchema
UserIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'appId': typing.Union[AppIdSchema, str, ],
        'userId': typing.Union[UserIdSchema, str, ],
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


request_path_app_id = api_client.PathParameter(
    name="appId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AppIdSchema,
    required=True,
)
request_path_user_id = api_client.PathParameter(
    name="userId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateAppConfigSchema


request_body_update_app_config = api_client.RequestBody(
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

    def _update_by_id_mapped_args(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if field_mappers is not None:
            _body["fieldMappers"] = field_mappers
        if custom_field_mappers is not None:
            _body["customFieldMappers"] = custom_field_mappers
        if custom_outbound_field_mappers is not None:
            _body["customOutboundFieldMappers"] = custom_outbound_field_mappers
        if disabled_field_mappers is not None:
            _body["disabledFieldMappers"] = disabled_field_mappers
        if enabled_outbound_field_mappers is not None:
            _body["enabledOutboundFieldMappers"] = enabled_outbound_field_mappers
        if template_matchers is not None:
            _body["templateMatchers"] = template_matchers
        if options is not None:
            _body["options"] = options
        args.body = _body
        if app_id is not None:
            _path_params["appId"] = app_id
        if user_id is not None:
            _path_params["userId"] = user_id
        args.path = _path_params
        return args

    async def _aupdate_by_id_oapg(
        self,
        body: typing.Any = None,
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
        Update an existing app
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
            request_path_user_id,
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
            path_template='/v1/app-config/{appId}/{userId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_app_config.serialize(body, content_type)
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


    def _update_by_id_oapg(
        self,
        body: typing.Any = None,
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
        Update an existing app
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
            request_path_user_id,
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
            path_template='/v1/app-config/{appId}/{userId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_app_config.serialize(body, content_type)
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


class UpdateByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_by_id(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_by_id_mapped_args(
            app_id=app_id,
            user_id=user_id,
            field_mappers=field_mappers,
            custom_field_mappers=custom_field_mappers,
            custom_outbound_field_mappers=custom_outbound_field_mappers,
            disabled_field_mappers=disabled_field_mappers,
            enabled_outbound_field_mappers=enabled_outbound_field_mappers,
            template_matchers=template_matchers,
            options=options,
        )
        return await self._aupdate_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_by_id(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_by_id_mapped_args(
            app_id=app_id,
            user_id=user_id,
            field_mappers=field_mappers,
            custom_field_mappers=custom_field_mappers,
            custom_outbound_field_mappers=custom_outbound_field_mappers,
            disabled_field_mappers=disabled_field_mappers,
            enabled_outbound_field_mappers=enabled_outbound_field_mappers,
            template_matchers=template_matchers,
            options=options,
        )
        return self._update_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateById(BaseApi):

    async def aupdate_by_id(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_by_id(
            app_id=app_id,
            user_id=user_id,
            field_mappers=field_mappers,
            custom_field_mappers=custom_field_mappers,
            custom_outbound_field_mappers=custom_outbound_field_mappers,
            disabled_field_mappers=disabled_field_mappers,
            enabled_outbound_field_mappers=enabled_outbound_field_mappers,
            template_matchers=template_matchers,
            options=options,
            **kwargs,
        )
    
    
    def update_by_id(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_by_id(
            app_id=app_id,
            user_id=user_id,
            field_mappers=field_mappers,
            custom_field_mappers=custom_field_mappers,
            custom_outbound_field_mappers=custom_outbound_field_mappers,
            disabled_field_mappers=disabled_field_mappers,
            enabled_outbound_field_mappers=enabled_outbound_field_mappers,
            template_matchers=template_matchers,
            options=options,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_by_id_mapped_args(
            app_id=app_id,
            user_id=user_id,
            field_mappers=field_mappers,
            custom_field_mappers=custom_field_mappers,
            custom_outbound_field_mappers=custom_outbound_field_mappers,
            disabled_field_mappers=disabled_field_mappers,
            enabled_outbound_field_mappers=enabled_outbound_field_mappers,
            template_matchers=template_matchers,
            options=options,
        )
        return await self._aupdate_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        app_id: str,
        user_id: str,
        field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_field_mappers: typing.Optional[typing.List[FieldMapper]] = None,
        custom_outbound_field_mappers: typing.Optional[typing.List[OutboundFieldMapper]] = None,
        disabled_field_mappers: typing.Optional[UpdateAppConfigDisabledFieldMappers] = None,
        enabled_outbound_field_mappers: typing.Optional[UpdateAppConfigEnabledOutboundFieldMappers] = None,
        template_matchers: typing.Optional[UpdateAppConfigTemplateMatchers] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_by_id_mapped_args(
            app_id=app_id,
            user_id=user_id,
            field_mappers=field_mappers,
            custom_field_mappers=custom_field_mappers,
            custom_outbound_field_mappers=custom_outbound_field_mappers,
            disabled_field_mappers=disabled_field_mappers,
            enabled_outbound_field_mappers=enabled_outbound_field_mappers,
            template_matchers=template_matchers,
            options=options,
        )
        return self._update_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

