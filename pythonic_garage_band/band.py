from abc import ABC, abstractmethod

class Band:
    '''
    
    '''
    instances = []

    def __init__ (self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos_list = []
        for member in self.members:
            solos_list.append(member.play_solo())
        return solos_list

    @classmethod
    def to_list(cls):
        return cls.instances

    def __str__(self):
        return "I am __str__"

    def __repr__(self):
        return "I am __repr__"


class Musician(Band):
    '''
    
    '''

    @abstractmethod
    def get_instrument():
        pass

    @abstractmethod
    def play_solo(self):
        pass



class Guitarist(Musician):
    '''
    
    '''
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):
    '''
    
    '''
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    '''
    
    '''
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'


guitarist_01 = Guitarist ('Kurt Cobain')
bassist_01 = Bassist ('Krist Novoselic')
drummer_01 = Drummer ('Dave Grohl')

band_01 = Band('one_band', [guitarist_01, bassist_01, drummer_01])