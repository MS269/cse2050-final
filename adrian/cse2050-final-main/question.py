from PyQt5.QtWidgets import QLayout, QRadioButton


class Question:
    def __init__(self):
        self._question_text: str = ""
        self._answer: str = ""

    def set_text(self, question_text: str):
        self._question_text = question_text

    def set_answer(self, answer_text: str):
        self._answer = answer_text

    def check_answer(self, answer_text: str):
        return self._answer == answer_text

    def clear_layout(self, layout: QLayout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i).widget
            layout.removeWidget(item)
            item.deleteLater()

    def display(self, layout: QLayout):
        pass
