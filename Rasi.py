from Degree import Degree
from Nakhetra import Nakhetra
from math import ceil
from mahadasha_config import nakhetra_number_mapping
class Rasi:
    spread = Degree(30, 0, 0)
    total_no_rasi = 12
    
    def __init__(self, rasi_number=None, rasi_degree=None):
        self.number = rasi_number
        self.degree = rasi_degree
        self.__max_spread = Degree(30, 0, 0)
        
    def from_abs_degree(self, abs_degree):
        self.number = ceil(abs_degree.degree / self.max_spread.degree)
        self.degree = abs_degree % self.max_spread
    
    def get_abs_degree(self):
        return self.__max_spread * (self.number - 1) + self.degree
    
    def to_nakhetra(self):
        padas_covered = (self.number - 1) * 9 + ceil(self.degree / Degree(3, 20, 0))
        nakhetra_number = ceil(padas_covered / 4)
        pada_number = (padas_covered % 4)
        if pada_number == 0:
            pada_number += 4
        pada_degree = self.degree % Degree(3, 20, 0)
        return Nakhetra(nakhetra_number, pada_number, pada_degree)
        
    
    @property
    def abs_degree(self):
        return self.max_spread * (self.number - 1) + self.degree
    
    @property
    def max_spread(self):
        return self.__max_spread
