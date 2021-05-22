from Nakhetra import Nakhetra
from math import ceil
from Rasi import Rasi
from NakhetraPada import NPada

class D9:
    def __init__(self, rasi: Rasi):
        self.rasi = rasi
        self.navamsha_number = None
    
    def get_navamsha(self):
        padas_covered_till_rasi = (self.rasi.number - 1) * 9
        max_degree_pada = NPada.spread
        padas_covered_in_rasi = ceil(self.rasi.degree / max_degree_pada)
        pada_number = padas_covered_till_rasi + padas_covered_in_rasi
        self.navamsha_number = pada_number % 12
        if self.navamsha_number == 0:
            self.navamsha_number = 12