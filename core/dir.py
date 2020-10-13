import re

class abstratValid:

    def __init__(self,dir):
        self.dir=dir

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

    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9\s+]+\s+\([a-zA-Z0-9\s]+\)";

    def onValidPass(self):
        print('has a series and star')
        return  True


class ifHasSeries(abstratValid):

    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9]+";

    def onValidPass(self):
        print('has a series')
        return True

class ifStar(abstratValid):

    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";

    def onValidPass(self):
        print('has a star')
        return True

class manageDir:

    def __init__(self,dir):
        self.ifStar= ifStar(dir)
        self.ifHasSeries = ifHasSeries(dir)
        self.ifStarAndSeries = ifStarAndSeries(dir)

    def set(self):
        self.runValidate()

    def runValidate(self):
        self.ifStar.validate()
        self.ifHasSeries.validate()
        self.ifStarAndSeries.validate()

