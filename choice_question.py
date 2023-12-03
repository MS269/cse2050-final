# By Dongwook Kim

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

    def display(self, ui):
        super().display(ui)

        ui.radio_button_1.setText(self._choices[0][0])
        ui.radio_button_2.setText(self._choices[1][0])
        ui.radio_button_3.setText(self._choices[2][0])
        ui.radio_button_4.setText(self._choices[3][0])

        ui.label_detail.setText(self._answer_comments)



