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

from chart_hop_python_sdk.model.data_view import DataView as DataViewSchema
from chart_hop_python_sdk.model.update_data_view_column_widths import UpdateDataViewColumnWidths as UpdateDataViewColumnWidthsSchema
from chart_hop_python_sdk.model.share_access import ShareAccess as ShareAccessSchema
from chart_hop_python_sdk.model.update_data_view import UpdateDataView as UpdateDataViewSchema

from chart_hop_python_sdk.type.share_access import ShareAccess
from chart_hop_python_sdk.type.update_data_view import UpdateDataView
from chart_hop_python_sdk.type.update_data_view_column_widths import UpdateDataViewColumnWidths
from chart_hop_python_sdk.type.data_view import DataView

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.data_view import DataView as DataViewPydantic
from chart_hop_python_sdk.pydantic.update_data_view_column_widths import UpdateDataViewColumnWidths as UpdateDataViewColumnWidthsPydantic
from chart_hop_python_sdk.pydantic.update_data_view import UpdateDataView as UpdateDataViewPydantic
from chart_hop_python_sdk.pydantic.share_access import ShareAccess as ShareAccessPydantic

from . import path

# Path params
OrgIdSchema = schemas.StrSchema
DataViewIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'dataViewId': typing.Union[DataViewIdSchema, str, ],
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
request_path_data_view_id = api_client.PathParameter(
    name="dataViewId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DataViewIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateDataViewSchema


request_body_update_data_view = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = DataViewSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DataView


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DataView


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
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_existing_view_mapped_args(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if columns is not None:
            _body["columns"] = columns
        if type is not None:
            _body["type"] = type
        if entity_type is not None:
            _body["entityType"] = entity_type
        if column_widths is not None:
            _body["columnWidths"] = column_widths
        if date is not None:
            _body["date"] = date
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if filter is not None:
            _body["filter"] = filter
        if sort is not None:
            _body["sort"] = sort
        if group_by is not None:
            _body["groupBy"] = group_by
        if share_access is not None:
            _body["shareAccess"] = share_access
        if sensitive is not None:
            _body["sensitive"] = sensitive
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        if data_view_id is not None:
            _path_params["dataViewId"] = data_view_id
        args.path = _path_params
        return args

    async def _aupdate_existing_view_oapg(
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
        Update an existing data view
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_data_view_id,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/data-view/{dataViewId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_data_view.serialize(body, content_type)
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


    def _update_existing_view_oapg(
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
        Update an existing data view
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_data_view_id,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/data-view/{dataViewId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_data_view.serialize(body, content_type)
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


class UpdateExistingViewRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_existing_view(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_view_mapped_args(
            org_id=org_id,
            data_view_id=data_view_id,
            name=name,
            columns=columns,
            type=type,
            entity_type=entity_type,
            column_widths=column_widths,
            date=date,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            sort=sort,
            group_by=group_by,
            share_access=share_access,
            sensitive=sensitive,
        )
        return await self._aupdate_existing_view_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_existing_view(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_view_mapped_args(
            org_id=org_id,
            data_view_id=data_view_id,
            name=name,
            columns=columns,
            type=type,
            entity_type=entity_type,
            column_widths=column_widths,
            date=date,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            sort=sort,
            group_by=group_by,
            share_access=share_access,
            sensitive=sensitive,
        )
        return self._update_existing_view_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateExistingView(BaseApi):

    async def aupdate_existing_view(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> DataViewPydantic:
        raw_response = await self.raw.aupdate_existing_view(
            org_id=org_id,
            data_view_id=data_view_id,
            name=name,
            columns=columns,
            type=type,
            entity_type=entity_type,
            column_widths=column_widths,
            date=date,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            sort=sort,
            group_by=group_by,
            share_access=share_access,
            sensitive=sensitive,
            **kwargs,
        )
        if validate:
            return DataViewPydantic(**raw_response.body)
        return api_client.construct_model_instance(DataViewPydantic, raw_response.body)
    
    
    def update_existing_view(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        validate: bool = False,
    ) -> DataViewPydantic:
        raw_response = self.raw.update_existing_view(
            org_id=org_id,
            data_view_id=data_view_id,
            name=name,
            columns=columns,
            type=type,
            entity_type=entity_type,
            column_widths=column_widths,
            date=date,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            sort=sort,
            group_by=group_by,
            share_access=share_access,
            sensitive=sensitive,
        )
        if validate:
            return DataViewPydantic(**raw_response.body)
        return api_client.construct_model_instance(DataViewPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_view_mapped_args(
            org_id=org_id,
            data_view_id=data_view_id,
            name=name,
            columns=columns,
            type=type,
            entity_type=entity_type,
            column_widths=column_widths,
            date=date,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            sort=sort,
            group_by=group_by,
            share_access=share_access,
            sensitive=sensitive,
        )
        return await self._aupdate_existing_view_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        data_view_id: str,
        name: typing.Optional[str] = None,
        columns: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        column_widths: typing.Optional[UpdateDataViewColumnWidths] = None,
        date: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        share_access: typing.Optional[typing.List[ShareAccess]] = None,
        sensitive: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_view_mapped_args(
            org_id=org_id,
            data_view_id=data_view_id,
            name=name,
            columns=columns,
            type=type,
            entity_type=entity_type,
            column_widths=column_widths,
            date=date,
            start_date=start_date,
            end_date=end_date,
            filter=filter,
            sort=sort,
            group_by=group_by,
            share_access=share_access,
            sensitive=sensitive,
        )
        return self._update_existing_view_oapg(
            body=args.body,
            path_params=args.path,
        )
