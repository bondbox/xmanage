# coding:utf-8

from xmanage.systemd.service import sd_service as systemd_service  # noqa:E501,F401

try:
    from xmanage.systemd.path import sd_path as systemd_path  # noqa:F401
except Exception:  # pragma: no cover
    pass  # pragma: no cover
