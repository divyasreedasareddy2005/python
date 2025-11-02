#student entity
from person import Abstractperson
class Student(Abstractperson):
    #class variables class data common to all students
    institute_name = "edify"
    def __init__(self,student_id = None,student_name = None,student_age = None,student_email = None,student_mobile_num = None):
        #super().__init__(id,name,age,email,mobile_num)
        Abstractperson.__init__(self,id = student_id,name=student_name,age=student_age,email=student_email,mobile_num=student_mobile_num)
    def session_credits_cal(self):
        #local variables
        total_sessions_attended= 0
        attendance_credit = 0
        
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        total_sessions_attended = total_sessions_attended

        if total_sessions_attended >=30:
            attendance_credits+=5
        elif total_sessions_attended >=20:
             attendance_credits +=3
        else:
            self.attendance_credit = 0
        return attendance_credits
    
    def performance_credit_cal(self,score):
        performance_credits = 0
        if score>=85:
           performance_credits +=5
        elif score>=70:
            performance_credits +=3
        else:
            performance_credits = 0
        return performance_credits
    
    def achivenemt_status(self):
        final_credit = self.session_credits_cal() +self.performance_credit_cal(90)
        if  final_credits >=10:
            print("got gold")
        elif final_credit >=8:
            print("got silver") 
        else:
            print("got bronze")

    # give trainer rating
    def trainer_rating_cal(self):
        trainer_rating = int(input("enter trainer rating (1-5): "))
        if trainer_rating >=5:
            return 5000
        else:
            return 0
    
    
    