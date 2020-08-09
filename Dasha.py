import datetime
from datetime import timedelta
from mahadasha_config import mahadasha_days
class Dasha:
    def __init__(self, dasha_no, 
                 dasha_begins, 
                 prev_dasha_sequence=None):
        self.dasha_no = dasha_no
        self.dasha_begins = dasha_begins
        self.total_period = 120 * 365 + 29 # dasha period calculated from dasha sequence
        if prev_dasha_sequence is not None:
            self._dasha_sequence = prev_dasha_sequence
        else:
            self._dasha_sequence = []
        self.dasha_sequence = self.dasha_no
        
    def get_next_dasha_no(self):
        if (self.dasha_no + 1) % 9  != 0:
            return (self.dasha_no + 1) % 9 
        else:
            return 9
    
    def __calculate_dasha_period(self):
        dasha_period_in_days = self.total_period
        #print(dasha_period_in_days, self.dasha_sequence)
        for dasha_no in self.dasha_sequence:
            dasha_period_in_days *= mahadasha_days[dasha_no]
        return dasha_period_in_days
    
    @property
    def dasha_ends(self):
        return self.dasha_begins + timedelta(days=self.dasha_period)
         
    @property
    def dasha_period(self):
        return self.__calculate_dasha_period()
    
    @property
    def dasha_sequence(self):
        return self._dasha_sequence
    
    @dasha_sequence.setter
    def dasha_sequence(self, value):
        self._dasha_sequence.append(value)
    
    def get_next_dasha(self):
        next_dasha_no = self.get_next_dasha_no()
        next_dasha_begins = self.dasha_ends
        next_dasha = self.__class__(next_dasha_no, 
                                    next_dasha_begins,  
                                    prev_dasha_sequence = self.dasha_sequence[:-1])
        return next_dasha
    
    def get_first_subdasha(self):
        subdasha_no = self.dasha_no
        subdasha_begins = self.dasha_begins
        subdasha = self.__class__(subdasha_no, 
                                  subdasha_begins, 
                                  prev_dasha_sequence = self.dasha_sequence)
        return subdasha