from datetime import date

# class Math:

#     def add(x,y):
#         return x+y
    
#     def add_5(num):
#         return num+5
    
#     def add_10(y):
#         return y+10
    
# x=Math.add(5,5)

# z=Math.add_5(x)

# y=Math.add_10(z)

# print(x,z,y)


#converting name and age to private by to underscore = encapulation.
#means no direct acsess
class Student:

    no_student=0

    def __init__(self,name,age,courses='none'):
        self.__name=name
        self.__age=age
        self.__courses=courses

        Student.no_student+=1

    #getter
    def get_name(self):
        return self.__name
    #setter
    def set_name(self,new_name):
        self.__name=new_name

    def describe(self):
        print(f"{self.__name} is {self.__age}")

    def is_old(self,num):
        if self.__age>num:
            print(f"{self.__name}is old")
        else:
            print(f"{self.__name}is not old")

    @classmethod
    def InitBirth(cls,name,birthyear):
        return cls(name,date.today().year-birthyear)


class Pizza:
    def __init__(self,ingred):
        self.ingred=ingred

    @classmethod
    def veg(cls):
        return cls(['tomato,onion,olives'])
    
    @classmethod
    def meet(cls):
        return cls(['turkey,romey,broast'])
    
    def __str__(self):
        return self.ingred
    


class Math:
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def add_5(num):
        return num+5
    
    @staticmethod
    def add_10(y):
        return y+10
    
class Dates:
    def __init__(self,date):
        self.date=date
    def get_date(self):
        return self.date
    @staticmethod
    def todashdate(date):
        return date.replace("-","/")
    
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"{self.name} is {self.age}"

class Man(Person):
    gender="man"
    noman=0
    def __init__(self, name, age,voice):
        super().__init__(name, age)
        self.voice=voice
    def display(self):
        string= super().display()
        return string + f"{self.voice} is {self.gender}"
    
class Women(Person):
    gender="female"
    def __init__(self, name, age,hair):
        super().__init__(name, age)
        self.hair=hair
    def display(self):
        string= super().display()
        return string + self.hair