# Made by Evan Thompson (903978131) 12/1/2023 12:41 AM

from lxml import etree
from question import question

class xml_parser():
   # Takes in a file_name and returns a list of question objects
   # Also formats all all variables inside of the question object
   def get_questions(file_name):
      tree = etree.parse(file_name) # Opens the given file as tree
      elem = tree.getroot()
      xml_questions = elem.findall('question') # Pulls all question xmls
      
      questions = [] # List of question objects
      for xml_question in xml_questions:
         question_text = xml_question.find("questionText").text # Retrieves question variable
         question_text = xml_parser.fix_text(question_text) 
         
         xml_image = xml_question.find("questionImage") # Retrieves image variable
         if xml_image != None: # Checks if image variable exists
            image = xml_image.get('path')
         else:
            image = None
         
         index = 0 # Index of current answer 
         correct_index = -1 # Index of the answer with the correct tag
         answers = [] 
         xml_answer = xml_question.findall("answer") # Retrieves all xml_answers
         for answer in xml_answer:
            answers.append(answer.text)
            correct = answer.get('correct') 
            if correct != None: # Checks if answer is correct
               correct_index = index
            index += 1
         
         comments = xml_question.find("answerComments").text # Retrieves comment variable
         comments = xml_parser.fix_text(comments)

         # This is a temporary question object for easy testing
         question_object = question(question_text, image, answers, correct_index, comments)
         questions.append(question_object)
         # This will need to be changed once question objects are created
      
      return questions # Returns the list of question objects
         
   # Removes all tabs and new line characters from a string
   def fix_text(str):
      removal_list = ['\t', '\n']
      for s in removal_list:
         str = str.replace(s, '')
      return str

