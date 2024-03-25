# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_comment.post import CreateNewComment
from chart_hop_python_sdk.paths.v1_org_org_id_comment_entity_entity_id.get import GetByEntityId
from chart_hop_python_sdk.paths.v1_org_org_id_comment_comment_id.get import GetById
from chart_hop_python_sdk.paths.v1_org_org_id_comment_comp_review_comp_review_id.get import ListCommentsOnCompReview
from chart_hop_python_sdk.paths.v1_org_org_id_comment_scenario_scenario_id.get import ListCommentsOnScenarioAndChanges
from chart_hop_python_sdk.paths.v1_org_org_id_comment_comment_id.delete import RemoveById
from chart_hop_python_sdk.apis.tags.comment_api_raw import CommentApiRaw


class CommentApi(
    CreateNewComment,
    GetByEntityId,
    GetById,
    ListCommentsOnCompReview,
    ListCommentsOnScenarioAndChanges,
    RemoveById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CommentApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CommentApiRaw(api_client)
