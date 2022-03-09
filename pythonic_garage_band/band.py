from abc import ABC, abstractmethod

class Band:
    '''
    A class to creat a band.
    Input: name of the band, members of the band 
    Consteructor: name, list of member(list of objects) , append the creted obeject to a global list
    Methods: play_solos, to_list
    '''
    instances = []

    def __init__ (self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        '''A method to creat a list of solo instrumentel sounds for each member in the band'''
        solos_list = []
        for member in self.members:
            solos_list.append(member.play_solo())
        return solos_list

    @classmethod
    def to_list(cls):
        '''A method to creat a list of objects created by this class (Band)'''
        return cls.instances

    def __str__(self):
        return f"Our band name is {self.name} and we play music"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"


class Musician:
    '''
    A class to create musicians. There are 3 sub-classes inherited from this class (Guitarist, Bassist, Drummer).
    This class force the inherited classes to have 2 methods (get_instrument, play_solo)
    '''

    @abstractmethod
    def get_instrument():
        pass

    @abstractmethod
    def play_solo(self):
        pass



class Guitarist(Musician):
    '''
    A class to creat a guitarist object.
    Input: name of the guitarist
    Constructor: name
    Methods: get_instrument, play_solo
    '''
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        '''A method returns the instrument that the this musician uses'''
        return 'guitar'

    def play_solo(self):
        '''A method returns a mimic the solo playing on this instrument'''
        return 'face melting guitar solo'


class Bassist(Musician):
    '''
    A class to creat a bassist object.
    Input: name of the bassist
    Constructor: name
    Methods: get_instrument, play_solo
    '''
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        '''A method returns the instrument that the this musician uses'''
        return 'bass'

    def play_solo(self):
        '''A method returns a mimic the solo playing on this instrument'''
        return 'bom bom buh bom'


class Drummer(Musician):
    '''
    A class to creat a drummer object.
    Input: name of the drummer
    Constructor: name
    Methods: get_instrument, play_solo
    '''
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        '''A method returns the instrument that the this musician uses'''
        return 'drums'

    def play_solo(self):
        '''A method returns a mimic the solo playing on this instrument'''
        return 'rattle boom crash'


guitarist_01 = Guitarist ('Kurt Cobain')
bassist_01 = Bassist ('Krist Novoselic')
drummer_01 = Drummer ('Dave Grohl')

band_01 = Band('one_band', [guitarist_01, bassist_01, drummer_01])