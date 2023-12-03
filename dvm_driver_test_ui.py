# By Dongwook Kim

import sys
from PyQt5 import QtCore, QtWidgets

from choice_question import ChoiceQuestion
from choice_image_question import ChoiceImageQuestion


class DVMDriverTestUI:
    def __init__(self, questions: list):
        self._questions = questions
        self._total_question = len(questions)
        self._current_question = 0
        self._correct_question = 0

        self._application = QtWidgets.QApplication(sys.argv)
        self._main_window = QtWidgets.QMainWindow()
        self._central_widget = QtWidgets.QWidget(self._main_window)

        self.widget = QtWidgets.QWidget(self._central_widget)
        self.grid_layout_main = QtWidgets.QGridLayout(self.widget)

        self.label_image = QtWidgets.QLabel(self.widget)
        self.label_text = QtWidgets.QLabel(self.widget)

        self.form_layout_answers = QtWidgets.QFormLayout()
        self.radio_button_1 = QtWidgets.QRadioButton(self.widget)
        self.radio_button_2 = QtWidgets.QRadioButton(self.widget)
        self.radio_button_3 = QtWidgets.QRadioButton(self.widget)
        self.radio_button_4 = QtWidgets.QRadioButton(self.widget)
        self.label_detail = QtWidgets.QLabel(self.widget)

        self.grid_layout_footer = QtWidgets.QGridLayout()
        self.label_info = QtWidgets.QLabel(self.widget)
        self.push_button_next = QtWidgets.QPushButton(self.widget)
        self.push_button_quit = QtWidgets.QPushButton(self.widget)

    def setup_ui(self):
        self._main_window.setObjectName("main_window")
        self._main_window.resize(800, 600)

        self._central_widget.setObjectName("central_widget")

        self.widget.setGeometry(QtCore.QRect(0, 2, 801, 601))
        self.widget.setObjectName("widget")

        self.grid_layout_main.setContentsMargins(12, 12, 12, 24)
        self.grid_layout_main.setObjectName("grid_layout_main")

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(size_policy)
        self.label_image.setObjectName("label_image")
        self.grid_layout_main.addWidget(self.label_image, 0, 0, 1, 1)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_text.sizePolicy().hasHeightForWidth())
        self.label_text.setSizePolicy(size_policy)
        self.label_text.setStyleSheet("font-size:20px;font-weight:600;")
        self.label_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_text.setWordWrap(True)
        self.label_text.setObjectName("label_text")
        self.grid_layout_main.addWidget(self.label_text, 1, 0, 1, 1)

        self.form_layout_answers.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.form_layout_answers.setContentsMargins(12, -1, -1, -1)
        self.form_layout_answers.setObjectName("form_layout_answers")

        self.radio_button_1.setEnabled(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.radio_button_1.sizePolicy().hasHeightForWidth())
        self.radio_button_1.setSizePolicy(size_policy)
        self.radio_button_1.setObjectName("radio_button_1")
        self.form_layout_answers.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radio_button_1)

        self.radio_button_2.setEnabled(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.radio_button_2.sizePolicy().hasHeightForWidth())
        self.radio_button_2.setSizePolicy(size_policy)
        self.radio_button_2.setChecked(True)
        self.radio_button_2.setObjectName("radio_button_2")
        self.form_layout_answers.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radio_button_2)

        self.radio_button_3.setEnabled(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.radio_button_3.sizePolicy().hasHeightForWidth())
        self.radio_button_3.setSizePolicy(size_policy)
        self.radio_button_3.setObjectName("radio_button_3")
        self.form_layout_answers.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radio_button_3)

        self.radio_button_4.setEnabled(True)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.radio_button_4.sizePolicy().hasHeightForWidth())
        self.radio_button_4.setSizePolicy(size_policy)
        self.radio_button_4.setObjectName("radio_button_4")
        self.form_layout_answers.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radio_button_4)

        self.grid_layout_main.addLayout(self.form_layout_answers, 2, 0, 1, 1)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_detail.sizePolicy().hasHeightForWidth())
        self.label_detail.setSizePolicy(size_policy)
        self.label_detail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_detail.setWordWrap(True)
        self.label_detail.setHidden(True)
        self.label_detail.setObjectName("label_detail")
        self.grid_layout_main.addWidget(self.label_detail, 3, 0, 1, 1)

        self.grid_layout_footer.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.grid_layout_footer.setObjectName("grid_layout_footer")

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(size_policy)
        self.label_info.setObjectName("label_info")
        self.grid_layout_footer.addWidget(self.label_info, 0, 0, 1, 1)

        self.push_button_next.setObjectName("push_button_next")
        self.grid_layout_footer.addWidget(self.push_button_next, 0, 2, 1, 1)

        self.push_button_quit.setObjectName("push_button_quit")
        self.grid_layout_footer.addWidget(self.push_button_quit, 0, 3, 1, 1)

        self.grid_layout_main.addLayout(self.grid_layout_footer, 4, 0, 1, 1)

        self._main_window.setCentralWidget(self._central_widget)

        self._main_window.setWindowTitle("DMV Driver\'s Test")
        self.push_button_next.setText("Next Question")
        self.push_button_quit.setText("Quit Quiz")

        self.update_ui()
        QtCore.QMetaObject.connectSlotsByName(self._main_window)

        self._main_window.show()
        sys.exit(self._application.exec_())

    def update_ui(self):
        self.label_info.setText(f"Question {self._current_question + 1} of {self._total_question} | Correct: {self._correct_question}/{self._total_question}")

        if type(self._questions[self._current_question]) is ChoiceQuestion:
            self.label_image.setVisible(False)
            self._questions[self._current_question].display(self)
        elif type(self._questions[self._current_question]) is ChoiceImageQuestion:
            self.label_image.setVisible(True)
            self._questions[self._current_question].display(self)
