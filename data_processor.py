from extension_checker import ExtensionChecker
from csv_files_parser import CsvFilesParser


class DataProcessor:
    def __init__(self, filenames):
        self.filenames = filenames
        self._min_amount_of_fields = 10 ** 6
        self._filename_with_min_fields = ''

    def get_file_with_min_amount_of_fields(self):
        for filename in self.filenames:
            extension_checker = ExtensionChecker(filename)

            if extension_checker.is_it_csv_file():
                csv_parser = CsvFilesParser()
                fieldnames = csv_parser.get_sorted_list_with_fieldnames(filename)

                if self._compare_current_len_of_fieldnames_with_min(len(fieldnames)):
                    self._set_new_min_amount_of_fields(len(fieldnames))
                    self._set_new_filename_with_min_fields(filename)

            elif extension_checker.is_it_xml_file():
                pass

            elif extension_checker.is_it_json_file():
                pass

        return self._filename_with_min_fields

    def _compare_current_len_of_fieldnames_with_min(self, fieldnames_list_length):
        return fieldnames_list_length < self._min_amount_of_fields

    def _set_new_min_amount_of_fields(self, fieldnames_list_length):
        self._min_amount_of_fields = fieldnames_list_length

    def _set_new_filename_with_min_fields(self, filename):
        self._filename_with_min_fields = filename

