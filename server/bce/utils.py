import json
import os

dirname = os.path.dirname(__file__)


def load_file(file_name, subdirectory="tests/fixtures"):
    with open(os.path.join(dirname, subdirectory, file_name), encoding="utf-8") as data_file:
        return json.loads(data_file.read())
