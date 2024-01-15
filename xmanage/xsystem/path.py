# coding:utf-8

from tabulate import tabulate
from xarg import add_command
from xarg import argp
from xarg import commands
from xarg import run_command

try:
    from ..utils import systemd_path

    @add_command("path")
    def add_cmd_path(_arg: argp):
        pass

    @run_command(add_cmd_path)
    def run_cmd_path(cmds: commands) -> int:
        if not cmds.has_sub(add_cmd_path):
            tabular = [(n, "\n".join(systemd_path[n])) for n in systemd_path]
            tstring = tabulate(tabular, headers=["name", "paths"])
            cmds.stdout(tstring)
        return 0
except Exception:
    pass
