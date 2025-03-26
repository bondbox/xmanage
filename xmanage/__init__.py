# coding:utf-8

from .utils import systemd_service  # noqa:F401

try:
    from .utils import systemd_path  # noqa:F401
except Exception:  # pylint: disable=broad-exception-caught
    pass
