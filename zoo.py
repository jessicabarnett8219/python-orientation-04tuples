zoo = ("dog", "sloth", "frog", "turtle")
print("zoo", zoo)

print(zoo.index("sloth"))

if "llama" in zoo:
  print("yes there is a llama in the zoo")
else:
  print("no there's no llama")

(dog, sloth, frog, turtle) = zoo
print(dog)

zoo_list = list(zoo)
print("zoo", zoo)
print("zoo_list", zoo_list)

zoo_list.extend(["worm", "tiger", "owl"])

print(zoo_list)

zoo = tuple(zoo_list)
