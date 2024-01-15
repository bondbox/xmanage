import os
import re
from re import Match
from typing import List
from typing import Tuple

dirname = os.path.dirname(__file__)
content = open(os.path.join(dirname, "path.c")).read()
pattern = "path_table\[_SD_PATH_MAX\] = {(?P<table>.+?)}"
search = re.search(pattern, content, re.DOTALL)
assert isinstance(search, Match)

path_table: List[Tuple[str, str]] = list()
table: str = search.group("table")
for line in table.splitlines():
    text = line.strip()
    if not text:
        continue
    what = re.search("\[SD_PATH_(?P<name>\S+)\].+\"(?P<value>\S+)\"", text)
    assert isinstance(what, Match)
    path_table.append((what.group("name"), what.group("value")))


with open(os.path.join(dirname, "path.py"), "w") as hdl:
    hdl.write("from enum import Enum\n\n\n")
    hdl.write("class table(Enum):\n")
    for item in path_table:
        name, value = item
        hdl.write(f"    {name} = \"{value}\"\n")
