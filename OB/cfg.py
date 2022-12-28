
from typing import Any

__author__ = 'Muhammad Hamza'
__github__ = 'https://github.com/hop09'
__facebook__ = 'https://m.facebook.com/hopoffocials'

class ConfigValue:
    def __init__(self, desc: str, default: Any):
        self.desc = desc
        self.value = default

    def __repr__(self):
        return f"ConfigValue({repr(self.desc)}, {repr(self.value)})"


class ConfigSegment(dict):
    def __init__(self, name, desc, **kwargs: ConfigValue):
        self.name = name
        self.desc = desc
        super().__init__(kwargs)
