class Studentt:
    def __init__(self,studentt_id,studentt_name,studentt_age = 0,studentt_email = 0,studentt_phone_num = 0):
        #identity info
        self.studentt_id = studentt_id
        self.studentt_name = studentt_name
        self.studentt_age = studentt_age
        self.studentt_email = studentt_email
        self.studentt_phone_num = studentt_phone_num
        
        #calculation info
        
        self.total_sessions_attended = 0
        self.attendance_credits = 0
        self.performance_credits = 0
        self.total_credits = 0
        self.trainer_rating = 0
    
    #hover like functionaality like name and ids
    
    def studentt_basic_info(self):
        print(f"studentt id : {self.studentt_id}")
        print(f"studentt name :{self.studentt_name}")
        
    #click lioke functionality
    def studentt_complete_info(self):
        print(f"studentt id : {self.studentt_id}")
        print(f"studentt name :{self.studentt_name}")
        print(f"studentt age : {self.studentt_age}")
        print(f"studentt email : {self.studentt_email}")
        print(f"studentt phone num : {self.studentt_phone_num}")
        
        
    #calculation 
    def sessions_credits_cal(self):
       total_sessions_attended = int(input("enter num of sessions attended :"))
       self.total_sessions_attended = total_sessions_attended
       if total_sessions_attended>=30:
          self.attendance_credits+=5
       elif total_sessions_attended >=20:
           self.attendance_credits+=3
       else:
           self.attendance_credits =0
       return self.attendance_credits
   
   #performance 
    def performance_credits_cal(self,score):
        
        if score>=95:
            self.performance_credits +=5
        elif score>=70:
            self.performance_credits +=3
        else:
            self.performance_credits=0
        return self.performance_credits
    
    #acheavement
    def achivement_status(self):
        self.final_credits = self.sessions_credits_cal()+self.performance_credits_cal(100)
        
        if self.final_credits>=10:
            print ("got gold")
        elif self.final_credits>=8:
            print ("got silver")
        else:
            print( "got bronze")
    
    #trainer rating
    def trainerr_rating_cal(self):
        self.trainerr_rating = int(input("enter trainerr rating (1-5):"))
        if self.trainerr_rating>=5:
            return 5000
        else:
            0
        
       
            