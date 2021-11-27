class Vehicle:

    # State
    def __init__(self, bname,v_type, price, clr):
        self.bname = bname
        self.price = price
        self.clr = clr
        self.v_type=v_type
    # Behavior
    def get_info(self):
        print("info of about vehicles ", self.bname, self.price, self.clr,self.v_type)


c_info = Vehicle("Hundai", "4 wheeler", "Grey", 3500000)
c_info.get_info()