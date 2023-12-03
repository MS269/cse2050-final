# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice_image_question.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap


class ChoiceImageQuestionUI(object):
    def __init__(self, main_window):
        self._main_window = main_window
        self.central_widget = QtWidgets.QWidget(self._main_window)

        self.widget = QtWidgets.QWidget(self.central_widget)
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

        self.central_widget.setObjectName("central_widget")

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
        self.label_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_detail.sizePolicy().hasHeightForWidth())
        self.label_detail.setSizePolicy(size_policy)
        self.label_detail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_detail.setWordWrap(True)
        self.label_detail.setObjectName("label_detail")
        self.grid_layout_main.addWidget(self.label_detail, 3, 0, 1, 1)

        self.grid_layout_main.addLayout(self.form_layout_answers, 2, 0, 1, 1)

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

        self._main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self._main_window)

        self.radio_button_1.toggled.connect(self.on_button_toggled)
        self.radio_button_2.toggled.connect(self.on_button_toggled)
        self.radio_button_3.toggled.connect(self.on_button_toggled)
        self.radio_button_4.toggled.connect(self.on_button_toggled)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self._main_window.setWindowTitle(_translate("main_window", "DMV Driver\'s Test"))
        self.label_image.setText(_translate("main_window", "image"))
        self.label_text.setText(_translate("main_window", "This sign warns you"))
        self.radio_button_1.setText(_translate("main_window", "to move onto the shoulder at high speed."))
        self.radio_button_2.setText(_translate("main_window", "not to leave the pavement."))
        self.radio_button_4.setText(_translate("main_window", "to move onto the shoulder at reduced speed."))
        self.radio_button_3.setText(_translate("main_window", "to increase your following distance to six seconds."))
        self.label_detail.setText(_translate("main_window", "This sign warns you about a soft shoulder. The dirt on the side of the road is soft. Don\'t leave the pavement except in an emergency."))
        self.label_info.setText(_translate("main_window", "Question 1 of 40 | Correct: 0/40"))
        self.push_button_next.setText(_translate("main_window", "Next Question"))
        self.push_button_quit.setText(_translate("main_window", "Quit Quiz"))

    def update_question(self, text, img, choices, detail):
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        self.label_image.setPixmap(pixmap)
        self.label_text.setText(text)

        for i in range(len(choices)):
            if i == 0:
                self.radio_button_1.setText(choices[i])
            if i == 1:
                self.radio_button_2.setText(choices[i])
            if i == 2:
                self.radio_button_3.setText(choices[i])
            if i == 3:
                self.radio_button_4.setText(choices[i])
        self.label_detail.setText(detail)

    def on_button_toggled(self, checked):
        if checked:
            # Uncheck all other radio buttons
            for radio_button in [self.radio_button_1, self.radio_button_2, self.radio_button_3, self.radio_button_4]:
                if radio_button.isChecked():
                    radio_button.setChecked(True)

