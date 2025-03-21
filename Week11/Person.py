class Person:
    #constructor
    def __init__(self, p_name, p_age , p_height):
        print("constructing the person object")
        #__ before name make property private
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop="I am public"


        #getter for name
    @property
    def name(self):
        return self.__name
        
        #setter for name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")

person1 = Person("Mark" , 20 , 6)
#version1
print("The Name of the person object:" + str(person1.name))

person1.name = "Alferd"
print("The Name of the person object:" + str(person1.name))

print("Public "+str(person1.public_prop))
