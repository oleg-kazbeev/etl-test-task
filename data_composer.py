import csv
import json
from xml.etree import ElementTree

from extension_checker import ExtensionChecker


def _record_json_file_into_results(filename, writer, columns):
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
        for row in json_data["fields"]:
            for key in row.copy().keys():
                if key not in columns:
                    row.pop(key)

            writer.writerow(row)


def _record_csv_file_into_results(filename, writer, columns):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            for key in row.copy().keys():
                if key not in columns:
                    row.pop(key)

            writer.writerow(row)


def _record_xml_file_into_results(filename, writer, columns):
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

    def record_leftovers_files_into_result(self, columns):
        for filename in self._input:
            extension_checker = ExtensionChecker(filename)
            with open(self._basic_results, 'a') as out:
                writer = csv.DictWriter(out, fieldnames=columns)

                if extension_checker.is_it_csv_file():
                    _record_csv_file_into_results(filename, writer, columns)

                elif extension_checker.is_it_json_file():
                    _record_json_file_into_results(filename, writer, columns)

                elif extension_checker.is_it_xml_file():
                    _record_xml_file_into_results(filename, writer, columns)

    def record_first_file_content_into_basic_result_file(self, filename, columns):
        extension_checker = ExtensionChecker(filename)
        with open(self._basic_results, 'w') as result_file:
            writer = csv.DictWriter(result_file,
                                    fieldnames=columns)
            writer.writeheader()

            if extension_checker.is_it_csv_file():
                _record_csv_file_into_results(filename, writer, columns)

            elif extension_checker.is_it_json_file():
                _record_json_file_into_results(filename, writer, columns)

            elif extension_checker.is_it_xml_file():
                _record_xml_file_into_results(filename, writer, columns)

        self._remove_recorded_file_from_input_list(filename)

    def _remove_recorded_file_from_input_list(self, filename):
        self._input.remove(filename)
