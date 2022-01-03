daynames = { 'one' : 'Monday' ,  'six' : 'Saturday' ,'three' : 'Wednesday' ,
             'two' : 'Tuesday' , 'five': 'Friday' ,  'seven': 'Sunday' }

class Dictionary:

    def __init__(self,dic):
        self.dict1=dic

    def Sort_value_ascending(self):
        sort=sorted(self.dict1.values())
        return sort

    def Sort_value_descending(self):
        sort=sorted(self.dict1.values(),reverse=True)
        print("Sorted by value in descending : ",sort)
a=Dictionary(daynames)
b=a.Sort_value_ascending()
print(b)
a.Sort_value_descending()