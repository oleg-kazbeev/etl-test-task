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
        self.filename = filename
        self._fieldnames = []

    def get_sorted_list_with_fieldnames(self):
        sorted_fieldnames = self._get_list_of_fieldnames()
        sorted_fieldnames.sort(key=natural_keys)
        self._fieldnames = sorted_fieldnames
        return self._fieldnames

    def _get_list_of_fieldnames(self):
        with open(self.filename) as csv_file:
            reader = csv.DictReader(csv_file)
            fieldnames = reader.fieldnames
        return fieldnames
