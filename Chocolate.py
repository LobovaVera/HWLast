from Icecream import Icecream

class Chocolate(Icecream):
    def __init__(self, name, expire_date, weight, chocolate_type):
        super().__init__(name)
        self._expire_date = expire_date
        self._weight = weight
        self._chocolate_type = chocolate_type
        

    @property
    def expire_date(self):
        return self._expire_date
    
    @property
    def weight(self):
        return self._weight
    @property
    def chocolate_type(self):
        return self._chocolate_type

 

    @expire_date.setter
    def age(self, new_expire_date):
        self._age = new_expire_date

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight
        
    @chocolate_type.setter
    def chocolate_type(self, new_chocolate_type):
        self._chocolate_type = new_chocolate_type

    def __str__(self) -> str:
        return f"{self.name} {self._expire_date} {self._weight} {self._chocolate_type}"