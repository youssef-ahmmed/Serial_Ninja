import os
from datetime import datetime
import json


class FileStorage:

    def __init__(self):
        self.__time_stamp = datetime.now().strftime("%m-%dT%H-%M")
        self.__object = {}
        self.list_of_log = []
        self.__file_path = os.path.join('../Logging/', f"file_at_{self.__time_stamp}.json")

        if not os.path.isdir('../Logging'):
            os.mkdir("../Logging")

    def new(self, log_dict):
        self.__object = log_dict.copy()

    def save(self):
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            self.list_of_log.append(self.__object)
            json.dump(self.list_of_log, f, indent=4)
