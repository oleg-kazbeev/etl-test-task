import csv
from parsers.sorting_tools import natural_keys


class CsvFilesParser:
    def __init__(self, filename):
        self._columns = []
        self._filename = filename

    def get_sorted_columns_header(self):
        columns = self._get_list_of_columns()
        columns.sort(key=natural_keys)
        self._columns = columns
        return self._columns

    def _get_list_of_columns(self):
        with open(self._filename) as csv_file:
            reader = csv.DictReader(csv_file)
            self._columns = reader.fieldnames
        return self._columns
