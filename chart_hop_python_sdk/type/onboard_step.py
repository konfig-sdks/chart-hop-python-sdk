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


class RequiredOnboardStep(TypedDict):
    # customer facing description
    description: str

    # unique id
    id: str

    # unique string that briefly describes the onboard step
    name: str

    # customer facing identifier
    label: str

    # url for charthop docs that describe how to accomplish this step
    docsUrl: str

    # url for charthop page that where this step can be completed
    actionUrl: str

    # text that shows up on the 'action button' of the card for this step
    actionText: str

    # file name of the picture for the step (does not include path)
    pictureFileName: str

    # numerical position for which the step appears in relationship to other onboard steps
    sort: int

    # event type (in the format of <COLLECTION NAME>.<CHANGE TYPE>) that triggers the completion of this onboard step
    eventType: str

class OptionalOnboardStep(TypedDict, total=False):
    pass

class OnboardStep(RequiredOnboardStep, OptionalOnboardStep):
    pass
