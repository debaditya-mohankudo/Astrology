class Degree:
    def __init__(self, degree, minute, second):
        self.degree = degree
        self.minute = minute
        self.second = second
        
    @property
    def degree_in_seconds(self):
        self._degree_in_seconds = self.degree * 3600 + self.minute * 60 + self.second
        return self._degree_in_seconds
    
    def __truediv__(self, x):
        return self.degree_in_seconds / x.degree_in_seconds
    
    def seconds_to_dms(self, total_seconds):
        d = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return self.__class__(d, m, s)
    
    def __sub__(self, x):
        diff = self.degree_in_seconds - x.degree_in_seconds
        return self.seconds_to_dms(diff)
          
    
    def __add__(self, x):
        sum = self.degree_in_seconds + x.degree_in_seconds
        return self.seconds_to_dms(sum)

    def __mul__(self, n):
        sum = self.degree_in_seconds * n
        return self.seconds_to_dms(sum)
    
    def __str__(self):
        return str(self.degree) + ',' + str(self.minute) + ',' +  str(self.second)