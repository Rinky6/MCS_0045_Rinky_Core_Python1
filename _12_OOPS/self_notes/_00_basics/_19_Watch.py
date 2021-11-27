class Watch:

    # State
    def __init__(self, bname,w_type, w_price):
        self.bname = bname
        self.w_type=w_type
        self.w_price = w_price
    # Behavior
    def get_info(self):

        print("info of about Watch ",  self.bname, self.w_price,self.w_type)


w_info = Watch("Fastrack", 3500 ,"Hand Watch")
w_info.get_info()