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

from chart_hop_python_sdk.model.money_range import MoneyRange as MoneyRangeSchema
from chart_hop_python_sdk.model.value_range import ValueRange as ValueRangeSchema
from chart_hop_python_sdk.model.basis_field_matrix import BasisFieldMatrix as BasisFieldMatrixSchema
from chart_hop_python_sdk.model.create_guideline import CreateGuideline as CreateGuidelineSchema

from chart_hop_python_sdk.type.value_range import ValueRange
from chart_hop_python_sdk.type.create_guideline import CreateGuideline
from chart_hop_python_sdk.type.money_range import MoneyRange
from chart_hop_python_sdk.type.basis_field_matrix import BasisFieldMatrix

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.create_guideline import CreateGuideline as CreateGuidelinePydantic
from chart_hop_python_sdk.pydantic.money_range import MoneyRange as MoneyRangePydantic
from chart_hop_python_sdk.pydantic.value_range import ValueRange as ValueRangePydantic
from chart_hop_python_sdk.pydantic.basis_field_matrix import BasisFieldMatrix as BasisFieldMatrixPydantic

from . import path

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
SchemaForRequestBodyApplicationJson = CreateGuidelineSchema


request_body_create_guideline = api_client.RequestBody(
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

    def _create_new_guideline_mapped_args(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if comp_review_id is not None:
            _body["compReviewId"] = comp_review_id
        if label is not None:
            _body["label"] = label
        if budget_pool_id is not None:
            _body["budgetPoolId"] = budget_pool_id
        if participants_expr is not None:
            _body["participantsExpr"] = participants_expr
        if applied_field is not None:
            _body["appliedField"] = applied_field
        if source_field is not None:
            _body["sourceField"] = source_field
        if calculation_type is not None:
            _body["calculationType"] = calculation_type
        if flag_mode is not None:
            _body["flagMode"] = flag_mode
        if flag_deviation_threshold is not None:
            _body["flagDeviationThreshold"] = flag_deviation_threshold
        if enable_populate_value is not None:
            _body["enablePopulateValue"] = enable_populate_value
        if basis_type is not None:
            _body["basisType"] = basis_type
        if basis_expr is not None:
            _body["basisExpr"] = basis_expr
        if basis_field_matrix is not None:
            _body["basisFieldMatrix"] = basis_field_matrix
        if fixed_amount_range is not None:
            _body["fixedAmountRange"] = fixed_amount_range
        if fixed_value_range is not None:
            _body["fixedValueRange"] = fixed_value_range
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.path = _path_params
        return args

    async def _acreate_new_guideline_oapg(
        self,
        body: typing.Any = None,
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
        Create a new guideline
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
            path_template='/v1/org/{orgId}/guideline',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_guideline.serialize(body, content_type)
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


    def _create_new_guideline_oapg(
        self,
        body: typing.Any = None,
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
        Create a new guideline
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
            path_template='/v1/org/{orgId}/guideline',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_guideline.serialize(body, content_type)
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


class CreateNewGuidelineRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_guideline(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_guideline_mapped_args(
            comp_review_id=comp_review_id,
            label=label,
            applied_field=applied_field,
            source_field=source_field,
            calculation_type=calculation_type,
            flag_mode=flag_mode,
            enable_populate_value=enable_populate_value,
            basis_type=basis_type,
            org_id=org_id,
            budget_pool_id=budget_pool_id,
            participants_expr=participants_expr,
            flag_deviation_threshold=flag_deviation_threshold,
            basis_expr=basis_expr,
            basis_field_matrix=basis_field_matrix,
            fixed_amount_range=fixed_amount_range,
            fixed_value_range=fixed_value_range,
        )
        return await self._acreate_new_guideline_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_guideline(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_guideline_mapped_args(
            comp_review_id=comp_review_id,
            label=label,
            applied_field=applied_field,
            source_field=source_field,
            calculation_type=calculation_type,
            flag_mode=flag_mode,
            enable_populate_value=enable_populate_value,
            basis_type=basis_type,
            org_id=org_id,
            budget_pool_id=budget_pool_id,
            participants_expr=participants_expr,
            flag_deviation_threshold=flag_deviation_threshold,
            basis_expr=basis_expr,
            basis_field_matrix=basis_field_matrix,
            fixed_amount_range=fixed_amount_range,
            fixed_value_range=fixed_value_range,
        )
        return self._create_new_guideline_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateNewGuideline(BaseApi):

    async def acreate_new_guideline(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_new_guideline(
            comp_review_id=comp_review_id,
            label=label,
            applied_field=applied_field,
            source_field=source_field,
            calculation_type=calculation_type,
            flag_mode=flag_mode,
            enable_populate_value=enable_populate_value,
            basis_type=basis_type,
            org_id=org_id,
            budget_pool_id=budget_pool_id,
            participants_expr=participants_expr,
            flag_deviation_threshold=flag_deviation_threshold,
            basis_expr=basis_expr,
            basis_field_matrix=basis_field_matrix,
            fixed_amount_range=fixed_amount_range,
            fixed_value_range=fixed_value_range,
            **kwargs,
        )
    
    
    def create_new_guideline(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_new_guideline(
            comp_review_id=comp_review_id,
            label=label,
            applied_field=applied_field,
            source_field=source_field,
            calculation_type=calculation_type,
            flag_mode=flag_mode,
            enable_populate_value=enable_populate_value,
            basis_type=basis_type,
            org_id=org_id,
            budget_pool_id=budget_pool_id,
            participants_expr=participants_expr,
            flag_deviation_threshold=flag_deviation_threshold,
            basis_expr=basis_expr,
            basis_field_matrix=basis_field_matrix,
            fixed_amount_range=fixed_amount_range,
            fixed_value_range=fixed_value_range,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_guideline_mapped_args(
            comp_review_id=comp_review_id,
            label=label,
            applied_field=applied_field,
            source_field=source_field,
            calculation_type=calculation_type,
            flag_mode=flag_mode,
            enable_populate_value=enable_populate_value,
            basis_type=basis_type,
            org_id=org_id,
            budget_pool_id=budget_pool_id,
            participants_expr=participants_expr,
            flag_deviation_threshold=flag_deviation_threshold,
            basis_expr=basis_expr,
            basis_field_matrix=basis_field_matrix,
            fixed_amount_range=fixed_amount_range,
            fixed_value_range=fixed_value_range,
        )
        return await self._acreate_new_guideline_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        comp_review_id: str,
        label: str,
        applied_field: str,
        source_field: str,
        calculation_type: str,
        flag_mode: str,
        enable_populate_value: bool,
        basis_type: str,
        org_id: str,
        budget_pool_id: typing.Optional[str] = None,
        participants_expr: typing.Optional[str] = None,
        flag_deviation_threshold: typing.Optional[typing.Union[int, float]] = None,
        basis_expr: typing.Optional[str] = None,
        basis_field_matrix: typing.Optional[BasisFieldMatrix] = None,
        fixed_amount_range: typing.Optional[MoneyRange] = None,
        fixed_value_range: typing.Optional[ValueRange] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_guideline_mapped_args(
            comp_review_id=comp_review_id,
            label=label,
            applied_field=applied_field,
            source_field=source_field,
            calculation_type=calculation_type,
            flag_mode=flag_mode,
            enable_populate_value=enable_populate_value,
            basis_type=basis_type,
            org_id=org_id,
            budget_pool_id=budget_pool_id,
            participants_expr=participants_expr,
            flag_deviation_threshold=flag_deviation_threshold,
            basis_expr=basis_expr,
            basis_field_matrix=basis_field_matrix,
            fixed_amount_range=fixed_amount_range,
            fixed_value_range=fixed_value_range,
        )
        return self._create_new_guideline_oapg(
            body=args.body,
            path_params=args.path,
        )

