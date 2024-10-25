# coding:utf-8

from .attribute import __author__  # noqa:F401
from .attribute import __author_email__  # noqa:F401
from .attribute import __description__  # noqa:F401
from .attribute import __project__  # noqa:F401
from .attribute import __urlbugs__  # noqa:F401
from .attribute import __urlcode__  # noqa:F401
from .attribute import __urldocs__  # noqa:F401
from .attribute import __urlhome__  # noqa:F401
from .attribute import __version__  # noqa:F401
from .systemd import systemd_service  # noqa:F401

try:
    from .systemd import systemd_path  # noqa:F401
except Exception:
    pass
