import sys

from parsers.terminal_parser import TerminalParser
from data_processor import DataProcessor


def main():
    terminal_command = sys.argv[1:]

    terminal_parser = TerminalParser()
    terminal_parser.add_argument('-i', '--input', default=[], nargs='+')
    terminal_parser.add_argument('-o', '--output', default=[], nargs='+')

    input_files = terminal_parser.get_list_of_input_files(terminal_command)
    output_files = terminal_parser.get_list_of_output_files(terminal_command)

    data_processor = DataProcessor(input_files)
    file_with_min_amount_of_columns = data_processor.get_file_with_min_amount_of_fields()


if __name__ == '__main__':
    main()
