from app.db.models import Stars,Series
from app.db.models import session

class BaseModelViewSet:
    session = session
    model = None

    def __init__(self,data):
        self.data=data

    def add_data(self,data):

        for item in data:
            if item['value']:
                setattr(self.data,item['db'],item['value'])

        self.session.add_all([self.data])
        self.session.commit()

class SetPhotoToSetiesView(BaseModelViewSet):

    model = Series()
    session = session

    def add_data(self, data):
        for item in self.data.sezons:
            for el in data:
                if item.name==el['db']:
                    if el['data-type'] == 'photo_location' and len(el['value']):
                        item.src=el['value']




class MoviesModelView(BaseModelViewSet):
    model = Series()
    session = session

class SeriesModelView(BaseModelViewSet):
    model = Series()
    session = session

class StarModelView(BaseModelViewSet):
    model = Stars()
    session = session
