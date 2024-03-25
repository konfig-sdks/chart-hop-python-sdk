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

from chart_hop_python_sdk.pydantic.form_response_answer import FormResponseAnswer
from chart_hop_python_sdk.pydantic.share_access import ShareAccess

class FormResponse(BaseModel):
    # globally unique id
    id: str = Field(alias='id')

    # parent organization id
    org_id: typing.Optional[str] = Field(None, alias='orgId')

    # if the response was imported from an external system, the unique identifier of the response from that system
    external_id: typing.Optional[str] = Field(None, alias='externalId')

    # form id that the response is a response for
    form_id: typing.Optional[str] = Field(None, alias='formId')

    # form version id that the response is a response for
    form_version_id: typing.Optional[str] = Field(None, alias='formVersionId')

    # person id who filled out the form response (null if anonymous)
    submit_person_id: typing.Optional[str] = Field(None, alias='submitPersonId')

    # user id who filled out the form response (can be null if anonymous or imported data)
    submit_user_id: typing.Optional[str] = Field(None, alias='submitUserId')

    # change id, if the form response is linked to a DATA change
    change_id: typing.Optional[str] = Field(None, alias='changeId')

    # assessment id, if the form response is related to an assesment
    assessment_id: typing.Optional[str] = Field(None, alias='assessmentId')

    # list of share access, if the form response has been shared with anyone
    share_access: typing.Optional[typing.List[ShareAccess]] = Field(None, alias='shareAccess')

    # sensitivity level of the author of the form response, if it differs from the form response
    author_sensitive: typing.Optional[Literal["ANONYMOUS", "PRIVATE", "HIGH", "MANAGER"]] = Field(None, alias='authorSensitive')

    # target entity id -- the entity that the form response is about
    target_entity_id: typing.Optional[str] = Field(None, alias='targetEntityId')

    # target entity type -- the entity that the form response is about
    target_entity_type: typing.Optional[Literal["NONE", "PERSON"]] = Field(None, alias='targetEntityType')

    # list of answers in the form response
    answers: typing.Optional[typing.List[FormResponseAnswer]] = Field(None, alias='answers')

    # timestamp that the form response was submitted
    submit_at: typing.Optional[int] = Field(None, alias='submitAt')

    # timestamp that the form response was approved
    approval_at: typing.Optional[int] = Field(None, alias='approvalAt')

    # user id who approved the form response
    approval_id: typing.Optional[str] = Field(None, alias='approvalId')

    # note left by the user who approved -- this is for backwards compatibility with the old approval system
    approval_note: typing.Optional[str] = Field(None, alias='approvalNote')

    # status of form response
    status: typing.Optional[Literal["ACTIVE", "PROPOSED", "REJECTED"]] = Field(None, alias='status')

    # created by user id
    create_id: typing.Optional[str] = Field(None, alias='createId')

    # created timestamp
    create_at: typing.Optional[str] = Field(None, alias='createAt')

    # last updated by user id
    update_id: typing.Optional[str] = Field(None, alias='updateId')

    # last updated timestamp
    update_at: typing.Optional[str] = Field(None, alias='updateAt')

    # deleted by user id
    delete_id: typing.Optional[str] = Field(None, alias='deleteId')

    # deleted timestamp
    delete_at: typing.Optional[str] = Field(None, alias='deleteAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
