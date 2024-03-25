# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class WebRegisteredCredential(BaseModel):
    # Credential id
    credential_id: str = Field(alias='credentialId')

    # The public key we're saving
    public_key_base64: str = Field(alias='publicKeyBase64')

    # The user handle - username
    user_handle_base64: str = Field(alias='userHandleBase64')

    # This is used to protect against duplicated key attacks
    signature_count: int = Field(alias='signatureCount')

    # When was this created
    created_at: int = Field(alias='createdAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
