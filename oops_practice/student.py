class Student:
    institute_name = "edify"
    
    def __init(self,student_id,student_name,student_age,student_email,student_mobile):
        #student identity info
        self.student_id = student_id
        self.student_name = student_name 
        self.student_age = student_age
        self.student_email = student_email
        self.student_mobile = student_mobile
        
        #student calculation info
        self.number_of_sessions_attended = 0
        self.attendance_credits = 0
        self.performance_credits = 0
        self.final_credits = 0
        self.trainer_rating = 0
        
    #hover like functionality
    def student_basic_info(self):
        print("======student_basic_info ======")
        print("student id :",self.student_id)
        print("student name :",self.student_name)
        
    #click like functionality
    def student_complete_info(self):
        print("=====student_complete_info=====")
        print(f"student id:{self.student_id}")
        print(f"student name :{self.student_name}")
        print(f"student age :{self.student_age}")
        print(f"student email:{self.student_email}")
        print(f"student mobile:{self.student_mobile}")
        
    #calculations
    def sessions_attendance_cal(self):
        total_num_of_sessions_attended = int(input("enter num of sessions attended :"))
        self.total_num_of_sessions_attended = total_num_of_sessions_attended
        
        if total_num_of_sessions_attended >=10:
            self.attendance_credits +=5
        elif total_num_of_sessions_attended >= 8:
            self.attendance_credits +=3
        else:
            self.attendance_credits = 0
            return self.attendance_credits
        
    #payment

    def payment_credit_cal(self,score):
        if score >=85:
            self.payment_credits +=5
        elif score >=65:
            self.payment_credits +=3
        else:
            self.payment_credits = 0
            return self.payment_credits
        
    #final credits
    
    def achivement_status(self):
        self.final_credits = self.sessions_attendance_cal()+self.payment_credit_cal(90)
        
        if self.final_credits >=10:
            print("you got gold")
        elif self.final_credits >=8:
            print("you got silver")
        else:
            print("you got bronze")
            
            
    #trainer rating
    def trainer_rating_cal(self):
        self.trainer_rating_cal = int(input("enter trainer rating (1-5):"))

        if self.trainer_rating >= 5:
            return 5000
        else:
            return 0
            
            