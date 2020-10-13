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
            return self.onValidPass()
        return  False

    def validate(self):
        return self.faindElment()

class ifHasSeries(abstratValid):

    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9]+";

    def onValidPass(self):
        print('Series - ' + str(self.dir))
        return True

class ifStar(abstratValid):

    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";

    def onValidPass(self):
        print('Star - ' + str(self.dir))
        return True

class manageDir:

    def __init__(self,dir):
        self.dir = dir
        self.ifStar= ifStar(dir)
        self.ifHasSeries = ifHasSeries(dir)

    def set(self):
        self.runValidate()

    def runValidate(self):
        starstan = self.ifStar.validate()
        seriesstan = self.ifHasSeries.validate()

        if starstan is False and seriesstan is False:
            print('normal - '+str(self.dir))


