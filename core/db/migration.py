from core.db.config import cur,con
class abstractMigration:
    def __init__(self):
        self.cur=cur
        self.con=con
        self.shema()
    def shema(self):
        pass
class migrationRun:
    def __init__(self,migrationList):
        self.migrations=migrationList
    def migrate(self):
        for item in self.migrations:
            item.shema()
        con.commit()