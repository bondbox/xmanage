# coding:utf-8

from xmanage.systemd.service import sd_uf_sec_service
from xmanage.systemd.unit import sd_uf_sec_install
from xmanage.systemd.unit import sd_uf_sec_unit

for section in [sd_uf_sec_unit, sd_uf_sec_install, sd_uf_sec_service]:
    for item in section.options:
        text: str = f"""
    @property
    def {item.value}(self) -> str:
        return self.get_option(self.options.{item.name}.value)

    @{item.value}.setter
    def {item.value}(self, value: str):
        self.set_option(self.options.{item.name}.value, value)"""

        print(text)
