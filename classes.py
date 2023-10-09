class Gains:
    def __init__(self, species, amount, fruit):
        self.species = species          #defines the spiecies of the grown Gain
        self.amount = amount            #defines the amount of the grown Gain
        if fruit == True:
            self.fruit = "Fruit"        #defines wether the grown Gain is a frouit or vegetable
            return
        self.fruit = "Vegetable"
    
    def add(self, amount):              #Add amount to already existing stock
        self.amout = self.amount + amount

    def jamify(self, amount):           #Makes the fruit into a jam if possible and removes amount from self.
        if amount>self.amount/2:
            return "Not enough to make jam!"
        self.amount = self.amount - amount*2
        print("Made ", amount, " kg of jam")
        return Jamm(self.species+" jam", amount)
    
    def val(self):                      #returns values of itself
        return str(self.amount) + "kg of " + str(self.species) + " which is considered a " + str(self.fruit)
    
    def aval(self):                     #same as val, but used to compare 2 objects
        return str(self.species) +  str(self.fruit)
    
class Jamm(Gains):                      #defines the Jam object for use
    def __init__(self, species, amount):
        super().__init__(species, amount, False)
        self.fruit="Jam"                #overwrites its "fruit" value to Jam
    
    def jamify(self, amount):           #Removes abitity to jam jam.
        return "You can't jam jam!"
