from abc import ABC
from app.db.models import session
from app.db.models import Producent, Stars, Movies, Series
from core.custum_errors import Error
from pathlib import Path
from core.setings import photo_ext
import os.path
import json
import os

producent_fields_defult = ['country', "baner", "year"]
producent_fields_defult2 = ['country', 'series', "baner", "year"]
series_fields_defults = ["years", "country", "number_of_sezons", "movies", "producent", "baner"]
movies_fields_defults = ["src", "short_stars", "sezon", "year", "country", "short_series"]
stars_fields_defults = ['weight', 'height', 'ethnicity', 'hair_color', 'short_series', 'nationality', 'birth_place',
                        'date_of_birth']
defult_producents_pages = 1
defult_movis = 10
defult_stars = 10
defult_series = 10

class CreateJSONDBLIST:
    Sesion = session
    series_fields = series_fields_defults
    stars_fields = stars_fields_defults
    movies_fields = movies_fields_defults
    producent_fields = producent_fields_defult2

    def base_get(self, Model, atters):

        if hasattr(Model, "__len__"):
            loop_all = Model
        else:
            loop = self.loop(Model)
            loop_all = loop.all()
        array_return = []
        for item_db in loop_all:
            item = self.add_defults(item_db)
            for atter in atters:
                if atter != "series" or atter != "stars" or atter != "top stars" or atter != "src" or atter != "producent":
                    if hasattr(item_db, atter):
                        item[atter] = str(getattr(item_db, self.escepe_string(atter)))
                if atter == "producent":
                    item["producent"] = self.return_producent(item_db)
                if atter == "src":
                    item[atter] = self.escepe_string(getattr(item_db, self.escepe_string(atter)))
                if atter == "series":
                    item["series"] = self.return_series(item_db)
                if atter == "movies":
                    item["movies"] = self.return_movies(item_db)
                if atter == "stars":
                    item["stars"] = self.return_stars(item_db)
                if atter == "top_stars":
                    item["top_stars"] = self.return_top_stars(item_db)
                if atter == "short_series":
                    item["short_series"] = self.return_short_series(item_db)
                if atter == "short_stars":
                    item["short_stars"] = self.return_short_stars(item_db)
            array_return.append(item)
        return array_return

    def return_producent(self, item_db):

        if len(item_db.producent):
            if len(item_db.producent):
                return {
                    "name": item_db.producent[0].show_name,
                    "dir": self.escepe_string(item_db.producent[0].dir),
                    "avatar": item_db.producent[0].avatar,
                }
        return {}

    def return_short_stars(self, item_db):
        array = []
        for item_db in item_db.stars:
            tag_json = {
                "id": item_db.id,
                "name": item_db.name,
                "dir": self.escepe_string(item_db.dir),
                "avatar": item_db.avatar,
            }
            array.append(tag_json)
        return array

    def return_short_series(self, item_db):
        if len(item_db.series):
            return {
                "id": item_db.series[0].id,
                "name": item_db.series[0].show_name,
                "dir": self.escepe_string(item_db.series[0].dir),
                "avatar": item_db.series[0].avatar,
            }
        return {}

    def return_top_stars(self, item):
        top_stars = []
        dir = item.dir + '/stars_counter.JSON'
        if os.path.isfile(dir) is False:
            dir = item.series[0].dir + '/stars_counter.JSON'
        with open(dir) as json_file:
            data = json.load(json_file)
            for star in data:
                if star['Count'] >= 3:
                    top_stars.append(star["StarObj"])
        return top_stars

    def return_stars(self, item):
        return self.base_get(item.stars, self.stars_fields)

    def return_movies(self, item):
        return self.base_get(item.movies, self.movies_fields)

    def return_series(self, item):
        return self.base_get(item.series, self.series_fields)

    def return_tags(self, tags):
        tags_array = []
        for tag in tags:
            tag_json = {
                "id": tag.id,
                "name": tag.name,
            }
            tags_array.append(tag_json)
        return tags_array

    def add_defults(self, item):
        data_JSON = {
            "id": item.id,
            "name": item.name,
            "show_name": item.show_name,
            "dir": self.escepe_string(item.dir),
            "description": item.description,
            "avatar": item.avatar,
            "rating": item.rating,
            "likes": item.likes,
            "views": item.likes,
            "favourite": str(getattr(item, self.escepe_string("favourite"))),
            "tags": self.return_tags(item.tags)
        }
        return data_JSON

    def escepe_string(self, string):
        return string.replace('\\', '/')

    def loop(self, Model):
        return self.Sesion.query(Model)

    def get_producnets(self):
        return self.base_get(Producent, self.producent_fields)

    def get_movies(self):
        return self.base_get(Movies, self.movies_fields)

    def get_series(self):
        return self.base_get(Series, self.series_fields)

    def get_stars(self):
        return self.base_get(Stars, self.stars_fields)

    def create(self):
        list = [
            {"OBJ": self.get_producnets(),
             'name': 'OUTPUT/json/producents.JSON', 'js': 'OUTPUT/js/producents.js', 'var_name': 'producents'},
            {"OBJ": self.get_movies(), 'name': 'OUTPUT/json/movies.JSON',
             'js': 'OUTPUT/js/movies.js', 'var_name': 'movies'},
            {"OBJ": self.get_series(),
             'name': 'OUTPUT/json/series.JSON',
             'js': 'OUTPUT/js/series.js', 'var_name': 'series'},
            {"OBJ": self.get_stars(), 'name': 'OUTPUT/json/stars.JSON',
             'js': 'OUTPUT/js/stars.js', 'var_name': 'stars'},
        ]
        if os.path.isdir('OUTPUT') is False:
            os.mkdir('OUTPUT')
            if os.path.isdir('OUTPUT/json') is False:
                os.mkdir('OUTPUT/json')
            if os.path.isdir('OUTPUT/js') is False:
                os.mkdir('OUTPUT/js')

        for el in list:
            if Path(el['name']).is_file() is True:
                os.remove(el['name'])
            f = open(el['name'], "x")
            f.write(json.dumps(el['OBJ']))
            f.close()
            if Path(el['js']).is_file() is True:
                os.remove(el['js'])
            f = open(el['js'], "x")
            string = 'var ' + el['var_name'] + ' = ' + str(el['OBJ'])
            f.write(string)
            f.close()

class AbstratJSONOtpus(ABC):
    input = ""
    Model = None
    fields = []
    CreateJSONDBLISTObj = CreateJSONDBLIST()

    def defult_add(self, Movie):
        data_JSON = {
            "id": Movie["id"],
            "name": Movie["name"],
            "show_name": Movie["show_name"],
            "dir": Movie["dir"],
            "description": Movie["description"],
            "avatar": Movie["avatar"],
            "tags": Movie['tags'],
            "rating": Movie['rating'],
            "likes": Movie['likes'],
            "views": Movie['views'],
        }
        return self.add_fields(data_JSON, Movie)

    def add_fields(self, data_JSON, Movie):
        return data_JSON

    def create(self):
        Error.throw_error_bool("input not exist", self.input != "")
        with open(self.input) as json_file:
            data = json.load(json_file)
            for movie in data:
                if Path(movie["dir"] + '\db.JSON').is_file() is True:
                    os.remove(movie["dir"] + '\db.JSON')
                f = open(movie["dir"] + '\db.JSON', "x")
                f.write(json.dumps(self.defult_add(movie)))
                f.close()

                if Path(movie["dir"] + '\db.js').is_file() is True:
                    os.remove(movie["dir"] + '\db.js')
                f = open(movie["dir"] + '\db.js', "x")
                string = 'var data = ' + str(self.defult_add(movie))
                f.write(string)
                f.close()

    def add_index(self, fields, data_JSON, Movie):
        for el in fields:
            data_JSON[el] = Movie[el]

class GenerateJSONOtputsMovies(AbstratJSONOtpus):
    input = "OUTPUT/json/movies.JSON"
    fields = movies_fields_defults
    Model = Movies

    def add_fields(self, data_JSON, Movie):
        self.add_index(self.fields, data_JSON, Movie)
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['photos'] = self.return_galery(data_JSON)
        data_JSON['series'] = self.CreateJSONDBLISTObj.base_get(data.series, series_fields_defults)
        data_JSON['movies_with_stars'] = self.CreateJSONDBLISTObj.base_get(self.set_movies_with_star(data.stars),
                                                                           movies_fields_defults)
        return data_JSON

    def set_movies_with_star(self, stars):
        movies = []
        for star in stars:
            movies.extend(star.movies)
        return movies

    def return_galery(self, JSON):
        photos = []
        for item in os.listdir(JSON['dir']):
            if item.endswith(photo_ext):
                photos.append({"photo": item, "name": JSON['name']})
        return photos

class GenerateJSONOtputsStars((AbstratJSONOtpus)):
    input = "OUTPUT/json/stars.JSON"
    fields = stars_fields_defults
    Model = Stars

    def add_fields(self, data_JSON, Movie):
        self.add_index(self.fields, data_JSON, Movie)
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['movies'] = self.CreateJSONDBLISTObj.base_get(data.movies, movies_fields_defults)
        data_JSON['photos'] = self.return_galery(data_JSON, Movie)

        return data_JSON

    def return_galery(self, JSON, Movie):
        name = JSON['name']
        photos = []
        dir = os.listdir(JSON['dir'] + '\\photo\DATA')
        for item in dir:
            if item.endswith(photo_ext):
                new_item = JSON['dir'] + '\\photo\DATA\\' + item
                photos.append({"photo": new_item, "name": JSON['name']})

        for movie in JSON['movies']:
            for star in movie['short_stars']:
                if star['name'] == JSON['name']:
                    for item in os.listdir(movie['dir']):
                        if item.endswith(photo_ext):
                            new_item = movie['dir'] + '\\' + item
                            name = movie['short_series']['name'] + ' - ' + movie['name']
                            photos.append({"photo": new_item, "name": name})
        return photos

class GenerateJSONOtputsSeries(AbstratJSONOtpus):
    input = "OUTPUT/json/series.JSON"
    fields = series_fields_defults
    Model = Series

    def add_fields(self, data_JSON, Movie):
        self.add_index(self.fields, data_JSON, Movie)
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['movies'] = self.CreateJSONDBLISTObj.base_get(data.movies, movies_fields_defults)
        data_JSON['stars'] = self.CreateJSONDBLISTObj.return_top_stars(data)
        data_JSON['photos'] = self.return_galery(data_JSON, Movie)
        return data_JSON

    def return_galery(self, JSON, Movie):
        photos = []
        for item in os.listdir(JSON['dir'] + '\\photo\DATA'):
            new_item = JSON['dir'] + '\\photo\DATA\\' + item
            photos.append({"photo": new_item, "name": JSON['name']})

        for movie in JSON['movies']:
            for item in os.listdir(movie['dir']):
                new_item = movie['dir'] + '\\' + item
                name = JSON['name'] + ' - ' + movie['name']
                if item.endswith(photo_ext):
                    photos.append({"photo": new_item, "name": name})
        return photos

class GenerateJSONOtputsProducent(AbstratJSONOtpus):
    input = "OUTPUT/json/producents.JSON"
    fields = producent_fields_defult
    Model = Producent

    def return_galery(self, JSON, Movie):
        photos = []
        for item in os.listdir(JSON['dir'] + '\\photo\DATA'):
            new_item = JSON['dir'] + '\\photo\DATA' + '\\' + item
            photos.append({"photo": new_item, "name": JSON['name']})
        for movie in JSON['movies']:
            for dir in os.listdir(movie['dir']):
                new_item = movie['dir'] + '\\' + dir
                name = movie['short_series']['name'] + ' - ' + movie['name']
                if dir.endswith(photo_ext):
                    photos.append({"photo": new_item, "name": name})
        return photos

    def add_movies(self, data):
        movies = [];
        for series in data:
            for Movie in series.movies:
                data_JSON = self.CreateJSONDBLISTObj.add_defults(Movie)
                data_JSON['short_series'] = self.CreateJSONDBLISTObj.return_short_series(Movie)
                data_JSON['short_stars'] = self.CreateJSONDBLISTObj.return_short_stars(Movie)
                movies.append(data_JSON)
        return movies

    def add_fields(self, data_JSON, Movie):
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        self.add_index(self.fields, data_JSON, Movie)
        data_JSON['series'] = self.CreateJSONDBLISTObj.base_get(data.series, self.fields)
        data_JSON['movies'] = self.add_movies(data.series)
        data_JSON['stars'] = self.CreateJSONDBLISTObj.return_top_stars(data)
        data_JSON['photos'] = self.return_galery(data_JSON, Movie)
        return data_JSON
