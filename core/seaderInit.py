from app.db.seaders import movies
from core.seader import initSeader

seaders=[movies()]


seader=initSeader(seaders)
seader.initNow()
