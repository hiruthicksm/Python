from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:

    qn=i["text"]
    ans=i["answer"]
    question=Question(qn,ans)
    question_bank.append(question)

qz_brn=QuizBrain(question_bank)
while qz_brn.still_has_question():
    qz_brn.next_question()
print("You have completed the quiz!!")
print(f"Your final score is {qz_brn.score}/{qz_brn.question_number}")

