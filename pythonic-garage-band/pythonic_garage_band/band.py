
from abc import abstractmethod


class Musician():
    '''
    a parent class that inherit other classes
    '''
    
    def __init__(self,name,instrument):
        self.name = name
        self.instrument = instrument

    
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    @abstractmethod
    def __repr__(self):
        pass
    
    def get_instrument(self):
        return self.instrument

    @abstractmethod
    def play_solo(self):
        pass



class Guitarist(Musician):
    '''
     a child class inherits from  musician class
    '''
    def __init__(self,name):
        self.name = name
        self.instrument = 'guitar'
   
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


    
    def play_solo(self):
        return f'face melting guitar solo'



class Bassist(Musician):
    '''
     a child class inherits from  musician class
    '''
    def __init__(self,name):
        self.name = name
        self.instrument = 'bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
    
    def play_solo(self):
        return  f'bom bom buh bom'




class Drummer(Musician):
    '''
     a child class inherits from  musician class

    '''
    def __init__(self,name):
        self.name = name
        self.instrument = 'drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    
    def play_solo(self):
        return f'rattle boom crash'



class Band:
    '''
    class Band that creates musicians
    '''
    instances = []
    members = []
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(cls):
        return [member.play_solo() for member in cls.members]

    