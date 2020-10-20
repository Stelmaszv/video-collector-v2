from app.db.models import movies,series,stars
from app.db.models import session

def runSeeader():
    objects = [movies(name="Film o Fudzim"), movies(name="Motsu w aksji"), movies(name="KOtek in City")]
    session.add_all(objects)
    session.commit()
    objects = [stars(name="Fudzi"), stars(name="Motsu")]
    session.add_all(objects)
    session.commit()
    objects = [series(name="Koty in the city")]
    session.add_all(objects)
    session.commit()
