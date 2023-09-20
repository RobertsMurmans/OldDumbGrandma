from re import A


class Gains:
    def __init__(self, species, amount, fruit):
        self.species = species  #defines the spiecies of the grown Gain
        self.amount = amount    #defines the amount of the grown Gain
        self.fruit = fruit      #defines wether the grown Gain is a frouit or vegetable
    
    def info(self):
        print(self.species, self.amount + " kg", self.fruit, sep="; ")

    def add(self, amount):      #Add amount to already existing stock
        self.amout = self.amount + amount

    def jamify(self, amount):   #Makes the fruit into a jam if possible and removes amount from self.
        if amount>self.amount/2:
            print("Not enough to make jam!")
            return
        self.amount = self.amount - amount*2
        print("Made ", amount, " kg of jam")
        return Jamm(self.species+" jam", amount)
    
class Jamm(Gains):
    def __init__(self, species, amount):
        super().__init__(species, amount, "jam")
    
    def jamify():               #Removes abitity to jam jam.
        print("You can't jam jam!")
        return




Apple = Gains("Apple", 12, "fruit")
Apple.info()
AppleJ = Apple.jamify(4)
Apple.info()
AppleJ.info()