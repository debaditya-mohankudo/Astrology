from Degree import Degree
class Rasi:
    def __init__(self, rasi_number=None, rasi_degree=None):
        self.number = rasi_number
        self.degree = rasi_degree
        
    def from_abs_degree(self, abs_degree):
        self.number = (abs_degree.degree // 30) + 1
        self.degree = abs_degree % Degree(30, 0, 0)
        
    @property
    def abs_degree(self):
        return Degree(self.number * 30 - 30, 0, 0) + self.degree
