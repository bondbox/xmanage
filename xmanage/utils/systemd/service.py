# coding:utf-8

from configparser import ConfigParser
from configparser import SectionProxy
from enum import Enum
import os
from typing import Optional
from typing import Set
from typing import Tuple

from .unit import sd_unit_file
from .unit import sd_unit_file_section

allowed_dirs: Optional[Tuple[str, ...]] = None
try:
    from .path import sd_path
    allowed_dirs = sd_path.systemd_system_dirs
except Exception:
    pass


class sd_uf_sec_service(sd_unit_file_section):
    """[Service] Section Options
    """
    SECTION_NAME: str = "Service"

    # https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html#Options
    class options(Enum):
        TYPE = "Type"
        EXITTYPE = "ExitType"
        REMAINAFTEREXIT = "RemainAfterExit"
        GUESSMAINPID = "GuessMainPID"
        PIDFILE = "PIDFile"
        BUSNAME = "BusName"
        EXECSTART = "ExecStart"
        EXECSTARTPRE = "ExecStartPre"
        EXECSTARTPOST = "ExecStartPost"
        EXECCONDITION = "ExecCondition"
        EXECRELOAD = "ExecReload"
        EXECSTOP = "ExecStop"
        EXECSTOPPOST = "ExecStopPost"
        RESTARTSEC = "RestartSec"
        RESTARTSTEPS = "RestartSteps"
        RESTARTMAXDELAYSEC = "RestartMaxDelaySec"
        TIMEOUTSTARTSEC = "TimeoutStartSec"
        TIMEOUTSTOPSEC = "TimeoutStopSec"
        TIMEOUTABORTSEC = "TimeoutAbortSec"
        TIMEOUTSEC = "TimeoutSec"
        TIMEOUTSTARTFAILUREMODE = "TimeoutStartFailureMode"
        TIMEOUTSTOPFAILUREMODE = "TimeoutStopFailureMode"
        RUNTIMEMAXSEC = "RuntimeMaxSec"
        RUNTIMERANDOMIZEDEXTRASEC = "RuntimeRandomizedExtraSec"
        WATCHDOGSEC = "WatchdogSec"
        RESTART = "Restart"
        RESTARTMODE = "RestartMode"
        SUCCESSEXITSTATUS = "SuccessExitStatus"
        RESTARTPREVENTEXITSTATUS = "RestartPreventExitStatus"
        RESTARTFORCEEXITSTATUS = "RestartForceExitStatus"
        ROOTDIRECTORYSTARTONLY = "RootDirectoryStartOnly"
        NONBLOCKING = "NonBlocking"
        NOTIFYACCESS = "NotifyAccess"
        SOCKETS = "Sockets"
        FILEDESCRIPTORSTOREMAX = "FileDescriptorStoreMax"
        FILEDESCRIPTORSTOREPRESERVE = "FileDescriptorStorePreserve"
        USBFUNCTIONDESCRIPTORS = "USBFunctionDescriptors"
        USBFUNCTIONSTRINGS = "USBFunctionStrings"
        OOMPOLICY = "OOMPolicy"
        OPENFILE = "OpenFile"
        RELOADSIGNAL = "ReloadSignal"
    OPTIONS: Set[str] = {i.value for i in options}

    def __init__(self, section: SectionProxy):
        super().__init__(self.SECTION_NAME, section)


class sd_service(sd_unit_file):

    def __init__(self, config: ConfigParser):
        super().__init__(config)
        _svc: SectionProxy = self.get_section(sd_uf_sec_service.SECTION_NAME)
        self.__section_service: sd_uf_sec_service = sd_uf_sec_service(_svc)

    @property
    def service_section(self) -> sd_uf_sec_service:
        return self.__section_service

    @classmethod
    def from_string(cls, value: str) -> "sd_service":
        assert isinstance(value, str), f"unexpected type: {type(value)}"
        return sd_service(cls.read_string(value))

    @classmethod
    def from_file(cls, file: str) -> "sd_service":
        assert os.path.exists(file), f"'{file}' not found."
        assert os.path.isfile(file), f"'{file}' is not a regular file."
        return sd_service.from_string(open(file).read())

    def create_unit(self, path: str, unit: str,
                    allow_update: bool = False) -> None:
        assert isinstance(path, str), f"unexpected type: {type(path)}"
        assert isinstance(unit, str), f"unexpected type: {type(unit)}"

        if allowed_dirs is not None:
            assert path in allowed_dirs, f"'{path}' is not in {allowed_dirs}"
        assert os.path.isdir(path), f"'{path}' not exists or is file"

        def get_service_unit_name(s: str) -> str:
            return s if s.endswith(".service") else ".".join([s, "service"])

        file: str = os.path.join(path, get_service_unit_name(unit))
        if os.path.exists(file) and not allow_update:
            raise FileExistsError(f"'{file}' already exists.")

        with open(file, "w") as hdl:
            self.parser.write(hdl)
