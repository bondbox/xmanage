# coding:utf-8

from .attribute import __author__
from .attribute import __author_email__
from .attribute import __description__
from .attribute import __project__
from .attribute import __url_bugs__
from .attribute import __url_code__
from .attribute import __url_docs__
from .attribute import __url_home__
from .attribute import __version__
from .systemd import systemd_service

try:
    from .systemd import systemd_path
except Exception:
    pass
