from app.db.models import Stars,Series
from app.db.models import session

class BaseModelViewSet:
    pass

class SetPhotoToSetiesView(BaseModelViewSet):

    model = Series()
    session = session

    def __init__(self,data):
        self.data=data

    def add_data(self, data):
        item=0
        for sezon in self.data.sezons:
            sezon.src=data[item]['value']
            item=item+1

class MoviesModelView(BaseModelViewSet):
    model = Series()
    session = session

    def __init__(self,data):
        self.data=data

    def add_data(self, data):

        if data[0]['value']:
            self.data.name = data[0]['value']

        if data[1]['value']:
            self.data.country = data[1]['value']

        if data[2]['value']:
            self.data.year = data[2]['value']

        if data[3]['value']:
            self.data.dir = data[3]['value']

        if data[4]['value']:
            self.data.avatar = data[4]['value']

        self.session.add_all([self.data])
        self.session.commit()

class SeriesModelView(BaseModelViewSet):
    model = Series()
    session = session

    def __init__(self,data):
        self.data=data

    def add_data(self,data):

        if data[0]['value']:
            self.data.name = data[0]['value']

        if data[1]['value']:
            self.data.dir = data[1]['value']

        if data[2]['value']:
            self.data.avatar = data[2]['value']

        self.session.add_all([self.data])
        self.session.commit()

class StarModelView(BaseModelViewSet):
    model = Stars()
    session = session

    def __init__(self,data):
        self.data = data

    def set_data(self):
        if self.data is None:
            return self.model
        return self.data

    def add_data(self,data):

        for item in data:
            if item['value']:
                setattr(self.data,item['db'],item['value'])

        self.session.add_all([self.data])
        self.session.commit()