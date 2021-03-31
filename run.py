import sys
from PyQt5.QtWidgets import QApplication

from app.db.models import session, Movies
from core.config import ConfigLoop, ConfigMovies
from core.dir import LoadFilesFromJson, PhotoMeaker
from core.setings import data_JSON,scan_photos,run_start_view
from view.menu.menu import Menu

class Run:

    scan_photos=scan_photos
    run_start_view=run_start_view

    def __init__(self,StartView):
        self.StartView=StartView

    def start(self):
        JSON = LoadFilesFromJson(data_JSON['dirs'])
        JSON.add_files()

        Config = ConfigLoop(data_JSON['dirs'])
        Config.load()

        Config = ConfigMovies(data_JSON['movies_photos'])
        Config.load()

        if self.scan_photos:
            for Movie in session.query(Movies).all():
                PM = PhotoMeaker(Movie, data_JSON['movies_photos'])
                PM.make()

    def show_start_view(self):
        if self.run_start_view:
            self.StartView.run_window()
        else:
            exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Run=Run(Menu())
    Run.start()
    Run.show_start_view()
    sys.exit(app.exec_())