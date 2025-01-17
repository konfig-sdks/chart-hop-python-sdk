# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

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


class CompReviewConfig(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "reviewerWorkbook",
            "eligibleEmployees",
            "reviewersAndApprovers",
            "collaborators",
            "keyDates",
        }
        
        class properties:
        
            @staticmethod
            def keyDates() -> typing.Type['CompReviewKeyDates']:
                return CompReviewKeyDates
        
            @staticmethod
            def eligibleEmployees() -> typing.Type['CompReviewEligibleEmployees']:
                return CompReviewEligibleEmployees
        
            @staticmethod
            def reviewersAndApprovers() -> typing.Type['CompReviewReviewersApprovers']:
                return CompReviewReviewersApprovers
        
            @staticmethod
            def collaborators() -> typing.Type['CompReviewCollaborators']:
                return CompReviewCollaborators
        
            @staticmethod
            def reviewerWorkbook() -> typing.Type['CompReviewReviewerWorkbook']:
                return CompReviewReviewerWorkbook
        
            @staticmethod
            def budgets() -> typing.Type['CompReviewBudgets']:
                return CompReviewBudgets
        
            @staticmethod
            def notifications() -> typing.Type['CompReviewNotifications']:
                return CompReviewNotifications
        
            @staticmethod
            def reassignments() -> typing.Type['CompReviewConfigReassignments']:
                return CompReviewConfigReassignments
            __annotations__ = {
                "keyDates": keyDates,
                "eligibleEmployees": eligibleEmployees,
                "reviewersAndApprovers": reviewersAndApprovers,
                "collaborators": collaborators,
                "reviewerWorkbook": reviewerWorkbook,
                "budgets": budgets,
                "notifications": notifications,
                "reassignments": reassignments,
            }
    
    reviewerWorkbook: 'CompReviewReviewerWorkbook'
    eligibleEmployees: 'CompReviewEligibleEmployees'
    reviewersAndApprovers: 'CompReviewReviewersApprovers'
    collaborators: 'CompReviewCollaborators'
    keyDates: 'CompReviewKeyDates'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyDates"]) -> 'CompReviewKeyDates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eligibleEmployees"]) -> 'CompReviewEligibleEmployees': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewersAndApprovers"]) -> 'CompReviewReviewersApprovers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collaborators"]) -> 'CompReviewCollaborators': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewerWorkbook"]) -> 'CompReviewReviewerWorkbook': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budgets"]) -> 'CompReviewBudgets': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifications"]) -> 'CompReviewNotifications': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reassignments"]) -> 'CompReviewConfigReassignments': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["keyDates", "eligibleEmployees", "reviewersAndApprovers", "collaborators", "reviewerWorkbook", "budgets", "notifications", "reassignments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyDates"]) -> 'CompReviewKeyDates': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eligibleEmployees"]) -> 'CompReviewEligibleEmployees': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewersAndApprovers"]) -> 'CompReviewReviewersApprovers': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collaborators"]) -> 'CompReviewCollaborators': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewerWorkbook"]) -> 'CompReviewReviewerWorkbook': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budgets"]) -> typing.Union['CompReviewBudgets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifications"]) -> typing.Union['CompReviewNotifications', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reassignments"]) -> typing.Union['CompReviewConfigReassignments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["keyDates", "eligibleEmployees", "reviewersAndApprovers", "collaborators", "reviewerWorkbook", "budgets", "notifications", "reassignments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        reviewerWorkbook: 'CompReviewReviewerWorkbook',
        eligibleEmployees: 'CompReviewEligibleEmployees',
        reviewersAndApprovers: 'CompReviewReviewersApprovers',
        collaborators: 'CompReviewCollaborators',
        keyDates: 'CompReviewKeyDates',
        budgets: typing.Union['CompReviewBudgets', schemas.Unset] = schemas.unset,
        notifications: typing.Union['CompReviewNotifications', schemas.Unset] = schemas.unset,
        reassignments: typing.Union['CompReviewConfigReassignments', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompReviewConfig':
        return super().__new__(
            cls,
            *args,
            reviewerWorkbook=reviewerWorkbook,
            eligibleEmployees=eligibleEmployees,
            reviewersAndApprovers=reviewersAndApprovers,
            collaborators=collaborators,
            keyDates=keyDates,
            budgets=budgets,
            notifications=notifications,
            reassignments=reassignments,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.comp_review_budgets import CompReviewBudgets
from chart_hop_python_sdk.model.comp_review_collaborators import CompReviewCollaborators
from chart_hop_python_sdk.model.comp_review_config_reassignments import CompReviewConfigReassignments
from chart_hop_python_sdk.model.comp_review_eligible_employees import CompReviewEligibleEmployees
from chart_hop_python_sdk.model.comp_review_key_dates import CompReviewKeyDates
from chart_hop_python_sdk.model.comp_review_notifications import CompReviewNotifications
from chart_hop_python_sdk.model.comp_review_reviewer_workbook import CompReviewReviewerWorkbook
from chart_hop_python_sdk.model.comp_review_reviewers_approvers import CompReviewReviewersApprovers
