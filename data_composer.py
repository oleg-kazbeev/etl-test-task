import csv
import json
import operator
from xml.etree import ElementTree

from extension_checker import ExtensionChecker


def _record_json_file_into_basic_results(filename, writer, columns):
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
        for row in json_data["fields"]:
            for key in row.copy().keys():
                if key not in columns:
                    row.pop(key)

            writer.writerow(row)


def _record_csv_file_into_basic_results(filename, writer, columns):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            for key in row.copy().keys():
                if key not in columns:
                    row.pop(key)

            writer.writerow(row)


def _record_xml_file_into_basic_results(filename, writer, columns):
    with open(filename, 'r') as xml_file:
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        row = {}

        for obj in root.findall('objects/object'):
            column_name = obj.attrib['name']
            if column_name in columns:
                row[column_name] = obj.find('value').text

    writer.writerow(row)


class DataComposer:
    def __init__(self, input_files, output_files):
        self._output = output_files
        self._input = input_files
        self._basic_results = self._output[0]
        self._advanced_results = self._output[1]

    def record_leftovers_files_into_basic_result(self, columns):
        for filename in self._input:
            extension_checker = ExtensionChecker(filename)
            with open(self._basic_results, 'a') as out:
                writer = csv.DictWriter(out, fieldnames=columns)

                if extension_checker.is_it_csv_file():
                    _record_csv_file_into_basic_results(filename, writer, columns)

                elif extension_checker.is_it_json_file():
                    _record_json_file_into_basic_results(filename, writer, columns)

                elif extension_checker.is_it_xml_file():
                    _record_xml_file_into_basic_results(filename, writer, columns)

    def record_first_file_content_into_basic_result_file(self, filename, columns):
        extension_checker = ExtensionChecker(filename)
        with open(self._basic_results, 'w') as result_file:
            writer = csv.DictWriter(result_file,
                                    fieldnames=columns)
            writer.writeheader()

            if extension_checker.is_it_csv_file():
                _record_csv_file_into_basic_results(filename, writer, columns)

            elif extension_checker.is_it_json_file():
                _record_json_file_into_basic_results(filename, writer, columns)

            elif extension_checker.is_it_xml_file():
                _record_xml_file_into_basic_results(filename, writer, columns)

        self._remove_recorded_file_from_input_list(filename)

    def _remove_recorded_file_from_input_list(self, filename):
        self._input.remove(filename)

    def sort_basic_results_file_content(self):
        basic_results = self._basic_results
        with open(basic_results, 'r+') as br:
            reader = csv.reader(br)
            sorted_basic_results = sorted(reader, key=operator.itemgetter(0))
            br.truncate(0)
        with open(basic_results, 'w') as br:
            writer = csv.writer(br)
            writer.writerows(sorted_basic_results)

    def record_advanced_results_based_on_basic(self):
        with open(self._advanced_results, 'w') as ar:
            writer = csv.writer(ar)

            column_names_row = self._get_row_with_columns_name_of_advanced_results_file()
            rows = self._get_rows_of_advanced_result_file_without_column_names()

            writer.writerow(column_names_row)
            writer.writerows(rows)

    def _get_rows_of_advanced_result_file_without_column_names(self):
        with open(self._basic_results) as br:
            reader = csv.reader(br)
            rows = []
            rows_index = 0
            row_number_in_basic = 0
            result = {}
            index = self._get_index_of_start_int_values_in_row()

            for row in reader:

                if row_number_in_basic == 0:
                    row_number_in_basic += 1

                else:
                    combined_string = ''

                    for value in row:
                        try:
                            int(value)
                        except ValueError:
                            combined_string += value

                    if combined_string in result.keys():
                        row_num = result[combined_string]

                        for i in range(index, len(row)):
                            m_int_value_in_result = int(rows[row_num][i])
                            m_int_value_current_row = int(row[i])
                            rows[row_num][i] = str(m_int_value_current_row + m_int_value_in_result)

                    else:
                        result[combined_string] = rows_index
                        rows.append(row)
                        rows_index += 1
        return rows

    def _get_index_of_start_int_values_in_row(self):
        with open(self._basic_results) as br:
            reader = csv.reader(br)
            index_of_start_int_values = 0
            row_number = 0

            for row in reader:
                if row_number == 0:
                    row_number += 1
                else:
                    for value in row:
                        try:
                            int(value)
                        except ValueError:
                            index_of_start_int_values += 1
                    break

        return index_of_start_int_values

    def _get_row_with_columns_name_of_advanced_results_file(self):
        index = 0
        row_number = 0
        column_names = []

        with open(self._basic_results, 'r') as br:
            reader = csv.reader(br)
            for _ in reader:
                if row_number == 0:
                    row_number += 1
                else:
                    index = self._get_index_of_start_int_values_in_row()
                    break

        with open(self._basic_results, 'r') as br:
            reader = csv.reader(br)
            for row in reader:
                num_of_ms = 1
                for i in range(index, len(row)):
                    row[i] = "MS" + str(num_of_ms)
                    num_of_ms += 1
                column_names = row
                break

        return column_names
