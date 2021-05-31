import json
class SeriesCreator:
    singles_limt=2
    movies_series_limit=3
    none_list=[]
    singles_list=[]
    series_list=[]
    create_list=[]

    def __init__(self, item: object) -> object:
        self.item=item

    def add_if_not_exist(self,array,data):

        stan=False
        for item in array:
            if item.id == data.id:
                stan=True
        if stan is False:
            array.append(data)

    def set_singles(self):
        series = self.item.series
        faind_star_in_movie_array = []

        def faind_star_in_movie(stars):
            for star in stars:
                if star.id == self.item.id:
                    return True
            return False

        def if_movie_on_series(movie,singles_list):
            add=False
            for star in movie.stars:
                if star == self.item:
                    add=True
            return add

        for serie in series:
            for movie in serie.movies:
                if faind_star_in_movie(movie.stars):
                    faind_star_in_movie_array.append({'series':serie,'movie':movie})

        series_array=self.series_order(faind_star_in_movie_array)
        for serie in series_array:
            count_star_in_series = self.cout_star_in_series(serie)

            if count_star_in_series <= self.singles_limt:

                for movie in serie.movies:
                    if if_movie_on_series(movie, self.singles_list):
                        self.add_if_not_exist(self.singles_list,movie)
            else:
                self.add_if_not_exist_series(self.series_list,serie)

    def cout_star_in_series(self,series) -> int:
        counter =1
        for movie in  series.movies:
            for star in movie.stars:
                if star == self.item:
                    counter=counter+1
        return counter

    def add_if_not_exist_series(self,array,data):

        stan=False
        for item in array:
            if item.id == data.id:
                stan=True
        if stan is False:
            array.append(data)

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

    def set_none(self):
        def if_movie_on_series(movie, singles_list):
            stan = True
            for item in singles_list:
                if item.id == movie.id:
                    stan = False
            return stan

        movies=self.item.movies
        for movie in movies:
            if len(movie.series) == 0:
                for star in movie.stars:
                    if if_movie_on_series(movie,self.none_list):
                        self.none_list.append(movie)

    def add_movies_to_series(self, movies_list) -> []:
        movies=[]

        for movie in movies_list:
            for star in movie.stars:
                if star.id == self.item.id:
                    movies.append(movie)

        if len(movies)<=self.singles_limt:
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

    def add_singles_from_series(self, item):
        for movie in item.movies:
            for star in movie.stars:
                if star.name == self.item.name:
                    self.add_if_not_exist(self.singles_list, movie)

    def set_element(self,item,elemnt,defult):
        new_elemnt=defult
        with open(self.item.config) as json_file:
            json_pars = json.load(json_file)
            if "series" in json_pars:
                for el in json_pars['series']:
                    if el['id'] == item.id:
                        if elemnt in el:
                            new_elemnt=el[elemnt]
        return new_elemnt

    def set_avatar(self,item):
        return self.set_element(item,'avatar',item.avatar)

    def add_series(self):
        for item in self.series_list:

            if self.count_items(item.movies)>=self.movies_series_limit:

                el = {
                    'id'    :  item.id,
                    'name'  :  item.name,
                    'star'  :  self.item,
                    'avatar':  self.set_avatar(item),
                    'movies': self.add_movies_to_series(item.movies)
                }
                self.create_list.append(el)

    def if_item_item_list(self,name=False,id=False):
        stan = True
        for item in self.create_list:
            if name:
                if name == item['name']:
                    stan=False
        return stan

    def create(self):
        if len(self.none_list) and self.if_item_item_list('none'):
            none = {
                'id'     : 0,
                'star'   : self.item,
                'name'   : 'none',
                'avatar' : self.item.none,
                'movies' : self.none_list
            }
            self.create_list.append(none)

        if len(self.singles_list) and self.if_item_item_list('singles'):
            singles = {
                'id': 0,
                'name'   : 'singles',
                'star'   : self.item.name,
                'avatar' : self.item.singles,
                'movies' : self.singles_list
            }
            self.create_list.append(singles)
        self.add_series()

    def reset_series(self):
        self.create_list = []
        self.none_list=[]
        self.singles_list=[]

    def return_obj(self):
        self.reset_series()
        self.set_none()
        self.set_singles()
        self.create()
        return self.create_list

