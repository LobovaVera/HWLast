from Vanilla import Vanilla
from Chocolate import Chocolate
from Icecreamshop import Icecreamshop

icecream1 = Vanilla("Leningradskoe", 01.24, 200)
icecream2 = Chocolate("Lakomka", 10.23, 220, "chocolate_chips")
icecreamshop = Icecreamshop()
icecreamshop.add_icecream(icecream1)
icecreamshop.add_icecream(icecream2)
icecreamshop.print()
icecreamshop.del_icecream(icecream1)
icecreamshop.print()