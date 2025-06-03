from quiz_data import question_data
count=0
class Quiz:
    def __init__(self,question,answer,count):
        self.question=question
        self.answer=answer
        self.question_number=count
    def next_question(self):
        s=input(f'Q.{self.question_number}: {self.question}')
        if s.lower()==self.answer.lower():
            print("Correct Answer")
            global count
            count +=1
        else:
            print("Wrong Answer")
        return count       
question_bank=[]
c=1
for question in question_data:
    que=question["question"]
    ans=question["correct_answer"]
    new_q=Quiz(que,ans,c)
    count=new_q.next_question()
    c+=1
print(f"You Scored {count} Marks.")

    


