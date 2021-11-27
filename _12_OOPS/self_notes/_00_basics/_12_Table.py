class Table:

    #State
    def __init__(self,bname,price,clr):
        self.bname=bname
        self.price=price
        self.clr=clr
 #Behavior
    def get_info(self):
     print("info of about Table  " ,self.bname, self.price,self.clr)


t_info=Table("Furniture" , 25000,"brown")
t_info.get_info()