class Question:
    def __init__(self):
        self.question_text = ""
        self.answer = ""

    def set_text(self, question_text):
        self.question_text = question_text

    def set_answer(self, answer_text):
        self.answer = answer_text

    def check_answer(self, answer_text):
        return self.answer == answer_text

    def display(self, layout):
        # Implementation for displaying the question.
        pass

class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self.choices = []
        self.answer_comments = ""

    def add_choice(self, choice, correct):
        self.choices.append((choice, correct))

    def set_answer_comments(self, comments):
        self.answer_comments = comments

    def display(self, layout):
        # Override to display question with choices.
        super().display(layout)
        # Additional implementation for displaying choices.
        pass

class ChoiceImageQuestion(Question):
    def __init__(self):
        super().__init__()
        self.image = None

    def set_image(self, img_path):
        with open(img_path, 'rb') as img_file:
            self.image = img_file.read()

    def display(self, layout):
        # Override to display question with image.
        super().display(layout)
        # Additional implementation for displaying the image.
        pass

# Example usage:
question1 = ChoiceQuestion()
question1.set_text("What is the capital of France?")
question1.add_choice("Paris", True)
question1.add_choice("Berlin", False)
question1.add_choice("London", False)
question1.set_answer("Paris")

question2 = ChoiceImageQuestion()
question2.set_text("Identify the traffic sign.")
question2.set_image("stop_sign.jpg")

# Delete the example usage when testing main file
