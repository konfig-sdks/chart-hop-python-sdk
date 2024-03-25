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

from chart_hop_python_sdk.model.change import Change as ChangeSchema
from chart_hop_python_sdk.model.partial_job import PartialJob as PartialJobSchema
from chart_hop_python_sdk.model.job_update import JobUpdate as JobUpdateSchema
from chart_hop_python_sdk.model.create_change import CreateChange as CreateChangeSchema

from chart_hop_python_sdk.type.partial_job import PartialJob
from chart_hop_python_sdk.type.job_update import JobUpdate
from chart_hop_python_sdk.type.create_change import CreateChange
from chart_hop_python_sdk.type.change import Change

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.partial_job import PartialJob as PartialJobPydantic
from chart_hop_python_sdk.pydantic.change import Change as ChangePydantic
from chart_hop_python_sdk.pydantic.job_update import JobUpdate as JobUpdatePydantic
from chart_hop_python_sdk.pydantic.create_change import CreateChange as CreateChangePydantic

from . import path

# Path params
OrgIdSchema = schemas.StrSchema
TypeSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
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


request_path_org_id = api_client.PathParameter(
    name="orgId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrgIdSchema,
    required=True,
)
request_path_type = api_client.PathParameter(
    name="type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TypeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CreateChangeSchema


request_body_create_change = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = ChangeSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Change


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Change


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
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _validate_change_operation_mapped_args(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if job_id is not None:
            _body["jobId"] = job_id
        if org_id is not None:
            _body["orgId"] = org_id
        if scenario_id is not None:
            _body["scenarioId"] = scenario_id
        if person_id is not None:
            _body["personId"] = person_id
        if other_job_id is not None:
            _body["otherJobId"] = other_job_id
        if type is not None:
            _body["type"] = type
        if date is not None:
            _body["date"] = date
        if announce_date is not None:
            _body["announceDate"] = announce_date
        if depart_type is not None:
            _body["departType"] = depart_type
        if depart_regret is not None:
            _body["departRegret"] = depart_regret
        if reason is not None:
            _body["reason"] = reason
        if promotion_type is not None:
            _body["promotionType"] = promotion_type
        if job is not None:
            _body["job"] = job
        if update is not None:
            _body["update"] = update
        if note is not None:
            _body["note"] = note
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        if type is not None:
            _path_params["type"] = type
        args.path = _path_params
        return args

    async def _avalidate_change_operation_oapg(
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
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Validate a change
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_type,
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
            path_template='/v1/org/{orgId}/change/{type}/validate',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_change.serialize(body, content_type)
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


    def _validate_change_operation_oapg(
        self,
        body: typing.Any = None,
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
        Validate a change
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_type,
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
            path_template='/v1/org/{orgId}/change/{type}/validate',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_change.serialize(body, content_type)
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


class ValidateChangeOperationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avalidate_change_operation(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validate_change_operation_mapped_args(
            org_id=org_id,
            type=type,
            job_id=job_id,
            org_id=org_id,
            scenario_id=scenario_id,
            person_id=person_id,
            other_job_id=other_job_id,
            type=type,
            date=date,
            announce_date=announce_date,
            depart_type=depart_type,
            depart_regret=depart_regret,
            reason=reason,
            promotion_type=promotion_type,
            job=job,
            update=update,
            note=note,
        )
        return await self._avalidate_change_operation_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def validate_change_operation(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validate_change_operation_mapped_args(
            org_id=org_id,
            type=type,
            job_id=job_id,
            org_id=org_id,
            scenario_id=scenario_id,
            person_id=person_id,
            other_job_id=other_job_id,
            type=type,
            date=date,
            announce_date=announce_date,
            depart_type=depart_type,
            depart_regret=depart_regret,
            reason=reason,
            promotion_type=promotion_type,
            job=job,
            update=update,
            note=note,
        )
        return self._validate_change_operation_oapg(
            body=args.body,
            path_params=args.path,
        )

class ValidateChangeOperation(BaseApi):

    async def avalidate_change_operation(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ChangePydantic:
        raw_response = await self.raw.avalidate_change_operation(
            org_id=org_id,
            type=type,
            job_id=job_id,
            org_id=org_id,
            scenario_id=scenario_id,
            person_id=person_id,
            other_job_id=other_job_id,
            type=type,
            date=date,
            announce_date=announce_date,
            depart_type=depart_type,
            depart_regret=depart_regret,
            reason=reason,
            promotion_type=promotion_type,
            job=job,
            update=update,
            note=note,
            **kwargs,
        )
        if validate:
            return ChangePydantic(**raw_response.body)
        return api_client.construct_model_instance(ChangePydantic, raw_response.body)
    
    
    def validate_change_operation(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ChangePydantic:
        raw_response = self.raw.validate_change_operation(
            org_id=org_id,
            type=type,
            job_id=job_id,
            org_id=org_id,
            scenario_id=scenario_id,
            person_id=person_id,
            other_job_id=other_job_id,
            type=type,
            date=date,
            announce_date=announce_date,
            depart_type=depart_type,
            depart_regret=depart_regret,
            reason=reason,
            promotion_type=promotion_type,
            job=job,
            update=update,
            note=note,
        )
        if validate:
            return ChangePydantic(**raw_response.body)
        return api_client.construct_model_instance(ChangePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validate_change_operation_mapped_args(
            org_id=org_id,
            type=type,
            job_id=job_id,
            org_id=org_id,
            scenario_id=scenario_id,
            person_id=person_id,
            other_job_id=other_job_id,
            type=type,
            date=date,
            announce_date=announce_date,
            depart_type=depart_type,
            depart_regret=depart_regret,
            reason=reason,
            promotion_type=promotion_type,
            job=job,
            update=update,
            note=note,
        )
        return await self._avalidate_change_operation_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        org_id: str,
        type: str,
        job_id: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        person_id: typing.Optional[str] = None,
        other_job_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        announce_date: typing.Optional[date] = None,
        depart_type: typing.Optional[str] = None,
        depart_regret: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        promotion_type: typing.Optional[str] = None,
        job: typing.Optional[PartialJob] = None,
        update: typing.Optional[JobUpdate] = None,
        note: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validate_change_operation_mapped_args(
            org_id=org_id,
            type=type,
            job_id=job_id,
            org_id=org_id,
            scenario_id=scenario_id,
            person_id=person_id,
            other_job_id=other_job_id,
            type=type,
            date=date,
            announce_date=announce_date,
            depart_type=depart_type,
            depart_regret=depart_regret,
            reason=reason,
            promotion_type=promotion_type,
            job=job,
            update=update,
            note=note,
        )
        return self._validate_change_operation_oapg(
            body=args.body,
            path_params=args.path,
        )

