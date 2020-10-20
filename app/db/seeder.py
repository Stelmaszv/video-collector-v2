from app.db.models import Movies,Series,Stars
from app.db.models import session

def runSeeader():
    objects = [Stars(name="Fudzi"), Stars(name="Motsu")]
    session.add_all(objects)
    session.commit()
    objects = [Series(name="Koty in the city")]
    session.add_all(objects)
    session.commit()
    objects = [Movies(name="Film o Fudzim"), Movies(name="Motsu w aksji"), Movies(name="KOtek in City")]
    session.add_all(objects)
    session.commit()

