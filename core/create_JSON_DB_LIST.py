from app.db.models import session
from app.db.models import Producent, Tags, Stars
import json

class CreateJSONDBLIST:
    Sesion = session

    def base_get(self, Model, atters):
        array_return = []
        loop = self.loop(Model)
        for item_db in loop.all():
            item = self.add_defults(item_db)
            for atter in atters:
                if atter != "series":
                    if hasattr(item_db, atter):
                        item[atter] = getattr(item_db, atter)
                    array_return.append(item)
                if atter == "series":
                    item["series"] = self.return_series(item_db)
        return array_return

    def return_series(self, item):
        series = []
        for item_db in item.series:
            item = self.add_defults(item_db)
            item["years"] = getattr(item_db, "years")
            item["country"] = getattr(item_db, "country")
            item['number_of_sezons'] = getattr(item_db, "number_of_sezons")
            series.append(item)
        return series

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
        return self.base_get(Stars, ['weight', 'height', 'ethnicity', 'hair_color', 'date_of_birth'])

    def create(self):
        list = []
        list.append({"producents": self.get_producnets()})
        list.append({"movies": self.get_movies()})
        list.append({"series": self.get_series()})
        # list.append({"stars": self.get_stars()})
        f = open('db.JSON', "x")
        f.write(json.dumps(list))
        f.close()
