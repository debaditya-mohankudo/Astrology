from DivisionalChart import DivisionalChart
from math import ceil
from Rasi import Rasi
from NakhetraPada import NPada

class D9(DivisionalChart):
    divisional_chart_no = 9

    def __init__(self, rasi: Rasi):
        super().__init__(rasi)
        self.divisional_chart_no = 9

