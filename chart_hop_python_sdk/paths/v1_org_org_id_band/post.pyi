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

from chart_hop_python_sdk.model.enum_value import EnumValue as EnumValueSchema
from chart_hop_python_sdk.model.money import Money as MoneySchema
from chart_hop_python_sdk.model.create_comp_band import CreateCompBand as CreateCompBandSchema

from chart_hop_python_sdk.type.money import Money
from chart_hop_python_sdk.type.create_comp_band import CreateCompBand
from chart_hop_python_sdk.type.enum_value import EnumValue

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.create_comp_band import CreateCompBand as CreateCompBandPydantic
from chart_hop_python_sdk.pydantic.money import Money as MoneyPydantic
from chart_hop_python_sdk.pydantic.enum_value import EnumValue as EnumValuePydantic

# Query params
DateSchema = schemas.DateSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'date': typing.Union[DateSchema, str, date, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    explode=True,
)
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
SchemaForRequestBodyApplicationJson = CreateCompBandSchema


request_body_create_comp_band = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
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

    def _create_comp_band_mapped_args(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if label is not None:
            _body["label"] = label
        if color is not None:
            _body["color"] = color
        if base_comp_max is not None:
            _body["baseCompMax"] = base_comp_max
        if base_comp_mid is not None:
            _body["baseCompMid"] = base_comp_mid
        if base_comp_min is not None:
            _body["baseCompMin"] = base_comp_min
        if base_spread is not None:
            _body["baseSpread"] = base_spread
        if base_interval is not None:
            _body["baseInterval"] = base_interval
        if base_target_pay is not None:
            _body["baseTargetPay"] = base_target_pay
        if base_target_pay_percentile is not None:
            _body["baseTargetPayPercentile"] = base_target_pay_percentile
        if equity_target_shares is not None:
            _body["equityTargetShares"] = equity_target_shares
        if equity_target_percent_of_base is not None:
            _body["equityTargetPercentOfBase"] = equity_target_percent_of_base
        if equity_target_value is not None:
            _body["equityTargetValue"] = equity_target_value
        if variable_value is not None:
            _body["variableValue"] = variable_value
        if variable_percent_of_base is not None:
            _body["variablePercentOfBase"] = variable_percent_of_base
        if job_tier_one_field is not None:
            _body["jobTierOneField"] = job_tier_one_field
        if job_tier_two_field is not None:
            _body["jobTierTwoField"] = job_tier_two_field
        if job_tier_three_field is not None:
            _body["jobTierThreeField"] = job_tier_three_field
        if job_level is not None:
            _body["jobLevel"] = job_level
        args.body = _body
        if date is not None:
            _query_params["date"] = date
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _acreate_comp_band_oapg(
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
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a comp band
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
            request_query_date,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/band',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_comp_band.serialize(body, content_type)
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


    def _create_comp_band_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a comp band
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
            request_query_date,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/band',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_comp_band.serialize(body, content_type)
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


class CreateCompBandRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_comp_band(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_comp_band_mapped_args(
            label=label,
            color=color,
            base_interval=base_interval,
            job_level=job_level,
            org_id=org_id,
            base_comp_max=base_comp_max,
            base_comp_mid=base_comp_mid,
            base_comp_min=base_comp_min,
            base_spread=base_spread,
            base_target_pay=base_target_pay,
            base_target_pay_percentile=base_target_pay_percentile,
            equity_target_shares=equity_target_shares,
            equity_target_percent_of_base=equity_target_percent_of_base,
            equity_target_value=equity_target_value,
            variable_value=variable_value,
            variable_percent_of_base=variable_percent_of_base,
            job_tier_one_field=job_tier_one_field,
            job_tier_two_field=job_tier_two_field,
            job_tier_three_field=job_tier_three_field,
            date=date,
        )
        return await self._acreate_comp_band_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def create_comp_band(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_comp_band_mapped_args(
            label=label,
            color=color,
            base_interval=base_interval,
            job_level=job_level,
            org_id=org_id,
            base_comp_max=base_comp_max,
            base_comp_mid=base_comp_mid,
            base_comp_min=base_comp_min,
            base_spread=base_spread,
            base_target_pay=base_target_pay,
            base_target_pay_percentile=base_target_pay_percentile,
            equity_target_shares=equity_target_shares,
            equity_target_percent_of_base=equity_target_percent_of_base,
            equity_target_value=equity_target_value,
            variable_value=variable_value,
            variable_percent_of_base=variable_percent_of_base,
            job_tier_one_field=job_tier_one_field,
            job_tier_two_field=job_tier_two_field,
            job_tier_three_field=job_tier_three_field,
            date=date,
        )
        return self._create_comp_band_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class CreateCompBand(BaseApi):

    async def acreate_comp_band(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acreate_comp_band(
            label=label,
            color=color,
            base_interval=base_interval,
            job_level=job_level,
            org_id=org_id,
            base_comp_max=base_comp_max,
            base_comp_mid=base_comp_mid,
            base_comp_min=base_comp_min,
            base_spread=base_spread,
            base_target_pay=base_target_pay,
            base_target_pay_percentile=base_target_pay_percentile,
            equity_target_shares=equity_target_shares,
            equity_target_percent_of_base=equity_target_percent_of_base,
            equity_target_value=equity_target_value,
            variable_value=variable_value,
            variable_percent_of_base=variable_percent_of_base,
            job_tier_one_field=job_tier_one_field,
            job_tier_two_field=job_tier_two_field,
            job_tier_three_field=job_tier_three_field,
            date=date,
            **kwargs,
        )
    
    
    def create_comp_band(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.create_comp_band(
            label=label,
            color=color,
            base_interval=base_interval,
            job_level=job_level,
            org_id=org_id,
            base_comp_max=base_comp_max,
            base_comp_mid=base_comp_mid,
            base_comp_min=base_comp_min,
            base_spread=base_spread,
            base_target_pay=base_target_pay,
            base_target_pay_percentile=base_target_pay_percentile,
            equity_target_shares=equity_target_shares,
            equity_target_percent_of_base=equity_target_percent_of_base,
            equity_target_value=equity_target_value,
            variable_value=variable_value,
            variable_percent_of_base=variable_percent_of_base,
            job_tier_one_field=job_tier_one_field,
            job_tier_two_field=job_tier_two_field,
            job_tier_three_field=job_tier_three_field,
            date=date,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_comp_band_mapped_args(
            label=label,
            color=color,
            base_interval=base_interval,
            job_level=job_level,
            org_id=org_id,
            base_comp_max=base_comp_max,
            base_comp_mid=base_comp_mid,
            base_comp_min=base_comp_min,
            base_spread=base_spread,
            base_target_pay=base_target_pay,
            base_target_pay_percentile=base_target_pay_percentile,
            equity_target_shares=equity_target_shares,
            equity_target_percent_of_base=equity_target_percent_of_base,
            equity_target_value=equity_target_value,
            variable_value=variable_value,
            variable_percent_of_base=variable_percent_of_base,
            job_tier_one_field=job_tier_one_field,
            job_tier_two_field=job_tier_two_field,
            job_tier_three_field=job_tier_three_field,
            date=date,
        )
        return await self._acreate_comp_band_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        label: str,
        color: str,
        base_interval: EnumValue,
        job_level: str,
        org_id: str,
        base_comp_max: typing.Optional[Money] = None,
        base_comp_mid: typing.Optional[Money] = None,
        base_comp_min: typing.Optional[Money] = None,
        base_spread: typing.Optional[typing.Union[int, float]] = None,
        base_target_pay: typing.Optional[Money] = None,
        base_target_pay_percentile: typing.Optional[typing.Union[int, float]] = None,
        equity_target_shares: typing.Optional[typing.Union[int, float]] = None,
        equity_target_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        equity_target_value: typing.Optional[typing.Union[int, float]] = None,
        variable_value: typing.Optional[Money] = None,
        variable_percent_of_base: typing.Optional[typing.Union[int, float]] = None,
        job_tier_one_field: typing.Optional[str] = None,
        job_tier_two_field: typing.Optional[str] = None,
        job_tier_three_field: typing.Optional[str] = None,
        date: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_comp_band_mapped_args(
            label=label,
            color=color,
            base_interval=base_interval,
            job_level=job_level,
            org_id=org_id,
            base_comp_max=base_comp_max,
            base_comp_mid=base_comp_mid,
            base_comp_min=base_comp_min,
            base_spread=base_spread,
            base_target_pay=base_target_pay,
            base_target_pay_percentile=base_target_pay_percentile,
            equity_target_shares=equity_target_shares,
            equity_target_percent_of_base=equity_target_percent_of_base,
            equity_target_value=equity_target_value,
            variable_value=variable_value,
            variable_percent_of_base=variable_percent_of_base,
            job_tier_one_field=job_tier_one_field,
            job_tier_two_field=job_tier_two_field,
            job_tier_three_field=job_tier_three_field,
            date=date,
        )
        return self._create_comp_band_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

