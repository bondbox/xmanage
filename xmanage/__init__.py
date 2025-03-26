# coding:utf-8

from xmanage.systemd import systemd_service  # noqa:F401

try:
    from xmanage.systemd import systemd_path  # noqa:F401
except Exception:  # pragma: no cover pylint: disable=broad-exception-caught
    pass  # pragma: no cover
