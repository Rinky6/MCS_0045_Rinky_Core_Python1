class Lappi:

    #State
    def __init__(self,l_bname,l_mno,l_price,l_clr):
        self.l_bname=l_bname
        self.l_mno=l_mno
        self.l_price=l_price
        self.l_clr=l_clr
 #Behavior
    def get_info(self):
     print("info of about Laptop  " ,self.l_bname,self.l_mno, self.l_price,self.l_clr)
l_info=Lappi("HP","HP4511BH00" , 65000,"Black")
l_info.get_info()