print("******animals******")

class Animals: 
    def __init__(self, aname, akinds, alegs): #name, kinds, number of feet of the animal
        self.animalname = aname 
        self.animalkinds = akinds 
        self.animallegs = alegs 
    def print_animalname(self): #printing animals name
        print(self.animalname)
    def print_animalkinds(self): #printing animals kinds
        print(self.animalkinds)
    def print_animallegs(self): #printing animals legs
        print(self.animallegs)
    def print_animalstatus(self):
        print(self.animalname + " is a " + self.animalkinds + " and have " + str(self.animallegs) + " legs.")
animal1 = Animals("Dodo", "Dog", 4)
animal1.print_animalname()
animal1.print_animalkinds()
animal1.print_animallegs()
animal1.print_animalstatus()

print("******animals******")

print("******dogs******")


class Dogs(Animals):
    def __init__(self, dname, dbreeds, dage): #name, breeds, age of the dogs
        self.dogname = dname 
        self.dogbreeds = dbreeds
        self.dogage = dage
    def print_dogname(self):
        print(self.dogname) #printing dog name
    def print_dogbreeds(self):
        print(self.dogbreeds) #printing dog breeds
    def print_dogage(self):
        print(self.dogage) #printing dog age
    def print_dogstatus(self):
        print(self.dogname + " is a " + self.dogbreeds + " and " + str(self.dogage) + " years old.")

dog1 = Dogs("Coco", "Bulldog", 3)
dog1.print_dogname()
dog1.print_dogbreeds()
dog1.print_dogage()
dog1.print_dogstatus()

print("******dogs******")

print("******cats******")


class Cats(Animals):
    def __init__(self, cname, cbreeds, cage): #name, breeds, age of the cats
        self.catname = cname 
        self.catbreeds = cbreeds
        self.catage = cage
    def print_catname(self):
        print(self.catname) #printing cat name
    def print_catbreeds(self):
        print(self.catbreeds) #printing cat breeds
    def print_catage(self):
        print(self.catage) #printing cat age
    def print_catstatus(self):
        print(self.catname + " is a " + self.catbreeds + " and " + str(self.catage) + " years old.")

cat1 = Cats("Bebe", "Tuxedo", 1)
cat1.print_catname()
cat1.print_catbreeds()
cat1.print_catage()
cat1.print_catstatus()

print("******cats******")
