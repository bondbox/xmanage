# coding:utf-8

from typing import List
from typing import Optional
from typing import Sequence

from xkits_command import ArgParser
from xkits_command import Command
from xkits_command import CommandArgument
from xkits_command import CommandExecutor

from xmanage.attribute import __description__
from xmanage.attribute import __project__
from xmanage.attribute import __urlhome__
from xmanage.attribute import __version__

subs: List[CommandArgument] = list()

try:
    from xmanage.xsystem.path import add_cmd_path
    subs.append(add_cmd_path)
except Exception:  # pragma: no cover
    pass  # pragma: no cover


@CommandArgument(__project__)
def add_cmd(_arg: ArgParser):
    pass


@CommandExecutor(add_cmd, *subs)
def run_cmd(cmds: Command) -> int:
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    cmds = Command()
    cmds.version = __version__
    return cmds.run(
        root=add_cmd,
        argv=argv,
        description=__description__,
        epilog=f"For more, please visit {__urlhome__}.")
