# By Dongwook Kim


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

    def display(self, ui):
        ui.label_text.setText(self._question_text)
