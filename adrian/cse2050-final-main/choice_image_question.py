from PyQt5.QtWidgets import QLayout, QLabel
from choice_question import ChoiceQuestion


class ChoiceImageQuestion(ChoiceQuestion):
    def __init__(self):
        super().__init__()
        self._image_label = QLabel()
        self._image: bytes = bytes()

    def set_image(self, image: str):
        with open(image, "rb") as img_file:
            self._image = img_file.read()

    def clear_layout(self, layout: QLayout):
        super().clear_layout(layout)

    def display(self, layout: QLayout):
        # TODO
        super().display(layout)
