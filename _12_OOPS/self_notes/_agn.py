class User:
    def __init__(self, name , id , dob):
        self.name = name
        self.id = id
        self.dob = dob
        print("Details of User : " , self.name, self.id,self.dob  )


class Employee(User):
      def get_info(self,loc):
          print("Information about ")

