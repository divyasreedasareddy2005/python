from student  import Student
from trainer  import Trainer

def main():

    #from hover functionality
    s1 = Student(101,"divya")

    #from click functionality
    s2 = Student(102,"yamini",20,"yamini@gmail.com","8890687789")

    #calling basic student info
    s1.student_basic_info()

    #calling complete student info
    s2.student_complete_info()
    
    #calling calculation functionality
    s1.achivenemt_status()

    #trainer functionality
    t1 = Trainer(101,"ravi")

    #calling basic trainer info
    t1.trainer_info()

    #calling payment functionality
    t1.sessions_payment_cal(s1)

main()