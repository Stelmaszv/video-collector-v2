from core.seader import abstractSeader
from app.db.models import Movies,Stars,Photos,Series
from core.strings import stringManipupations
class movies(abstractSeader):

    model=Movies

    def run(self):
        self.addMovies()

    def addMovies(self):
        self.objects = [
            self.model(
                name="Świat to za mało [1999]",
                src="C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi"
            ),
            self.model(
                name="qe",
                src="C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi"
            ),
            self.model(
                name="qeqe",
                src="C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi"
            ),
            self.model(
                name="fqef",
                src="C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi"
            ),
            self.model(
                name="zvzcv",
                src="C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi"
            ),
            self.model(
                name="vqeqegqegqeg",
                src="C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi"
            ),
        ]
        #self.generateObjects(self.model, 25)
        self.addItems()

class stars(abstractSeader):

    model=Stars

    def run(self):
        pass
        #self.addStar()
        #self.addRelationsList()

    def addRelationsList(self):
        self.getItem(1)
        self.addRelations(self.item.movies, Movies, [1,2,3,4,5,6])
        self.addRelations(self.item.photos, Photos, [1,2,3,4,5,6,7,8])
        self.addRelations(self.item.series, Series, [1,2])

        self.getItem(2)
        self.addRelations(self.item.series, Series, [1,2])

    def addStar(self):
        self.objects=[
            self.model(name="topcia",avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
            self.model(name="test", avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
        ]
        #self.addItems()
        #self.addMovieRelations()

    def addMovieRelations(self):
        self.getItem(1)
        movie = self.series.query(Movies).get(1)
        self.addRelations(movie.stars, Stars, [self.item.id])
        self.getItem(2)
        movie = self.series.query(Movies).get(1)
        self.addRelations(movie.stars, Stars, [self.item.id])


class photos(abstractSeader):

    model = Photos

    def run(self):
        self.addPhotos()

    def addPhotos(self):
        self.objects = [
            self.model(src="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            self.model(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
            self.model(src="C:/Users/DeadlyComputer/Desktop/photo/unnamed.jpg"),
            self.model(src="C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg"),
            self.model(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
            self.model(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
        ]
        self.addItems()

class series(abstractSeader):

    model = Series

    def run(self):
        pass
        #self.addSeries()
        #self.addMoviesToSeries()

    def addSeries(self):
        self.objects = [
            self.model(name="ser1 jdpqi jpqjf qipe jfpiqe ", avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
            self.model(name="ser1", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
            self.model(name="ser1", avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        ]
        self.addItems()

    def addMoviesToSeries(self):
        self.getItem(1)
        self.addRelations(self.item.movies, Movies, [1,2,3])



class initSeader:

    seaders = [photos(),movies(),series(), stars()]

    def initNow(self):
        for item in self.seaders:
            item.run()


