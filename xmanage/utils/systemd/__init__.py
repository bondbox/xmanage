# coding:utf-8

from .service import sd_service as systemd_service  # noqa:F401

try:
    from .path import sd_path as systemd_path  # noqa:F401
except Exception:
    pass
