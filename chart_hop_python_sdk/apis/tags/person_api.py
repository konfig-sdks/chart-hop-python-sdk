# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v2_org_org_id_person.post import CreateNewPerson
from chart_hop_python_sdk.paths.v2_org_org_id_person.get import FindInOrganization
from chart_hop_python_sdk.paths.v2_org_org_id_person_person_id.get import GetById
from chart_hop_python_sdk.paths.v2_org_org_id_person_geocodes.get import GetGeocodesForOrg
from chart_hop_python_sdk.paths.v2_org_org_id_person_person_id.delete import RemoveById
from chart_hop_python_sdk.paths.v2_org_org_id_person_person_id.patch import UpdateById
from chart_hop_python_sdk.apis.tags.person_api_raw import PersonApiRaw


class PersonApi(
    CreateNewPerson,
    FindInOrganization,
    GetById,
    GetGeocodesForOrg,
    RemoveById,
    UpdateById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PersonApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PersonApiRaw(api_client)