import json
from parsers.sorting_tools import natural_keys


class JsonFilesParser:
    def __init__(self, filename):
        self._columns = []
        self._filename = filename

    def get_sorted_columns_header(self):
        columns_header = self._get_list_of_columns_header()
        columns_header.sort(key=natural_keys)
        self._columns = columns_header
        return self._columns

    def _get_list_of_columns_header(self):
        with open(self._filename, 'r') as fn:
            json_data = json.load(fn)

            for column_name in json_data['fields'][0]:
                self._columns.append(column_name)

        return self._columns
