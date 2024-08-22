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

    def get_option(self, option: str,
                   fallback: Optional[str] = None) -> Optional[str]:
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
    def Description(self) -> Optional[str]:
        return self.get_option(self.options.DESCRIPTION.name)


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
