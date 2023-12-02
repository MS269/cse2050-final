from PyQt5.QtWidgets import QLayout

from choice_question import ChoiceQuestion


class ChoiceImageQuestion(ChoiceQuestion):
    def __init__(self):
        super().__init__()
        self._image: bytes = bytes()

    def set_image(self, image: str):
        # TODO
        pass

    def display(self, layout: QLayout):
        # TODO
        super().display(layout)
