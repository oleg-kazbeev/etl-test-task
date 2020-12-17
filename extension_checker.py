import os


class ExtensionChecker:
    def __init__(self, filename):
        self._XML = '.xml'
        self._CSV = '.csv'
        self._JSON = '.json'
        self.filename = filename

    def is_it_xml_file(self):
        return self._extract_extension_from_filename() == self._XML

    def is_it_csv_file(self):
        return self._extract_extension_from_filename() == self._CSV

    def is_it_json_file(self):
        return self._extract_extension_from_filename() == self._JSON

    def _extract_extension_from_filename(self):
        _, _file_extension = os.path.splitext(self.filename)
        return _file_extension
