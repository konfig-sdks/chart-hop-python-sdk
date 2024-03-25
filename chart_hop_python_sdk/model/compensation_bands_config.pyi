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


class CompensationBandsConfig(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "hourlySalaries",
            "hoursPerWeek",
            "hasLocationMultiplier",
            "hasTargetSalary",
            "annualizedSalaries",
            "currencyRounding",
            "weeksPerYear",
        }
        
        class properties:
            annualizedSalaries = schemas.BoolSchema
            hourlySalaries = schemas.BoolSchema
            hoursPerWeek = schemas.NumberSchema
            weeksPerYear = schemas.NumberSchema
            hasTargetSalary = schemas.BoolSchema
            hasLocationMultiplier = schemas.BoolSchema
            
            
            class currencyRounding(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Money']:
                        return Money
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Money'], typing.List['Money']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currencyRounding':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Money':
                    return super().__getitem__(i)
            annualizedSalariesType = schemas.StrSchema
            hourlySalariesType = schemas.StrSchema
            targetSalaryType = schemas.StrSchema
            equityFormat = schemas.StrSchema
            variableBonusFormat = schemas.StrSchema
            tiersNotMappedToCodes = schemas.BoolSchema
            firstTier = schemas.StrSchema
            secondTier = schemas.StrSchema
            thirdTier = schemas.StrSchema
            jobLevelSource = schemas.StrSchema
            marketJobLevelSystem = schemas.StrSchema
            hasMigratedBands = schemas.BoolSchema
            __annotations__ = {
                "annualizedSalaries": annualizedSalaries,
                "hourlySalaries": hourlySalaries,
                "hoursPerWeek": hoursPerWeek,
                "weeksPerYear": weeksPerYear,
                "hasTargetSalary": hasTargetSalary,
                "hasLocationMultiplier": hasLocationMultiplier,
                "currencyRounding": currencyRounding,
                "annualizedSalariesType": annualizedSalariesType,
                "hourlySalariesType": hourlySalariesType,
                "targetSalaryType": targetSalaryType,
                "equityFormat": equityFormat,
                "variableBonusFormat": variableBonusFormat,
                "tiersNotMappedToCodes": tiersNotMappedToCodes,
                "firstTier": firstTier,
                "secondTier": secondTier,
                "thirdTier": thirdTier,
                "jobLevelSource": jobLevelSource,
                "marketJobLevelSystem": marketJobLevelSystem,
                "hasMigratedBands": hasMigratedBands,
            }
    
    hourlySalaries: MetaOapg.properties.hourlySalaries
    hoursPerWeek: MetaOapg.properties.hoursPerWeek
    hasLocationMultiplier: MetaOapg.properties.hasLocationMultiplier
    hasTargetSalary: MetaOapg.properties.hasTargetSalary
    annualizedSalaries: MetaOapg.properties.annualizedSalaries
    currencyRounding: MetaOapg.properties.currencyRounding
    weeksPerYear: MetaOapg.properties.weeksPerYear
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualizedSalaries"]) -> MetaOapg.properties.annualizedSalaries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlySalaries"]) -> MetaOapg.properties.hourlySalaries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hoursPerWeek"]) -> MetaOapg.properties.hoursPerWeek: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weeksPerYear"]) -> MetaOapg.properties.weeksPerYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasTargetSalary"]) -> MetaOapg.properties.hasTargetSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasLocationMultiplier"]) -> MetaOapg.properties.hasLocationMultiplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyRounding"]) -> MetaOapg.properties.currencyRounding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualizedSalariesType"]) -> MetaOapg.properties.annualizedSalariesType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlySalariesType"]) -> MetaOapg.properties.hourlySalariesType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetSalaryType"]) -> MetaOapg.properties.targetSalaryType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["equityFormat"]) -> MetaOapg.properties.equityFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variableBonusFormat"]) -> MetaOapg.properties.variableBonusFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tiersNotMappedToCodes"]) -> MetaOapg.properties.tiersNotMappedToCodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstTier"]) -> MetaOapg.properties.firstTier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondTier"]) -> MetaOapg.properties.secondTier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thirdTier"]) -> MetaOapg.properties.thirdTier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobLevelSource"]) -> MetaOapg.properties.jobLevelSource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["marketJobLevelSystem"]) -> MetaOapg.properties.marketJobLevelSystem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasMigratedBands"]) -> MetaOapg.properties.hasMigratedBands: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["annualizedSalaries", "hourlySalaries", "hoursPerWeek", "weeksPerYear", "hasTargetSalary", "hasLocationMultiplier", "currencyRounding", "annualizedSalariesType", "hourlySalariesType", "targetSalaryType", "equityFormat", "variableBonusFormat", "tiersNotMappedToCodes", "firstTier", "secondTier", "thirdTier", "jobLevelSource", "marketJobLevelSystem", "hasMigratedBands", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualizedSalaries"]) -> MetaOapg.properties.annualizedSalaries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlySalaries"]) -> MetaOapg.properties.hourlySalaries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hoursPerWeek"]) -> MetaOapg.properties.hoursPerWeek: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weeksPerYear"]) -> MetaOapg.properties.weeksPerYear: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasTargetSalary"]) -> MetaOapg.properties.hasTargetSalary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasLocationMultiplier"]) -> MetaOapg.properties.hasLocationMultiplier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyRounding"]) -> MetaOapg.properties.currencyRounding: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualizedSalariesType"]) -> typing.Union[MetaOapg.properties.annualizedSalariesType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlySalariesType"]) -> typing.Union[MetaOapg.properties.hourlySalariesType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetSalaryType"]) -> typing.Union[MetaOapg.properties.targetSalaryType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["equityFormat"]) -> typing.Union[MetaOapg.properties.equityFormat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variableBonusFormat"]) -> typing.Union[MetaOapg.properties.variableBonusFormat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tiersNotMappedToCodes"]) -> typing.Union[MetaOapg.properties.tiersNotMappedToCodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstTier"]) -> typing.Union[MetaOapg.properties.firstTier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondTier"]) -> typing.Union[MetaOapg.properties.secondTier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thirdTier"]) -> typing.Union[MetaOapg.properties.thirdTier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobLevelSource"]) -> typing.Union[MetaOapg.properties.jobLevelSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["marketJobLevelSystem"]) -> typing.Union[MetaOapg.properties.marketJobLevelSystem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasMigratedBands"]) -> typing.Union[MetaOapg.properties.hasMigratedBands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["annualizedSalaries", "hourlySalaries", "hoursPerWeek", "weeksPerYear", "hasTargetSalary", "hasLocationMultiplier", "currencyRounding", "annualizedSalariesType", "hourlySalariesType", "targetSalaryType", "equityFormat", "variableBonusFormat", "tiersNotMappedToCodes", "firstTier", "secondTier", "thirdTier", "jobLevelSource", "marketJobLevelSystem", "hasMigratedBands", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hourlySalaries: typing.Union[MetaOapg.properties.hourlySalaries, bool, ],
        hoursPerWeek: typing.Union[MetaOapg.properties.hoursPerWeek, decimal.Decimal, int, float, ],
        hasLocationMultiplier: typing.Union[MetaOapg.properties.hasLocationMultiplier, bool, ],
        hasTargetSalary: typing.Union[MetaOapg.properties.hasTargetSalary, bool, ],
        annualizedSalaries: typing.Union[MetaOapg.properties.annualizedSalaries, bool, ],
        currencyRounding: typing.Union[MetaOapg.properties.currencyRounding, list, tuple, ],
        weeksPerYear: typing.Union[MetaOapg.properties.weeksPerYear, decimal.Decimal, int, float, ],
        annualizedSalariesType: typing.Union[MetaOapg.properties.annualizedSalariesType, str, schemas.Unset] = schemas.unset,
        hourlySalariesType: typing.Union[MetaOapg.properties.hourlySalariesType, str, schemas.Unset] = schemas.unset,
        targetSalaryType: typing.Union[MetaOapg.properties.targetSalaryType, str, schemas.Unset] = schemas.unset,
        equityFormat: typing.Union[MetaOapg.properties.equityFormat, str, schemas.Unset] = schemas.unset,
        variableBonusFormat: typing.Union[MetaOapg.properties.variableBonusFormat, str, schemas.Unset] = schemas.unset,
        tiersNotMappedToCodes: typing.Union[MetaOapg.properties.tiersNotMappedToCodes, bool, schemas.Unset] = schemas.unset,
        firstTier: typing.Union[MetaOapg.properties.firstTier, str, schemas.Unset] = schemas.unset,
        secondTier: typing.Union[MetaOapg.properties.secondTier, str, schemas.Unset] = schemas.unset,
        thirdTier: typing.Union[MetaOapg.properties.thirdTier, str, schemas.Unset] = schemas.unset,
        jobLevelSource: typing.Union[MetaOapg.properties.jobLevelSource, str, schemas.Unset] = schemas.unset,
        marketJobLevelSystem: typing.Union[MetaOapg.properties.marketJobLevelSystem, str, schemas.Unset] = schemas.unset,
        hasMigratedBands: typing.Union[MetaOapg.properties.hasMigratedBands, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompensationBandsConfig':
        return super().__new__(
            cls,
            *args,
            hourlySalaries=hourlySalaries,
            hoursPerWeek=hoursPerWeek,
            hasLocationMultiplier=hasLocationMultiplier,
            hasTargetSalary=hasTargetSalary,
            annualizedSalaries=annualizedSalaries,
            currencyRounding=currencyRounding,
            weeksPerYear=weeksPerYear,
            annualizedSalariesType=annualizedSalariesType,
            hourlySalariesType=hourlySalariesType,
            targetSalaryType=targetSalaryType,
            equityFormat=equityFormat,
            variableBonusFormat=variableBonusFormat,
            tiersNotMappedToCodes=tiersNotMappedToCodes,
            firstTier=firstTier,
            secondTier=secondTier,
            thirdTier=thirdTier,
            jobLevelSource=jobLevelSource,
            marketJobLevelSystem=marketJobLevelSystem,
            hasMigratedBands=hasMigratedBands,
            _configuration=_configuration,
            **kwargs,
        )

from chart_hop_python_sdk.model.money import Money