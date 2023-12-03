class ChoiceQuestion(Question):
    def __init__(self, question_text, answer):
        super().__init__(question_text, answer)
        self.choices = []
        self.answer_comments = ""

    def add_choice(self, choice, correct):
        self.choices.append((choice, correct))

    def set_answer_comments(self, comments):
        self.answer_comments = comments

    def display(self, layout):
        super().display(layout)
        for choice, correct in self.choices:
            layout.addWidget(QLabel(f"Choice: {choice}, Correct: {correct}"))
        layout.addWidget(QLabel(f"Answer Comments: {self.answer_comments}"))

