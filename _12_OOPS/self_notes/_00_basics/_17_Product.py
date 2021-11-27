class Product:

    # State
    def __init__(self, pid,pname,p_type, p_price):
        self.pid = pid
        self.pname = pname
        self.p_price = p_price
        self.p_type=p_type
    # Behavior
    def get_info(self):

        print("info of about product ", self.pid, self.pname, self.p_price,self.p_type)


p_info = Product("p002", "Furniture",30000,"Bed")
p_info.get_info()