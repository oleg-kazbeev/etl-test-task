import csv
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [atoi(c) for c in re.split(r'(\d+)', text)]


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
