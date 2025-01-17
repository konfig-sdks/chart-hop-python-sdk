# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_dates.post import AdjustDatesRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_bulk_archive.post import BulkArchiveScenariosRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_combine.post import CombineScenariosRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario.post import CreateNewRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_bulk_delete.post import DeleteBulkScenariosRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id.get import GetByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario.get import ListPaginatedScenariosRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_recalculate_metadata.post import ManuallyRecalculateMetadataRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_merge.post import MergeIntoPrimaryTimelineRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id.delete import RemoveByIdRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_bulk_unarchive.post import UnarchiveSetOfScenariosRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id.patch import UpdateScenarioChangeRaw
from chart_hop_python_sdk.paths.v1_org_org_id_scenario_scenario_id_update_shared_view.post import UpdateSharedViewConfigRaw


class ScenarioApiRaw(
    AdjustDatesRaw,
    BulkArchiveScenariosRaw,
    CombineScenariosRaw,
    CreateNewRaw,
    DeleteBulkScenariosRaw,
    GetByIdRaw,
    ListPaginatedScenariosRaw,
    ManuallyRecalculateMetadataRaw,
    MergeIntoPrimaryTimelineRaw,
    RemoveByIdRaw,
    UnarchiveSetOfScenariosRaw,
    UpdateScenarioChangeRaw,
    UpdateSharedViewConfigRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
