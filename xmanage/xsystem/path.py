# coding:utf-8

from tabulate import tabulate
from xkits_command import ArgParser
from xkits_command import Command
from xkits_command import CommandArgument
from xkits_command import CommandExecutor

try:
    from xmanage.systemd import systemd_path

    @CommandArgument("path", help="show system and user paths")
    def add_cmd_path(_arg: ArgParser):
        _arg.add_argument(dest="sd_path_titles", type=str, nargs="*",
                          default=[], action="extend", metavar="NAME",
                          choices=systemd_path.titles + [[]],
                          help="the path value with this name is shown")

    @CommandExecutor(add_cmd_path)
    def run_cmd_path(cmds: Command) -> int:
        if not cmds.has_sub(add_cmd_path):
            titles = cmds.args.sd_path_titles
            values = titles if len(titles) > 0 else systemd_path
            tabular = [(n, "\n".join(systemd_path[n])) for n in values]
            tstring = tabulate(tabular, headers=["name", "paths"])
            cmds.stdout(tstring)
        return 0
except Exception:  # pragma: no cover
    pass  # pragma: no cover
