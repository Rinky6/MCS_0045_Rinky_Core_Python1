class Fan:

    #State
    def __init__(self,f_bname,f_mno,f_price,f_clr):
        self.f_bname=f_bname
        self.f_mno=f_mno
        self.f_price=f_price
        self.f_clr=f_clr
 #Behavior
    def get_info(self):
     price=self.f_price - self.f_price*10/100
     print("info of Fan  " ,self.f_bname,self.f_mno, price,self.f_clr)
f_info=Fan("USHA","1ght" , 2400,"blue")
f_info.get_info()