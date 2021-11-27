class Person:

    # State
    def __init__(self, pname,pheight, pweight):
        self.pname= pname
        self.pheight = pheight
        self.pweight = pweight
    # Behavior
    def get_info(self):

        print("info of about person ", self.pname, self.pheight, self.pweight)


p_info = Person("Rama", "6'8",75)
p_info.get_info()