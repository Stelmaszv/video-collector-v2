from core.setings import data_JSON
from pathlib import Path
import os

class HTMLGenaratorBase:
    dir = data_JSON['html_output'] + '\HTML Generator'
    sites = data_JSON['html_output'] + '\HTML Generator\sites'
    css = data_JSON['html_output'] + '\HTML Generator\css'
    js = data_JSON['html_output'] + '\HTML Generator\js'
    project_genarator_url = data_JSON['project_url']

    def __init__(self):
        if os.path.isdir(self.dir) is False:
            os.mkdir(self.dir)

        if os.path.isdir(self.sites) is False:
            os.mkdir(self.sites)

        if os.path.isdir(self.css) is False:
            os.mkdir(self.css)

        if os.path.isdir(self.js) is False:
            os.mkdir(self.js)

    def generate(self):
        self.create_file(
            self.dir,
            'index.html',
            data_JSON['project_url'] + '\HTML_Genarator\index.html')

        self.create_file(
            self.sites,
            'stars.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema\stars.html')
        self.create_file(
            self.sites,
            'producent.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema\producent.html')
        self.create_file(
            self.sites,
            'series.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema\series.html')
        self.create_file(
            self.sites,
            'movies.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema\movies.html')

        self.create_file(
            self.css,
            'main.css',
            data_JSON['project_url'] + '\HTML_Genarator\css\main.css')
        self.create_file(
            self.js,
            'main.js',
            data_JSON['project_url'] + '\HTML_Genarator\js\main.js')

    def return_html_as_string(self, shema_url):
        return Path(shema_url).read_text()

    def create_file(self, dir, file_name, shema_url):
        if Path(dir + '\\' + file_name).is_file() is True:
            os.remove(dir + '\\' + file_name)
        f = open(dir + '\\' + file_name, "x")
        f.write(self.return_html_as_string(shema_url))
        f.close()
