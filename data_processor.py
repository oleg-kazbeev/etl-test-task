import os


class DataProcessor:
    # csv_files_parser =
    def __init__(self, filenames):
        self.filenames = filenames
        self.fields_titles_of_result_table = []
        self._file_extension = ''
        self._CSV = '.csv'
        self._XML = '.xml'
        self._JSON = '.json'

    def find_file_with_min_amount_of_M_fields(self):
        for file in self.filenames:
            if self._is_it_csv_file(file):
                pass

            elif self._is_it_xml_file(file):
                pass

            elif self._is_it_json_file(file):
                pass

    def _is_it_xml_file(self, file):
        return self._extract_extension_from_filename(file) == self._XML

    def _is_it_csv_file(self, file):
        return self._extract_extension_from_filename(file) == self._CSV

    def _is_it_json_file(self, file):
        return self._extract_extension_from_filename(file) == self._JSON

    def _extract_extension_from_filename(self, file):
        _, self._file_extension = os.path.splitext(file)
        return self._file_extension


