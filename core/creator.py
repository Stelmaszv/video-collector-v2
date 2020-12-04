class SeriesCreator:
    none_list=[]
    singles_list=[]
    series_list=[]
    create_list=[]

    def __init__(self,item):
        self.item=item

    def set_singles(self):
        series= self.item.series
        faind_star_in_movie=[]
        for serie in series:
            for movie in serie.movies:
                if self.faind_star_in_movie(movie.stars):
                    faind_star_in_movie.append({'series':serie,'movie':movie})


        series_array=self.series_order(faind_star_in_movie)
        for serie in series_array:
            if len(serie.movies) < 3:
                for movie in serie.movies:
                    self.singles_list.append(movie)
            else:
                self.series_list.append(serie)

    def series_order(self,series):
        series_array=[]

        def series_item_item_in_array(id):
            stan=True
            for item in series_array:
                if item.id==id:
                    stan=False
            return stan

        for item in series:
            if series_item_item_in_array(item['series'].id):
                series_array.append(item['series'])

        return series_array




    def faind_star_in_movie(self,stars):
        for star in stars:
            if star.id == self.item.id:
                return True
        return False

    def set_none(self):
        movies=self.item.movies
        for movie in movies:
            if len(movie.series) == 0:
                for star in movie.stars:
                    if star.id == self.item.id:
                        self.none_list.append(movie)

    def add_movies_to_series(self, movies_list) -> []:
        movies=[]
        for movie in movies_list:
            for star in movie.stars:
                if star.id == self.item.id:
                    movies.append(movie)

        if len(movies)<5:
            for movie in movies:
                self.singles_list.append(movie)
        return  movies

    def count_items(self, movies_list):
        items = 0
        for movie in movies_list:
            for star in movie.stars:
                if star.id == self.item.id:
                    items=items+1
        return items

    def if_showin_Serie(self, movies_list) ->bool:
        stan=False
        for movie in movies_list:
            for star in movie.stars:
                if star.id == self.item.id:
                    stan=True

        return stan

    def add_singles_from_series(self, movies_list):
        for movie in movies_list:
            self.singles_list.append(movie)

    def add_series(self):
        for item in self.series_list:
            if self.if_showin_Serie(item.movies) and self.count_items(item.movies)>3 :

                el = {
                    'name'  :  item.name,
                    'avatar': item.avatar,
                    'movies': self.add_movies_to_series(item.movies)
                }
                self.create_list.append(el)

            else:

                self.add_singles_from_series(item.movies)


    def create(self):

        if len(self.none_list):
            none = {
                'name'   : 'none',
                'avatar' : 'C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg',
                'movies' : self.none_list
            }
            self.create_list.append(none)

        if len(self.singles_list):
            singles = {
                'name'   : 'singles',
                'avatar' :'C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg',
                'movies': self.singles_list
            }
            self.create_list.append(singles)
        self.add_series()

    def return_obj(self):
        self.set_none()
        self.set_singles()
        self.create()
        return self.create_list

