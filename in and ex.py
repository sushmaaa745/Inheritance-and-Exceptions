#Inheritance
class Bird:
    def __init__(self, species, color):
        self.species = species
        self.color = color
    def display_info(self):
        print("Species:", self.species)
        print("Color:", self.color)
    def make_sound(self):
        print(self.species, " making a sound")
class Parrot(Bird):
    def __init__(self, species, color, vocabulary_size):
        super().__init__(species, color)
        self.vocabulary_size = vocabulary_size
    def display_info(self):
        super().display_info()
        print("Vocabulary Size:", self.vocabulary_size, "words")
    def speak(self):
        print("The parrot can say", self.vocabulary_size, "words")
class Eagle(Bird):
    def __init__(self, species, color, flight_altitude):
        super().__init__(species, color)
        self.flight_altitude = flight_altitude
    def display_info(self):
        super().display_info()
        print("Flight Altitude:", self.flight_altitude, "meters")
    def soar(self):
        print("The eagle soars", self.flight_altitude, "meters")
''
#polymorphism and inheritance

class Bird:
  def make_sound(self):
    print("Generic bird sound")
class Parrot(Bird):
  def make_sound(self):
    print("Squawk!")
class Sparrow(Bird):
  def make_sound(self):
    print("Chirp!")
class Macaw(Parrot):  
  pass

#single inheritance

class Bird:
    def __init__(self, species):
        self.species = species
    def make_sound(self):
        print("Generic birdsound")
class Parrot(Bird):
    def make_sound(self):
        print("Squawk!")
        
#multiple inheritance

class Flyer:
    def fly(self):
        print("Flying highhh!")
class Bird:
    def __init__(self, species):
        self.species = species
    def make_sound(self):
        print("Generic bird sound")
class Parrot(Bird, Flyer):
    def make_sound(self):
        print("Squawk!")
        
#multiple inheritance

class Flyer:
    def fly(self):
        print("Flying highh!")
class Bird:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic bird sound")
class Parrot(Bird, Flyer):
    def make_sound(self):
        print("Squawk!")
        
#multilevel inheritance 

class Bird:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic bird sound")
class Parrot(Bird):
    def make_sound(self):
        print("Squawk!")

class Macaw(Parrot):
    def make_sound(self):
        print("Macaw Squawkk!")

#hierarchial inheritance

class Bird:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic bird sound")
class Parrot(Bird):
    def make_sound(self):
        print("Squawk!")
class Sparrow(Bird):
    def make_sound(self):
        print("Chirp!")
        
#hybrid inheritance

class Bird:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic bird sound")
class Flyer:
    def fly(self):
        print("Flying high!")
class Parrot(Bird):
    def make_sound(self):
        print("Squawk!")
class FlyingParrot(Parrot, Flyer):
    pass

#method overriding
class Bird:
    def make_sound(self):
        print("Generic bird sound")
class Parrot(Bird):
    def make_sound(self):
        print("Squawk!")

#using super with __init__
class Bird:
    def __init__(self, species):
        self.species = species
class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color
    def display_info(self):
        print("Species:", self.species)
        print("Color:", self.color)
    
#using super with __str__
class Bird:
    def __init__(self, species):
        self.species = species
    def __str__(self):
        return "Species: " + self.species
class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color
    def __str__(self):
        return super().__str__() + ", Color: " + self.color
    
#try and except
try:
    with open("example.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
    
#else block
try:
    result = 10 / 3
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful. Result:", result)

#final block 
try:
    file = open("filename", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")
    
#zerodivisionerror
try:
    result = 30 / 2
except ZeroDivisionError:
    print("Error: Division by zero")

#index error
try:
    my_list = [1, 2, 3, 4]
    print(my_list[5])
except IndexError:
    print("Error")
    
#keyerror
try:
    my_dict = {"p": 1, "q": 2}
    print(my_dict["r"])
except KeyError:
    print("Error")
    
#value error
try:
    num = int("pqr")
except ValueError:
    print("Error")
    
#type error
try:
    result = "cde" / 2
except TypeError:
    print("Unsupported operation")
    
#filenotfound error
try:
    with open("--filename--", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("not found")
    
#IO error
try:
    with open("--filename--", "w") as file:
        file.write("Hello, world!")
except IOError:
    print("Input/output operation failed")


























