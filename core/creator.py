class seriesCreator:
    noneList=[]
    singlesList=[]
    seriesList=[]
    createList=[]

    def __init__(self,item):
        self.item=item

    def setNone(self):
        movies=self.item.movies
        for movie in movies:
            if len(movie.series) == 0:
                for star in movie.stars:
                    if star.id == self.item.id:
                        self.noneList.append(movie)

    def setSingles(self):
        series= self.item.series
        for serie in series:
            if len(serie.movies) < 6:
                for movie in serie.movies:
                    self.singlesList.append(movie)
            else:
                self.seriesList.append(serie)


    def addMoviesToSeries(self,moviesList) -> []:
        movies=[]
        for movie in moviesList:
            for star in movie.stars:
                if star.id == self.item.id:
                    movies.append(movie)

        if len(movies)<5:
            for movie in movies:
                self.singlesList.append(movie)
        return  movies

    def countItems(self,moviesList):
        items = 0
        for movie in moviesList:
            for star in movie.stars:
                if star.id == self.item.id:
                    items=items+1
        return items

    def ifShowinSerie(self,moviesList) ->bool:
        stan=False
        for movie in moviesList:
            for star in movie.stars:
                if star.id == self.item.id:
                    stan=True

        return stan

    def addSinglesFromSeries(self,moviesList):
        for movie in moviesList:
            self.singlesList.append(movie)

    def addSeries(self):
        for item in self.seriesList:
            if self.ifShowinSerie(item.movies) and self.countItems(item.movies)>5:

                el = {
                    'name': item.name,
                    'avatar': item.avatar,
                    'movies': self.addMoviesToSeries(item.movies)
                }
                self.createList.append(el)

            else:

                self.addSinglesFromSeries(item.movies)


    def create(self):

        if len(self.noneList):
            none = {
                'name'   : 'none',
                'avatar' : 'C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg',
                'movies' : self.noneList
            }
            self.createList.append(none)

        print(self.singlesList)
        if len(self.singlesList):
            singles = {
                'name'   : 'singles',
                'avatar' :'C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg',
                'movies': self.singlesList
            }
            self.createList.append(singles)

        self.addSeries()

    def returnObj(self):
        self.setNone()
        self.setSingles()
        self.create()
        return self.createList