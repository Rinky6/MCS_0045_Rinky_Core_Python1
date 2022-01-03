
Product_list = {'P 01': 'DBMS', 'P 02': 'OS',
                'P 0 3 ': 'Soft Computing'}


class A:

    def __init__(self,dictionary):
        self.dict1=dictionary

    def remove_spaces(self):
        self.dict1 = {x.replace(" ",''): y
                        for x, y in self.dict1.items()}


        print(" New dictionary : ", self.dict1)



a=A(Product_list)
a.remove_spaces()
