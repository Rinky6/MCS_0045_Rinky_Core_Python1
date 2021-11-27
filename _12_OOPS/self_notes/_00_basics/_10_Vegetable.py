class Vegetable:

    #State
    def __init__(self,vname,vprice,Calories ):
        self.vname=vname
        self.vprice=vprice
        self.Calories=Calories
 #Behavior
    def get_info(self):
     print("info of about vegetable  " ,self.vname, self.vprice,self.Calories)
v_info=Vegetable("Ladies Finger" , 30, 20.5)
v_info.get_info()