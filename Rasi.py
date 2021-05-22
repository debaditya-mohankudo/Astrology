from Degree import Degree
from Nakhetra import Nakhetra
from math import ceil
from mahadasha_config import nakhetra_number_mapping
class Rasi:
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
        
    def to_navamsha(self):
        padas_covered_till_rasi = (self.number - 1) * 9
        max_degree_pada = Degree(30, 0, 0) * (1/9)
        padas_covered_in_rasi = ceil(self.degree / max_degree_pada)
        self.pada_number = padas_covered_till_rasi + padas_covered_in_rasi
        self.navamsha_number = self.pada_number % 12
        if self.navamsha_number == 0:
            self.navamsha_number = 12
        
        ## self.navamsha_nakhetra_pada_degree = self.degree % max_degree_pada
        ## self.padas_covered_in_navamsha_nakhetra = ceil( self.navamsha_nakhetra_pada_degree / (Degree(3, 20, 0) * (1/9)) )
        
        ## self.navamsha_nakhetra_padas = (self.navamsha_number - 1) * 9 + self.padas_covered_in_navamsha_nakhetra
        ## self.navamsha_nakhetra_number = ceil(self.navamsha_nakhetra_padas / 4)
        ## self.navamsha_nakhetra = nakhetra_number_mapping[self.navamsha_nakhetra_number]
    
    @property
    def abs_degree(self):
        return self.max_spread * (self.number - 1) + self.degree
    
    @property
    def max_spread(self):
        return self.__max_spread
