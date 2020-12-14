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
        self._fieldnames = []

    def get_sorted_list_with_fieldnames(self, filename):
        sorted_fieldnames = self._get_list_of_fieldnames(filename)
        sorted_fieldnames.sort(key=natural_keys)
        self._fieldnames = sorted_fieldnames
        return self._fieldnames

    def _get_list_of_fieldnames(self, filename):
        with open(filename) as csv_file:
            reader = csv.DictReader(csv_file)
            self._fieldnames = reader.fieldnames
        return self._fieldnames
