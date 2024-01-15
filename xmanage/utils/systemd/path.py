# coding:utf-8

from enum import Enum
import os
import shutil
from typing import Dict
from typing import List
from typing import Tuple

from xarg import singleton

CMD_SD_PATH = "systemd-path"


if shutil.which(CMD_SD_PATH):

    @singleton
    class __sd_path:

        class table(Enum):
            TEMPORARY = "temporary"
            TEMPORARY_LARGE = "temporary-large"
            SYSTEM_BINARIES = "system-binaries"
            SYSTEM_INCLUDE = "system-include"
            SYSTEM_LIBRARY_PRIVATE = "system-library-private"
            SYSTEM_LIBRARY_ARCH = "system-library-arch"
            SYSTEM_SHARED = "system-shared"
            SYSTEM_CONFIGURATION_FACTORY = "system-configuration-factory"
            SYSTEM_STATE_FACTORY = "system-state-factory"
            SYSTEM_CONFIGURATION = "system-configuration"
            SYSTEM_RUNTIME = "system-runtime"
            SYSTEM_RUNTIME_LOGS = "system-runtime-logs"
            SYSTEM_STATE_PRIVATE = "system-state-private"
            SYSTEM_STATE_LOGS = "system-state-logs"
            SYSTEM_STATE_CACHE = "system-state-cache"
            SYSTEM_STATE_SPOOL = "system-state-spool"
            USER_BINARIES = "user-binaries"
            USER_LIBRARY_PRIVATE = "user-library-private"
            USER_LIBRARY_ARCH = "user-library-arch"
            USER_SHARED = "user-shared"
            USER_CONFIGURATION = "user-configuration"
            USER_RUNTIME = "user-runtime"
            USER_STATE_CACHE = "user-state-cache"
            USER_STATE_PRIVATE = "user-state-private"
            USER = "user"
            USER_DOCUMENTS = "user-documents"
            USER_MUSIC = "user-music"
            USER_PICTURES = "user-pictures"
            USER_VIDEOS = "user-videos"
            USER_DOWNLOAD = "user-download"
            USER_PUBLIC = "user-public"
            USER_TEMPLATES = "user-templates"
            USER_DESKTOP = "user-desktop"
            SEARCH_BINARIES = "search-binaries"
            SEARCH_BINARIES_DEFAULT = "search-binaries-default"
            SEARCH_LIBRARY_PRIVATE = "search-library-private"
            SEARCH_LIBRARY_ARCH = "search-library-arch"
            SEARCH_SHARED = "search-shared"
            SEARCH_CONFIGURATION_FACTORY = "search-configuration-factory"
            SEARCH_STATE_FACTORY = "search-state-factory"
            SEARCH_CONFIGURATION = "search-configuration"
            SYSTEMD_UTIL = "systemd-util"
            SYSTEMD_SYSTEM_UNIT = "systemd-system-unit"
            SYSTEMD_SYSTEM_PRESET = "systemd-system-preset"
            SYSTEMD_SYSTEM_CONF = "systemd-system-conf"
            SYSTEMD_USER_UNIT = "systemd-user-unit"
            SYSTEMD_USER_PRESET = "systemd-user-preset"
            SYSTEMD_USER_CONF = "systemd-user-conf"
            SYSTEMD_SEARCH_SYSTEM_UNIT = "systemd-search-system-unit"
            SYSTEMD_SEARCH_USER_UNIT = "systemd-search-user-unit"
            SYSTEMD_SYSTEM_GENERATOR = "systemd-system-generator"
            SYSTEMD_USER_GENERATOR = "systemd-user-generator"
            SYSTEMD_SEARCH_SYSTEM_GENERATOR = "systemd-search-system-generator"
            SYSTEMD_SEARCH_USER_GENERATOR = "systemd-search-user-generator"
            SYSTEMD_SLEEP = "systemd-sleep"
            SYSTEMD_SHUTDOWN = "systemd-shutdown"
            TMPFILES = "tmpfiles"
            SYSUSERS = "sysusers"
            SYSCTL = "sysctl"
            BINFMT = "binfmt"
            MODULES_LOAD = "modules-load"
            CATALOG = "catalog"
            SYSTEMD_SEARCH_NETWORK = "systemd-search-network"
            SYSTEMD_SYSTEM_ENVIRONMENT_GENERATOR = "systemd-system-environment-generator"
            SYSTEMD_USER_ENVIRONMENT_GENERATOR = "systemd-user-environment-generator"
            SYSTEMD_SEARCH_SYSTEM_ENVIRONMENT_GENERATOR = "systemd-search-system-environment-generator"
            SYSTEMD_SEARCH_USER_ENVIRONMENT_GENERATOR = "systemd-search-user-environment-generator"

        def __init__(self):
            self.__items: Dict[str, Tuple[str, ...]] = dict()
            for line in os.popen(CMD_SD_PATH).readlines():
                name, path = line.split(":", 1)
                assert isinstance(name, str)
                assert isinstance(path, str)
                dirs: List[str] = path.strip().split(":")
                self.__items[name.strip()] = tuple([i.strip() for i in dirs])

        def __iter__(self):
            return iter(self.__items.keys())

        def __getitem__(self, key) -> Tuple[str, ...]:
            return self.__items[key]

    sd_path = __sd_path()
