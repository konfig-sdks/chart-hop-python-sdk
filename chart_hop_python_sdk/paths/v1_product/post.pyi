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

from chart_hop_python_sdk.model.create_product import CreateProduct as CreateProductSchema
from chart_hop_python_sdk.model.product import Product as ProductSchema
from chart_hop_python_sdk.model.create_product_feature_options import CreateProductFeatureOptions as CreateProductFeatureOptionsSchema
from chart_hop_python_sdk.model.create_product_features import CreateProductFeatures as CreateProductFeaturesSchema

from chart_hop_python_sdk.type.create_product import CreateProduct
from chart_hop_python_sdk.type.create_product_features import CreateProductFeatures
from chart_hop_python_sdk.type.product import Product
from chart_hop_python_sdk.type.create_product_feature_options import CreateProductFeatureOptions

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.create_product import CreateProduct as CreateProductPydantic
from chart_hop_python_sdk.pydantic.create_product_feature_options import CreateProductFeatureOptions as CreateProductFeatureOptionsPydantic
from chart_hop_python_sdk.pydantic.product import Product as ProductPydantic
from chart_hop_python_sdk.pydantic.create_product_features import CreateProductFeatures as CreateProductFeaturesPydantic

# body param
SchemaForRequestBodyApplicationJson = CreateProductSchema


request_body_create_product = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = ProductSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Product


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Product


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_product_mapped_args(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if sku is not None:
            _body["sku"] = sku
        if salesforce_product_id is not None:
            _body["salesforceProductId"] = salesforce_product_id
        if stripe_product_id is not None:
            _body["stripeProductId"] = stripe_product_id
        if features is not None:
            _body["features"] = features
        if feature_options is not None:
            _body["featureOptions"] = feature_options
        args.body = _body
        return args

    async def _acreate_new_product_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new product
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/v1/product',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_product.serialize(body, content_type)
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


    def _create_new_product_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new product
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/v1/product',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_product.serialize(body, content_type)
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


class CreateNewProductRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_product(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_product_mapped_args(
            name=name,
            salesforce_product_id=salesforce_product_id,
            stripe_product_id=stripe_product_id,
            features=features,
            sku=sku,
            feature_options=feature_options,
        )
        return await self._acreate_new_product_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_product(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_product_mapped_args(
            name=name,
            salesforce_product_id=salesforce_product_id,
            stripe_product_id=stripe_product_id,
            features=features,
            sku=sku,
            feature_options=feature_options,
        )
        return self._create_new_product_oapg(
            body=args.body,
        )

class CreateNewProduct(BaseApi):

    async def acreate_new_product(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProductPydantic:
        raw_response = await self.raw.acreate_new_product(
            name=name,
            salesforce_product_id=salesforce_product_id,
            stripe_product_id=stripe_product_id,
            features=features,
            sku=sku,
            feature_options=feature_options,
            **kwargs,
        )
        if validate:
            return ProductPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductPydantic, raw_response.body)
    
    
    def create_new_product(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
        validate: bool = False,
    ) -> ProductPydantic:
        raw_response = self.raw.create_new_product(
            name=name,
            salesforce_product_id=salesforce_product_id,
            stripe_product_id=stripe_product_id,
            features=features,
            sku=sku,
            feature_options=feature_options,
        )
        if validate:
            return ProductPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_product_mapped_args(
            name=name,
            salesforce_product_id=salesforce_product_id,
            stripe_product_id=stripe_product_id,
            features=features,
            sku=sku,
            feature_options=feature_options,
        )
        return await self._acreate_new_product_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        salesforce_product_id: str,
        stripe_product_id: str,
        features: CreateProductFeatures,
        sku: typing.Optional[str] = None,
        feature_options: typing.Optional[CreateProductFeatureOptions] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_product_mapped_args(
            name=name,
            salesforce_product_id=salesforce_product_id,
            stripe_product_id=stripe_product_id,
            features=features,
            sku=sku,
            feature_options=feature_options,
        )
        return self._create_new_product_oapg(
            body=args.body,
        )

