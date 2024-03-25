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

from chart_hop_python_sdk.model.approval_request_patch_body import ApprovalRequestPatchBody as ApprovalRequestPatchBodySchema

from chart_hop_python_sdk.type.approval_request_patch_body import ApprovalRequestPatchBody

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.approval_request_patch_body import ApprovalRequestPatchBody as ApprovalRequestPatchBodyPydantic

from . import path

# Query params
PreviewJobIdSchema = schemas.StrSchema
IsFinalApprovalSchema = schemas.BoolSchema
CollaboratorSelectedReviewerJobIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'previewJobId': typing.Union[PreviewJobIdSchema, str, ],
        'isFinalApproval': typing.Union[IsFinalApprovalSchema, bool, ],
        'collaboratorSelectedReviewerJobId': typing.Union[CollaboratorSelectedReviewerJobIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_preview_job_id = api_client.QueryParameter(
    name="previewJobId",
    style=api_client.ParameterStyle.FORM,
    schema=PreviewJobIdSchema,
    explode=True,
)
request_query_is_final_approval = api_client.QueryParameter(
    name="isFinalApproval",
    style=api_client.ParameterStyle.FORM,
    schema=IsFinalApprovalSchema,
    explode=True,
)
request_query_collaborator_selected_reviewer_job_id = api_client.QueryParameter(
    name="collaboratorSelectedReviewerJobId",
    style=api_client.ParameterStyle.FORM,
    schema=CollaboratorSelectedReviewerJobIdSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.StrSchema
CompReviewIdSchema = schemas.StrSchema
ApprovalRequestIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'compReviewId': typing.Union[CompReviewIdSchema, str, ],
        'approvalRequestId': typing.Union[ApprovalRequestIdSchema, str, ],
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
request_path_comp_review_id = api_client.PathParameter(
    name="compReviewId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompReviewIdSchema,
    required=True,
)
request_path_approval_request_id = api_client.PathParameter(
    name="approvalRequestId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ApprovalRequestIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ApprovalRequestPatchBodySchema


request_body_approval_request_patch_body = api_client.RequestBody(
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

    def _update_approval_request_status_mapped_args(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if status is not None:
            _body["status"] = status
        if message is not None:
            _body["message"] = message
        args.body = _body
        if preview_job_id is not None:
            _query_params["previewJobId"] = preview_job_id
        if is_final_approval is not None:
            _query_params["isFinalApproval"] = is_final_approval
        if collaborator_selected_reviewer_job_id is not None:
            _query_params["collaboratorSelectedReviewerJobId"] = collaborator_selected_reviewer_job_id
        if org_id is not None:
            _path_params["orgId"] = org_id
        if comp_review_id is not None:
            _path_params["compReviewId"] = comp_review_id
        if approval_request_id is not None:
            _path_params["approvalRequestId"] = approval_request_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_approval_request_status_oapg(
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
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update approval request status, including any rollups
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
            request_path_comp_review_id,
            request_path_approval_request_id,
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
            request_query_preview_job_id,
            request_query_is_final_approval,
            request_query_collaborator_selected_reviewer_job_id,
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
            path_template='/v1/org/{orgId}/comp-review/{compReviewId}/approval-requests/{approvalRequestId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_approval_request_patch_body.serialize(body, content_type)
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


    def _update_approval_request_status_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Update approval request status, including any rollups
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
            request_path_comp_review_id,
            request_path_approval_request_id,
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
            request_query_preview_job_id,
            request_query_is_final_approval,
            request_query_collaborator_selected_reviewer_job_id,
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
            path_template='/v1/org/{orgId}/comp-review/{compReviewId}/approval-requests/{approvalRequestId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_approval_request_patch_body.serialize(body, content_type)
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


class UpdateApprovalRequestStatusRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_approval_request_status(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_approval_request_status_mapped_args(
            status=status,
            org_id=org_id,
            comp_review_id=comp_review_id,
            approval_request_id=approval_request_id,
            message=message,
            preview_job_id=preview_job_id,
            is_final_approval=is_final_approval,
            collaborator_selected_reviewer_job_id=collaborator_selected_reviewer_job_id,
        )
        return await self._aupdate_approval_request_status_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_approval_request_status(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_approval_request_status_mapped_args(
            status=status,
            org_id=org_id,
            comp_review_id=comp_review_id,
            approval_request_id=approval_request_id,
            message=message,
            preview_job_id=preview_job_id,
            is_final_approval=is_final_approval,
            collaborator_selected_reviewer_job_id=collaborator_selected_reviewer_job_id,
        )
        return self._update_approval_request_status_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateApprovalRequestStatus(BaseApi):

    async def aupdate_approval_request_status(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_approval_request_status(
            status=status,
            org_id=org_id,
            comp_review_id=comp_review_id,
            approval_request_id=approval_request_id,
            message=message,
            preview_job_id=preview_job_id,
            is_final_approval=is_final_approval,
            collaborator_selected_reviewer_job_id=collaborator_selected_reviewer_job_id,
            **kwargs,
        )
    
    
    def update_approval_request_status(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_approval_request_status(
            status=status,
            org_id=org_id,
            comp_review_id=comp_review_id,
            approval_request_id=approval_request_id,
            message=message,
            preview_job_id=preview_job_id,
            is_final_approval=is_final_approval,
            collaborator_selected_reviewer_job_id=collaborator_selected_reviewer_job_id,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_approval_request_status_mapped_args(
            status=status,
            org_id=org_id,
            comp_review_id=comp_review_id,
            approval_request_id=approval_request_id,
            message=message,
            preview_job_id=preview_job_id,
            is_final_approval=is_final_approval,
            collaborator_selected_reviewer_job_id=collaborator_selected_reviewer_job_id,
        )
        return await self._aupdate_approval_request_status_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        status: str,
        org_id: str,
        comp_review_id: str,
        approval_request_id: str,
        message: typing.Optional[str] = None,
        preview_job_id: typing.Optional[str] = None,
        is_final_approval: typing.Optional[bool] = None,
        collaborator_selected_reviewer_job_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_approval_request_status_mapped_args(
            status=status,
            org_id=org_id,
            comp_review_id=comp_review_id,
            approval_request_id=approval_request_id,
            message=message,
            preview_job_id=preview_job_id,
            is_final_approval=is_final_approval,
            collaborator_selected_reviewer_job_id=collaborator_selected_reviewer_job_id,
        )
        return self._update_approval_request_status_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

