from app.db.models import Movies,Series,Stars,Photos
from app.db.models import session

def runSeeader():
    objects = [
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/unnamed.jpg"),
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/578211-gettyimages-542930526.jpg"),
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"),
        Photos(src="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
    ]
    session.add_all(objects)
    session.commit()
    objects = [
        Stars(name="Fudzi",avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        Stars(name="Topcia",avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg")
    ]
    session.add_all(objects)
    session.commit()
    objects = [
        Series(name="Koty in the city",avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        Series(name="Koty in the city2",avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg"),
        Series(name="Koty in the city3",avatar="C:/Users/DeadlyComputer/Desktop/photo/61mJMflh3uL._AC_SY450_.jpg")
    ]
    session.add_all(objects)
    session.commit()
    objects = [
        Movies(name="fajna Topcia"),
        Movies(name="2"),
        Movies(name="3"),
        Movies(name="4"),
        Movies(name="5"),
        Movies(name="6"),
        Movies(name="7"),
        Movies(name="8"),
        Movies(name="9"),
        Movies(name="8"),
        Movies(name="9"),
        Movies(name="10")
    ]
    session.add_all(objects)
    session.commit()

    addSeries()
    addPhotos()
    addStarToMovie()

    query=session.query(Movies).get(1)
    star=session.query(Stars).get(2)
    query.stars.append(star)
    session.add_all(objects)


def addPhotos():
    star = session.query(Stars).get(2)
    photo = session.query(Photos).get(1)
    photo2 = session.query(Photos).get(2)
    photo3 = session.query(Photos).get(3)
    photo4 = session.query(Photos).get(4)
    photo5 = session.query(Photos).get(5)
    photo6 = session.query(Photos).get(5)
    star.photos.append(photo)
    star.photos.append(photo2)
    star.photos.append(photo3)
    star.photos.append(photo4)
    star.photos.append(photo5)
    star.photos.append(photo6)

def addSeries():

    star = session.query(Stars).get(2)
    serie = session.query(Series).get(1)
    star.series.append(serie)

    serie = session.query(Series).get(2)
    star.series.append(serie)

def addStarToMovie():
    star = session.query(Stars).get(2)
    serie = session.query(Series).get(1)
    movie = session.query(Movies).get(1)
    serie.movies.append(movie)
    movie.stars.append(star)
    movie = session.query(Movies).get(2)
    serie.movies.append(movie)
    movie = session.query(Movies).get(3)
    serie.movies.append(movie)
    movie.stars.append(star)
    movie = session.query(Movies).get(4)
    serie.movies.append(movie)
    movie = session.query(Movies).get(6)
    serie.movies.append(movie)
    movie.stars.append(star)

    serie = session.query(Series).get(2)
    movie = session.query(Movies).get(1)
    movie.stars.append(star)
    serie.movies.append(movie)
    movie = session.query(Movies).get(2)
    serie.movies.append(movie)
    movie.stars.append(star)
    movie = session.query(Movies).get(3)
    serie.movies.append(movie)
    movie.stars.append(star)
    movie = session.query(Movies).get(4)
    serie.movies.append(movie)
    movie.stars.append(star)
    movie = session.query(Movies).get(6)
    serie.movies.append(movie)
    movie.stars.append(star)











