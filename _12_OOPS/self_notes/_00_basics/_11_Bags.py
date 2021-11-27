class Bag:

    #State
    def __init__(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Bag  " ,self.bname, self.price,self.clr)
b_info=Bag("Safari" , 2600,"Blue+yellow")
b_info.get_info()