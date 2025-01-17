# coding: utf-8

"""
    ChartHop API

    REST API for ChartHop

    The version of the OpenAPI document: V1.0.0
    Contact: support@charthop.com
    Created by: https://www.charthop.com
"""

from chart_hop_python_sdk.paths.v1_org_org_id_calendar.get import GetEntriesByTimePeriod
from chart_hop_python_sdk.apis.tags.calendar_api_raw import CalendarApiRaw


class CalendarApi(
    GetEntriesByTimePeriod,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CalendarApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CalendarApiRaw(api_client)
