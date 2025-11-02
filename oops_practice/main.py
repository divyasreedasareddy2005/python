from student import Student
from trainer import Trainer

def main():
    #hover functionality
    s1 = Student(101,"divya")
    #click like functionality
    s2 = Student(102,"lucky",20,"lucky@gmail.com",1234567890)
    #
    s1.student_basic_info()
    #
    s2.student_complete_info()
    #
    s1.achivement_status()
    #trainer info
    t1 = Trainer(100,"ravi")
    #
    t1.trainer_basic_info()
    #
    t1.total_sessions_cal()
    
main()
    