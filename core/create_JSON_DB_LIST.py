from abc import ABC
from app.db.models import session
from app.db.models import Producent, Stars, Movies, Series
from core.custum_errors import Error
from pathlib import Path
import json
import os

class CreateJSONDBLIST:
    Sesion = session
    series_fields = ["years", "country", "number_of_sezons", 'top stars']
    stars_fields = ['weight', 'height', 'ethnicity', 'hair_color', 'date_of_birth']
    movies_fields = ["short_series", "short_stars"]
    producent_fields = ['country', 'series', 'top stars']

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
                if atter != "series" or atter != "stars" or atter != "top stars":
                    if hasattr(item_db, atter):
                        item[atter] = getattr(item_db, atter)
                if atter == "series":
                    item["series"] = self.return_series(item_db)
                if atter == "movies":
                    item["movies"] = self.return_movies(item_db)
                if atter == "stars":
                    item["stars"] = self.return_stars(item_db)
                if atter == "top stars":
                    item["top_stars"] = self.return_top_stars(item_db)
                if atter == "short_series":
                    item["short_series"] = self.return_short_series(item_db)
                if atter == "short_stars":
                    item["short_stars"] = self.return_short_stars(item_db)
            array_return.append(item)
        return array_return

    def return_short_stars(self, item_db):
        array = []
        for item_db in item_db.stars:
            tag_json = {
                "name": item_db.name,
                "dir": item_db.dir,
                "avatar": item_db.avatar,
            }
            array.append(tag_json)
        return array

    def return_short_series(self, item_db):
        return item_db.series[0].show_name

    def return_top_stars(self, item):
        top_stars = []
        with open(item.dir + '/stars_counter.JSON') as json_file:
            data = json.load(json_file)
            for star in data:
                if star['Count'] > 3:
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
            "dir": item.dir,
            "description": item.description,
            "avatar": item.avatar,
            "tags": self.return_tags(item.tags)
        }
        return data_JSON

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
            {"OBJ": self.get_producnets(), 'name': 'JSONOUTPUT/producents.JSON'},
            {"OBJ": self.get_movies(), 'name': 'JSONOUTPUT/movies.JSON'},
            {"OBJ": self.get_series(), 'name': 'JSONOUTPUT/series.JSON'},
            {"OBJ": self.get_stars(), 'name': 'JSONOUTPUT/stars.JSON'}
        ]
        os.mkdir('JSONOUTPUT')
        for el in list:
            if Path(el['name']).is_file() is True:
                os.remove(el['name'])
            f = open(el['name'], "x")
            f.write(json.dumps(el['OBJ']))
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
            "tags": Movie['tags']
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


class GenerateJSONOtputsMovies(AbstratJSONOtpus):
    input = "JSONOUTPUT/movies.JSON"
    fields = []
    Model = Movies


class GenerateJSONOtputsStars((AbstratJSONOtpus)):
    input = "JSONOUTPUT/stars.JSON"
    fields = ["short_series", "short_stars"]
    Model = Stars

    def add_fields(self, data_JSON, Movie):
        data_JSON['weight'] = Movie['weight']
        data_JSON['height'] = Movie['height']
        data_JSON['ethnicity'] = Movie['ethnicity']
        data_JSON['hair_color'] = Movie['hair_color']
        data_JSON['hair_color'] = Movie['date_of_birth']
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['movies'] = self.CreateJSONDBLISTObj.base_get(data.movies, self.fields)
        return data_JSON
