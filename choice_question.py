# By Dongwook Kim

from PyQt5.QtWidgets import QLayout

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

    def display(self, layout: QLayout):
        # TODO
        super().display(layout)
