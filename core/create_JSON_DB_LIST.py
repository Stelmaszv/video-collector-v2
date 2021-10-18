import json


class CreateJSONDBLIST:

    def get_producnets(self):
        return {}

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
