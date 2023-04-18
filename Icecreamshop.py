from Vanilla import Vanilla
from Chocolate import Chocolate

class Icecreamshop():
    def __init__(self):
        list = []
        self._list = list

    def add_icecream(self, icecream):
        self._list.append(icecream)

    def del_icecream(self, icecream):
        self._list.remove(icecream)

    def print(self):
        for el in self._list:
            print(str(el))