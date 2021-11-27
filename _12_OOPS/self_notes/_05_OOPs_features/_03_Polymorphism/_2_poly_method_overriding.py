"""OVERRIDE *
II: All sub classes required  : a. Common  signature and
                                b. unique implementation

                            --> method signature -  common behavior
                            --> method body      -  unique** implementation


   If we write classes without inheritance as below,
                 Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()
	We cant understand common behavior.
	So this will not work out.

    ==> We have to use inheritance mechanism here

								Animal
									eating()

                Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()

Above mechanism is called as Method Overriding **



class Animal:

    def _init_(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Generic Behavior")  # Generic impl.


class Tiger(Animal):

    def _init_(self):
        print("SUB  :: Tiger constructor")

    def eating(self):  # Method overriding
        print("SUB :: Tiger eating in specific manner ")  # specific (our own) impl.


tiger = Tiger()
tiger.eating()


print(".........................................................")


class EarthHuman:

    def _init_(self):
        print('Earth Human')

    def talk(self):
        print("Human talk ........")


class IndiaHuman(EarthHuman):
    def _init_(self):
        print("India Human")

    def talk(self):
        print("India Human talk ........")


class AmericaHuman(EarthHuman):
    def _init_(self):
        print("American Human ")

    def talk(self):
        print("America Human talk ........")


class ChinaHuman(EarthHuman):
    def _init_(self):
        print("China Human ")

    def talk(self):
        print("China Human talk ........")


eh = EarthHuman()
eh.talk()

ih = IndiaHuman()
ih.talk()

ah = AmericaHuman()
ah.talk()

ch = ChinaHuman()
ch.talk()

SC 3: Few sub classes required
                     common behavior +
                     common** implementation   (Tiger,Lion)
      Remaining sub classes required
                     common behavior(method) +
                     unique** implementation  (Cat, Dog)


								Animal
									eating()
                Tiger   		Lion        Cat        Dog
					                          eating()   eating()

"""


class Animal:
    def _init_(self):
        pass
        # print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal Generic eating----")


class Tiger(Animal):
    def _init_(self):
        pass
        # print("SUB  :: Tiger constructor")


class Lion(Animal):
    def _init_(self):
        pass
        # print("SUB  :: Lion constructor")


class Cat(Animal):
    def _init_(self):
        pass
        # print("SUB  :: Cat constructor")

    def eating(self):  # Method overriding
        print("SUB :: Cat eating----")


class Dog(Animal):
    def _init_(self):
        pass
        # print("SUB  :: Dog constructor")

    def eating(self):  # Method overriding
        print("SUB :: Dog eating----")


anim = Animal()
anim.eating()

tiger = Tiger()
tiger.eating()

lion = Lion()
lion.eating()

cat = Cat()
cat.eating()

dog = Dog()
dog.eating()


print(".........................................................")


class EarthHuman:

    def _init_(self):
        print('Earth Human')

    def talk(self):
        print("Human talk language ........")


class IndiaHuman(EarthHuman):
    def _init_(self):
        print("India Human")

    def talk(self):
        print("India Human talk Hindi ........")


class ChinaHuman(EarthHuman):
    def _init_(self):
        print("China Human ")

    def talk(self):
        print("China Human talk Chinese ........")


class AmericaHuman(EarthHuman):
    def _init_(self):
        print("American Human ")

    def talk(self):
        print("America Human talk English........")


class UsaHuman(EarthHuman):
    def _init_(self):
        print("USA Human ")

    def talk(self):
        print("Usa Human talk English........")


eh = EarthHuman()
eh.talk()

ih = IndiaHuman()
ih.talk()

ch = ChinaHuman()
ch.talk()

ah = AmericaHuman()
ah.talk()

uh = UsaHuman()
uh.talk()