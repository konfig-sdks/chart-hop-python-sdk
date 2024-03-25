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


class Contact(BaseModel):
    # type identifier for the contact
    type: Literal["ADP", "BAMBOO", "EMPLOYEE", "GREENHOUSE", "GOOGLE", "GUSTO", "HUMAANS", "JOBVITE", "JUSTWORKS", "LEVER", "NAMELY", "OKTA", "PAYLOCITY", "SAPLING", "PRISM", "SUCCESSFACTORS", "RIPPLING", "TRINET", "ULTIPRO", "WORKDAY", "ZENEFITS", "LINKEDIN", "TWITTER", "GITHUB", "SLACK", "TIMETASTIC", "HOME_EMAIL", "MOBILE_PHONE", "WORK_EMAIL", "HOME_PHONE", "WORK_PHONE", "WORK_FAX", "FINCH", "ALPHASTAFF", "LEVER_JOB_POSTING", "DEEL", "ADP_ASSOCIATE_ID", "ADP_WORKER_ID"] = Field(alias='type')

    # format for the value
    format: Literal["PHONE", "EMAIL", "ID"] = Field(alias='format')

    # value for the contact
    value: typing.Optional[str] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
