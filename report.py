import os
from time import sleep


class GenerateAllureReport:

    def __init__(self, case_path, xml_path, report_path):
        self.case_path = case_path
        self.xml_path = xml_path
        self.report_path = report_path

    def run(self):
        generate_xml = "pytest " + self.case_path + " -s -q --alluredir " + self.xml_path
        os.system(generate_xml)
        sleep(10)
        generate_report = "allure generate " + self.xml_path + " -o " + self.report_path + " --clean"
        os.system(generate_report)
        sleep(10)


if __name__ == '__main__':
    GenerateAllureReport(".", "TestResult",
                         "TestResult//Report").run()

