import csv


class DataComposer:
    def __init__(self, input_files, output_files):
        self._output = output_files
        self._input = input_files
        self._success_message = ''
        self._basic_results = self._output[0]

    def record_leftovers_files_into_result(self, columns):
        for filename in self._input:
            with open(self._basic_results, 'a') as out:
                writer = csv.DictWriter(out, fieldnames=columns)

                with open(filename, 'r') as infile:
                    reader = csv.DictReader(infile)

                    for row in reader:
                        for key in row.copy().keys():
                            if key not in columns:
                                row.pop(key)

                        writer.writerow(row)

    def record_file_content_into_basic_result_file(self, filename, columns):
        with open(self._basic_results, 'w') as result_file:
            writer = csv.DictWriter(result_file, fieldnames=columns)  # TODO: вызвать метод get_sorted_colums_header вместо передачи columns
            writer.writeheader()

            with open(filename, 'r') as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    writer.writerow(row)

        self._remove_recorded_file_from_input_list(filename)

    def _remove_recorded_file_from_input_list(self, filename):
        self._input.remove(filename)
