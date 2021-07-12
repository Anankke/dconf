"""Make Config Great Again."""

from __future__ import annotations

from typing import Callable, TextIO
from collections import UserDict


class DotConfig(UserDict):
    def __getattr__(self, item):
        if item in self.data:
            result = self.data[item]
            if type(result) == dict:
                result = DotConfig(result)
            elif type(result) == list:
                for i in result:
                    if type(i) != dict:
                        return result
                result = [DotConfig(i) for i in result]
            return result
        raise AttributeError("Key '{}' dose not exist.".format(item))

    def load(self, load_function: Callable[[TextIO], dict], config_name: str) -> dict:
        try:
            fs = open(config_name)
        except:
            raise Exception("Failed to open configuration file.")
        try:
            config = load_function(fs)
        except:
            raise Exception("Failed to load configuration file.")
        self.__init__(config)
        return config

    def to_dict(self):
        return self.data
