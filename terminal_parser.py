import argparse


class TerminalParser(argparse.ArgumentParser):
    def _get_options_from_command_line(self, cl_content):
        return self.parse_args(cl_content)

    def get_list_of_input_files(self, terminal_command):
        _options = self._get_options_from_command_line(terminal_command)
        return _options.input

    def get_list_of_output_files(self, terminal_command):
        _options = self._get_options_from_command_line(terminal_command)
        return _options.output
