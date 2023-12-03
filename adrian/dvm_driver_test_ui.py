import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

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

        self.next_button = QPushButton("Next Question")
        self.next_button.clicked.connect(self.display_next)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit)

    def display(self):
        if isinstance(self._questions[self._current_question], ChoiceQuestion):
            self._choice_question_ui.setup_ui()
            self._choice_question_ui.retranslate_ui()
            self._questions[self._current_question].display(self._main_window)

        elif isinstance(self._questions[self._current_question], ChoiceImageQuestion):
            self._choice_image_question_ui.update_question()
            self._choice_image_question_ui.retranslate_ui()
            self._questions[self._current_question].display(self._main_window)

        self._main_window.show()
        sys.exit(self._application.exec_())

    def clear(self):
        if isinstance(self._questions[self._current_question], ChoiceQuestion):
            self._questions[self._current_question].clear_layout(self._main_window)
        elif isinstance(self._questions[self._current_question], ChoiceImageQuestion):
            self._questions[self._current_question].clear_layout(self._main_window)

    def display_next(self):
        self.clear()
        self._current_question += 1
        self.display()

    def quit(self):
        self._application.quit()
