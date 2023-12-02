from xml_parser import XMLParser
from dvm_driver_test_ui import DVMDriverTestUI


def main():
    xml_parser = XMLParser()
    xml_parser.parse_xml("resources/florida_drivers_test.xml")

    dvm_driver_test_ui = DVMDriverTestUI(xml_parser.questions)
    dvm_driver_test_ui.display()


main()
