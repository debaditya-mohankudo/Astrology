from Degree import Degree
from NakhetraPada import NPada
from mahadasha_config import nakhetra_number_mapping

class Nakhetra:
    spread = Degree(13, 20, 0)
    
    def __init__(self, nakhetra_number, nakhetra_pada_number, pada_degree=None):
        self.number = nakhetra_number
        self.pada = NPada(nakhetra_pada_number)
        self.pada_number = self.pada.pada_no
        self.pada_degree = pada_degree
    

    
    def __str__(self):
        return str(nakhetra_number_mapping[self.number]) + ',\nPada Number:::' + str(self.pada_number) + ",\nPada degree:::" + str(self.pada_degree)