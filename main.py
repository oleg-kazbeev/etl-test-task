import sys

from terminal_parser import TerminalParser
from data_processor import DataProcessor


def main():
    terminal_command = sys.argv[1:]

    terminal_parser = TerminalParser()
    terminal_parser.add_argument('-i', '--input', default=[], nargs='+')
    terminal_parser.add_argument('-o', '--output', default=[], nargs='+')

    input_files = terminal_parser.get_list_of_input_files(terminal_command)
    output_files = terminal_parser.get_list_of_output_files(terminal_command)

    for file in input_files:
        data_processor = DataProcessor(file)

        if data_processor.is_it_csv_file():
            print("It is a csv file")

        if data_processor.is_it_xml_file():
            print("It is a xml file")

        if data_processor.is_it_json_file():
            print("It is a json file")


if __name__ == '__main__':
    main()
