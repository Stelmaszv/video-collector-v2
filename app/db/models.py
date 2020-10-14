from core.db.model import abstractModel
from app.db.migrations import movies as moviesMigration

class movies(abstractModel):
    migration=moviesMigration()

movies().insert([['fqef',0],['fqef',0],['fqef',0],['fqef',0],['fqef',0],['fqef',0],['fqef',0]])
for item in movies().all():
    print(item['name'])
movies().dropTable()
