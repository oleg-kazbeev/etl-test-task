import csv


class CsvFilesParser:
    def __init__(self, filename):
        self.filename = filename
        self._headers = []

    def get_headers(self):
        with open(self.filename) as csv_file:
            reader = csv.DictReader(csv_file)
            self._headers = reader.fieldnames
        return self._headers
