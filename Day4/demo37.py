class Animal:
    def speak(self):
        print("Animal makes Sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()


# Creating objects

#obj = Animal()
#obj.speak()

obj1 = Dog()
obj1.speak()