from student import Student
from trainer import Trainer

def main():
    #create a student
    s = Student(101,"divya",21),"divya@gmail.com",8890876543)
    #display student
    
    #calling complete student info
    s.student_complete_info()
    
    #calling calculation functionality
    s.achivenemt_status()

    #trainer functionality
    t = Trainer(101,"ravi",44,"ravi@gmail.com",55679004)

    #calling basic trainer info
    t.trainer_complete_info()

    #calling payment functionality
    t.sessions_payment_cal(s)

main()
