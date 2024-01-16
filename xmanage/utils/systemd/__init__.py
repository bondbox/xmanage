# coding:utf-8

from .service import sd_service as systemd_service

try:
    from .path import sd_path as systemd_path
except Exception:
    pass
