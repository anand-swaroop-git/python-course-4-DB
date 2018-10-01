# Definitions
# Class - a template​
# Method or Message - A defined capability of a class ​
# Field or attribute- A bit of data in a class​
# Object or Instance - A particular instance of a class

# Terminology: Class​
# Defines the abstract characteristics of a thing (object), including the thing's characteristics (its attributes, fields or properties) and the thing's behaviors (the things it can do, or methods, operations or features). One might say that a class is a blueprint or factory that describes the nature of something. For example, the class Dog would consist of traits shared by all dogs, such as breed and fur color (characteristics), and the ability to bark and sit (behaviors).​

# Terminology: Instance​
# One can have an instance of a class or a particular object. The instance is the actual object created at runtime. In programmer jargon, the Lassie object is an instance of the Dog class. The set of values of the attributes of a particular object is called its state. The object consists of state and the behavior that's defined in the object's class.​

# Terminology: Method​
# An object's abilities. In language, methods are verbs. Lassie, being a Dog, has the ability to bark. So bark() is one of Lassie's methods. She may have other methods as well, for example sit() or eat() or walk() or save_timmy(). Within the program, using a method usually affects only one particular object; all Dogs can bark, but you need only one particular dog to do the barking​

# Making our first Function in Python:
# class PartyAnimal:
#    x = 0
#    name = ''
#    def __init__(self, nam):
#      self.name = nam
#      print(self.name,'constructed')

#    def party(self) :
#      self.x = self.x + 1
#      print(self.name,'party count',self.x)

# stuff = list()
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print (stuff[0])
# print (stuff.__getitem__(0))
# print (list.__getitem__(stuff,0))

#Object-Lifecycle - Constructors and Destructers
# class PartyAnimal:​
#    x = 0​
#    def __init__(self):​
#      print('I am constructed')​
#    def party(self) :​
#      self.x = self.x + 1​
#      print('So far',self.x)​
#    def __del__(self):​
#      print('I am destructed', self.x)​
# an = PartyAnimal()​
# an.party()​
# an.party()​
# an = 42​
# print('an contains',an)​

# The output of above program:
# $ python party4.py ​
# I am constructed​
# So far 1​
# So far 2​
# I am destructed 2​
# an contains 42​

# Multiple Instances:
# Constructors can have additional parameters.  These can be used to set up instance variables for the particular instance of the class (i.e., for the particular object).

# class PartyAnimal:
#    x = 0
#    name = ''
#    def __init__(self, nam):
#      self.name = nam
#      print(self.name,'constructed')

#    def party(self) :
#      self.x = self.x + 1
#      print(self.name,'party count',self.x)

# s = PartyAnimal('Sally')
# j = PartyAnimal('Jim')

# s.party()
# j.party()
# s.party()
# Output of the above program:
# Sally constructed​
# Jim constructed​
# Sally party count 1​
# Jim party count 1​
# Sally party count 2


# Inheritance
# When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class​
# Another form of store and reuse​
# Write once - reuse many times​
# The new class (child) has all the capabilities of the old class (parent) - and then some more​
# ‘Subclasses’ are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.  ​

# class PartyAnimal:​
#    x = 0​
#    name = ""​
#    def __init__(self, nam):​
#      self.name = nam​
#      print(self.name,"constructed")​
#    def party(self) :​
#      self.x = self.x + 1​
#      print(self.name,"party count",self.x)​
# class FootballFan(PartyAnimal):​
#    points = 0​
#    def touchdown(self):​
#       self.points = self.points + 7​
#       self.party()​
#       print(self.name,"points",self.points)​

# Output of the above program- FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more:
# s = PartyAnimal("Sally")​
# s.party()​
# j = FootballFan("Jim")​
# j.party()​
# j.touchdown()​

# Definitions
# Class - a template​
# Attribute – A variable within a class​
# Method - A function within a class​
# Object - A particular instance of a class​
# Constructor – Code that runs when an object is created​
# Inheritance - The ability to extend a class to make a new class.​