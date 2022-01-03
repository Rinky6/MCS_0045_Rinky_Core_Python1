dic={1:23,30:45,4:56,7:23,9:56}

class Dictionary:

    def __init__(self,dictionary):
        self.dic1=dictionary

    def Unique_values(self):
        print("Unique values : ",sorted(set(self.dic1.values())))

unique=Dictionary(dic)
unique.Unique_values()
