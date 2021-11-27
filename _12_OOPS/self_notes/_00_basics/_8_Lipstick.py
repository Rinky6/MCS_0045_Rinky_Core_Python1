class Lipstick:

    #State
    def __init__(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about LIPSTICK " ,self.bname, self.price,self.clr)
lp_info=Lipstick("Estee Lauder" , 3650,"sting")
lp_info.get_info()