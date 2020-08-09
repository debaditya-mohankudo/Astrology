from Degree import Degree
class Rasi:
    def __init__(self, rasi_number, rasi_degree=Degree(0,0,0)):
        self.number = rasi_number
        self.degree = rasi_degree
        
    @property
    def abs_degree(self):
        return Degree(self.number * 30 - 30, 0, 0) + self.degree