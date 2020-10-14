from core.db.migration import abstractMigration

class movies(abstractMigration):
    def shema(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY ASC,
                name varchar(250) NOT NULL,
                series INTEGER NOT NULL, 
                FOREIGN KEY(series) REFERENCES series(id)
        )""")

class series(abstractMigration):
    def shema(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY ASC,
            name varchar(250) NOT NULL
            )"""
        )
class stars(abstractMigration):
    def shema(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS stars (
            id INTEGER PRIMARY KEY ASC,
            name varchar(250) NOT NULL
            )"""
        )
class starsinmovies(abstractMigration):
    def shema(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS starsinmovies (
                id INTEGER PRIMARY KEY ASC,
                movie INTEGER NOT NULL,
                star INTEGER NOT NULL, 
                FOREIGN KEY(movie) REFERENCES movies(id),
                FOREIGN KEY(star)  REFERENCES stars(id)
            )
            """
        )




