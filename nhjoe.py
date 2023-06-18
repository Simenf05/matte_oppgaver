
from traceback import print_tb


navn = "Erik"

class Person:
    
    def __init__(self, navn, hoyde):
        self.navn = navn
        self.hoyde = hoyde
        
        
simen = Person("simen", 182)

print(simen.navn, simen.hoyde)


"""
def funksjon():
    
    
    navn = "Erik2"
    
    
    print("n")
    

funksjon()

print(navn)

print("n")"""