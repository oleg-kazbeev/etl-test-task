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
    def __init__(self):
        self._columns = []

    def get_sorted_columns_header(self, filename):
        columns = self._get_list_of_columns(filename)
        columns.sort(key=natural_keys)
        self._columns = columns
        return self._columns

    def _get_list_of_columns(self, filename):
        with open(filename) as csv_file:
            reader = csv.DictReader(csv_file)
            self._columns = reader.fieldnames
        return self._columns
