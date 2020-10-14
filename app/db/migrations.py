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





