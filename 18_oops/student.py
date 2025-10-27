#student class

class Student:
    #class varaible -> class data common to all students
    institute_name = "edify"
    #one more constructor for basic info->below approach is overloadingnot allowed in python
    #def __init__(self,student_id,student_name):
    #    #identity info
    #    self.student_id = student_id
    #    self.student_name = student_name
    #instance data specific to each student
    def __init__(self,student_id,student_name,student_age=None,student_email=None,student_mobile_number = None):
        #identity info
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_email = student_email
        self.student_mobile_number = student_mobile_number

        #calculation info
        self.total_sessions_attended = 0
        self.attendance_credits = 0
        self.performance_credits = 0
        self.final_credits =0
        self.trainer_rating = 0

    #however like functionality ->display basic info
    def student_basic_info(self):
        print("==========basic student info ============")
        print(f"student id : {self.student_id}")
        print(f"student name : {self.student_name}")

    #click like functionality -> display complete info
    def student_complete_info(self):
        print("========student complete info=======")
        print(f"student id : {self.student_id}")
        print(f"student name : {self.student_name}")
        print(f"student age : {self.student_age}")
        print(f"student email : {self.student_email}")
        print(f"student mobile number : {self.student_mobile_number}")
        print(f"Student Institute Name: {Student.institute_name}")
    #calculate session attended credits
    def session_credits_cal(self):
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        self.total_sessions_attended = total_sessions_attended

        if total_sessions_attended >=30:
            self.attendance_credits+=5
        elif total_sessions_attended >=20:
             self.attendance_credits +=3
        else:
            self.attendance_credit = 0
        return self.attendance_credits
    
    # calculate performance credit based on score
    def performance_credit_cal(self,score):
        if score>=85:
           self.performance_credits +=5
        elif score>=70:
            self.performance_credits +=3
        else:
            self.performance_credits = 0
        return self.performance_credits
    
    #calculate achievement (based on above two calculations)
    def achivenemt_status(self):
        self.final_credit = self.session_credits_cal() +self.performance_credit_cal(90)
        if self. final_credits >=10:
            print("got gold")
        elif self .final_credit >=8:
            print("got silver") 
        else:
            print("got bronze")

    # give trainer rating
    def trainer_rating_cal(self):
        self.trainer_rating = int(input("enter trainer rating (1-5): "))
        if self. trainer_rating >=5:
            return 5000
        else:
            return 0