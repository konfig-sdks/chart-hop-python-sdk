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


class PartialJob(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            jobId = schemas.StrSchema
            orgId = schemas.StrSchema
            snapshotId = schemas.StrSchema
        
            @staticmethod
            def comp() -> typing.Type['Comp']:
                return Comp
            
            
            class sensitive(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GLOBAL(cls):
                    return cls("GLOBAL")
                
                @schemas.classproperty
                def ORG(cls):
                    return cls("ORG")
                
                @schemas.classproperty
                def ORG_OTHER(cls):
                    return cls("ORG_OTHER")
                
                @schemas.classproperty
                def PERSONAL_DEMOG(cls):
                    return cls("PERSONAL_DEMOG")
                
                @schemas.classproperty
                def PERSONAL_BIRTH(cls):
                    return cls("PERSONAL_BIRTH")
                
                @schemas.classproperty
                def PERSONAL_CONTACT(cls):
                    return cls("PERSONAL_CONTACT")
                
                @schemas.classproperty
                def PERSONAL_PRIVATE(cls):
                    return cls("PERSONAL_PRIVATE")
                
                @schemas.classproperty
                def SENSITIVE_BIRTH(cls):
                    return cls("SENSITIVE_BIRTH")
                
                @schemas.classproperty
                def SENSITIVE_CONTACT(cls):
                    return cls("SENSITIVE_CONTACT")
                
                @schemas.classproperty
                def TIMEOFF(cls):
                    return cls("TIMEOFF")
                
                @schemas.classproperty
                def COMP_CASH(cls):
                    return cls("COMP_CASH")
                
                @schemas.classproperty
                def COMP_EQUITY(cls):
                    return cls("COMP_EQUITY")
                
                @schemas.classproperty
                def SENSITIVE(cls):
                    return cls("SENSITIVE")
                
                @schemas.classproperty
                def PERSONAL(cls):
                    return cls("PERSONAL")
                
                @schemas.classproperty
                def MANAGER(cls):
                    return cls("MANAGER")
                
                @schemas.classproperty
                def GRAND_MANAGER(cls):
                    return cls("GRAND_MANAGER")
                
                @schemas.classproperty
                def DIRECT(cls):
                    return cls("DIRECT")
                
                @schemas.classproperty
                def PEERS(cls):
                    return cls("PEERS")
                
                @schemas.classproperty
                def HIGH(cls):
                    return cls("HIGH")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
            
            
            class relationships(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JobRelationship']:
                        return JobRelationship
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['JobRelationship'], typing.List['JobRelationship']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JobRelationship':
                    return super().__getitem__(i)
        
            @staticmethod
            def groupIds() -> typing.Type['PartialJobGroupIds']:
                return PartialJobGroupIds
            
            
            class groupAssignments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GroupAssignment']:
                        return GroupAssignment
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GroupAssignment'], typing.List['GroupAssignment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groupAssignments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GroupAssignment':
                    return super().__getitem__(i)
            
            
            class placement(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NORMAL(cls):
                    return cls("NORMAL")
                
                @schemas.classproperty
                def ASSISTANT(cls):
                    return cls("ASSISTANT")
            
            
            class employment(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FULL(cls):
                    return cls("FULL")
                
                @schemas.classproperty
                def PART(cls):
                    return cls("PART")
                
                @schemas.classproperty
                def TEMP(cls):
                    return cls("TEMP")
                
                @schemas.classproperty
                def CONTRACT(cls):
                    return cls("CONTRACT")
                
                @schemas.classproperty
                def INTERN(cls):
                    return cls("INTERN")
                
                @schemas.classproperty
                def EXPAT(cls):
                    return cls("EXPAT")
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("OPEN")
                
                @schemas.classproperty
                def FILLED(cls):
                    return cls("FILLED")
                
                @schemas.classproperty
                def DEPART(cls):
                    return cls("DEPART")
                
                @schemas.classproperty
                def START(cls):
                    return cls("START")
        
            @staticmethod
            def fields() -> typing.Type['PartialJobFields']:
                return PartialJobFields
        
            @staticmethod
            def fieldDates() -> typing.Type['PartialJobFieldDates']:
                return PartialJobFieldDates
        
            @staticmethod
            def fieldsProposed() -> typing.Type['PartialJobFieldsProposed']:
                return PartialJobFieldsProposed
            createDate = schemas.DateSchema
            startDate = schemas.DateSchema
            startDatePlanned = schemas.DateSchema
            personStartDate = schemas.DateSchema
            personEndDate = schemas.DateSchema
            personJobStartDate = schemas.DateSchema
            personIdDate = schemas.DateSchema
            personJobEndDate = schemas.DateSchema
            personId = schemas.StrSchema
            backfillPersonId = schemas.StrSchema
            backfillByJobId = schemas.StrSchema
            
            
            class upcoming(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UpcomingChange']:
                        return UpcomingChange
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UpcomingChange'], typing.List['UpcomingChange']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'upcoming':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UpcomingChange':
                    return super().__getitem__(i)
            scenarioId = schemas.StrSchema
            scenarioChangedId = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "jobId": jobId,
                "orgId": orgId,
                "snapshotId": snapshotId,
                "comp": comp,
                "sensitive": sensitive,
                "relationships": relationships,
                "groupIds": groupIds,
                "groupAssignments": groupAssignments,
                "placement": placement,
                "employment": employment,
                "state": state,
                "fields": fields,
                "fieldDates": fieldDates,
                "fieldsProposed": fieldsProposed,
                "createDate": createDate,
                "startDate": startDate,
                "startDatePlanned": startDatePlanned,
                "personStartDate": personStartDate,
                "personEndDate": personEndDate,
                "personJobStartDate": personJobStartDate,
                "personIdDate": personIdDate,
                "personJobEndDate": personJobEndDate,
                "personId": personId,
                "backfillPersonId": backfillPersonId,
                "backfillByJobId": backfillByJobId,
                "upcoming": upcoming,
                "scenarioId": scenarioId,
                "scenarioChangedId": scenarioChangedId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snapshotId"]) -> MetaOapg.properties.snapshotId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comp"]) -> 'Comp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sensitive"]) -> MetaOapg.properties.sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupIds"]) -> 'PartialJobGroupIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupAssignments"]) -> MetaOapg.properties.groupAssignments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placement"]) -> MetaOapg.properties.placement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment"]) -> MetaOapg.properties.employment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'PartialJobFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldDates"]) -> 'PartialJobFieldDates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldsProposed"]) -> 'PartialJobFieldsProposed': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createDate"]) -> MetaOapg.properties.createDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDatePlanned"]) -> MetaOapg.properties.startDatePlanned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personStartDate"]) -> MetaOapg.properties.personStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personEndDate"]) -> MetaOapg.properties.personEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personJobStartDate"]) -> MetaOapg.properties.personJobStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personIdDate"]) -> MetaOapg.properties.personIdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personJobEndDate"]) -> MetaOapg.properties.personJobEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personId"]) -> MetaOapg.properties.personId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backfillPersonId"]) -> MetaOapg.properties.backfillPersonId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backfillByJobId"]) -> MetaOapg.properties.backfillByJobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upcoming"]) -> MetaOapg.properties.upcoming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenarioId"]) -> MetaOapg.properties.scenarioId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scenarioChangedId"]) -> MetaOapg.properties.scenarioChangedId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "jobId", "orgId", "snapshotId", "comp", "sensitive", "relationships", "groupIds", "groupAssignments", "placement", "employment", "state", "fields", "fieldDates", "fieldsProposed", "createDate", "startDate", "startDatePlanned", "personStartDate", "personEndDate", "personJobStartDate", "personIdDate", "personJobEndDate", "personId", "backfillPersonId", "backfillByJobId", "upcoming", "scenarioId", "scenarioChangedId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> typing.Union[MetaOapg.properties.jobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snapshotId"]) -> typing.Union[MetaOapg.properties.snapshotId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comp"]) -> typing.Union['Comp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sensitive"]) -> typing.Union[MetaOapg.properties.sensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupIds"]) -> typing.Union['PartialJobGroupIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupAssignments"]) -> typing.Union[MetaOapg.properties.groupAssignments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placement"]) -> typing.Union[MetaOapg.properties.placement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment"]) -> typing.Union[MetaOapg.properties.employment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['PartialJobFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldDates"]) -> typing.Union['PartialJobFieldDates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldsProposed"]) -> typing.Union['PartialJobFieldsProposed', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createDate"]) -> typing.Union[MetaOapg.properties.createDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDatePlanned"]) -> typing.Union[MetaOapg.properties.startDatePlanned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personStartDate"]) -> typing.Union[MetaOapg.properties.personStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personEndDate"]) -> typing.Union[MetaOapg.properties.personEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personJobStartDate"]) -> typing.Union[MetaOapg.properties.personJobStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personIdDate"]) -> typing.Union[MetaOapg.properties.personIdDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personJobEndDate"]) -> typing.Union[MetaOapg.properties.personJobEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personId"]) -> typing.Union[MetaOapg.properties.personId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backfillPersonId"]) -> typing.Union[MetaOapg.properties.backfillPersonId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backfillByJobId"]) -> typing.Union[MetaOapg.properties.backfillByJobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upcoming"]) -> typing.Union[MetaOapg.properties.upcoming, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenarioId"]) -> typing.Union[MetaOapg.properties.scenarioId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scenarioChangedId"]) -> typing.Union[MetaOapg.properties.scenarioChangedId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "jobId", "orgId", "snapshotId", "comp", "sensitive", "relationships", "groupIds", "groupAssignments", "placement", "employment", "state", "fields", "fieldDates", "fieldsProposed", "createDate", "startDate", "startDatePlanned", "personStartDate", "personEndDate", "personJobStartDate", "personIdDate", "personJobEndDate", "personId", "backfillPersonId", "backfillByJobId", "upcoming", "scenarioId", "scenarioChangedId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        jobId: typing.Union[MetaOapg.properties.jobId, str, schemas.Unset] = schemas.unset,
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        snapshotId: typing.Union[MetaOapg.properties.snapshotId, str, schemas.Unset] = schemas.unset,
        comp: typing.Union['Comp', schemas.Unset] = schemas.unset,
        sensitive: typing.Union[MetaOapg.properties.sensitive, str, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, list, tuple, schemas.Unset] = schemas.unset,
        groupIds: typing.Union['PartialJobGroupIds', schemas.Unset] = schemas.unset,
        groupAssignments: typing.Union[MetaOapg.properties.groupAssignments, list, tuple, schemas.Unset] = schemas.unset,
        placement: typing.Union[MetaOapg.properties.placement, str, schemas.Unset] = schemas.unset,
        employment: typing.Union[MetaOapg.properties.employment, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        fields: typing.Union['PartialJobFields', schemas.Unset] = schemas.unset,
        fieldDates: typing.Union['PartialJobFieldDates', schemas.Unset] = schemas.unset,
        fieldsProposed: typing.Union['PartialJobFieldsProposed', schemas.Unset] = schemas.unset,
        createDate: typing.Union[MetaOapg.properties.createDate, str, date, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        startDatePlanned: typing.Union[MetaOapg.properties.startDatePlanned, str, date, schemas.Unset] = schemas.unset,
        personStartDate: typing.Union[MetaOapg.properties.personStartDate, str, date, schemas.Unset] = schemas.unset,
        personEndDate: typing.Union[MetaOapg.properties.personEndDate, str, date, schemas.Unset] = schemas.unset,
        personJobStartDate: typing.Union[MetaOapg.properties.personJobStartDate, str, date, schemas.Unset] = schemas.unset,
        personIdDate: typing.Union[MetaOapg.properties.personIdDate, str, date, schemas.Unset] = schemas.unset,
        personJobEndDate: typing.Union[MetaOapg.properties.personJobEndDate, str, date, schemas.Unset] = schemas.unset,
        personId: typing.Union[MetaOapg.properties.personId, str, schemas.Unset] = schemas.unset,
        backfillPersonId: typing.Union[MetaOapg.properties.backfillPersonId, str, schemas.Unset] = schemas.unset,
        backfillByJobId: typing.Union[MetaOapg.properties.backfillByJobId, str, schemas.Unset] = schemas.unset,
        upcoming: typing.Union[MetaOapg.properties.upcoming, list, tuple, schemas.Unset] = schemas.unset,
        scenarioId: typing.Union[MetaOapg.properties.scenarioId, str, schemas.Unset] = schemas.unset,
        scenarioChangedId: typing.Union[MetaOapg.properties.scenarioChangedId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PartialJob':
        return super().__new__(
            cls,
            *args,
            title=title,
            jobId=jobId,
            orgId=orgId,
            snapshotId=snapshotId,
            comp=comp,
            sensitive=sensitive,
            relationships=relationships,
            groupIds=groupIds,
            groupAssignments=groupAssignments,
            placement=placement,
            employment=employment,
            state=state,
            fields=fields,
            fieldDates=fieldDates,
            fieldsProposed=fieldsProposed,
            createDate=createDate,
            startDate=startDate,
            startDatePlanned=startDatePlanned,
            personStartDate=personStartDate,
            personEndDate=personEndDate,
            personJobStartDate=personJobStartDate,
            personIdDate=personIdDate,
            personJobEndDate=personJobEndDate,
            personId=personId,
            backfillPersonId=backfillPersonId,
            backfillByJobId=backfillByJobId,
            upcoming=upcoming,
            scenarioId=scenarioId,
            scenarioChangedId=scenarioChangedId,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.comp import Comp
from chart_hop_python_sdk.model.group_assignment import GroupAssignment
from chart_hop_python_sdk.model.job_relationship import JobRelationship
from chart_hop_python_sdk.model.partial_job_field_dates import PartialJobFieldDates
from chart_hop_python_sdk.model.partial_job_fields import PartialJobFields
from chart_hop_python_sdk.model.partial_job_fields_proposed import PartialJobFieldsProposed
from chart_hop_python_sdk.model.partial_job_group_ids import PartialJobGroupIds
from chart_hop_python_sdk.model.upcoming_change import UpcomingChange
