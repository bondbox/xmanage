# coding:utf-8

from configparser import ConfigParser
import os
from typing import Optional
from typing import Tuple

allowed_dirs: Optional[Tuple[str, ...]] = None
try:
    from .path import sd_path
    allowed_dirs = sd_path.systemd_system_dirs
except Exception:
    pass


class sd_service:

    def __init__(self, config: ConfigParser):
        assert isinstance(config, ConfigParser), \
            f"unexpected type: {type(config)}"
        self.__config: ConfigParser = config

    @classmethod
    def from_string(cls, value: str) -> "sd_service":
        config: ConfigParser = ConfigParser()
        config.optionxform = lambda option: option  # type: ignore
        config.read_string(value)
        return sd_service(config)

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

        def get_service_unit_name(s: str) -> str:
            return s if s.endswith(".service") else ".".join([s, "service"])

        file: str = os.path.join(path, get_service_unit_name(unit))
        if os.path.exists(file) and not allow_update:
            raise FileExistsError(f"'{file}' already exists.")

        with open(file, "w") as hdl:
            self.__config.write(hdl)
