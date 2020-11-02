from core.seader import abstractSeader
from app.db.models import Movies,Stars

class movies(abstractSeader):

    model=Movies

    def run(self):
        self.addMovies()

    def addMovies(self):
        self.generateObjects(self.model, 10)
        self.addItems()

class stars(abstractSeader):

    model=Stars

    def run(self):
        self.addStar()
        self.addRelationsMovies()

    def addRelationsMovies(self):
        self.getItem(1)
        self.addRelations(self.item.movies,Movies,[2,4,5,7])
        print(self.item.movies)

    def addStar(self):
        self.objects=[
            self.model(name="topcia")
        ]
        self.addItems()



