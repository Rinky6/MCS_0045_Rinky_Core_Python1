class AC:

    #State
    def __init__(self,ac_brand,ac_mno,ac_price):
        self.ac_brand=ac_brand
        self.ac_mno=ac_mno
        self.ac_price=ac_price
 #Behavior
    def get_info(self):
     print("info of AC  " ,self.ac_brand,self.ac_mno, self.ac_price)
ac_info=AC("Voltas","1.5 Ton" , 34000)
ac_info.get_info()
