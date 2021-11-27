class Employee:

    # State
    def __init__(self, eid,ename,edept, esal):
        self.eid = eid
        self.ename = ename
        self.edept = edept
        self.esal=esal
    # Behavior
    def get_info(self):
        sal=self.esal+self.esal*25/100
        print("info of about employee ", self.eid, self.ename, self.edept,sal)


e_info = Employee("GB101", "Ramanuja", "HR", 30000)
e_info.get_info()