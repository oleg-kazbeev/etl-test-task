import sys

from parsers.terminal_parser import TerminalParser
from data_processor import DataProcessor
from data_composer import DataComposer


def main():
    terminal_command = sys.argv[1:]

    terminal_parser = TerminalParser()
    terminal_parser.add_argument('-i', '--input', default=[], nargs='+')
    terminal_parser.add_argument('-o', '--output', default=[], nargs='+')

    input_files = terminal_parser.get_list_of_input_files(terminal_command)
    output_files = terminal_parser.get_list_of_output_files(terminal_command)

    data_processor = DataProcessor(input_files)
    file_with_min_col = data_processor.get_file_with_min_amount_of_columns()
    columns_of_result_file = data_processor.get_sorted_columns_of_result_file()

    data_composer = DataComposer(input_files, output_files)
    data_composer.record_first_file_content_into_basic_result_file(file_with_min_col,
                                                                   columns_of_result_file)
    data_composer.record_leftovers_files_into_basic_result(columns_of_result_file)
    data_composer.sort_basic_results_file_content()


if __name__ == '__main__':
    main()
