# By Dongwook Kim

from PyQt5.QtWidgets import QLayout

from choice_question import ChoiceQuestion


class ChoiceImageQuestion(ChoiceQuestion):
    def __init__(self):
        super().__init__()
        self._image: bytes = bytes()

    def set_image(self, image: str):
        # From taki
        with open(image, 'rb') as img_file:
            self._image = img_file.read()

    def display(self, layout: QLayout):
        # TODO
        super().display(layout)
