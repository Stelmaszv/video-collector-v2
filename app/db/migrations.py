from core.db.config import cur,con

cur.execute("DROP TABLE IF EXISTS series;")
cur.execute("DROP TABLE IF EXISTS movies;")
cur.execute("DROP TABLE IF EXISTS stars;")
cur.execute("DROP TABLE IF EXISTS starsinmovies;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS stars (
        id INTEGER PRIMARY KEY ASC,
        name varchar(250) NOT NULL
    )""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY ASC,
        name varchar(250) NOT NULL
    )""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY ASC,
        name varchar(250) NOT NULL,
        series INTEGER NOT NULL, 
        FOREIGN KEY(series) REFERENCES series(id)
    )""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS starsinmovies (
        id INTEGER PRIMARY KEY ASC,
        movie INTEGER NOT NULL,
        star INTEGER NOT NULL, 
        FOREIGN KEY(movie) REFERENCES movies(id),
        FOREIGN KEY(star)  REFERENCES stars(id)
    )""")

con.commit()



