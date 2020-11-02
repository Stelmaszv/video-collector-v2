from core.seader import abstractSeader
from app.db.models import Movies,Stars,Photos,Series

class movies(abstractSeader):

    model=Movies

    def run(self):
        self.addMovies()

    def addMovies(self):
        self.generateObjects(self.model, 1000)
        self.addItems()

class stars(abstractSeader):

    model=Stars

    def run(self):
        self.addStar()
        self.addRelationsList()

    def addRelationsList(self):
        self.getItem(1)
        self.addRelations(self.item.movies,Movies,[2,4,5,7])
        self.addRelations(self.item.photos,Photos,[1,2,3,4,5,6,7,8])
        self.addRelations(self.item.series, Series, [1, 2,3,4,5,6,7,8,9])

    def addStar(self):
        self.objects=[
            self.model(name="topcia",avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
        ]
        self.addItems()

class photos(abstractSeader):

    model = Photos

    def run(self):
        self.addPhotos()

    def addPhotos(self):
        self.objects = [
            Photos(src="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
            Photos(src="C:/Users/DeadlyComputer/Desktop/photo/unnamed.jpg"),
            Photos(src="C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg"),
            Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
            Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
        ]
        self.addItems()

class series(abstractSeader):

    model = Series

    def run(self):
        self.addSeries()
        self.addMoviesToSeries()

    def addSeries(self):
        self.objects = [
            Series(name="Koty in the city", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="Koty in the city2", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="Koty in the city3", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="4", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="5", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="6", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="7", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="8", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            Series(name="9", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg")
        ]
        self.addItems()

    def addMoviesToSeries(self):
        self.getItem(1)
        self.addRelations(self.item.movies, Movies, [1, 2, 3, 4, 5])
        self.getItem(2)
        self.addRelations(self.item.movies, Movies, [6, 7, 8, 9, 10])
        self.getItem(3)
        self.addRelations(self.item.movies, Movies, [11, 12, 13, 14, 15])
        self.getItem(4)
        self.addRelations(self.item.movies, Movies, [16])
        self.getItem(5)
        self.addRelations(self.item.movies, Movies, [16])
        self.getItem(6)
        self.addRelations(self.item.movies, Movies, [16])
        self.getItem(7)
        self.addRelations(self.item.movies, Movies, [16])
        self.getItem(8)
        self.addRelations(self.item.movies, Movies, [16])
        self.getItem(9)
        self.addRelations(self.item.movies, Movies, [16])



class initSeader:

    seaders = [photos(),movies(),series(), stars()]

    def initNow(self):
        for item in self.seaders:
            item.run()


