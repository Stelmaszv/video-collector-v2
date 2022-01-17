from pathlib import Path
from app.db.models import session, Movies
from core.config import ConfigLoop, ConfigMovies,SetTags,CreateXML,CreateMovieList
from core.dir import LoadFilesFromJson, PhotoMeaker
from core.html_gerator import HTMLGenaratorMain, GenerateHTMLMovies, GenerateHTMLProducents, GenerateHTMLSeries, \
    GenerateHTMLStars
from core.setings import data_JSON, setings_array
from core.create_JSON_DB_LIST import CreateJSONDBLIST, GenerateJSONOtputsMovies, GenerateJSONOtputsStars, \
    GenerateJSONOtputsSeries, GenerateJSONOtputsProducent
from core.webadmin import WebAdminProducents, WebAdminSeries, WebAdminTags, WebAdminStars, WebAdminMovies, CleanWebAdmin


class LoopRun:
    objets = []

    def run_object(self, Obj, method, run, start_string, end_string):
        if run:
            print(start_string)
            method = getattr(Obj, method)
            method()
            print(end_string)

    def loop(self):
        for objet in self.objets:
            self.run_object(objet['obj'], objet['method'], objet['stan'], objet['start_mes'], objet['end_mees'])
class JSONRun:

    def __init__(self, StartView, JSONConfigView):
        self.StartView = StartView
        self.JSONConfigView = JSONConfigView

    def show_start_view(self):
        self.StartView.run_window()

class Run:
    scan_photos = setings_array["scan_photos"]
    run_start_view = setings_array["run_start_view"]
    config=True

    def __init__(self, StartView, JSONConfigView):
        self.StartView=StartView
        self.JSONConfigView = JSONConfigView
        self.LoopRun = LoopRun()

    def start(self):

        self.LoopRun.objets = [
            {
                "obj": LoadFilesFromJson(data_JSON['dirs']), "method": 'add_files',
                "stan": setings_array["scan_dir"], "start_mes": 'Scaning Dir in progres', "end_mees": 'End of scaning'
            },
            {
                "obj": ConfigLoop(data_JSON['dirs']), "method": 'load',
                "stan": setings_array["config"], "start_mes": 'Config in progres', "end_mees": 'End of Config'
            },
            {
                "obj": ConfigMovies(data_JSON['movies_photos']), "method": 'load',
                "stan": setings_array["config"], "start_mes": 'Config Movies in progres',
                "end_mees": 'End of Movies in progres'
            },

            {
                "obj": SetTags(data_JSON['dirs']), "method": 'set',
                "stan": setings_array["config"], "start_mes": 'Set Tags in progres',
                "end_mees": 'End of Set Tags in progres'
            },
            {
                "obj": CreateXML(data_JSON['dirs']), "method": 'load',
                "stan": setings_array["create_xml"], "start_mes": 'Createing XML in progres',
                "end_mees": 'End of Createing XML in progres'
            },
            {
                "obj": CreateMovieList(data_JSON['dirs']), "method": 'load',
                "stan": setings_array["create_movie_list"], "start_mes": 'Createing Movies List in progres',
                "end_mees": 'End of Createing Movies List in progres'
            },
            {
                "obj": CreateJSONDBLIST(), "method": 'create',
                "stan": setings_array["generate_json"], "start_mes": 'Config JSON Outputs in progres',
                "end_mees": 'End of Config JSON Outputs in progres'
            },
            {
                "obj": GenerateJSONOtputsSeries(), "method": 'create',
                "stan": setings_array["generate_json"], "start_mes": 'Config Series in progres',
                "end_mees": 'End of Series in progres'
            },
            {
                "obj": GenerateJSONOtputsMovies(), "method": 'create',
                "stan": setings_array["generate_json"], "start_mes": 'Config JSON Outputs for movies in progres',
                "end_mees": 'End of Config JSON Outputs for movies in progres'
            },
            {
                "obj": GenerateJSONOtputsStars(), "method": 'create',
                "stan": setings_array["generate_json"], "start_mes": 'Config JSON Outputs for stars in progres',
                "end_mees": 'End of Config JSON Outputs for stars in progres'
            },
            {
                "obj": GenerateJSONOtputsProducent(), "method": 'create',
                "stan": setings_array["generate_json"], "start_mes": 'Config JSON Outputs for producent in progres',
                "end_mees": 'End of Config JSON Outputs for producent in progres'
            },
            {
                "obj": HTMLGenaratorMain(), "method": 'generate',
                "stan": setings_array["generate_html"], "start_mes": 'Genereting HTML Base',
                "end_mees": 'End of Genereting HTML Base'
            },
            {
                "obj": GenerateHTMLMovies(), "method": 'generate',
                "stan": setings_array["generate_html"], "start_mes": 'Genereting HTML Movies',
                "end_mees": 'End of Genereting HTML Movies'
            },
            {
                "obj": GenerateHTMLProducents(), "method": 'generate',
                "stan": setings_array["generate_html"], "start_mes": 'Genereting HTML Producents',
                "end_mees": 'End of Genereting HTML Producents'
            },
            {
                "obj": GenerateHTMLSeries(), "method": 'generate',
                "stan": setings_array["generate_html"], "start_mes": 'Genereting HTML Series',
                "end_mees": 'End of Genereting HTML Series'
            },
            {
                "obj": GenerateHTMLStars(), "method": 'generate',
                "stan": setings_array["generate_html"], "start_mes": 'Genereting HTML Stars',
                "end_mees": 'End of Genereting HTML Stars'
            },
            {
                "obj": CleanWebAdmin(), "method": 'clean',
                "stan": setings_array["web_admin"], "start_mes": 'Start Cleaning web Amidn !',
                "end_mees": 'End of Cleaning web Amidn'
            },
            {
                "obj": WebAdminProducents(), "method": 'generate',
                "stan": setings_array["web_admin"], "start_mes": 'Star Web admin Producents',
                "end_mees": 'End Web admin Producents'
            },
            {
                "obj": WebAdminSeries(), "method": 'generate',
                "stan": setings_array["web_admin"], "start_mes": 'Star Web admin Series',
                "end_mees": 'End Web admin Series'
            },
            {
                "obj": WebAdminTags(), "method": 'generate',
                "stan": setings_array["web_admin"], "start_mes": 'Star Web admin Tags',
                "end_mees": 'End Web admin Tags'
            },
            {
                "obj": WebAdminStars(), "method": 'generate',
                "stan": setings_array["web_admin"], "start_mes": 'Star Web admin Stars',
                "end_mees": 'End Web admin Stars'
            },
            {
                "obj": WebAdminMovies(), "method": 'generate',
                "stan": setings_array["web_admin"], "start_mes": 'Star Web admin Stars',
                "end_mees": 'End Web admin Stars'
            }
        ]

        if Path('data.json').is_file():
            self.LoopRun.loop()

            if self.scan_photos:
                print("Createing screen shots in progres")
                for Movie in session.query(Movies).all():
                    PM = PhotoMeaker(Movie, data_JSON['movies_photos'])
                    PM.make()

        else:
            self.config=False
            self.JSONConfigView.run_window()

    def show_start_view(self):
        if self.run_start_view:
            self.StartView.run_window()
        else:
            exit()
