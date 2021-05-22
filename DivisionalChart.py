from math import ceil
from Rasi import Rasi
from NakhetraPada import NPada

class DivisionalChart:
    

    def __init__(self, rasi: Rasi):
        self.rasi = rasi
        self.divisional_chart_no = None
    
    
    def get_rasi_in_divisional_chart(self):
        padas_covered_till_rasi = (self.rasi.number - 1) * self.divisional_chart_no
        max_degree_pada = NPada.spread
        padas_covered_in_rasi = ceil(self.rasi.degree / max_degree_pada)
        pada_number = padas_covered_till_rasi + padas_covered_in_rasi
        rasi_no_in_divisional_chart = pada_number % Rasi.total_no_rasi
        if rasi_no_in_divisional_chart == 0:
            rasi_no_in_divisional_chart = Rasi.total_no_rasi
        return rasi_no_in_divisional_chart