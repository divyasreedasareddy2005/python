from student import Student

class Trainer:
    def __init__(self,trainer_id,trainer_name):
        #identity info
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        
        #calculation
        self.total_sessions_taken = 0
        self.payment_for_session = 0
        self.trainer_bonus = 0
        self.final_payment = 0
        
    def trainer_basic_info(self):
        print("=====trainer basic info======")
        print(f"trainer id :{self.trainer_id}")
        print(f"trainer_name :{self.trainer_name}")
        
    #payment
    def total_sessions_cal(self):
        self.total_sessions_taken = int(input("enter num of sessions taken:"))
        basic_pay_for_session = 2000
        self.payment_for_session = self.total_sessions_taken*basic_pay_for_session
        
        print("=====student rating======")
        self.training_bonus = s1.trainer_rating_cal()
        self.final_payment = self.payment_for_session + self.trainer_bonus
        
        print("====trainer final payment======")
        
        print("final payment:",self.final_payment)
