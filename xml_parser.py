# Made by Evan Thompson (903978131) 12/1/2023 12:41 AM
# Edited by Dongwook Kim (903923872) 12/01/2023 6:01 PM

from lxml import etree

from choice_question import ChoiceQuestion
from choice_image_question import ChoiceImageQuestion


class XMLParser:
    def __init__(self):
        self.questions = []

    # Takes in a file_name and returns a list of question objects
    # Also formats all variables inside the question object
    def parse_xml(self, file_name: str):
        tree = etree.parse(file_name)  # Opens the given file as tree
        elem = tree.getroot()
        xml_questions = elem.findall('question')  # Pulls all question xmls

        for xml_question in xml_questions:
            xml_question_image = xml_question.find("questionImage")  # Retrieves image variable
            if xml_question_image is None:  # Checks if image variable exists
                question = ChoiceQuestion()
            else:
                question = ChoiceImageQuestion()
                question.set_image(xml_question_image.get('path'))

            xml_question_text = xml_question.find("questionText")
            question.set_text(fix_text(xml_question_text.text))

            xml_answers = xml_question.findall("answer")  # Retrieves all xml_answers
            for xml_answer in xml_answers:
                xml_correct = xml_answer.get("correct")
                if xml_correct is None:
                    question.add_choice(xml_answer.text, False)
                else:
                    question.add_choice(xml_answer.text, True)
                    question.set_answer(xml_answer.text)

            xml_answer_comments = xml_question.find("answerComments")  # Retrieves comment variable
            question.set_answer_comments(fix_text(xml_answer_comments.text))

            self.questions.append(question)


# Removes all tabs and new line characters from a string
def fix_text(text: str):
    removal_list = ['\t', '\n']
    for c in removal_list:
        text = text.replace(c, '')
    return text
