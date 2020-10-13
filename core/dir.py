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

class faindSeries:

    str = ''

    def __init__(self,dir):
        self.dir=dir
        self.start = self.dir.find("[")
        self.end = self.dir.find("]")
        self.returnSeriesInString()

    def returnSeriesInString(self):
        for i in range(self.start+1,self.end):
            self.str=self.str+self.dir[i]

class ifHasSeries(abstratValid):

    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9]+";

    def __init__(self,dir):
        super(ifHasSeries, self).__init__(dir)
        self.faindSeriesObj = faindSeries(dir)

    def onValidPass(self):
        self.faindSereis()
        return True

    def faindSereis(self):
        print(self.faindSeriesObj.str)

class faindStar:

    str = ''
    starArray=[]

    def __init__(self,dir):
        self.dir=dir
        self.start = self.dir.find("(")
        self.end = self.dir.find(")")
        self.createStarList()

    def returnStarsInString(self):
        for i in range(self.start+1,self.end):
            self.str=self.str+self.dir[i]
    def createStarList(self):
        self.returnStarsInString()
        self.starArray = self.str.split('and')
        return self.str

class ifStar(abstratValid):

    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";

    def __init__(self,dir):
        super(ifStar, self).__init__(dir)
        self.faindStarObj = faindStar(dir)

    def onValidPass(self):
        self.faindStar()
        return True
    def faindStar(self):
        print(self.faindStarObj.starArray)

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
            pass


