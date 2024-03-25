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

from chart_hop_python_sdk.model.update_field_data_fetch_types import UpdateFieldDataFetchTypes as UpdateFieldDataFetchTypesSchema
from chart_hop_python_sdk.model.enum_value import EnumValue as EnumValueSchema
from chart_hop_python_sdk.model.table_ref import TableRef as TableRefSchema
from chart_hop_python_sdk.model.update_field import UpdateField as UpdateFieldSchema
from chart_hop_python_sdk.model.update_field_aliases import UpdateFieldAliases as UpdateFieldAliasesSchema

from chart_hop_python_sdk.type.table_ref import TableRef
from chart_hop_python_sdk.type.update_field_data_fetch_types import UpdateFieldDataFetchTypes
from chart_hop_python_sdk.type.update_field import UpdateField
from chart_hop_python_sdk.type.update_field_aliases import UpdateFieldAliases
from chart_hop_python_sdk.type.enum_value import EnumValue

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.update_field_aliases import UpdateFieldAliases as UpdateFieldAliasesPydantic
from chart_hop_python_sdk.pydantic.table_ref import TableRef as TableRefPydantic
from chart_hop_python_sdk.pydantic.update_field_data_fetch_types import UpdateFieldDataFetchTypes as UpdateFieldDataFetchTypesPydantic
from chart_hop_python_sdk.pydantic.enum_value import EnumValue as EnumValuePydantic
from chart_hop_python_sdk.pydantic.update_field import UpdateField as UpdateFieldPydantic

from . import path

# Path params
OrgIdSchema = schemas.StrSchema
FieldIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'orgId': typing.Union[OrgIdSchema, str, ],
        'fieldId': typing.Union[FieldIdSchema, str, ],
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
request_path_field_id = api_client.PathParameter(
    name="fieldId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FieldIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateFieldSchema


request_body_update_field = api_client.RequestBody(
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
}


class BaseApi(api_client.Api):

    def _update_existing_field_mapped_args(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if label is not None:
            _body["label"] = label
        if question is not None:
            _body["question"] = question
        if in_use is not None:
            _body["inUse"] = in_use
        if expr is not None:
            _body["expr"] = expr
        if expr_type is not None:
            _body["exprType"] = expr_type
        if type is not None:
            _body["type"] = type
        if plural is not None:
            _body["plural"] = plural
        if values is not None:
            _body["values"] = values
        if default_value is not None:
            _body["defaultValue"] = default_value
        if options is not None:
            _body["options"] = options
        if sensitive is not None:
            _body["sensitive"] = sensitive
        if hide_expr is not None:
            _body["hideExpr"] = hide_expr
        if expire_days is not None:
            _body["expireDays"] = expire_days
        if status is not None:
            _body["status"] = status
        if table_ref is not None:
            _body["tableRef"] = table_ref
        if is_unique is not None:
            _body["isUnique"] = is_unique
        if is_required is not None:
            _body["isRequired"] = is_required
        if is_effective_dated is not None:
            _body["isEffectiveDated"] = is_effective_dated
        if data_fetch_types is not None:
            _body["dataFetchTypes"] = data_fetch_types
        if aliases is not None:
            _body["aliases"] = aliases
        if calc is not None:
            _body["calc"] = calc
        if category_id is not None:
            _body["categoryId"] = category_id
        if classification is not None:
            _body["classification"] = classification
        if places is not None:
            _body["places"] = places
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        if field_id is not None:
            _path_params["fieldId"] = field_id
        args.path = _path_params
        return args

    async def _aupdate_existing_field_oapg(
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
        Update an existing field
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_field_id,
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
            path_template='/v1/org/{orgId}/field/{fieldId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_field.serialize(body, content_type)
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


    def _update_existing_field_oapg(
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
        Update an existing field
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
            request_path_field_id,
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
            path_template='/v1/org/{orgId}/field/{fieldId}',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_field.serialize(body, content_type)
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


class UpdateExistingFieldRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_existing_field(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_field_mapped_args(
            org_id=org_id,
            field_id=field_id,
            description=description,
            name=name,
            label=label,
            question=question,
            in_use=in_use,
            expr=expr,
            expr_type=expr_type,
            type=type,
            plural=plural,
            values=values,
            default_value=default_value,
            options=options,
            sensitive=sensitive,
            hide_expr=hide_expr,
            expire_days=expire_days,
            status=status,
            table_ref=table_ref,
            is_unique=is_unique,
            is_required=is_required,
            is_effective_dated=is_effective_dated,
            data_fetch_types=data_fetch_types,
            aliases=aliases,
            calc=calc,
            category_id=category_id,
            classification=classification,
            places=places,
        )
        return await self._aupdate_existing_field_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_existing_field(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_field_mapped_args(
            org_id=org_id,
            field_id=field_id,
            description=description,
            name=name,
            label=label,
            question=question,
            in_use=in_use,
            expr=expr,
            expr_type=expr_type,
            type=type,
            plural=plural,
            values=values,
            default_value=default_value,
            options=options,
            sensitive=sensitive,
            hide_expr=hide_expr,
            expire_days=expire_days,
            status=status,
            table_ref=table_ref,
            is_unique=is_unique,
            is_required=is_required,
            is_effective_dated=is_effective_dated,
            data_fetch_types=data_fetch_types,
            aliases=aliases,
            calc=calc,
            category_id=category_id,
            classification=classification,
            places=places,
        )
        return self._update_existing_field_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateExistingField(BaseApi):

    async def aupdate_existing_field(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_existing_field(
            org_id=org_id,
            field_id=field_id,
            description=description,
            name=name,
            label=label,
            question=question,
            in_use=in_use,
            expr=expr,
            expr_type=expr_type,
            type=type,
            plural=plural,
            values=values,
            default_value=default_value,
            options=options,
            sensitive=sensitive,
            hide_expr=hide_expr,
            expire_days=expire_days,
            status=status,
            table_ref=table_ref,
            is_unique=is_unique,
            is_required=is_required,
            is_effective_dated=is_effective_dated,
            data_fetch_types=data_fetch_types,
            aliases=aliases,
            calc=calc,
            category_id=category_id,
            classification=classification,
            places=places,
            **kwargs,
        )
    
    
    def update_existing_field(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_existing_field(
            org_id=org_id,
            field_id=field_id,
            description=description,
            name=name,
            label=label,
            question=question,
            in_use=in_use,
            expr=expr,
            expr_type=expr_type,
            type=type,
            plural=plural,
            values=values,
            default_value=default_value,
            options=options,
            sensitive=sensitive,
            hide_expr=hide_expr,
            expire_days=expire_days,
            status=status,
            table_ref=table_ref,
            is_unique=is_unique,
            is_required=is_required,
            is_effective_dated=is_effective_dated,
            data_fetch_types=data_fetch_types,
            aliases=aliases,
            calc=calc,
            category_id=category_id,
            classification=classification,
            places=places,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_field_mapped_args(
            org_id=org_id,
            field_id=field_id,
            description=description,
            name=name,
            label=label,
            question=question,
            in_use=in_use,
            expr=expr,
            expr_type=expr_type,
            type=type,
            plural=plural,
            values=values,
            default_value=default_value,
            options=options,
            sensitive=sensitive,
            hide_expr=hide_expr,
            expire_days=expire_days,
            status=status,
            table_ref=table_ref,
            is_unique=is_unique,
            is_required=is_required,
            is_effective_dated=is_effective_dated,
            data_fetch_types=data_fetch_types,
            aliases=aliases,
            calc=calc,
            category_id=category_id,
            classification=classification,
            places=places,
        )
        return await self._aupdate_existing_field_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        field_id: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        question: typing.Optional[str] = None,
        in_use: typing.Optional[bool] = None,
        expr: typing.Optional[str] = None,
        expr_type: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        plural: typing.Optional[str] = None,
        values: typing.Optional[typing.List[EnumValue]] = None,
        default_value: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        options: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sensitive: typing.Optional[str] = None,
        hide_expr: typing.Optional[bool] = None,
        expire_days: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        table_ref: typing.Optional[TableRef] = None,
        is_unique: typing.Optional[bool] = None,
        is_required: typing.Optional[bool] = None,
        is_effective_dated: typing.Optional[bool] = None,
        data_fetch_types: typing.Optional[UpdateFieldDataFetchTypes] = None,
        aliases: typing.Optional[UpdateFieldAliases] = None,
        calc: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        classification: typing.Optional[str] = None,
        places: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_field_mapped_args(
            org_id=org_id,
            field_id=field_id,
            description=description,
            name=name,
            label=label,
            question=question,
            in_use=in_use,
            expr=expr,
            expr_type=expr_type,
            type=type,
            plural=plural,
            values=values,
            default_value=default_value,
            options=options,
            sensitive=sensitive,
            hide_expr=hide_expr,
            expire_days=expire_days,
            status=status,
            table_ref=table_ref,
            is_unique=is_unique,
            is_required=is_required,
            is_effective_dated=is_effective_dated,
            data_fetch_types=data_fetch_types,
            aliases=aliases,
            calc=calc,
            category_id=category_id,
            classification=classification,
            places=places,
        )
        return self._update_existing_field_oapg(
            body=args.body,
            path_params=args.path,
        )

