from core.creator import SeriesCreator
from app.db.models import Stars,session
data= session.query(Stars).filter(Stars.name == 'Sean Conery').first()
list=SeriesCreator(data).return_obj()
print(list)