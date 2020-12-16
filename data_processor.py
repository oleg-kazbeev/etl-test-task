from extension_checker import ExtensionChecker
from parsers.csv_files_parser import CsvFilesParser


class DataProcessor:
    def __init__(self, filenames):
        self.filenames = filenames
        self._min_amount_of_fields = 10 ** 6
        self._file_with_min_amount_of_columns = ""
        self._columns_of_result_file = []

    def get_file_with_min_amount_of_columns(self):
        for filename in self.filenames:
            extension_checker = ExtensionChecker(filename)

            if extension_checker.is_it_csv_file():
                csv_parser = CsvFilesParser()
                self._columns_of_result_file = csv_parser.get_sorted_list_with_columns(filename)

                if self._compare_current_len_of_columns_with_min():
                    self._set_new_min_amount_of_columns()
                    self._set_new_file_with_min_columns(filename)

            elif extension_checker.is_it_xml_file():
                pass

            elif extension_checker.is_it_json_file():
                pass

        return self._file_with_min_amount_of_columns

    def _compare_current_len_of_columns_with_min(self):
        return len(self._columns_of_result_file) < self._min_amount_of_fields

    def _set_new_min_amount_of_columns(self):
        self._min_amount_of_fields = len(self._columns_of_result_file)

    def _set_new_file_with_min_columns(self, filename):
        self._file_with_min_amount_of_columns = filename
