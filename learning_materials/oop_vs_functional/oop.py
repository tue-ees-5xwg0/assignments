class Animal:
    def __init__(self, name):
        self._name = name  # Encapsulation: Data (name) is encapsulated within the object.

    def speak(self):
        pass  # Abstract method for polymorphism.

    def get_name(self):
        return self._name  # Encapsulation: Getter method to access the name.


class Dog(Animal):  # Inheritance: Dog class inherits from Animal class.
    def speak(self):  # Polymorphism: Method overridden to provide specific behavior for Dog.
        return "Woof!"


class Cat(Animal):  # Inheritance: Cat class inherits from Animal class.
    def speak(self):  # Polymorphism: Method overridden to provide specific behavior for Cat.
        return "Meow!"


dog = Dog("Buddy")  # Creating a Dog object
cat = Cat("Whiskers")  # Creating a Cat object

print(dog.get_name())  # Output: Buddy - Encapsulation: Accessing the name using a getter method.
print(cat.get_name())  # Output: Whiskers - Encapsulation: Accessing the name using a getter method.

print(dog.speak())  # Output: Woof! - Polymorphism: Dog's speak method is called.
print(cat.speak())  # Output: Meow! - Polymorphism: Cat's speak method is called.

