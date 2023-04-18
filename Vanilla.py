from Icecream import Icecream

class Vanilla(Icecream):
    def __init__(self, name, expire_date, weight):
        super().__init__(name)
        self._expire_date = expire_date
        self._weight = weight
        

    @property
    def expire_date(self):
        return self._expire_date
    
    @property
    def weight(self):
        return self._weight

 

    @expire_date.setter
    def age(self, new_expire_date):
        self._age = new_expire_date

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight


    def __str__(self) -> str:
        return f"{self.name} {self._expire_date} {self._weight} "
