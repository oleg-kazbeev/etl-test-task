import csv


class CsvFilesParser:
    def __init__(self):
        self._columns = []

    def get_sorted_list_with_columns(self, filename):
        columns = self._get_list_of_columns(filename)
        sorted_columns = sorted(columns, key=lambda x: int("".join([i for i in x if i.isdigit()])))
        self._columns = sorted_columns
        return self._columns

    def _get_list_of_columns(self, filename):
        with open(filename) as csv_file:
            reader = csv.DictReader(csv_file)
            self._columns = reader.fieldnames
        return self._columns
