
from Nakhetra import Nakhetra
from datetime import timedelta
from Degree import Degree
from Dasha import Dasha
from mahadasha_config import mahadasha_number_planet_mapping
from mahadasha_config import mahadasha_days
from mahadasha_config import total_vimshottari_mahadasha_seconds
from mahadasha_config import max_level



class vimshottari:
    no_of_dashas_in_one_cycle = 9


    def __init__(self, date_of_birth, moon):
        self.date_of_birth = date_of_birth
        self.moon = moon
        self.total_vimshottari_dasha_seconds = total_vimshottari_mahadasha_seconds
        self.no_of_dashas = self.__class__.no_of_dashas_in_one_cycle
        self.max_level = max_level
        
    @property
    def mahadasha_no_at_birth(self):
        if self.moon.nakhetra.number % self.no_of_dashas == 0:
            return self.no_of_dashas
        else:
            return self.moon.nakhetra.number % self.no_of_dashas
        
    @property
    def dasha_degrees_remaining_fraction(self):
        tot_abs_degree =  Nakhetra.spread * self.moon.nakhetra.number
        moon_abs_degree =  self.moon.rasi.get_abs_degree()
        nakhetra_degree = Nakhetra.spread
        return (tot_abs_degree - moon_abs_degree) / nakhetra_degree
    
    @property
    def dasha_degrees_over_fraction(self):
        return 1 - self.dasha_degrees_remaining_fraction
    
    @property
    def virtual_beginning_of_dasha(self):
        return self.date_of_birth - timedelta(seconds=self.dasha_degrees_over_fraction * self.total_vimshottari_dasha_seconds * mahadasha_days[self.mahadasha_no_at_birth])
        
    def find_dasha_running(self, date):
        self.dasha_at_birth_obj = Dasha(self.mahadasha_no_at_birth, 
                                        self.virtual_beginning_of_dasha)

        self.__find_dasha_running(date, self.dasha_at_birth_obj)
        self.print_dasha_running(self.found_dasha_running)
        
    def __find_dasha_running(self, date, dasha_obj):
        self.found_dasha_running = dasha_obj
        if len(dasha_obj.dasha_sequence) < self.max_level:
            if date > dasha_obj.dasha_ends:
                next_dasha_obj = dasha_obj.get_next_dasha()
                self.__find_dasha_running(date, next_dasha_obj)
            else:
                subdasha = dasha_obj.get_first_subdasha()
                self.__find_dasha_running(date, subdasha)
    
    def print_dasha_running(self, dasha_obj):
        print([mahadasha_number_planet_mapping[dasha_no] for dasha_no in dasha_obj.dasha_sequence])
        