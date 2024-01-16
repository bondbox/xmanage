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

    def __init__(self):
        pass

    @classmethod
    def read(cls, file: str) -> ConfigParser:
        assert os.path.exists(file), f"'{file}' not found."
        assert os.path.isfile(file), f"'{file}' is not a regular file."
        return cls.read_string(open(file).read())

    @classmethod
    def read_string(cls, value: str) -> ConfigParser:
        config: ConfigParser = ConfigParser()
        config.read_string(value)
        return config

    def create_unit(self, path: str, unit: str, conf: ConfigParser) -> None:
        assert isinstance(path, str), f"unexpected type: {type(path)}"
        assert isinstance(unit, str), f"unexpected type: {type(unit)}"
        assert isinstance(conf, ConfigParser), f"unexpected type: {type(conf)}"

        if allowed_dirs is not None:
            assert path in allowed_dirs, f"'{path}' is not in {allowed_dirs}"

        def get_service_unit_name(s: str) -> str:
            return s if s.endswith(".service") else ".".join([s, "service"])

        file: str = os.path.join(path, get_service_unit_name(unit))
        if os.path.exists(file):
            raise FileExistsError(f"'{file}' already exists.")

        with open(file, "w") as hdl:
            conf.write(hdl)
