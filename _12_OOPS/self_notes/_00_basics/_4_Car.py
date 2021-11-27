class Car:

    #State
    def __init__(self,c_name,c_mno,c_price):
        self.c_name=c_name
        self.c_mno=c_mno
        self.c_price=c_price
 #Behavior
    def get_info(self):
     price=self.c_price + self.c_price*10/100
     print("info of Car  " ,self.c_name,self.c_mno, price)
c_info=Car("FORTUNER","1.5MT" , 3400000)
c_info.get_info()