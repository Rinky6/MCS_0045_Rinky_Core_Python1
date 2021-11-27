class Tiles:

    #State
    def __init__(self,t_bname,t_price,t_clr):
        self.t_bname=t_bname
        self.t_price=t_price
        self.t_clr=t_clr
 #Behavior
    def get_info(self):
     print("info of about Laptop  " ,self.t_bname, self.t_price,self.t_clr)
t_info=Tiles("somany" , 650,"Fossil Natural")
t_info.get_info()