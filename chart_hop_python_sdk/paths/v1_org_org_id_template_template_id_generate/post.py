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

from chart_hop_python_sdk.model.generate_template_request import GenerateTemplateRequest as GenerateTemplateRequestSchema
from chart_hop_python_sdk.model.process import Process as ProcessSchema

from chart_hop_python_sdk.type.process import Process
from chart_hop_python_sdk.type.generate_template_request import GenerateTemplateRequest

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.process import Process as ProcessPydantic
from chart_hop_python_sdk.pydantic.generate_template_request import GenerateTemplateRequest as GenerateTemplateRequestPydantic

from . import path

# Path params
OrgIdSchema = schemas.StrSchema
TemplateIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'templateId': typing.Union[TemplateIdSchema, str, ],
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
request_path_template_id = api_client.PathParameter(
    name="templateId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TemplateIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = GenerateTemplateRequestSchema


request_body_generate_template_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor204ResponseBodyApplicationJson = ProcessSchema


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: Process


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: Process


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor204ResponseBodyApplicationJson),
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
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _generate_pdfs_and_emails_mapped_args(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if filter is not None:
            _body["filter"] = filter
        if email_subject is not None:
            _body["emailSubject"] = email_subject
        if email_message is not None:
            _body["emailMessage"] = email_message
        if save_to_files is not None:
            _body["saveToFiles"] = save_to_files
        if file_sensitive is not None:
            _body["fileSensitive"] = file_sensitive
        if file_field is not None:
            _body["fileField"] = file_field
        if send_to_managers is not None:
            _body["sendToManagers"] = send_to_managers
        if send_to_persons is not None:
            _body["sendToPersons"] = send_to_persons
        if scenario_id is not None:
            _body["scenarioId"] = scenario_id
        if date is not None:
            _body["date"] = date
        if use_scenario_changes is not None:
            _body["useScenarioChanges"] = use_scenario_changes
        if change_grouping_type is not None:
            _body["changeGroupingType"] = change_grouping_type
        if change_grouping_id is not None:
            _body["changeGroupingId"] = change_grouping_id
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        if template_id is not None:
            _path_params["templateId"] = template_id
        args.path = _path_params
        return args

    async def _agenerate_pdfs_and_emails_oapg(
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
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Automatically generate PDFs of the templates, and distribute emails to managers and people to download
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_template_id,
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
            path_template='/v1/org/{orgId}/template/{templateId}/generate',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_generate_template_request.serialize(body, content_type)
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


    def _generate_pdfs_and_emails_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Automatically generate PDFs of the templates, and distribute emails to managers and people to download
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_template_id,
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
            path_template='/v1/org/{orgId}/template/{templateId}/generate',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_generate_template_request.serialize(body, content_type)
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


class GeneratePdfsAndEmailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agenerate_pdfs_and_emails(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_pdfs_and_emails_mapped_args(
            save_to_files=save_to_files,
            send_to_managers=send_to_managers,
            send_to_persons=send_to_persons,
            use_scenario_changes=use_scenario_changes,
            org_id=org_id,
            template_id=template_id,
            filter=filter,
            email_subject=email_subject,
            email_message=email_message,
            file_sensitive=file_sensitive,
            file_field=file_field,
            scenario_id=scenario_id,
            date=date,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return await self._agenerate_pdfs_and_emails_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def generate_pdfs_and_emails(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_pdfs_and_emails_mapped_args(
            save_to_files=save_to_files,
            send_to_managers=send_to_managers,
            send_to_persons=send_to_persons,
            use_scenario_changes=use_scenario_changes,
            org_id=org_id,
            template_id=template_id,
            filter=filter,
            email_subject=email_subject,
            email_message=email_message,
            file_sensitive=file_sensitive,
            file_field=file_field,
            scenario_id=scenario_id,
            date=date,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return self._generate_pdfs_and_emails_oapg(
            body=args.body,
            path_params=args.path,
        )

class GeneratePdfsAndEmails(BaseApi):

    async def agenerate_pdfs_and_emails(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProcessPydantic:
        raw_response = await self.raw.agenerate_pdfs_and_emails(
            save_to_files=save_to_files,
            send_to_managers=send_to_managers,
            send_to_persons=send_to_persons,
            use_scenario_changes=use_scenario_changes,
            org_id=org_id,
            template_id=template_id,
            filter=filter,
            email_subject=email_subject,
            email_message=email_message,
            file_sensitive=file_sensitive,
            file_field=file_field,
            scenario_id=scenario_id,
            date=date,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
            **kwargs,
        )
        if validate:
            return ProcessPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProcessPydantic, raw_response.body)
    
    
    def generate_pdfs_and_emails(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ProcessPydantic:
        raw_response = self.raw.generate_pdfs_and_emails(
            save_to_files=save_to_files,
            send_to_managers=send_to_managers,
            send_to_persons=send_to_persons,
            use_scenario_changes=use_scenario_changes,
            org_id=org_id,
            template_id=template_id,
            filter=filter,
            email_subject=email_subject,
            email_message=email_message,
            file_sensitive=file_sensitive,
            file_field=file_field,
            scenario_id=scenario_id,
            date=date,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        if validate:
            return ProcessPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProcessPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._generate_pdfs_and_emails_mapped_args(
            save_to_files=save_to_files,
            send_to_managers=send_to_managers,
            send_to_persons=send_to_persons,
            use_scenario_changes=use_scenario_changes,
            org_id=org_id,
            template_id=template_id,
            filter=filter,
            email_subject=email_subject,
            email_message=email_message,
            file_sensitive=file_sensitive,
            file_field=file_field,
            scenario_id=scenario_id,
            date=date,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return await self._agenerate_pdfs_and_emails_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        save_to_files: bool,
        send_to_managers: bool,
        send_to_persons: bool,
        use_scenario_changes: bool,
        org_id: str,
        template_id: str,
        filter: typing.Optional[str] = None,
        email_subject: typing.Optional[str] = None,
        email_message: typing.Optional[str] = None,
        file_sensitive: typing.Optional[str] = None,
        file_field: typing.Optional[str] = None,
        scenario_id: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        change_grouping_type: typing.Optional[str] = None,
        change_grouping_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._generate_pdfs_and_emails_mapped_args(
            save_to_files=save_to_files,
            send_to_managers=send_to_managers,
            send_to_persons=send_to_persons,
            use_scenario_changes=use_scenario_changes,
            org_id=org_id,
            template_id=template_id,
            filter=filter,
            email_subject=email_subject,
            email_message=email_message,
            file_sensitive=file_sensitive,
            file_field=file_field,
            scenario_id=scenario_id,
            date=date,
            change_grouping_type=change_grouping_type,
            change_grouping_id=change_grouping_id,
        )
        return self._generate_pdfs_and_emails_oapg(
            body=args.body,
            path_params=args.path,
        )

