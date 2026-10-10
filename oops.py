class Human:
    # Class attributes
    species = "Homosapiens"
    legs = 2
    eyes = 2
    hands = 2

    # Initializer
    def __init__(self, name, gender):
        if gender == "Male" or gender == "Female":
            self.name = name
            self.gender = gender
            self.age = 0
        else:
            raise NameError("Such gender is not supported.")

    # Instance functions
    def say(self, message):
        print("{name}:{message}".format(name=self.name, message=message))

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def sing(self):
        print("Nee ketaa unna kooda Un kaiyil vittu poguren Aasa pola vaazhndhukkoyen po..")


class SuperHuman(Human):        #inheritance
    species = 'SuperHuman'
    def __init__(self, name, hero_alias, age):
        self.name = name
        self.hero_alias = hero_alias
        self.age = age
        super().__init__(self.name, "Male")
        super().setAge(self.age)
        self.powers = []

    def add_power(self, power):
        self.powers.append(power)

    def boast(self):
        for power in self.powers:
            print("I have a power "+  power)



# Create object AFTER the class definition
try:
    h = SuperHuman("Hulk", "Body_builder", 44)
    h.say("I am Batman")
    h.add_power("More strength")
    h.add_power("Muscles grow")
    h.add_power("Body color Green")

    j = Human("saro", "Male")
    j.say("I am ordinary man")
    
    h.boast()
    h.sing()
    print("{} has {} legs ".format(h.hero_alias, h.legs))

except NameError as e:
    print(e)

print(h.age)
h.setAge(40)
print(h.name + " has an age of {}".format(h.getAge()))