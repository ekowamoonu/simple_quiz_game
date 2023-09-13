class QuizBrain:
    question_number = 0
    score = 0

    def __init__(self,q_bank):
        self.questions_bank = q_bank

    def still_has_questions(self):
        return self.question_number  < len(self.questions_bank)

    def next_question(self):
       current_question = self.questions_bank[self.question_number]
       answer = input(f"Q{self.question_number+1}. {current_question.text} (True/False):")
       self.check_answer(  answer,current_question.answer )
       self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct answer!")
        else:
            print("Psyche! Wrong answer")


