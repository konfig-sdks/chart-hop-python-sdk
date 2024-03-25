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

from chart_hop_python_sdk.model.product_item import ProductItem as ProductItemSchema
from chart_hop_python_sdk.model.address import Address as AddressSchema
from chart_hop_python_sdk.model.customer import Customer as CustomerSchema
from chart_hop_python_sdk.model.create_customer import CreateCustomer as CreateCustomerSchema

from chart_hop_python_sdk.type.product_item import ProductItem
from chart_hop_python_sdk.type.customer import Customer
from chart_hop_python_sdk.type.create_customer import CreateCustomer
from chart_hop_python_sdk.type.address import Address

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.address import Address as AddressPydantic
from chart_hop_python_sdk.pydantic.create_customer import CreateCustomer as CreateCustomerPydantic
from chart_hop_python_sdk.pydantic.product_item import ProductItem as ProductItemPydantic
from chart_hop_python_sdk.pydantic.customer import Customer as CustomerPydantic

# body param
SchemaForRequestBodyApplicationJson = CreateCustomerSchema


request_body_create_customer = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = CustomerSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Customer


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Customer


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

    def _create_new_customer_mapped_args(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if name is not None:
            _body["name"] = name
        if email is not None:
            _body["email"] = email
        if bill_address is not None:
            _body["billAddress"] = bill_address
        if industry is not None:
            _body["industry"] = industry
        if source is not None:
            _body["source"] = source
        if status is not None:
            _body["status"] = status
        if salesforce_account_id is not None:
            _body["salesforceAccountId"] = salesforce_account_id
        if products is not None:
            _body["products"] = products
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if next_invoice_date is not None:
            _body["nextInvoiceDate"] = next_invoice_date
        if primary_head_count_filter is not None:
            _body["primaryHeadCountFilter"] = primary_head_count_filter
        if secondary_head_count_filter is not None:
            _body["secondaryHeadCountFilter"] = secondary_head_count_filter
        if arr is not None:
            _body["arr"] = arr
        if projected_arr is not None:
            _body["projectedArr"] = projected_arr
        if trial_start_date is not None:
            _body["trialStartDate"] = trial_start_date
        if trial_end_date is not None:
            _body["trialEndDate"] = trial_end_date
        if stripe_subscription_sync is not None:
            _body["stripeSubscriptionSync"] = stripe_subscription_sync
        args.body = _body
        return args

    async def _acreate_new_customer_oapg(
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
        Create a new customer
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
            path_template='/v1/customer',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_customer.serialize(body, content_type)
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


    def _create_new_customer_oapg(
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
        Create a new customer
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
            path_template='/v1/customer',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_customer.serialize(body, content_type)
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


class CreateNewCustomerRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_customer(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_customer_mapped_args(
            name=name,
            email=email,
            start_date=start_date,
            bill_address=bill_address,
            industry=industry,
            source=source,
            status=status,
            salesforce_account_id=salesforce_account_id,
            products=products,
            end_date=end_date,
            next_invoice_date=next_invoice_date,
            primary_head_count_filter=primary_head_count_filter,
            secondary_head_count_filter=secondary_head_count_filter,
            arr=arr,
            projected_arr=projected_arr,
            trial_start_date=trial_start_date,
            trial_end_date=trial_end_date,
            stripe_subscription_sync=stripe_subscription_sync,
        )
        return await self._acreate_new_customer_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_customer(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_customer_mapped_args(
            name=name,
            email=email,
            start_date=start_date,
            bill_address=bill_address,
            industry=industry,
            source=source,
            status=status,
            salesforce_account_id=salesforce_account_id,
            products=products,
            end_date=end_date,
            next_invoice_date=next_invoice_date,
            primary_head_count_filter=primary_head_count_filter,
            secondary_head_count_filter=secondary_head_count_filter,
            arr=arr,
            projected_arr=projected_arr,
            trial_start_date=trial_start_date,
            trial_end_date=trial_end_date,
            stripe_subscription_sync=stripe_subscription_sync,
        )
        return self._create_new_customer_oapg(
            body=args.body,
        )

class CreateNewCustomer(BaseApi):

    async def acreate_new_customer(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CustomerPydantic:
        raw_response = await self.raw.acreate_new_customer(
            name=name,
            email=email,
            start_date=start_date,
            bill_address=bill_address,
            industry=industry,
            source=source,
            status=status,
            salesforce_account_id=salesforce_account_id,
            products=products,
            end_date=end_date,
            next_invoice_date=next_invoice_date,
            primary_head_count_filter=primary_head_count_filter,
            secondary_head_count_filter=secondary_head_count_filter,
            arr=arr,
            projected_arr=projected_arr,
            trial_start_date=trial_start_date,
            trial_end_date=trial_end_date,
            stripe_subscription_sync=stripe_subscription_sync,
            **kwargs,
        )
        if validate:
            return CustomerPydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomerPydantic, raw_response.body)
    
    
    def create_new_customer(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CustomerPydantic:
        raw_response = self.raw.create_new_customer(
            name=name,
            email=email,
            start_date=start_date,
            bill_address=bill_address,
            industry=industry,
            source=source,
            status=status,
            salesforce_account_id=salesforce_account_id,
            products=products,
            end_date=end_date,
            next_invoice_date=next_invoice_date,
            primary_head_count_filter=primary_head_count_filter,
            secondary_head_count_filter=secondary_head_count_filter,
            arr=arr,
            projected_arr=projected_arr,
            trial_start_date=trial_start_date,
            trial_end_date=trial_end_date,
            stripe_subscription_sync=stripe_subscription_sync,
        )
        if validate:
            return CustomerPydantic(**raw_response.body)
        return api_client.construct_model_instance(CustomerPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_customer_mapped_args(
            name=name,
            email=email,
            start_date=start_date,
            bill_address=bill_address,
            industry=industry,
            source=source,
            status=status,
            salesforce_account_id=salesforce_account_id,
            products=products,
            end_date=end_date,
            next_invoice_date=next_invoice_date,
            primary_head_count_filter=primary_head_count_filter,
            secondary_head_count_filter=secondary_head_count_filter,
            arr=arr,
            projected_arr=projected_arr,
            trial_start_date=trial_start_date,
            trial_end_date=trial_end_date,
            stripe_subscription_sync=stripe_subscription_sync,
        )
        return await self._acreate_new_customer_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        email: str,
        start_date: date,
        bill_address: typing.Optional[Address] = None,
        industry: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        salesforce_account_id: typing.Optional[str] = None,
        products: typing.Optional[typing.List[ProductItem]] = None,
        end_date: typing.Optional[date] = None,
        next_invoice_date: typing.Optional[date] = None,
        primary_head_count_filter: typing.Optional[str] = None,
        secondary_head_count_filter: typing.Optional[str] = None,
        arr: typing.Optional[typing.Union[int, float]] = None,
        projected_arr: typing.Optional[typing.Union[int, float]] = None,
        trial_start_date: typing.Optional[date] = None,
        trial_end_date: typing.Optional[date] = None,
        stripe_subscription_sync: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_customer_mapped_args(
            name=name,
            email=email,
            start_date=start_date,
            bill_address=bill_address,
            industry=industry,
            source=source,
            status=status,
            salesforce_account_id=salesforce_account_id,
            products=products,
            end_date=end_date,
            next_invoice_date=next_invoice_date,
            primary_head_count_filter=primary_head_count_filter,
            secondary_head_count_filter=secondary_head_count_filter,
            arr=arr,
            projected_arr=projected_arr,
            trial_start_date=trial_start_date,
            trial_end_date=trial_end_date,
            stripe_subscription_sync=stripe_subscription_sync,
        )
        return self._create_new_customer_oapg(
            body=args.body,
        )

