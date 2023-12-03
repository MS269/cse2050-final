# Made by Evan Thompson (903978131) 12/1/2023 12:41 AM

# This is a temporary question object class
class question():
   def __init__(self, question, image, answers, correct_index, comments):
      self.question = question
      self.image = image
      self.answers = answers
      self.correct_index = correct_index
      self.comments = comments

   def get_question(self):
      return self.question

   def get_image(self):
      return self.image

   def get_answers(self):
      return self.answers

   def get_correct_index(self):
      return self.correct_index
   
   def get_comments(self):
      return self.comments
