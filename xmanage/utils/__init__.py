# coding:utf-8

from xmanage.utils.systemd import systemd_service  # noqa:F401

try:
    from xmanage.utils.systemd import systemd_path  # noqa:F401
except Exception:
    pass
