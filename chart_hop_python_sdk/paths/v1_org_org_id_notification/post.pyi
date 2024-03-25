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

from chart_hop_python_sdk.model.notification_job_data import NotificationJobData as NotificationJobDataSchema
from chart_hop_python_sdk.model.notification_request_to_user_ids import NotificationRequestToUserIds as NotificationRequestToUserIdsSchema
from chart_hop_python_sdk.model.notification_request import NotificationRequest as NotificationRequestSchema

from chart_hop_python_sdk.type.notification_request import NotificationRequest
from chart_hop_python_sdk.type.notification_request_to_user_ids import NotificationRequestToUserIds
from chart_hop_python_sdk.type.notification_job_data import NotificationJobData

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.notification_job_data import NotificationJobData as NotificationJobDataPydantic
from chart_hop_python_sdk.pydantic.notification_request_to_user_ids import NotificationRequestToUserIds as NotificationRequestToUserIdsPydantic
from chart_hop_python_sdk.pydantic.notification_request import NotificationRequest as NotificationRequestPydantic

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
SchemaForRequestBodyApplicationJson = NotificationRequestSchema


request_body_notification_request = api_client.RequestBody(
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

    def _send_email_or_in_app_notification_mapped_args(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if template_name is not None:
            _body["templateName"] = template_name
        if to_user_ids is not None:
            _body["toUserIds"] = to_user_ids
        if job_data is not None:
            _body["jobData"] = job_data
        if ats_name is not None:
            _body["atsName"] = ats_name
        if org_name is not None:
            _body["orgName"] = org_name
        if user_name is not None:
            _body["userName"] = user_name
        if sync_summary is not None:
            _body["syncSummary"] = sync_summary
        if process_id is not None:
            _body["processId"] = process_id
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.path = _path_params
        return args

    async def _asend_email_or_in_app_notification_oapg(
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
        Send a email or in-app notification
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/notification',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_notification_request.serialize(body, content_type)
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


    def _send_email_or_in_app_notification_oapg(
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
        Send a email or in-app notification
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/notification',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_notification_request.serialize(body, content_type)
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


class SendEmailOrInAppNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asend_email_or_in_app_notification(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_email_or_in_app_notification_mapped_args(
            template_name=template_name,
            to_user_ids=to_user_ids,
            job_data=job_data,
            org_id=org_id,
            ats_name=ats_name,
            org_name=org_name,
            user_name=user_name,
            sync_summary=sync_summary,
            process_id=process_id,
        )
        return await self._asend_email_or_in_app_notification_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def send_email_or_in_app_notification(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_email_or_in_app_notification_mapped_args(
            template_name=template_name,
            to_user_ids=to_user_ids,
            job_data=job_data,
            org_id=org_id,
            ats_name=ats_name,
            org_name=org_name,
            user_name=user_name,
            sync_summary=sync_summary,
            process_id=process_id,
        )
        return self._send_email_or_in_app_notification_oapg(
            body=args.body,
            path_params=args.path,
        )

class SendEmailOrInAppNotification(BaseApi):

    async def asend_email_or_in_app_notification(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.asend_email_or_in_app_notification(
            template_name=template_name,
            to_user_ids=to_user_ids,
            job_data=job_data,
            org_id=org_id,
            ats_name=ats_name,
            org_name=org_name,
            user_name=user_name,
            sync_summary=sync_summary,
            process_id=process_id,
            **kwargs,
        )
    
    
    def send_email_or_in_app_notification(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.send_email_or_in_app_notification(
            template_name=template_name,
            to_user_ids=to_user_ids,
            job_data=job_data,
            org_id=org_id,
            ats_name=ats_name,
            org_name=org_name,
            user_name=user_name,
            sync_summary=sync_summary,
            process_id=process_id,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_email_or_in_app_notification_mapped_args(
            template_name=template_name,
            to_user_ids=to_user_ids,
            job_data=job_data,
            org_id=org_id,
            ats_name=ats_name,
            org_name=org_name,
            user_name=user_name,
            sync_summary=sync_summary,
            process_id=process_id,
        )
        return await self._asend_email_or_in_app_notification_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        template_name: str,
        to_user_ids: NotificationRequestToUserIds,
        job_data: NotificationJobData,
        org_id: str,
        ats_name: typing.Optional[str] = None,
        org_name: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        sync_summary: typing.Optional[str] = None,
        process_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_email_or_in_app_notification_mapped_args(
            template_name=template_name,
            to_user_ids=to_user_ids,
            job_data=job_data,
            org_id=org_id,
            ats_name=ats_name,
            org_name=org_name,
            user_name=user_name,
            sync_summary=sync_summary,
            process_id=process_id,
        )
        return self._send_email_or_in_app_notification_oapg(
            body=args.body,
            path_params=args.path,
        )

