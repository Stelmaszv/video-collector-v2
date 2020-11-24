import re
from app.db.models import Stars,Movies,Series
from app.db.models import session
from abc import ABC

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
    model = Stars
    movies = Movies
    objects_stars=[]
    objects_movies=[]
    session= session

    def __init__(self,dir,name,series=False):
        super(ifStar, self).__init__(dir)
        self.series=series
        self.faindStarObj = faindStar(dir)
        self.name=name

    def onValidPass(self):
        self.faindStar()
        return True

    def faindStar(self):
        for star in self.faindStarObj.starArray:
            self.objects_stars.append(
                self.model(
                    name=star,
                    avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"
                )
            )

        self.session.add_all(self.objects_stars)
        self.session.commit()

        self.objects_movies=[
            self.movies(name=self.name)
        ]

        if self.series:
            self.series.movies.append(self.objects_movies[0])
        self.session.add_all(self.objects_movies)
        self.session.commit()

        self.add_stars_to_movie()

    def add_stars_to_movie(self):

        for movie in self.objects_movies:
            for star in self.objects_stars:
                movie.stars.append(star)

class AbstractManageDir(ABC):

    objects_stars=[]
    objects_movies=[]
    objects_series=[]
    session = session

    def set_name(self,name):

        str=''
        stop=False

        for i in range(0,len(name)):

            if name[i] == "." or name[i] == "(":
                stop=True

            if stop is False:
                str=str+name[i]

        return str

    def add_item_to_model(self,Model,array,data):
        array.append(
            Model(
                name=data[0],
                avatar=data[1]
            )
        )
        self.session.add_all(array)
        self.session.commit()

        return array[0]

class ManageDir(AbstractManageDir):

    def __init__(self,dir,base_view,series=False):
        self.series=series
        self.dir = dir
        self.base_view_model=base_view.model
        self.ifStar = ifStar(dir,self.clear_name(dir),series)

    def clear_name(self,dir):
        str=''
        stop=False
        for i in range(0,len(dir)):

            if dir[i] == "(":
                stop=True

            if dir[i] == ".":
                stop=False

            if stop is False:
                str=str+dir[i]

        return str

    def set(self):
        self.runValidate()

    def runValidate(self):
        starstan = self.ifStar.validate()

        if starstan is False:
            name =self.set_name(self.dir)
            self.objects_movies = [
                Movies(name=name)
            ]

            if self.series:
                self.series.movies.append(self.objects_movies[0])

            self.session.add_all(self.objects_movies)
            self.session.commit()

class MovieNormalLoopDir(AbstractManageDir):

    def __init__(self,filenames,obj):
        for files in filenames:
            dir = ManageDir(files, obj, False)
            dir.set()

class MoviesIsStarNameDir(AbstractManageDir):

    def __init__(self,movies):
        index=0
        for movie in movies:
            name=self.set_name(movie)
            self.objects_stars.append(
                Stars(
                    name=name,
                    avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"
                )
            )

            self.objects_movies.append(
                Movies(
                    name=name,
                    stars=[]
                )
            )

            self.objects_movies[index].stars.append(self.objects_stars[index])

            index=index+1

        self.session.add_all(self.objects_stars)
        self.session.commit()
        self.session.add_all(self.objects_movies)
        self.session.commit()

class AddMovieToStarDir(AbstractManageDir):

    def __init__(self,movies,star,base_view):

        add_star= self.add_item_to_model(
            Stars,
            self.objects_stars,
            [star,"C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"]
        )

        index=0
        for files in movies:
            name = self.set_name(files)
            self.objects_movies.append(
                Movies(
                    name=name,
                    stars=[]
                )
            )

            self.objects_movies[index].stars.append(add_star)
            index=index+1

        self.session.add_all(self.objects_movies)
        self.session.commit()

class AddMovieToSeriesDir(AbstractManageDir):

    def __init__(self, movies, series, base_view):

        addseries = self.add_item_to_model(
            Series,
            self.objects_series,
            [series,"C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"]
        )

        for files in movies:
            dir = ManageDir(files, base_view,addseries)
            dir.set()













