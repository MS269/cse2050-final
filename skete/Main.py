import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFormLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from xml.etree import ElementTree as ET

def main():
    app = QApplication(sys.argv)

    xml_path = 'florida_drivers_test.xml'
    questions = parse_xml(xml_path)

    quiz_app = QuizApp(questions)

    sys.exit(app.exec_())