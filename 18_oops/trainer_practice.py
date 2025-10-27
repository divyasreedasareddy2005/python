from student_practice import Studentt

class Trainerr:
    def __init__(self,trainerr_id,trainerr_name):
         #identity info
         self.trainerr_id = trainerr_id
         self.trainerr_name = trainerr_name
         #calculation info
         self.total_sessions_taken = 0
         self.payment_for_session = 0
         self.trainerr_bonus = 0
         self.final_amount = 0
    def trainerr_basic_info(self):
        print("=====basic info=====")
        print(f"trainerr id : {self.trainerr_id}")
        print(f"trainerr name : {self.trainerr_name}")
        
    def sessions_payment_cal(self,s1):
        total_sessions_taken = int(input("enter num of sessions taken :"))
        basic_pay_for_session = 2000
        self.total_sessions_taken = self.total_sessions_taken *basic_pay_for_session
        
    def final_payment(self):
        self.trainerr_bonus = s1.trainerr_rating_cal()
        self.final_payment = self.total_sessions_taken +self.trainerr_bonus
        print(f"final payment : {self.final_payment}")
