class Student:

    # State
    def __init__(self, roll_no,sname,sclass):
        self.sname = sname
        self.roll_no=roll_no
        self.sclass = sclass
    # Behavior
    def get_info(self):

        print("info of about Student: ",  self.roll_no, self.sname,self.sclass)

s_info = Student("01", "Rani" ,"IV")
s_info.get_info()