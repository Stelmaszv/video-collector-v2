from app.db.models import session
from app.db.models import Producent, Tags
import json

class CreateJSONDBLIST:
    Sesion = session

    def return_tags(self):
        tags = self.loop(Tags)
        tags_array = []
        for tag in tags.all():
            tag_json = {
                "id": tag.id,
                "name": tag.name
            }
            tags_array.append(tag_json)
        return tags_array

    def loop(self, Model):
        return self.Sesion.query(Model)

    def get_producnets(self):
        producents = []
        loop = self.loop(Producent)
        for item in loop.all():
            item = {
                "id": item.id,
                "name": item.name,
                "avatar": item.avatar,
                "dir": item.dir,
                "country": item.country,
                "description": item.description,
                "tags": self.return_tags()
            }
            producents.append(item)
        return producents

    def get_movies(self):
        return {}

    def get_series(self):
        return {}

    def get_stars(self):
        return {}

    def create(self):
        list = []
        list.append({"producents": self.get_producnets()})
        list.append({"movies": self.get_movies()})
        list.append({"series": self.get_series()})
        list.append({"stars": self.get_stars()})
        f = open('db.JSON', "x")
        f.write(json.dumps(list))
        f.close()
