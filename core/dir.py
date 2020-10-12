import re


class ifStarAndSeries:
    dir = '[feqfqef] qfqefjqepfjqepfj (fqefqef and qefqefqef)';

    def ifStarAndSeries(self):
        if re.search("\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9\s+]+\s+\([a-zA-Z0-9\s]+\)", self.dir):
            return True
        return False

    def faindElment(self):
        if self.ifStarAndSeries():
            print('has a series and star')

    def validate(self):
        self.faindElment()

class ifHasSeries:
    dir = '[feqfqef] qfqefjqepfjqepfj';
    def ifHasSeries(self):
        if re.search("\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9]+", self.dir):
            return True
        return False
    def faindElment(self):
        if self.ifHasSeries():
            print('has a series')
    def validate(self):
        self.faindElment()

class ifStar:
    dir = 'test (dqdwqwd and qdqwd)'
    def ifHasAStar(self):
        if re.search("[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)", self.dir):
            return True
        return False
    def faindElment(self):
        if self.ifHasAStar():
            print('has a star')

    def validate(self):
        self.faindElment()

class manageDir:
    dir = 'test (dqdwqwd qdqwd)'
    def __init__(self):
        self.ifStar=ifStar()
        self.ifHasSeries = ifHasSeries()
        self.ifStarAndSeries = ifStarAndSeries()
    def set(self):
        self.runValidate()
    def runValidate(self):
        self.ifStar.validate()
        self.ifHasSeries.validate()
        self.ifStarAndSeries.validate()

