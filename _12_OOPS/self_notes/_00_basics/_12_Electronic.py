class Electronic:

    #State
    def __init__(self,e_name,e_price):
        self.e_name=e_name
        self.e_price=e_price
 #Behavior
    def get_info(self):
     print("info of about Electronic  " ,self.e_name, self.e_price)
e_info=Electronic("Home Theater" , 17999)
e_info.get_info()