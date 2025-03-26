# coding:utf-8

from typing import List
from typing import Optional
from typing import Sequence

from xkits import add_command
from xkits import argp
from xkits import commands
from xkits import run_command

from xmanage.attribute import __description__
from xmanage.attribute import __project__
from xmanage.attribute import __urlhome__
from xmanage.attribute import __version__

subs: List[add_command] = list()

try:
    from xmanage.xsystem.path import add_cmd_path
    subs.append(add_cmd_path)
except Exception:
    pass


@add_command(__project__)
def add_cmd(_arg: argp):
    pass


@run_command(add_cmd, *subs)
def run_cmd(cmds: commands) -> int:
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    cmds = commands()
    cmds.version = __version__
    return cmds.run(
        root=add_cmd,
        argv=argv,
        description=__description__,
        epilog=f"For more, please visit {__urlhome__}.")
