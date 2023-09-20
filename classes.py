class Gains:
    def __init__(self, species, amount, fruit):
        self.species = species #defines the spiecies of the grown Gain
        self.amount = amount #defines the amount of the grown Gain
        self.fruit = fruit #defines wether the grown Gain is a frouit or vegetable
    
    def jamming(self, species, amount):
        self.species = species + " jam"
        self.amount = amount/2
