
from abc import ABC,abstractmethod
class Musician:
    def __init__(self, name):
        self.name = name

    
class Guitarist(Musician):
     def __init__(self,name):
        super().__init__(name)


     def __str__(self):
        return f'My name is {self.name} and I play guitar'
     
     def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
     
     def get_instrument(self):
         return f'guitar'
     
     def play_solo(self):
        return 'face melting guitar solo'
     

class Drummer(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f'My name is {self.name} and I play drums'
     
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
         return 'drums'
    
    def play_solo(self):
        return 'rattle boom crash'
        

class Bassist(Musician):
     
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f'My name is {self.name} and I play bass'
     
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
         return 'bass'
    
    
    def play_solo(self):
        return 'bom bom buh bom'
    



    


class Band():
    instances =[]

    def __init__(self, name, members):
        self.members = members
        self.name = name
        Band.instances.append(self)

    def __str__(self):
        return f'{self.name} {self.members}'
    
    def __repr__(self):
        return f'{self.name} {self.members}'
    
    def play_solos(self):
        return ["face melting guitar solo" ,"bom bom buh bom","rattle boom crash"]
    
    @classmethod
    def to_list(cls):
    
        return cls.instances
    
   





