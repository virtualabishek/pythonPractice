class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check(self):
        if self.age > 18:
            print("You can vote.")
        else:
            print("You can't vote.")

# Create instances of the Animal class
animal1 = Animal("Dog", 45)
animal2 = Animal("Cat", 12)

# Call the check method for both instances
animal1.check()  # This will print "You can vote."
animal2.check()  # This will print "You can't vote."

