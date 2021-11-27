class Cloths:

    # State
    def __init__(self, bname,c_type, price, clr):
        self.bname = bname
        self.price = price
        self.clr = clr
        self.c_type=c_type
    # Behavior
    def get_info(self):
        print("info of about Cloths ", self.bname, self.price, self.clr,self.c_type)


c_info = Cloths("LEVIS", "Party Wear", "Red&Black",8475)
c_info.get_info()