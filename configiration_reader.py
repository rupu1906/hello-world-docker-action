import json
from os import path

from pyjavaproperties import Properties


class ConfigurationReader:
    @staticmethod
    def read_json(dir_name, file_name):
        file_path = path.join(dir_name, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def get_config(component, path_name):
        config = ConfigurationReader()
        end_point = config.read_json("", "").get(component).get(path_name)
        return end_point
