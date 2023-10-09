class Gains:
    def __init__(self, species, amount, fruit):
        self.species = species  #defines the spiecies of the grown Gain
        self.amount = amount    #defines the amount of the grown Gain
        if fruit == True:
            self.fruit = "Fruit"      #defines wether the grown Gain is a frouit or vegetable
            return
        self.fruit = "Vegetable"
    
    def info(self):
        print(self.species, self.amount, self.fruit, sep="; ")

    def add(self, amount):      #Add amount to already existing stock
        self.amount = self.amount + amount

    def jamify(self, amount):   #Makes the fruit into a jam if possible and removes amount from self.
        if amount>self.amount/2:
            print("Not enough to make jam!")
            return
        self.amount = self.amount - amount*2
        print("Made ", amount, " kg of jam")
        return Jamm(self.species+" jam", amount)
    
    def val(self):
        return str(self.species) + " " + str(self.amount) + "kg " + str(self.fruit)
    
    def aval(self):
        return str(self.species) + " " + str(self.fruit)
    
class Jamm(Gains):
    def __init__(self, species, amount):
        super().__init__(species, amount, "Jam")
    
    def jamify():               #Removes abitity to jam jam.
        print("You can't jam jam!")
        return



def add(addingTo, addingThis):
    for i in range(len(addingTo)):
        print("Comparing: ", addingTo[i].aval() ," To: ", addingThis.aval())
        if addingTo[i].aval() == addingThis.aval():
            addingTo[i].add(addingThis.amount)
            return addingTo
    addingTo.append(addingThis)
    return addingTo



Gain = []


adding1 = Gains("vax",20,True)
adding2 = Gains("Dog",47,False)
adding3 = Gains("water",69,False)
adding4 = Gains("vax",21,True)

print(type(Gain))
Gain = add(Gain, adding1)
print(type(Gain))
Gain = add(Gain, adding2)
Gain = add(Gain, adding3)
Gain = add(Gain, adding4)

vals = []

for i in range(len(Gain)):
    vals.append(Gain[i].val())

print(vals)
