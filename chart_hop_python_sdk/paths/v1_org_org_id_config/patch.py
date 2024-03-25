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

from chart_hop_python_sdk.model.built_in_category_map import BuiltInCategoryMap as BuiltInCategoryMapSchema
from chart_hop_python_sdk.model.update_org_config_scenario_approval_chains import UpdateOrgConfigScenarioApprovalChains as UpdateOrgConfigScenarioApprovalChainsSchema
from chart_hop_python_sdk.model.compensation_bands_config import CompensationBandsConfig as CompensationBandsConfigSchema
from chart_hop_python_sdk.model.update_org_config_hidden_field_ids import UpdateOrgConfigHiddenFieldIds as UpdateOrgConfigHiddenFieldIdsSchema
from chart_hop_python_sdk.model.built_in_field_config import BuiltInFieldConfig as BuiltInFieldConfigSchema
from chart_hop_python_sdk.model.update_org_config_required_job_fields import UpdateOrgConfigRequiredJobFields as UpdateOrgConfigRequiredJobFieldsSchema
from chart_hop_python_sdk.model.update_org_config import UpdateOrgConfig as UpdateOrgConfigSchema
from chart_hop_python_sdk.model.smart_currency_option import SmartCurrencyOption as SmartCurrencyOptionSchema
from chart_hop_python_sdk.model.grant_alias import GrantAlias as GrantAliasSchema

from chart_hop_python_sdk.type.update_org_config_scenario_approval_chains import UpdateOrgConfigScenarioApprovalChains
from chart_hop_python_sdk.type.update_org_config_hidden_field_ids import UpdateOrgConfigHiddenFieldIds
from chart_hop_python_sdk.type.built_in_field_config import BuiltInFieldConfig
from chart_hop_python_sdk.type.grant_alias import GrantAlias
from chart_hop_python_sdk.type.update_org_config import UpdateOrgConfig
from chart_hop_python_sdk.type.update_org_config_required_job_fields import UpdateOrgConfigRequiredJobFields
from chart_hop_python_sdk.type.compensation_bands_config import CompensationBandsConfig
from chart_hop_python_sdk.type.built_in_category_map import BuiltInCategoryMap
from chart_hop_python_sdk.type.smart_currency_option import SmartCurrencyOption

from ...api_client import Dictionary
from chart_hop_python_sdk.pydantic.update_org_config_required_job_fields import UpdateOrgConfigRequiredJobFields as UpdateOrgConfigRequiredJobFieldsPydantic
from chart_hop_python_sdk.pydantic.grant_alias import GrantAlias as GrantAliasPydantic
from chart_hop_python_sdk.pydantic.update_org_config_hidden_field_ids import UpdateOrgConfigHiddenFieldIds as UpdateOrgConfigHiddenFieldIdsPydantic
from chart_hop_python_sdk.pydantic.built_in_field_config import BuiltInFieldConfig as BuiltInFieldConfigPydantic
from chart_hop_python_sdk.pydantic.built_in_category_map import BuiltInCategoryMap as BuiltInCategoryMapPydantic
from chart_hop_python_sdk.pydantic.smart_currency_option import SmartCurrencyOption as SmartCurrencyOptionPydantic
from chart_hop_python_sdk.pydantic.compensation_bands_config import CompensationBandsConfig as CompensationBandsConfigPydantic
from chart_hop_python_sdk.pydantic.update_org_config import UpdateOrgConfig as UpdateOrgConfigPydantic
from chart_hop_python_sdk.pydantic.update_org_config_scenario_approval_chains import UpdateOrgConfigScenarioApprovalChains as UpdateOrgConfigScenarioApprovalChainsPydantic

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
SchemaForRequestBodyApplicationJson = UpdateOrgConfigSchema


request_body_update_org_config = api_client.RequestBody(
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
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
    '500': _response_for_500,
}


class BaseApi(api_client.Api):

    def _patch_existing_config_mapped_args(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if hidden_field_ids is not None:
            _body["hiddenFieldIds"] = hidden_field_ids
        if builtin_category_map is not None:
            _body["builtinCategoryMap"] = builtin_category_map
        if builtin_field_config is not None:
            _body["builtinFieldConfig"] = builtin_field_config
        if compensation_bands_config is not None:
            _body["compensationBandsConfig"] = compensation_bands_config
        if smart_currency_options is not None:
            _body["smartCurrencyOptions"] = smart_currency_options
        if smart_currency_default is not None:
            _body["smartCurrencyDefault"] = smart_currency_default
        if required_job_fields is not None:
            _body["requiredJobFields"] = required_job_fields
        if scenario_approval_chains is not None:
            _body["scenarioApprovalChains"] = scenario_approval_chains
        if is_open_job_role_approval_enabled is not None:
            _body["isOpenJobRoleApprovalEnabled"] = is_open_job_role_approval_enabled
        if grant_configuration is not None:
            _body["grantConfiguration"] = grant_configuration
        args.body = _body
        if org_id is not None:
            _path_params["orgId"] = org_id
        args.path = _path_params
        return args

    async def _apatch_existing_config_oapg(
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
        Update an existing org config
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/config',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_org_config.serialize(body, content_type)
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


    def _patch_existing_config_oapg(
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
        Update an existing org config
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/org/{orgId}/config',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_org_config.serialize(body, content_type)
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


class PatchExistingConfigRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apatch_existing_config(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._patch_existing_config_mapped_args(
            org_id=org_id,
            hidden_field_ids=hidden_field_ids,
            builtin_category_map=builtin_category_map,
            builtin_field_config=builtin_field_config,
            compensation_bands_config=compensation_bands_config,
            smart_currency_options=smart_currency_options,
            smart_currency_default=smart_currency_default,
            required_job_fields=required_job_fields,
            scenario_approval_chains=scenario_approval_chains,
            is_open_job_role_approval_enabled=is_open_job_role_approval_enabled,
            grant_configuration=grant_configuration,
        )
        return await self._apatch_existing_config_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch_existing_config(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._patch_existing_config_mapped_args(
            org_id=org_id,
            hidden_field_ids=hidden_field_ids,
            builtin_category_map=builtin_category_map,
            builtin_field_config=builtin_field_config,
            compensation_bands_config=compensation_bands_config,
            smart_currency_options=smart_currency_options,
            smart_currency_default=smart_currency_default,
            required_job_fields=required_job_fields,
            scenario_approval_chains=scenario_approval_chains,
            is_open_job_role_approval_enabled=is_open_job_role_approval_enabled,
            grant_configuration=grant_configuration,
        )
        return self._patch_existing_config_oapg(
            body=args.body,
            path_params=args.path,
        )

class PatchExistingConfig(BaseApi):

    async def apatch_existing_config(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.apatch_existing_config(
            org_id=org_id,
            hidden_field_ids=hidden_field_ids,
            builtin_category_map=builtin_category_map,
            builtin_field_config=builtin_field_config,
            compensation_bands_config=compensation_bands_config,
            smart_currency_options=smart_currency_options,
            smart_currency_default=smart_currency_default,
            required_job_fields=required_job_fields,
            scenario_approval_chains=scenario_approval_chains,
            is_open_job_role_approval_enabled=is_open_job_role_approval_enabled,
            grant_configuration=grant_configuration,
            **kwargs,
        )
    
    
    def patch_existing_config(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.patch_existing_config(
            org_id=org_id,
            hidden_field_ids=hidden_field_ids,
            builtin_category_map=builtin_category_map,
            builtin_field_config=builtin_field_config,
            compensation_bands_config=compensation_bands_config,
            smart_currency_options=smart_currency_options,
            smart_currency_default=smart_currency_default,
            required_job_fields=required_job_fields,
            scenario_approval_chains=scenario_approval_chains,
            is_open_job_role_approval_enabled=is_open_job_role_approval_enabled,
            grant_configuration=grant_configuration,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._patch_existing_config_mapped_args(
            org_id=org_id,
            hidden_field_ids=hidden_field_ids,
            builtin_category_map=builtin_category_map,
            builtin_field_config=builtin_field_config,
            compensation_bands_config=compensation_bands_config,
            smart_currency_options=smart_currency_options,
            smart_currency_default=smart_currency_default,
            required_job_fields=required_job_fields,
            scenario_approval_chains=scenario_approval_chains,
            is_open_job_role_approval_enabled=is_open_job_role_approval_enabled,
            grant_configuration=grant_configuration,
        )
        return await self._apatch_existing_config_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        org_id: str,
        hidden_field_ids: typing.Optional[UpdateOrgConfigHiddenFieldIds] = None,
        builtin_category_map: typing.Optional[typing.List[BuiltInCategoryMap]] = None,
        builtin_field_config: typing.Optional[typing.List[BuiltInFieldConfig]] = None,
        compensation_bands_config: typing.Optional[CompensationBandsConfig] = None,
        smart_currency_options: typing.Optional[typing.List[SmartCurrencyOption]] = None,
        smart_currency_default: typing.Optional[str] = None,
        required_job_fields: typing.Optional[UpdateOrgConfigRequiredJobFields] = None,
        scenario_approval_chains: typing.Optional[UpdateOrgConfigScenarioApprovalChains] = None,
        is_open_job_role_approval_enabled: typing.Optional[bool] = None,
        grant_configuration: typing.Optional[typing.List[GrantAlias]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._patch_existing_config_mapped_args(
            org_id=org_id,
            hidden_field_ids=hidden_field_ids,
            builtin_category_map=builtin_category_map,
            builtin_field_config=builtin_field_config,
            compensation_bands_config=compensation_bands_config,
            smart_currency_options=smart_currency_options,
            smart_currency_default=smart_currency_default,
            required_job_fields=required_job_fields,
            scenario_approval_chains=scenario_approval_chains,
            is_open_job_role_approval_enabled=is_open_job_role_approval_enabled,
            grant_configuration=grant_configuration,
        )
        return self._patch_existing_config_oapg(
            body=args.body,
            path_params=args.path,
        )

