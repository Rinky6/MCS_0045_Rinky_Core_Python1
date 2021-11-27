class Bottle:

    #State
    def __init__(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Bottle  " ,self.bname, self.price,self.clr)
b_info=Bottle("bkr" , 2600,"white")
b_info.get_info()