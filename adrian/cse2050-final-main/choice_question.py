from PyQt5.QtWidgets import QLayout, QFormLayout, QRadioButton
from question import Question


class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices: [(str, bool)] = []
        self._answer_comments: str = ""

    def add_choice(self, choice: str, correct: bool):
        self._choices.append((choice, correct))

    def set_answer_comments(self, comments: str):
        self._answer_comments = comments

    def clear_layout(self, layout: QLayout):
        super().clear_layout(layout)

    def display(self, layout: QLayout):
        super().display(layout)
