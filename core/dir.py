import re

class abstratValid:

    def valid(self):
        if re.search(self.validValue, self.dir):
            return True
        return False

    def onValidPass(self):
        pass

    def faindElment(self):
        if self.valid():
            self.onValidPass()

    def validate(self):
        self.faindElment()

class ifStarAndSeries(abstratValid):

    dir = '[feqfqef] qfqefjqepfjqepfj (fqefqef and qefqefqef)';
    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9\s+]+\s+\([a-zA-Z0-9\s]+\)";

    def onValidPass(self):
        print('has a series and star')


class ifHasSeries(abstratValid):

    dir = '[feqfqef] qfqefjqepfjqepfj';
    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9]+";

    def onValidPass(self):
        print('has a series')

class ifStar(abstratValid):


    dir = 'test (dqdwqwd and qdqwd)';
    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";

    def onValidPass(self):
        print('has a series')

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

