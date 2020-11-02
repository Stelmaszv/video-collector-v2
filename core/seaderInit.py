from app.db.seaders import movies,stars
from core.seader import initSeader

seaders=[movies(),stars()]
seader=initSeader(seaders)
seader.initNow()
