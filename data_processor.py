import os


class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.fields_titles_of_result_table = []
        self._file_extension = ''
        self._CSV = '.csv'
        self._XML = '.xml'
        self._JSON = '.json'

    def _extract_extension_from_filename(self):
        _, self._file_extension = os.path.splitext(self.filename)
        return self._file_extension

    def is_it_xml_file(self):
        return self._extract_extension_from_filename() == self._XML

    def is_it_csv_file(self):
        return self._extract_extension_from_filename() == self._CSV

    def is_it_json_file(self):
        return self._extract_extension_from_filename() == self._JSON

    def define_table_fields_of_result_file(self):
        pass
