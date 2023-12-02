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
        self._current_question = 0

    def display(self):
        # TODO
        if isinstance(self._questions[self._current_question], ChoiceQuestion):
            self._choice_question_ui.setup_ui()
            self._choice_question_ui.retranslate_ui()
        elif isinstance(self._questions[self._current_question], ChoiceImageQuestion):
            self._choice_image_question_ui.setup_ui()
            self._choice_image_question_ui.retranslate_ui()

        self._main_window.show()
        sys.exit(self._application.exec_())
