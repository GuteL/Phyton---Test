#-------------------------------------------------------------------------------------------------------------------------
#Klasse Hund
class dog:
    species = 'German Shepherd'
    def __init__(self, name, age, bark):
        self.name = name
        self.age = age
        self.bark = bark
        
    def __str__(self):
        return f'{self.name} is {self.age} years old and barks like {self.bark}!'
        
#Test Vererbung
class dog2 (dog):
    def __init__(self, type):
        super().__init__('Bonny', 3, 'Wuff')
        self.type = type 
    
    def __str__(self):
        return f'{self.name} is {self.age} years old and barks like {self.bark}!'


#Beispiele
Calida = dog('Calida', 2, 'Wuf')
Bonny = dog2('Löwe')

#Ausgabe
print(f'{Bonny}' + f'{Bonny.type}')
#-------------------------------------------------------------------------------------------------------------------------