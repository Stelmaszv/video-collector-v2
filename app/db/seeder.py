from app.db.models import Movies,Series,Stars,Photos
from app.db.models import session

def runSeeader():
    objects = [
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")

    ]
    session.add_all(objects)
    session.commit()
    objects = [
        Stars(name="Fudzi",avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        Stars(name="Motsu",avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
    ]
    session.add_all(objects)
    session.commit()
    objects = [
        Series(name="Koty in the city")
    ]
    session.add_all(objects)
    session.commit()
    objects = [
        Movies(name="Fajny Film"),
        Movies(name="Motsu w aksji"),
        Movies(name="KOtek in City")
    ]
    session.add_all(objects)
    session.commit()
    query=session.query(Movies).get(1)
    star=session.query(Stars).get(1)
    query.stars.append(star)


    photo = session.query(Photos).get(1)
    photo2 = session.query(Photos).get(2)
    star.photos.append(photo)
    star.photos.append(photo2)


