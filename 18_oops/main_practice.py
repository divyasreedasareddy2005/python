from student_practice import Studentt
from trainer_practice import Trainerr

def main():
    #hover like fiuntionalitis
    s1 = Studentt(101,"divya")
    #click like funtionalitis
    s2 = Studentt(102,"yamini",23,"yamin@gmail.com",8888899994)
    #basic info
    s1.studentt_basic_info()
    #complete info
    s2.studentt_complete_info()
    #achivement status
    s1.achivement_status()
    #trainer info
    t1 = Trainerr(303,"ravi")
    #trainer cal
    t1.trainerr_basic_info()
    #
    t1.sessions_payment_cal(s1)
main()