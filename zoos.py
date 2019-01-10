# Create a tuple named zoo that contains your favorite animals.
zoo = ("Dog", "Tiger", "Panda", "Giraffe")

# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("Tiger"))

# Determine if an animal is in your tuple by using value in tuple.
panda_check = "Panda" in zoo
print(panda_check)
fish_check = "Fish" in zoo
print(fish_check)

# Create a variable for each of the animals in your tuple with this cool feature of Python.
(Dog, Tiger, Panda, Giraffe) = zoo
print(Dog)
print(Panda)

# Convert your tuple into a list.
my_zoo = list(zoo)
print(my_zoo)

# Use extend() to add three more animals to your zoo.
my_zoo.extend(["Fish", "Bear", "Python"])
print(my_zoo)

# Convert the list back into a tuple.
zoo = tuple(my_zoo)