class QuizApp(QWidget):
    def __init__(self, questions):
        super().__init__()

        self.questions = questions
        self.current_question_index = 0

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Driver\'s Test Quiz')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.display_current_question()

        self.setLayout(self.layout)
        self.show()

    def display_current_question(self):
        if 0 <= self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            question.display(self.layout)

            if isinstance(question, ChoiceImageQuestion):
                next_button_text = "Next Image Question" if self.current_question_index < len(self.questions) - 1 else "Finish"
            else:
                next_button_text = "Next Question" if self.current_question_index < len(self.questions) - 1 else "Finish"

            next_button = QPushButton(next_button_text, self)
            next_button.clicked.connect(self.next_question)
            self.layout.addWidget(next_button)

    def next_question(self):
        self.current_question_index += 1
        self.layout.itemAt(0).widget().setParent(None)  # Remove the previous question from the layout
        self.display_current_question()


def parse_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    questions = []

    for question_elem in root.findall('.//question'):
        question_text = question_elem.find('questionText').text
        answer_elem = question_elem.find('answer[@correct="true"]')
        answer = answer_elem.text if answer_elem is not None else None

        if 'path' in question_elem.find('questionImage').attrib:
            image_question = ChoiceImageQuestion(question_text, answer)
            image_question.set_image(question_elem.find('questionImage').attrib['path'])
            for choice_elem in question_elem.findall('answer'):
                choice_text = choice_elem.text
                correct = choice_elem.get('correct') == "true"
                image_question.add_choice(choice_text, correct)
            image_question.set_answer_comments(question_elem.find('answerComments').text)
            questions.append(image_question)
        else:
            choice_question = ChoiceQuestion(question_text, answer)
            for choice_elem in question_elem.findall('answer'):
                choice_text = choice_elem.text
                correct = choice_elem.get('correct') == "true"
                choice_question.add_choice(choice_text, correct)
            choice_question.set_answer_comments(question_elem.find('answerComments').text)
            questions.append(choice_question)

    return questions