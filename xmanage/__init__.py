# coding:utf-8

from .utils import systemd_service

try:
    from .utils import systemd_path
except Exception:
    pass
