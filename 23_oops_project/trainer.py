#trainer entity
from person import Abstractperson
class Trainer(Abstractperson):
    def __init__(self,trainer_id = None,trainer_name = None,trainer_age = None,trainer_email = None,trainer_mobile_num = None):
        #super().__init__(id,name,age,email,mobile_num)
        Abstractperson.__init__(self,id = trainer_id,name=trainer_name,age=trainer_age,email=trainer_email,mobile_num=trainer_mobile_num)
        
    def sessions_payment_cal(self,s1):
        total_sessions_taken = int(input("entetr total sessions taken:"))
        basic_pay_for_session = 2000
        payment_for_session = total_sessions_taken *basic_pay_for_session
        
        #get student rating
        #s1 = student()

        print("=====student rating=====")
        training_bonus = s1.trainer_rating_cal()
        total_payment = payment_for_session + training_bonus
        print("=====total payment=====")
        print(f"total payment : {total_payment}")


    
        


