# By Dongwook Kim

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from choice_question import ChoiceQuestion
from choice_question_ui import ChoiceQuestionUI
from choice_image_question import ChoiceImageQuestion
from choice_image_question_ui import ChoiceImageQuestionUI


class DVMDriverTestUI:
    def __init__(self, questions: [ChoiceQuestion | ChoiceImageQuestion]):
        self._application = QApplication(sys.argv)
        self._main_window = QMainWindow()
        self._choice_question_ui = ChoiceQuestionUI(self._main_window)
        self._choice_image_question_ui = ChoiceImageQuestionUI(self._main_window)

        self._questions = questions
        self._total_question = len(questions)
        self._current_question = 0
        self._correct_question = 0

    def display(self):
        self._choice_question_ui.setup_ui()
        self._choice_question_ui.retranslate_ui()

        self._choice_image_question_ui.setup_ui()
        self._choice_image_question_ui.retranslate_ui()

        self.update_ui()

        self._main_window.show()
        sys.exit(self._application.exec_())

    def update_ui(self):
        new_label_info = f"Question {self._current_question + 1} of {self._total_question} | Correct: {self._correct_question}/{self._total_question}"

        if type(self._questions[self._current_question]) is ChoiceQuestion:
            self._choice_question_ui.label_info.setText(new_label_info)
            self._questions[self._current_question].display(self._choice_question_ui)
        elif type(self._questions[self._current_question]) is ChoiceImageQuestion:
            self._choice_image_question_ui.label_info.setText(new_label_info)
            self._questions[self._current_question].display(self._choice_image_question_ui)
