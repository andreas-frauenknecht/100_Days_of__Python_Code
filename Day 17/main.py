from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

my_Quiz = QuizBrain(question_bank)

while(my_Quiz.still_has_questions()):
    my_Quiz.next_question()

print(f"You finished the quiz. Your final score is {my_Quiz.score}/{my_Quiz.question_number}")