# coding:utf-8

from tabulate import tabulate
from xarg import add_command
from xarg import argp
from xarg import commands
from xarg import run_command

try:
    from ..utils import systemd_path

    @add_command("path", help="show system and user paths")
    def add_cmd_path(_arg: argp):
        _arg.add_argument(dest="sd_path_titles", type=str, nargs="*",
                          default=[], action="extend", metavar="NAME",
                          choices=systemd_path.titles + [[]],
                          help="the path value with this name is shown")

    @run_command(add_cmd_path)
    def run_cmd_path(cmds: commands) -> int:
        if not cmds.has_sub(add_cmd_path):
            titles = cmds.args.sd_path_titles
            values = titles if len(titles) > 0 else systemd_path
            tabular = [(n, "\n".join(systemd_path[n])) for n in values]
            tstring = tabulate(tabular, headers=["name", "paths"])
            cmds.stdout(tstring)
        return 0
except Exception:
    pass
