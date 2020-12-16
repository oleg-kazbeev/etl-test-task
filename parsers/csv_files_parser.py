import csv


class CsvFilesParser:
    def __init__(self):
        self._fieldnames = []

    def get_sorted_list_with_fieldnames(self, filename):
        fieldnames = self._get_list_of_fieldnames(filename)
        sorted_fieldnames = sorted(fieldnames, key=lambda x: int("".join([i for i in x if i.isdigit()])))
        self._fieldnames = sorted_fieldnames
        return self._fieldnames

    def _get_list_of_fieldnames(self, filename):
        with open(filename) as csv_file:
            reader = csv.DictReader(csv_file)
            self._fieldnames = reader.fieldnames
        return self._fieldnames
