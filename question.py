from PyQt5.QtWidgets import QLayout


class Question:
    def __init__(self):
        self._question_text: str = ""
        self._answer: str = ""

    def set_text(self, question_text: str):
        self._question_text = question_text

    def set_answer(self, answer_text: str):
        self._answer = answer_text

    def check_answer(self, answer_text: str):
        # TODO
        return self._answer == answer_text

    def display(self, layout: QLayout):
        # TODO
        pass
