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


class RequiredWebRegisteredCredential(TypedDict):
    # Credential id
    credentialId: str

    # The public key we're saving
    publicKeyBase64: str

    # The user handle - username
    userHandleBase64: str

    # This is used to protect against duplicated key attacks
    signatureCount: int

    # When was this created
    createdAt: int

class OptionalWebRegisteredCredential(TypedDict, total=False):
    pass

class WebRegisteredCredential(RequiredWebRegisteredCredential, OptionalWebRegisteredCredential):
    pass
