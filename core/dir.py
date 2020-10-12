import re

class ifStar:
    dir = 'test (dqdwqwd and qdqwd)'
    def ifHasAstar(self):
        x=re.search("[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)", self.dir)
        if x:
            return True
        return False
    def faindElment(self):
        if self.ifHasAstar():
            print('fqefeqf')

    def validate(self):
        self.ifHasAstar()
        self.faindElment()

class manageDir:
    dir = 'test (dqdwqwd qdqwd)'
    def __init__(self):
        self.ifStar=ifStar()
    def set(self):
        self.runValidate()
    def runValidate(self):
        self.ifStar.validate()

