"""
Electronic gadget
   Fan                    AC                   laptop               laptop
(electricity)        (electricity)           (electricity)        (electricity)


                                                        (Charge)
  """





class E_Gadget:
    def __init__(self):
        print("Super class")

    def electricity(self):
        print("Need electricity")


class Fan(E_Gadget):
    print("Fan is working")


class AC(E_Gadget):
    print("AC is working")


class Laptop(E_Gadget):
    print("laptop working")

    def charge(self):
        print("put in charge")


class Mobile(Laptop):
    print("mobile is working")

    def charge(self):
        pass


obj = E_Gadget()
obj.electricity()

obj1 = Laptop()
obj1.charge()
obj1.electricity()

obj2 = Mobile()
obj2.electricity()
