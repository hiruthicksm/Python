
class QuizBrain():
    def __init__(self,q_list):
        self.question_number=0
        self.score = 0
        self.question_list=q_list

    def still_has_question(self):
        return self.question_number<len(self.question_list)
    def next_question(self):
        current_qn=self.question_list[self.question_number]
        self.question_number +=1
        option=input(f"Q.{self.question_number}: {current_qn.text} (TRUE/FALSE)")
        self.check_ans(option,current_qn.answer)

    def check_ans(self,opt,crt):
        if opt.lower()==crt.lower():
            self.score = self.score+1
            print("Your'e right")

        else:
            print("You're wrong!")
        print(f"Your current score is {self.score}/{self.question_number}")




