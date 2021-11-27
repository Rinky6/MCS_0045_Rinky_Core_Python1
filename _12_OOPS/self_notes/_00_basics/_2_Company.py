class Company:
   #State
    def __init__(self , c_name,c_hq,c_size,c_tbranch):
     self.c_name=c_name
     self.c_hq = c_hq
     self.c_size=c_size
     self.c_tbranch=c_tbranch
 #Behavior
    def get_info(self):
     print("Company information    ", self.c_name, self.c_hq, self.c_size,self.c_tbranch)

c_info=Company("Grab","USA",1001,5)     #obj creation
c_info.get_info()    #calling the method






