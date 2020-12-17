from xml.etree import ElementTree
from parsers.sorting_tools import natural_keys


class XmlFilesParser:
    def __init__(self, filename):
        self._columns = []
        self._filename = filename

    def get_sorted_list_of_columns_header(self):
        columns_header = self._get_list_of_columns_header()
        columns_header.sort(key=natural_keys)
        self._columns = columns_header
        return self._columns

    def _get_list_of_columns_header(self):
        with open(self._filename, 'r') as xml_file:
            tree = ElementTree.parse(xml_file)
            root = tree.getroot()
            for column in root.findall("objects/object"):
                self._columns.append(column.attrib['name'])

        return self._columns

