class ChoiceImageQuestion(ChoiceQuestion):
    def __init__(self, question_text, answer):
        super().__init__(question_text, answer)
        self.image = None

    def set_image(self, img_path):
        with open(img_path, "rb") as f:
            self.image = f.read()

    def display(self, layout):
        super().display(layout)
        if self.image:
            pixmap = QPixmap()
            pixmap.loadFromData(self.image)
            label = QLabel()
            label.setPixmap(pixmap)
            layout.addWidget(label)