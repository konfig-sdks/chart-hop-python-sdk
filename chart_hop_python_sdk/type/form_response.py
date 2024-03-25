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

from chart_hop_python_sdk.type.form_response_answer import FormResponseAnswer
from chart_hop_python_sdk.type.share_access import ShareAccess

class RequiredFormResponse(TypedDict):
    # globally unique id
    id: str

class OptionalFormResponse(TypedDict, total=False):
    # parent organization id
    orgId: str

    # if the response was imported from an external system, the unique identifier of the response from that system
    externalId: str

    # form id that the response is a response for
    formId: str

    # form version id that the response is a response for
    formVersionId: str

    # person id who filled out the form response (null if anonymous)
    submitPersonId: str

    # user id who filled out the form response (can be null if anonymous or imported data)
    submitUserId: str

    # change id, if the form response is linked to a DATA change
    changeId: str

    # assessment id, if the form response is related to an assesment
    assessmentId: str

    # list of share access, if the form response has been shared with anyone
    shareAccess: typing.List[ShareAccess]

    # sensitivity level of the author of the form response, if it differs from the form response
    authorSensitive: str

    # target entity id -- the entity that the form response is about
    targetEntityId: str

    # target entity type -- the entity that the form response is about
    targetEntityType: str

    # list of answers in the form response
    answers: typing.List[FormResponseAnswer]

    # timestamp that the form response was submitted
    submitAt: int

    # timestamp that the form response was approved
    approvalAt: int

    # user id who approved the form response
    approvalId: str

    # note left by the user who approved -- this is for backwards compatibility with the old approval system
    approvalNote: str

    # status of form response
    status: str

    # created by user id
    createId: str

    # created timestamp
    createAt: str

    # last updated by user id
    updateId: str

    # last updated timestamp
    updateAt: str

    # deleted by user id
    deleteId: str

    # deleted timestamp
    deleteAt: str

class FormResponse(RequiredFormResponse, OptionalFormResponse):
    pass
