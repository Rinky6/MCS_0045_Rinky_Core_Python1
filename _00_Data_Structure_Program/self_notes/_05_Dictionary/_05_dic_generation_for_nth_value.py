class Dictionary:

    def __init__(self):
        self.num=int(input("Enter the input number : "))

    def Dict_creation(self):
        dic={}
        for i in range(1,self.num+1):
            dic[i]=i*i
        print(dic)

dic=Dictionary()
dic.Dict_creation()