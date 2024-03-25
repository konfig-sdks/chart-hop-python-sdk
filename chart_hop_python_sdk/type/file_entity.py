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


class RequiredFileEntity(TypedDict):
    # globally unique id of file
    id: str

    # customer facing filename of file
    filename: str

    # original filename of file
    originalFilename: str

    # mime type of file
    type: str

    # extension of file
    ext: str

    # size of file in bytes
    bytes: int

class OptionalFileEntity(TypedDict, total=False):
    # parent org id
    orgId: str

    # entity id that the file is attached to
    entityId: str

    # entity type (should only be PERSON or USER)
    entityType: str

    # field name that the file uses, if the file is tied to a field
    field: str

    # level of sensitivity of the file, if the file is not tied to a field
    sensitive: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class FileEntity(RequiredFileEntity, OptionalFileEntity):
    pass
