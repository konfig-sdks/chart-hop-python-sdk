# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_comment.post import CreateNewCommentRaw
from chart_hop_python_sdk.paths.v1_org_org_id_comment_entity_entity_id.get import GetByEntityIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_comment_comment_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_comment_comp_review_comp_review_id.get import ListCommentsOnCompReviewRaw
from chart_hop_python_sdk.paths.v1_org_org_id_comment_scenario_scenario_id.get import ListCommentsOnScenarioAndChangesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_comment_comment_id.delete import RemoveByIdRaw


class CommentApiRaw(
    CreateNewCommentRaw,
    GetByEntityIdRaw,
    GetByIdRaw,
    ListCommentsOnCompReviewRaw,
    ListCommentsOnScenarioAndChangesRaw,
    RemoveByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
