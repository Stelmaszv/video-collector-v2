from core.db.model import abstractModel

class movies(abstractModel):
    pass

movies().insert([['fqef',0],['fqef',0],['fqef',0],['fqef',0],['fqef',0],['fqef',0],['fqef',0]])
for item in movies().all():
    print(item['name'])
movies().dropTable()
