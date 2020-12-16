import csv


class DataComposer:
    def __init__(self, input_files, output_files):
        self._output = output_files
        self._input = input_files
        self._success_message = ''

    def record_file_content_into_basic_result_file(self, filename):
        _basic_results = self._output[0]

        with open(_basic_results, 'a') as result_file:
            writer = csv.writer(result_file)
            with open(filename, 'r') as infile:
                reader = csv.reader(infile)
                for row in reader:
                    writer.writerow(row)

        self._remove_recorded_file_from_input_list(filename)

    def _remove_recorded_file_from_input_list(self, filename):
        self._input.remove(filename)
