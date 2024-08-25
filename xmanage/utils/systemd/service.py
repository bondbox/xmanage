# coding:utf-8

from configparser import ConfigParser
from configparser import SectionProxy
from datetime import datetime
from enum import Enum
import os
from typing import Optional
from typing import Set
from typing import Tuple

from ..attribute import __project__
from ..attribute import __version__
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

    @property
    def Type(self) -> str:
        return self.get_option(self.options.TYPE.value)

    @Type.setter
    def Type(self, value: str):
        self.set_option(self.options.TYPE.value, value)

    @property
    def ExitType(self) -> str:
        return self.get_option(self.options.EXITTYPE.value)

    @ExitType.setter
    def ExitType(self, value: str):
        self.set_option(self.options.EXITTYPE.value, value)

    @property
    def RemainAfterExit(self) -> str:
        return self.get_option(self.options.REMAINAFTEREXIT.value)

    @RemainAfterExit.setter
    def RemainAfterExit(self, value: str):
        self.set_option(self.options.REMAINAFTEREXIT.value, value)

    @property
    def GuessMainPID(self) -> str:
        return self.get_option(self.options.GUESSMAINPID.value)

    @GuessMainPID.setter
    def GuessMainPID(self, value: str):
        self.set_option(self.options.GUESSMAINPID.value, value)

    @property
    def PIDFile(self) -> str:
        return self.get_option(self.options.PIDFILE.value)

    @PIDFile.setter
    def PIDFile(self, value: str):
        self.set_option(self.options.PIDFILE.value, value)

    @property
    def BusName(self) -> str:
        return self.get_option(self.options.BUSNAME.value)

    @BusName.setter
    def BusName(self, value: str):
        self.set_option(self.options.BUSNAME.value, value)

    @property
    def ExecStart(self) -> str:
        return self.get_option(self.options.EXECSTART.value)

    @ExecStart.setter
    def ExecStart(self, value: str):
        self.set_option(self.options.EXECSTART.value, value)

    @property
    def ExecStartPre(self) -> str:
        return self.get_option(self.options.EXECSTARTPRE.value)

    @ExecStartPre.setter
    def ExecStartPre(self, value: str):
        self.set_option(self.options.EXECSTARTPRE.value, value)

    @property
    def ExecStartPost(self) -> str:
        return self.get_option(self.options.EXECSTARTPOST.value)

    @ExecStartPost.setter
    def ExecStartPost(self, value: str):
        self.set_option(self.options.EXECSTARTPOST.value, value)

    @property
    def ExecCondition(self) -> str:
        return self.get_option(self.options.EXECCONDITION.value)

    @ExecCondition.setter
    def ExecCondition(self, value: str):
        self.set_option(self.options.EXECCONDITION.value, value)

    @property
    def ExecReload(self) -> str:
        return self.get_option(self.options.EXECRELOAD.value)

    @ExecReload.setter
    def ExecReload(self, value: str):
        self.set_option(self.options.EXECRELOAD.value, value)

    @property
    def ExecStop(self) -> str:
        return self.get_option(self.options.EXECSTOP.value)

    @ExecStop.setter
    def ExecStop(self, value: str):
        self.set_option(self.options.EXECSTOP.value, value)

    @property
    def ExecStopPost(self) -> str:
        return self.get_option(self.options.EXECSTOPPOST.value)

    @ExecStopPost.setter
    def ExecStopPost(self, value: str):
        self.set_option(self.options.EXECSTOPPOST.value, value)

    @property
    def RestartSec(self) -> str:
        return self.get_option(self.options.RESTARTSEC.value)

    @RestartSec.setter
    def RestartSec(self, value: str):
        self.set_option(self.options.RESTARTSEC.value, value)

    @property
    def RestartSteps(self) -> str:
        return self.get_option(self.options.RESTARTSTEPS.value)

    @RestartSteps.setter
    def RestartSteps(self, value: str):
        self.set_option(self.options.RESTARTSTEPS.value, value)

    @property
    def RestartMaxDelaySec(self) -> str:
        return self.get_option(self.options.RESTARTMAXDELAYSEC.value)

    @RestartMaxDelaySec.setter
    def RestartMaxDelaySec(self, value: str):
        self.set_option(self.options.RESTARTMAXDELAYSEC.value, value)

    @property
    def TimeoutStartSec(self) -> str:
        return self.get_option(self.options.TIMEOUTSTARTSEC.value)

    @TimeoutStartSec.setter
    def TimeoutStartSec(self, value: str):
        self.set_option(self.options.TIMEOUTSTARTSEC.value, value)

    @property
    def TimeoutStopSec(self) -> str:
        return self.get_option(self.options.TIMEOUTSTOPSEC.value)

    @TimeoutStopSec.setter
    def TimeoutStopSec(self, value: str):
        self.set_option(self.options.TIMEOUTSTOPSEC.value, value)

    @property
    def TimeoutAbortSec(self) -> str:
        return self.get_option(self.options.TIMEOUTABORTSEC.value)

    @TimeoutAbortSec.setter
    def TimeoutAbortSec(self, value: str):
        self.set_option(self.options.TIMEOUTABORTSEC.value, value)

    @property
    def TimeoutSec(self) -> str:
        return self.get_option(self.options.TIMEOUTSEC.value)

    @TimeoutSec.setter
    def TimeoutSec(self, value: str):
        self.set_option(self.options.TIMEOUTSEC.value, value)

    @property
    def TimeoutStartFailureMode(self) -> str:
        return self.get_option(self.options.TIMEOUTSTARTFAILUREMODE.value)

    @TimeoutStartFailureMode.setter
    def TimeoutStartFailureMode(self, value: str):
        self.set_option(self.options.TIMEOUTSTARTFAILUREMODE.value, value)

    @property
    def TimeoutStopFailureMode(self) -> str:
        return self.get_option(self.options.TIMEOUTSTOPFAILUREMODE.value)

    @TimeoutStopFailureMode.setter
    def TimeoutStopFailureMode(self, value: str):
        self.set_option(self.options.TIMEOUTSTOPFAILUREMODE.value, value)

    @property
    def RuntimeMaxSec(self) -> str:
        return self.get_option(self.options.RUNTIMEMAXSEC.value)

    @RuntimeMaxSec.setter
    def RuntimeMaxSec(self, value: str):
        self.set_option(self.options.RUNTIMEMAXSEC.value, value)

    @property
    def RuntimeRandomizedExtraSec(self) -> str:
        return self.get_option(self.options.RUNTIMERANDOMIZEDEXTRASEC.value)

    @RuntimeRandomizedExtraSec.setter
    def RuntimeRandomizedExtraSec(self, value: str):
        self.set_option(self.options.RUNTIMERANDOMIZEDEXTRASEC.value, value)

    @property
    def WatchdogSec(self) -> str:
        return self.get_option(self.options.WATCHDOGSEC.value)

    @WatchdogSec.setter
    def WatchdogSec(self, value: str):
        self.set_option(self.options.WATCHDOGSEC.value, value)

    @property
    def Restart(self) -> str:
        return self.get_option(self.options.RESTART.value)

    @Restart.setter
    def Restart(self, value: str):
        self.set_option(self.options.RESTART.value, value)

    @property
    def RestartMode(self) -> str:
        return self.get_option(self.options.RESTARTMODE.value)

    @RestartMode.setter
    def RestartMode(self, value: str):
        self.set_option(self.options.RESTARTMODE.value, value)

    @property
    def SuccessExitStatus(self) -> str:
        return self.get_option(self.options.SUCCESSEXITSTATUS.value)

    @SuccessExitStatus.setter
    def SuccessExitStatus(self, value: str):
        self.set_option(self.options.SUCCESSEXITSTATUS.value, value)

    @property
    def RestartPreventExitStatus(self) -> str:
        return self.get_option(self.options.RESTARTPREVENTEXITSTATUS.value)

    @RestartPreventExitStatus.setter
    def RestartPreventExitStatus(self, value: str):
        self.set_option(self.options.RESTARTPREVENTEXITSTATUS.value, value)

    @property
    def RestartForceExitStatus(self) -> str:
        return self.get_option(self.options.RESTARTFORCEEXITSTATUS.value)

    @RestartForceExitStatus.setter
    def RestartForceExitStatus(self, value: str):
        self.set_option(self.options.RESTARTFORCEEXITSTATUS.value, value)

    @property
    def RootDirectoryStartOnly(self) -> str:
        return self.get_option(self.options.ROOTDIRECTORYSTARTONLY.value)

    @RootDirectoryStartOnly.setter
    def RootDirectoryStartOnly(self, value: str):
        self.set_option(self.options.ROOTDIRECTORYSTARTONLY.value, value)

    @property
    def NonBlocking(self) -> str:
        return self.get_option(self.options.NONBLOCKING.value)

    @NonBlocking.setter
    def NonBlocking(self, value: str):
        self.set_option(self.options.NONBLOCKING.value, value)

    @property
    def NotifyAccess(self) -> str:
        return self.get_option(self.options.NOTIFYACCESS.value)

    @NotifyAccess.setter
    def NotifyAccess(self, value: str):
        self.set_option(self.options.NOTIFYACCESS.value, value)

    @property
    def Sockets(self) -> str:
        return self.get_option(self.options.SOCKETS.value)

    @Sockets.setter
    def Sockets(self, value: str):
        self.set_option(self.options.SOCKETS.value, value)

    @property
    def FileDescriptorStoreMax(self) -> str:
        return self.get_option(self.options.FILEDESCRIPTORSTOREMAX.value)

    @FileDescriptorStoreMax.setter
    def FileDescriptorStoreMax(self, value: str):
        self.set_option(self.options.FILEDESCRIPTORSTOREMAX.value, value)

    @property
    def FileDescriptorStorePreserve(self) -> str:
        return self.get_option(self.options.FILEDESCRIPTORSTOREPRESERVE.value)

    @FileDescriptorStorePreserve.setter
    def FileDescriptorStorePreserve(self, value: str):
        self.set_option(self.options.FILEDESCRIPTORSTOREPRESERVE.value, value)

    @property
    def USBFunctionDescriptors(self) -> str:
        return self.get_option(self.options.USBFUNCTIONDESCRIPTORS.value)

    @USBFunctionDescriptors.setter
    def USBFunctionDescriptors(self, value: str):
        self.set_option(self.options.USBFUNCTIONDESCRIPTORS.value, value)

    @property
    def USBFunctionStrings(self) -> str:
        return self.get_option(self.options.USBFUNCTIONSTRINGS.value)

    @USBFunctionStrings.setter
    def USBFunctionStrings(self, value: str):
        self.set_option(self.options.USBFUNCTIONSTRINGS.value, value)

    @property
    def OOMPolicy(self) -> str:
        return self.get_option(self.options.OOMPOLICY.value)

    @OOMPolicy.setter
    def OOMPolicy(self, value: str):
        self.set_option(self.options.OOMPOLICY.value, value)

    @property
    def OpenFile(self) -> str:
        return self.get_option(self.options.OPENFILE.value)

    @OpenFile.setter
    def OpenFile(self, value: str):
        self.set_option(self.options.OPENFILE.value, value)

    @property
    def ReloadSignal(self) -> str:
        return self.get_option(self.options.RELOADSIGNAL.value)

    @ReloadSignal.setter
    def ReloadSignal(self, value: str):
        self.set_option(self.options.RELOADSIGNAL.value, value)


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

    def create_unit(self, unit: str, folder: Optional[str] = None,
                    allow_update: bool = False) -> None:
        if folder is None:
            folder = sd_path.systemd_system_conf_dir
        assert isinstance(unit, str), f"unexpected type: {type(unit)}"
        assert isinstance(folder, str), f"unexpected type: {type(folder)}"

        if allowed_dirs is not None:
            assert folder in allowed_dirs, f"'{folder}' is not in {allowed_dirs}"  # noqa
        assert os.path.isdir(folder), f"'{folder}' not exists or is file"

        def get_service_unit_name(s: str) -> str:
            return s if s.endswith(".service") else ".".join([s, "service"])

        unitname: str = get_service_unit_name(unit)
        filepath: str = os.path.join(folder, unitname)
        if os.path.exists(filepath) and not allow_update:
            raise FileExistsError(f"'{filepath}' already exists.")

        with open(filepath, "w") as hdl:
            now: datetime = datetime.now()
            hdl.write(f"# {unitname} created by {__project__} {__version__}\n")
            hdl.write(f"# {now.strftime('%a %b %d %H:%M:%S CST %Y')}\n\n\n")
            self.parser.write(hdl)
