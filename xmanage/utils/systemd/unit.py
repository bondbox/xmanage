# coding:utf-8

from configparser import ConfigParser
from configparser import SectionProxy
from enum import Enum
from typing import Any
from typing import ItemsView
from typing import KeysView
from typing import List
from typing import Optional
from typing import Set
from typing import Union
from typing import ValuesView


class sd_unit_file_section:
    """unit file section
    """

    def __init__(self, name: str, section: SectionProxy):
        assert isinstance(name, str), f"unexpected type: {type(name)}"
        assert isinstance(section, SectionProxy), \
            f"unexpected type: {type(section)}"
        self.__section_name: str = name
        self.__section: SectionProxy = section

    def __iter__(self):
        return iter(self.items)

    def __getattr__(self, attr: str) -> Any:
        try:
            return object.__getattribute__(self, attr)
        except AttributeError as e:
            if attr in object.__getattribute__(self, "OPTIONS"):
                return self.get_option(attr)
            raise e

    def __setattr__(self, attr: str, value: str) -> None:
        try:
            if attr in self.__getattribute__("OPTIONS"):
                return self.set_option(attr, value)
        except AttributeError:
            pass
        return super().__setattr__(attr, value)

    @property
    def name(self) -> str:
        return self.__section_name

    @property
    def items(self) -> ItemsView[str, str]:
        return self.__section.items()

    @property
    def keys(self) -> KeysView[str]:
        return self.__section.keys()

    @property
    def values(self) -> ValuesView[str]:
        return self.__section.values()

    def get_option(self, option: str, fallback: Optional[str] = "") -> Union[str, Any]:  # noqa
        """Get an option value.
        """
        return self.__section.get(option, fallback)

    def set_option(self, option: str, value: str):
        """Set value for an option.
        """
        self.__section[option] = value

    def setdefault(self, option: str, default: str) -> str:
        """Set default value for an option.
        """
        return self.__section.setdefault(option, default)


class sd_uf_sec_unit(sd_unit_file_section):
    """[Unit] Section Options
    """
    SECTION_NAME: str = "Unit"

    # https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html#%5BUnit%5D%20Section%20Options
    class options(Enum):
        DESCRIPTION = "Description"
        DOCUMENTATION = "Documentation"
        WANTS = "Wants"
        REQUIRES = "Requires"
        REQUISITE = "Requisite"
        BINDSTO = "BindsTo"
        PARTOF = "PartOf"
        UPHOLDS = "Upholds"
        CONFLICTS = "Conflicts"
        BEFORE = "Before"
        AFTER = "After"
        ONFAILURE = "OnFailure"
        ONSUCCESS = "OnSuccess"
        PROPAGATESRELOADTO = "PropagatesReloadTo"
        RELOADPROPAGATEDFROM = "ReloadPropagatedFrom"
        PROPAGATESSTOPTO = "PropagatesStopTo"
        STOPPROPAGATEDFROM = "StopPropagatedFrom"
        JOINSNAMESPACEOF = "JoinsNamespaceOf"
        REQUIRESMOUNTSFOR = "RequiresMountsFor"
        ONSUCCESSJOBMODE = "OnSuccessJobMode"
        ONFAILUREJOBMODE = "OnFailureJobMode"
        IGNOREONISOLATE = "IgnoreOnIsolate"
        STOPWHENUNNEEDED = "StopWhenUnneeded"
        REFUSEMANUALSTART = "RefuseManualStart"
        REFUSEMANUALSTOP = "RefuseManualStop"
        ALLOWISOLATE = "AllowIsolate"
        DEFAULTDEPENDENCIES = "DefaultDependencies"
        SURVIVEFINALKILLSIGNAL = "SurviveFinalKillSignal"
        COLLECTMODE = "CollectMode"
        FAILUREACTION = "FailureAction"
        SUCCESSACTION = "SuccessAction"
        FAILUREACTIONEXITSTATUS = "FailureActionExitStatus"
        SUCCESSACTIONEXITSTATUS = "SuccessActionExitStatus"
        JOBTIMEOUTSEC = "JobTimeoutSec"
        JOBRUNNINGTIMEOUTSEC = "JobRunningTimeoutSec"
        JOBTIMEOUTACTION = "JobTimeoutAction"
        JOBTIMEOUTREBOOTARGUMENT = "JobTimeoutRebootArgument"
        STARTLIMITINTERVALSEC = "StartLimitIntervalSec"
        STARTLIMITBURST = "StartLimitBurst"
        STARTLIMITACTION = "StartLimitAction"
        REBOOTARGUMENT = "RebootArgument"
        SOURCEPATH = "SourcePath"
    OPTIONS: Set[str] = {i.value for i in options}

    def __init__(self, section: SectionProxy):
        super().__init__(self.SECTION_NAME, section)

    @property
    def Description(self) -> str:
        return self.get_option(self.options.DESCRIPTION.value)

    @Description.setter
    def Description(self, value: str):
        self.set_option(self.options.DESCRIPTION.value, value)

    @property
    def Documentation(self) -> str:
        return self.get_option(self.options.DOCUMENTATION.value)

    @Documentation.setter
    def Documentation(self, value: str):
        self.set_option(self.options.DOCUMENTATION.value, value)

    @property
    def Wants(self) -> str:
        return self.get_option(self.options.WANTS.value)

    @Wants.setter
    def Wants(self, value: str):
        self.set_option(self.options.WANTS.value, value)

    @property
    def Requires(self) -> str:
        return self.get_option(self.options.REQUIRES.value)

    @Requires.setter
    def Requires(self, value: str):
        self.set_option(self.options.REQUIRES.value, value)

    @property
    def Requisite(self) -> str:
        return self.get_option(self.options.REQUISITE.value)

    @Requisite.setter
    def Requisite(self, value: str):
        self.set_option(self.options.REQUISITE.value, value)

    @property
    def BindsTo(self) -> str:
        return self.get_option(self.options.BINDSTO.value)

    @BindsTo.setter
    def BindsTo(self, value: str):
        self.set_option(self.options.BINDSTO.value, value)

    @property
    def PartOf(self) -> str:
        return self.get_option(self.options.PARTOF.value)

    @PartOf.setter
    def PartOf(self, value: str):
        self.set_option(self.options.PARTOF.value, value)

    @property
    def Upholds(self) -> str:
        return self.get_option(self.options.UPHOLDS.value)

    @Upholds.setter
    def Upholds(self, value: str):
        self.set_option(self.options.UPHOLDS.value, value)

    @property
    def Conflicts(self) -> str:
        return self.get_option(self.options.CONFLICTS.value)

    @Conflicts.setter
    def Conflicts(self, value: str):
        self.set_option(self.options.CONFLICTS.value, value)

    @property
    def Before(self) -> str:
        return self.get_option(self.options.BEFORE.value)

    @Before.setter
    def Before(self, value: str):
        self.set_option(self.options.BEFORE.value, value)

    @property
    def After(self) -> str:
        return self.get_option(self.options.AFTER.value)

    @After.setter
    def After(self, value: str):
        self.set_option(self.options.AFTER.value, value)

    @property
    def OnFailure(self) -> str:
        return self.get_option(self.options.ONFAILURE.value)

    @OnFailure.setter
    def OnFailure(self, value: str):
        self.set_option(self.options.ONFAILURE.value, value)

    @property
    def OnSuccess(self) -> str:
        return self.get_option(self.options.ONSUCCESS.value)

    @OnSuccess.setter
    def OnSuccess(self, value: str):
        self.set_option(self.options.ONSUCCESS.value, value)

    @property
    def PropagatesReloadTo(self) -> str:
        return self.get_option(self.options.PROPAGATESRELOADTO.value)

    @PropagatesReloadTo.setter
    def PropagatesReloadTo(self, value: str):
        self.set_option(self.options.PROPAGATESRELOADTO.value, value)

    @property
    def ReloadPropagatedFrom(self) -> str:
        return self.get_option(self.options.RELOADPROPAGATEDFROM.value)

    @ReloadPropagatedFrom.setter
    def ReloadPropagatedFrom(self, value: str):
        self.set_option(self.options.RELOADPROPAGATEDFROM.value, value)

    @property
    def PropagatesStopTo(self) -> str:
        return self.get_option(self.options.PROPAGATESSTOPTO.value)

    @PropagatesStopTo.setter
    def PropagatesStopTo(self, value: str):
        self.set_option(self.options.PROPAGATESSTOPTO.value, value)

    @property
    def StopPropagatedFrom(self) -> str:
        return self.get_option(self.options.STOPPROPAGATEDFROM.value)

    @StopPropagatedFrom.setter
    def StopPropagatedFrom(self, value: str):
        self.set_option(self.options.STOPPROPAGATEDFROM.value, value)

    @property
    def JoinsNamespaceOf(self) -> str:
        return self.get_option(self.options.JOINSNAMESPACEOF.value)

    @JoinsNamespaceOf.setter
    def JoinsNamespaceOf(self, value: str):
        self.set_option(self.options.JOINSNAMESPACEOF.value, value)

    @property
    def RequiresMountsFor(self) -> str:
        return self.get_option(self.options.REQUIRESMOUNTSFOR.value)

    @RequiresMountsFor.setter
    def RequiresMountsFor(self, value: str):
        self.set_option(self.options.REQUIRESMOUNTSFOR.value, value)

    @property
    def OnSuccessJobMode(self) -> str:
        return self.get_option(self.options.ONSUCCESSJOBMODE.value)

    @OnSuccessJobMode.setter
    def OnSuccessJobMode(self, value: str):
        self.set_option(self.options.ONSUCCESSJOBMODE.value, value)

    @property
    def OnFailureJobMode(self) -> str:
        return self.get_option(self.options.ONFAILUREJOBMODE.value)

    @OnFailureJobMode.setter
    def OnFailureJobMode(self, value: str):
        self.set_option(self.options.ONFAILUREJOBMODE.value, value)

    @property
    def IgnoreOnIsolate(self) -> str:
        return self.get_option(self.options.IGNOREONISOLATE.value)

    @IgnoreOnIsolate.setter
    def IgnoreOnIsolate(self, value: str):
        self.set_option(self.options.IGNOREONISOLATE.value, value)

    @property
    def StopWhenUnneeded(self) -> str:
        return self.get_option(self.options.STOPWHENUNNEEDED.value)

    @StopWhenUnneeded.setter
    def StopWhenUnneeded(self, value: str):
        self.set_option(self.options.STOPWHENUNNEEDED.value, value)

    @property
    def RefuseManualStart(self) -> str:
        return self.get_option(self.options.REFUSEMANUALSTART.value)

    @RefuseManualStart.setter
    def RefuseManualStart(self, value: str):
        self.set_option(self.options.REFUSEMANUALSTART.value, value)

    @property
    def RefuseManualStop(self) -> str:
        return self.get_option(self.options.REFUSEMANUALSTOP.value)

    @RefuseManualStop.setter
    def RefuseManualStop(self, value: str):
        self.set_option(self.options.REFUSEMANUALSTOP.value, value)

    @property
    def AllowIsolate(self) -> str:
        return self.get_option(self.options.ALLOWISOLATE.value)

    @AllowIsolate.setter
    def AllowIsolate(self, value: str):
        self.set_option(self.options.ALLOWISOLATE.value, value)

    @property
    def DefaultDependencies(self) -> str:
        return self.get_option(self.options.DEFAULTDEPENDENCIES.value)

    @DefaultDependencies.setter
    def DefaultDependencies(self, value: str):
        self.set_option(self.options.DEFAULTDEPENDENCIES.value, value)

    @property
    def SurviveFinalKillSignal(self) -> str:
        return self.get_option(self.options.SURVIVEFINALKILLSIGNAL.value)

    @SurviveFinalKillSignal.setter
    def SurviveFinalKillSignal(self, value: str):
        self.set_option(self.options.SURVIVEFINALKILLSIGNAL.value, value)

    @property
    def CollectMode(self) -> str:
        return self.get_option(self.options.COLLECTMODE.value)

    @CollectMode.setter
    def CollectMode(self, value: str):
        self.set_option(self.options.COLLECTMODE.value, value)

    @property
    def FailureAction(self) -> str:
        return self.get_option(self.options.FAILUREACTION.value)

    @FailureAction.setter
    def FailureAction(self, value: str):
        self.set_option(self.options.FAILUREACTION.value, value)

    @property
    def SuccessAction(self) -> str:
        return self.get_option(self.options.SUCCESSACTION.value)

    @SuccessAction.setter
    def SuccessAction(self, value: str):
        self.set_option(self.options.SUCCESSACTION.value, value)

    @property
    def FailureActionExitStatus(self) -> str:
        return self.get_option(self.options.FAILUREACTIONEXITSTATUS.value)

    @FailureActionExitStatus.setter
    def FailureActionExitStatus(self, value: str):
        self.set_option(self.options.FAILUREACTIONEXITSTATUS.value, value)

    @property
    def SuccessActionExitStatus(self) -> str:
        return self.get_option(self.options.SUCCESSACTIONEXITSTATUS.value)

    @SuccessActionExitStatus.setter
    def SuccessActionExitStatus(self, value: str):
        self.set_option(self.options.SUCCESSACTIONEXITSTATUS.value, value)

    @property
    def JobTimeoutSec(self) -> str:
        return self.get_option(self.options.JOBTIMEOUTSEC.value)

    @JobTimeoutSec.setter
    def JobTimeoutSec(self, value: str):
        self.set_option(self.options.JOBTIMEOUTSEC.value, value)

    @property
    def JobRunningTimeoutSec(self) -> str:
        return self.get_option(self.options.JOBRUNNINGTIMEOUTSEC.value)

    @JobRunningTimeoutSec.setter
    def JobRunningTimeoutSec(self, value: str):
        self.set_option(self.options.JOBRUNNINGTIMEOUTSEC.value, value)

    @property
    def JobTimeoutAction(self) -> str:
        return self.get_option(self.options.JOBTIMEOUTACTION.value)

    @JobTimeoutAction.setter
    def JobTimeoutAction(self, value: str):
        self.set_option(self.options.JOBTIMEOUTACTION.value, value)

    @property
    def JobTimeoutRebootArgument(self) -> str:
        return self.get_option(self.options.JOBTIMEOUTREBOOTARGUMENT.value)

    @JobTimeoutRebootArgument.setter
    def JobTimeoutRebootArgument(self, value: str):
        self.set_option(self.options.JOBTIMEOUTREBOOTARGUMENT.value, value)

    @property
    def StartLimitIntervalSec(self) -> str:
        return self.get_option(self.options.STARTLIMITINTERVALSEC.value)

    @StartLimitIntervalSec.setter
    def StartLimitIntervalSec(self, value: str):
        self.set_option(self.options.STARTLIMITINTERVALSEC.value, value)

    @property
    def StartLimitBurst(self) -> str:
        return self.get_option(self.options.STARTLIMITBURST.value)

    @StartLimitBurst.setter
    def StartLimitBurst(self, value: str):
        self.set_option(self.options.STARTLIMITBURST.value, value)

    @property
    def StartLimitAction(self) -> str:
        return self.get_option(self.options.STARTLIMITACTION.value)

    @StartLimitAction.setter
    def StartLimitAction(self, value: str):
        self.set_option(self.options.STARTLIMITACTION.value, value)

    @property
    def RebootArgument(self) -> str:
        return self.get_option(self.options.REBOOTARGUMENT.value)

    @RebootArgument.setter
    def RebootArgument(self, value: str):
        self.set_option(self.options.REBOOTARGUMENT.value, value)

    @property
    def SourcePath(self) -> str:
        return self.get_option(self.options.SOURCEPATH.value)

    @SourcePath.setter
    def SourcePath(self, value: str):
        self.set_option(self.options.SOURCEPATH.value, value)


class sd_uf_sec_install(sd_unit_file_section):
    """[Install] Section Options
    """
    SECTION_NAME: str = "Install"

    # https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html#%5BInstall%5D%20Section%20Options
    class options(Enum):
        ALIAS = "Alias"
        WANTEDBY = "WantedBy"
        REQUIREDBY = "RequiredBy"
        UPHELDBY = "UpheldBy"
        ALSO = "Also"
        DEFAULTINSTANCE = "DefaultInstance"
    OPTIONS: Set[str] = {i.value for i in options}

    def __init__(self, section: SectionProxy):
        super().__init__(self.SECTION_NAME, section)

    @property
    def Alias(self) -> str:
        return self.get_option(self.options.ALIAS.value)

    @Alias.setter
    def Alias(self, value: str):
        self.set_option(self.options.ALIAS.value, value)

    @property
    def WantedBy(self) -> str:
        return self.get_option(self.options.WANTEDBY.value)

    @WantedBy.setter
    def WantedBy(self, value: str):
        self.set_option(self.options.WANTEDBY.value, value)

    @property
    def RequiredBy(self) -> str:
        return self.get_option(self.options.REQUIREDBY.value)

    @RequiredBy.setter
    def RequiredBy(self, value: str):
        self.set_option(self.options.REQUIREDBY.value, value)

    @property
    def UpheldBy(self) -> str:
        return self.get_option(self.options.UPHELDBY.value)

    @UpheldBy.setter
    def UpheldBy(self, value: str):
        self.set_option(self.options.UPHELDBY.value, value)

    @property
    def Also(self) -> str:
        return self.get_option(self.options.ALSO.value)

    @Also.setter
    def Also(self, value: str):
        self.set_option(self.options.ALSO.value, value)

    @property
    def DefaultInstance(self) -> str:
        return self.get_option(self.options.DEFAULTINSTANCE.value)

    @DefaultInstance.setter
    def DefaultInstance(self, value: str):
        self.set_option(self.options.DEFAULTINSTANCE.value, value)


class sd_unit_file:
    """A plain text ini-style unit file.
    """

    def __init__(self, parser: ConfigParser):
        assert isinstance(parser, ConfigParser), \
            f"unexpected type: {type(parser)}"
        self.__parser: ConfigParser = parser
        _uni: SectionProxy = self.get_section(sd_uf_sec_unit.SECTION_NAME)
        _ins: SectionProxy = self.get_section(sd_uf_sec_install.SECTION_NAME)
        self.__section_unit: sd_uf_sec_unit = sd_uf_sec_unit(_uni)
        self.__section_install: sd_uf_sec_install = sd_uf_sec_install(_ins)

    @property
    def parser(self) -> ConfigParser:
        return self.__parser

    @property
    def sections(self) -> List[str]:
        return self.__parser.sections()

    @property
    def unit_section(self) -> sd_uf_sec_unit:
        return self.__section_unit

    @property
    def install_section(self) -> sd_uf_sec_install:
        return self.__section_install

    @classmethod
    def read_string(cls, value: str) -> ConfigParser:
        config: ConfigParser = ConfigParser()
        config.optionxform = lambda option: option  # type: ignore
        config.read_string(value)
        return config

    def get_section(self, section: str) -> SectionProxy:
        """Get a named section.

        Create a new section if it not exist.
        """
        if not self.__parser.has_section(section):
            self.__parser.add_section(section)
        return self.__parser[section]
