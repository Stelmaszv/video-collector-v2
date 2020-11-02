from core.seader import abstractSeader
from app.db.models import Movies
from app.db.models import session
class movies(abstractSeader):

    model=Movies

    def run(self):
        self.addMovies()

    def addMovies(self):
        self.generateObjects(self.model, 10)
        self.addItems()



