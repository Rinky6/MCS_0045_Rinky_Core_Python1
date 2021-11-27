class Lensekart:

    # State
    def __init__(self, pid,pname,p_type, p_price):
        self.pid = pid
        self.pname = pname
        self.p_price = p_price
        self.p_type=p_type
    # Behavior
    def get_info(self):

        print("info of about Spectacles ", self.pid, self.pname, self.p_price,self.p_type)


p_info = Lensekart("sw101", "Spectacles","Full frem",2750)
p_info.get_info()