
class Planet:
    def __init__(self, planet_name, Rasi, Nakhetra=None):
        self.planet_name = planet_name
        self.rasi = Rasi
        self.nakhetra = self.rasi.to_nakhetra()