from extension_checker import ExtensionChecker
from parsers.csv_files_parser import CsvFilesParser
from parsers.json_files_parser import JsonFilesParser
from parsers.xml_files_parser import XmlFilesParser


class DataProcessor:
    def __init__(self, filenames):
        self.filenames = filenames
        self._min_amount_of_fields = 2147483647
        self._file_with_min_amount_of_columns = ""
        self._columns_of_result_file = []

    def get_file_with_min_amount_of_columns(self):

        for filename in self.filenames:
            extension_checker = ExtensionChecker(filename)

            if extension_checker.is_it_csv_file():
                csv_parser = CsvFilesParser(filename)
                columns_header = csv_parser.get_sorted_columns_header()

                if self._compare_current_len_of_columns_with_min(columns_header):
                    self._set_new_file_with_min_columns(filename)
                    self._set_new_columns_and_amount_of_result_file(columns_header)

            elif extension_checker.is_it_xml_file():
                xml_parser = XmlFilesParser(filename)
                print(xml_parser.get_sorted_list_of_columns_header())

            elif extension_checker.is_it_json_file():
                json_parser = JsonFilesParser(filename)
                columns_header = json_parser.get_sorted_columns_header()
                print(columns_header)

                if self._compare_current_len_of_columns_with_min(columns_header):
                    self._set_new_file_with_min_columns(filename)
                    self._set_new_columns_and_amount_of_result_file(columns_header)

        return self._file_with_min_amount_of_columns

    def get_sorted_columns_of_result_file(self):
        return self._columns_of_result_file

    def _compare_current_len_of_columns_with_min(self, columns):
        return len(columns) < self._min_amount_of_fields

    def _set_new_columns_and_amount_of_result_file(self, columns):
        self._columns_of_result_file = columns
        self._min_amount_of_fields = len(self._columns_of_result_file)

    def _set_new_file_with_min_columns(self, filename):
        self._file_with_min_amount_of_columns = filename
