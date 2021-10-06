import json
import os
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget, QFileDialog
from app.forms import JSONDataConfigForm
from app.model_view import ConfigAddDataModel
from view.menu.menu import Menu
from core.custum_errors import Error
class JSONConfigView(QWidget,AbstractBaseView):
    FormSchema = JSONDataConfigForm
    ModelView  = ConfigAddDataModel
    search_in='search_in'
    window_title = 'JSON data config'
    resolution_index   = 'Menu'
    show_elemnts = ['Title','Info','Galery','Nav','Avatar','List']

    def add_json(self, values):
        def valid_JSON(data):
            if 'dirs' not in data or 'movies_photos' not in data:
                print('Invalid JSON File !')
                exit()
            for dir in data['dirs']:
                if 'type' not in dir or 'dir' not in dir:
                    print('Invalid JSON File !')
                    exit()
        file_filter = 'Data File (*.JSON)'
        response = QFileDialog.getOpenFileName(
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter
        )

        with open(response[0]) as json_file:
            data = json.load(json_file)
            valid_JSON(data)
            array = {
                "drive": "Z",
                "dirs": [{
                    "type": "stars",
                    "dir": data['dirs'][0]
                },
                    {
                        "type": "series",
                        "dir": data['dirs'][1]
                    },
                    {
                        "type": "producents",
                        "dir": data['dirs'][2]
                    }

                ],
                "movies_photos": data['movies_photos'],
            }
            json_array = json.dumps(array)
            f = open('data.JSON', "x")
            f.write(json_array)
            f.close()
            self.close()
            M = Menu(0)
            M.run_window()

    def submit_click(self,values):
        self.Submit.auto_model=False
        self.Submit.set_data(values)
        self.Submit.run()
        if len(self.Submit.error)==0:
            array = {
                "dirs": [{
                        "type": "stars",
                        "dir": values[0]['value']
                    },
                    {
                        "type": "series",
                        "dir": values[1]['value']
                    },
                    {
                        "type": "producents",
                        "dir": values[2]['value']
                    }

                ],
                "movies_photos": values[2]['value'],
            }
            json_array = json.dumps(array)
            f = open('data.JSON', "x")
            f.write(json_array)
            f.close()
            self.close()
            M = Menu(0)
            M.run_window()
