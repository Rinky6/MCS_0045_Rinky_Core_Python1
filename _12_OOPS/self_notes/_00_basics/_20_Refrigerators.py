class Refrigerators:

    # State
    def __init__(self, bname,f_clr, f_price):
        self.bname = bname
        self.f_clr=f_clr
        self.f_price = f_price
    # Behavior
    def get_info(self):

        print("info of about Refrigerators: ",  self.bname, self.f_price,self.f_clr)


f_info = Refrigerators("Samsung", 48999 ,"Goldyred")
f_info.get_info()