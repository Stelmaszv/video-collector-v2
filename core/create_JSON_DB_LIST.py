from app.db.models import session
from app.db.models import Producent, Tags, Stars
import json

class CreateJSONDBLIST:
    Sesion = session
    series_fields = ["years", "country", "number_of_sezons", "movies", "stars"]
    stars_fields = ['weight', 'height', 'ethnicity', 'hair_color', 'date_of_birth']
    movies_fields = []

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
                if atter != "series":
                    if hasattr(item_db, atter):
                        item[atter] = getattr(item_db, atter)
                if atter == "series":
                    item["series"] = self.return_series(item_db)
                if atter == "movies":
                    item["movies"] = self.return_movies(item_db)
                if atter == "stars":
                    item["stars"] = self.return_stars(item_db)
            array_return.append(item)
        return array_return

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
        return self.base_get(Producent, ['country', 'series'])

    def get_movies(self):
        return {}

    def get_series(self):
        return {}

    def get_stars(self):
        return self.base_get(Stars, self.stars_fields)

    def create(self):
        list = []
        list.append({"producents": self.get_producnets()})
        list.append({"movies": self.get_movies()})
        list.append({"series": self.get_series()})
        # list.append({"stars": self.get_stars()})
        f = open('db.JSON', "x")
        f.write(json.dumps(list))
        f.close()
