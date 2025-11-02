#contract for entities like student ,trainer,admin etc
fromabc import ABC, abstractmethod

class Perosonal(ABC):
    @abstractmethod
    def set_personal_details(self,id,name,age,email,mobile_num):
        pass
    #display personal details like student, trainer, admin etc
    @abstractmethod
    def personal_complete_info(self):
        pass