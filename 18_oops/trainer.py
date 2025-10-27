#trainer class

from student import Student

class Trainer:
    def __init__(self,trainer_id,trainer_name):
        #identity info
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        #calculate info
        self.total_sessions_taken = 0
        self.payment_for_session = 0
        self.trainer_bonus = 0
        self.total_payment =0

    #trainer info
    def trainer_info(self):
        print("====trainer info =====")
        print(f"trainer id:{self.trainer_id}")
        print(f"trainer name:{self.trainer_name}")
    #payment calculation
    def sessions_payment_cal(self,s1):
        self.total_sessions_taken = int(input("entetr total sessions taken:"))
        basic_pay_for_session = 2000
        self.payment_for_session = self.total_sessions_taken *basic_pay_for_session
        
        #get student rating
        #s1 = student()

        print("=====student rating=====")
        self.training_bonus = s1.trainer_rating_cal()
        self.total_payment = self.payment_for_session + self.training_bonus
        print("=====total payment=====")
        print(f"total payment : {self.total_payment}")


    
        


