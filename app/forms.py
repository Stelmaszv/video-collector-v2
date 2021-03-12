from core.custum_errors import Error
import os

class FormConstract:
    row=0
    coll=0

    def __init__(self,BaseFormShema):
        self.BaseFormShema=BaseFormShema

    def field_valid(self,details,fields=[]):
        Error.throw_error_bool('Row not exist in details ', 'row' in details)
        Error.throw_error_bool('Coll not exist in details ', 'coll' in details)
        Error.throw_error_bool('Place holder not exist in details ', 'place_holder' in details)
        Error.throw_error_bool('Name not exist in details ', 'name' in details)

    def create_grid(self,details):

        if 'new_row' in details:
            self.coll=0

        if details['row']:
            self.row = self.row + 1

        if details['coll']:
            self.coll = self.coll + 1

        return  [self.row, self.coll, 1, 1]

    def combo_box(self,details):
        self.field_valid(details)

        return {
            'type': 'combo_box',
            'name': details['name'],
            'data_type': 'combo_box_dir',
            'place_holder': details['place_holder'],
            'combo_box_list': self.BaseFormShema.get_files_in_dir_for_movie(
                getattr(self.BaseFormShema.BaseView.data,details['name']),
                self.BaseFormShema.BaseView.data
            ),
            'grid_data': self.create_grid(details)
        }

    def label(self,details):
        self.field_valid(details)
        return {
            'data_type': "",
            'type': 'label',
            'name': details['name'],
            'place_holder': details['place_holder'],
            'grid_data': self.create_grid(details)
        }

    def button(self,details):
        name= 'button'
        self.field_valid(details)
        if 'is_submit' in details:
            name = 'button_submit'
        return {
            'type': name,
            'data_type':"",
            'name': details['place_holder'],
            'obj_name': details['name'],
            'place_holder': details['place_holder'],
            'grid_data': self.create_grid(details),
            'click': self.BaseFormShema.add_method(
                getattr(self.BaseFormShema.BaseView, details['name']),
                details['name']
            ),
            'arguments': []
        }

    def edit_line(self,details):
        self.field_valid(details)
        data_type = 'data_type'
        if 'data_type' in details:
            data_type = details['data_type']
        return {
            'type': 'edit_line',
            'name': details['name'],
            'validation': "",
            'data_type': data_type,
            'place_holder': self.BaseFormShema.set_value_if_exist(
                getattr(self.BaseFormShema.BaseView.data,details['name']),details['name']),
            'grid_data': self.create_grid(details)
        }

class BaseFormShema:
    from_section=[]
    def __init__(self, BaseView,methods=[]):
        self.BaseView = BaseView
        self.chcek_nethods(methods)
        self.methods=methods
        self.ElmentsShema=FormConstract(self)
        self.form()

    def chcek_nethods(self,methods):
        for method in methods:
            Error.throw_error_bool(str(method)+' not exist in Baseview ',self.is_method(method))

    def form(self):
        pass

    def get_files_from_dir(self,defult,dir):
        dir_loop=[]
        dir_loop.append(defult)
        for item in os.listdir(dir):
            dir_loop_elment=dir + '/' +str(item)
            dir_loop.append(dir_loop_elment)
        return dir_loop

    def get_files_in_dir_for_movie(self,defult,Data):
        return self.get_files_from_dir(defult, Data.dir)

    def get_files_in_dir(self,defult):
        dir=self.BaseView.data.dir + '' +str('/photo')
        return self.get_files_from_dir(defult,dir)

    def set_value_if_exist(self,value,empty):
        if value is None :
            return empty
        return str(value)

    def return_from_section(self):
        return self.from_section

    def add_method(self,method,method_str):

        if method_str in self.methods is not True:
            return  method
        else:
            Error.throw_error_bool(str(method_str) + ' not exist in Baseview ', False)

    def is_method(self, method):
        return callable(getattr(self.BaseView, method, None))

    def add_iten(self,item,details):
        if hasattr(self.ElmentsShema,item):
            method=getattr(self.ElmentsShema,item)
            self.from_section.append(method(details))
        else:
            Error.throw_error('Method '+item+' not found !')



class MovieEditForm(BaseFormShema):
    def form(self):
        self.from_section = []
        self.add_iten('label',{
            'place_holder':'Name',
            'name': 'name',
            "row" : False,
            "coll": False
        })

        self.add_iten('edit_line', {
            'place_holder': 'Name',
            'name': 'name',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Country',
            'name': 'country',
            "row": True,
            "coll": False,
            'new_row':True
        })

        self.add_iten('edit_line', {
            'place_holder': 'Cuntry',
            'name': 'country',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Year',
            'name': 'country',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('edit_line', {
            'place_holder': 'Year',
            'name': 'year',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Dir Location',
            'name': 'dir',
            'data_type':'dir',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('edit_line', {
            'place_holder': 'Dir Location',
            'name': 'dir',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Avatar',
            'name': 'avatar',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('combo_box', {
            'place_holder': 'Avatar',
            'name': 'avatar',
            "row": False,
            "coll": True,
        })

        self.add_iten('button', {
            'place_holder': 'Add tag',
            'name': 'add_tag',
            "row": True,
            "coll": True,
            'new_row': True
        })

        self.add_iten('button', {
            'place_holder': 'Add Star',
            'name': 'add_star',
            "row": True,
            "coll": True,
            'new_row': True
        })

        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            "row": True,
            "coll": True,
            "is_submit":True,
            'new_row': True
        })


class AdvanceSearchForm(BaseFormShema):
    def form(self):
        self.from_section = []
        self.from_section.append({
            'type': 'label',
            'name': 'name',
            'place_holder': 'Name',
            'grid_data': [0, 0, 1, 1]
        })
        self.from_section.append({
            'type': 'edit_line',
            'name': 'name',
            'validation': "",
            'data_type': 'string',
            'place_holder': self.set_value_if_exist(None,'Hukaj'),
            'grid_data': [0, 1, 1, 1]
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'advance',
            'name': 'Add Tag',
            'place_holder': 'advance',
            'grid_data': [1, 1, 1, 1],
            'click': self.add_method(self.BaseView.add_tag,'add_tag'),
            'arguments':[]
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'advance',
            'name': 'Add Star',
            'place_holder': 'advance',
            'grid_data': [2, 1, 1, 1],
            'click': self.add_method(self.BaseView.add_star,'add_star'),
            'arguments':[]
        })

        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [3, 1, 1, 1],
            'click': self.add_method(self.BaseView.submit_click, 'submit_click'),
            'arguments': []
        })


class MenuFormSchena(BaseFormShema):

    def form(self):
        self.from_section = []
        self.from_section.append({
            'type'        : 'label',
            'name'        : 'name',
            'place_holder': 'Name',
            'grid_data'   : [0, 0, 1, 1]
        })
        self.from_section.append({
            'type': 'edit_line',
            'name': 'name',
            'validation': "",
            'data_type': 'string',
            'place_holder': self.set_value_if_exist(None,self.BaseView.search_faze),
            'grid_data': [0, 1, 1, 1]
        })

        self.from_section.append({
            'type': 'combo_box',
            'obj_name': 'sections',
            'name': 'Sections',
            'data_type': 'string',
            'validation': "[a-z]+.?[a-z]+.?[A-Z]+.?[A-Z]{,2}",
            'place_holder': 'sections',
            'grid_data': [0, 2, 1, 1],
            'combo_box_list': [self.BaseView.search_in, 'series', 'stars', 'movies'],
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'advance',
            'name': 'Advance',
            'place_holder': 'advance',
            'grid_data': [1, 1, 1, 1],
            'click': self.add_method(self.BaseView.advance,'advance'),
            'arguments': []
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'reset',
            'name': 'Reset',
            'place_holder': 'reset',
            'grid_data': [2, 1, 1, 1],
            'click': self.add_method(self.BaseView.reset,'reset'),
            'arguments': []
        })

        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [3, 1, 1, 1],
            'click': self.BaseView.submit_click,
            'arguments': []
        })

class AddStarToModelForm(BaseFormShema):

    def form(self):
        self.from_section = []
        self.from_section.append({
            'type'        : 'label',
            'name'        : 'name',
            'place_holder': 'Name',
            'grid_data'   : [0, 0, 1, 1]
        })
        self.from_section.append({
            'type': 'edit_line',
            'name': 'name',
            'validation': "",
            'data_type': 'string',
            'place_holder': self.set_value_if_exist(None,"Star Name"),
            'grid_data': [0, 1, 1, 1]
        })
        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [0, 2, 1, 1],
            'click': self.BaseView.submit_click,
            'arguments': []
        })

class SetPhotoToSeriesForm(BaseFormShema):

    def form(self):
        self.from_section = []
        row=0
        for item in self.BaseView.data.sezons:
            self.from_section.append({
                'type': 'label',
                'name': 'name',
                'place_holder':  "Sezon name "+str(item.name),
                'grid_data': [row, 0, 1, 1]
            })

            self.from_section.append({
                'type': 'combo_box',
                'name': 'avatar_edit_line',
                'data_type': 'combo_box_dir',
                'validation': "",
                'place_holder': self.set_value_if_exist(item.src,"Sezon name "+str(item.name)),
                'grid_data': [row, 1, 1, 1],
                'combo_box_list': self.get_files_in_dir(item.src)
            })

            row=row+1

        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [row+1, 1, 1, 1],
            'click': self.BaseView.submit_click
        })

class TagsForm(BaseFormShema):

    def form(self):
        self.from_section = []
        self.from_section.append({
            'type'        : 'label',
            'name'        : 'name',
            'place_holder': 'Name',
            'grid_data'   : [0, 0, 1, 1]
        })
        self.from_section.append({
            'type': 'edit_line',
            'name': 'name',
            'validation': "[A-Z]+.?[a-z]+.?[a-z]+.?[A-Z]+.?[a-z]+.?",
            'data_type': 'string',
            'place_holder': self.set_value_if_exist(None,"Format - Full Name"),
            'grid_data': [0, 1, 1, 1]
        })
        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [0, 2, 1, 1],
            'click': self.add_method(self.BaseView.submit_click,'submit_click'),
            'arguments': []
        })

class SeriesForm(BaseFormShema):

    def form(self):
        self.from_section = []
        self.from_section.append({
            'type'        : 'label',
            'name'        : 'name',
            'place_holder': 'Name',
            'grid_data'   : [0, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'name',
            'validation': "",
            'data_type': 'string',
            'place_holder': self.set_value_if_exist(self.BaseView.data.name,"Format - Full Name"),
            'grid_data': [0, 1, 1, 1]
        })
        self.from_section.append({
            'type'        : 'label',
            'name'        : 'name',
            'place_holder': 'Dir Location',
            'grid_data'   : [1, 0, 1, 1]
        })
        self.from_section.append({
            'type': 'edit_line',
            'name': 'dir_edit_line',
            'data_type': 'dir',
            'validation': "",
            'place_holder': self.set_value_if_exist(self.BaseView.data.dir,'Location dir with data'),
            'grid_data': [1, 1, 1, 1]
        })
        if self.BaseView.data.dir:

            self.from_section.append({
                'type': 'label',
                'name': 'avatar_label',
                'place_holder': 'Avatar',
                'grid_data': [7, 0, 1, 1]
            })

            self.from_section.append({
                'type': 'combo_box',
                'name': 'avatar_edit_line',
                'data_type': 'combo_box_dir',
                'validation': "",
                'place_holder': self.set_value_if_exist(self.BaseView.data.avatar,'Avator'),
                'grid_data': [7, 1, 1, 1],
                'combo_box_list': self.get_files_in_dir(self.BaseView.data.avatar)
            })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'submit',
            'name': 'Add Tag',
            'place_holder': 'Submit',
            'grid_data': [10, 1, 1, 1],
            'click': self.add_method(self.BaseView.add_tag,'add_tag'),
            'arguments':[]
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'submit',
            'name': 'Set photo for series',
            'place_holder': 'Submit',
            'grid_data': [11, 1, 1, 1],
            'click': self.add_method(self.BaseView.set_photo_for_series,'set_photo_for_series'),
            'arguments': []
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'submit',
            'name': 'Add Star',
            'place_holder': 'Submit',
            'grid_data': [12, 1, 1, 1],
            'click': self.add_method(self.BaseView.add_star,'add_star'),
            'arguments': []
        })

        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [13, 1, 1, 1],
            'click': self.add_method(self.BaseView.submit_click,'submit_click'),
            'arguments': []
        })

class StarsForm(BaseFormShema):

    def form(self):
        self.from_section=[]
        self.from_section.append({
            'type'        : 'label',
            'name'        : 'name',
            'place_holder': 'Name',
            'grid_data'   : [0, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'name',
            'validation': "[A-Z]+.?[a-z]+.?[a-z]+.?[A-Z]+.?[a-z]+.?",
            'data_type': 'string',
            'place_holder': self.set_value_if_exist(self.BaseView.data.name,"Format - Full Name"),
            'grid_data': [0, 1, 1, 1]
        })


        self.from_section.append({
            'type': 'label',
            'name': 'height',
            'place_holder': 'Height',
            'grid_data': [1, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'height',
            'data_type': 'int',
            'validation': "[0-9][0-9][0-9]",
            'place_holder': self.set_value_if_exist(str(self.BaseView.data.height)+' cm','value in cm'),
            'grid_data': [1, 1, 1, 1]
        })

        self.from_section.append({
            'type': 'label',
            'name': 'weight',
            'place_holder': 'Weight',
            'grid_data': [2, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'weight',
            'data_type': 'int',
            'validation': "[0-9][0-9][0-9]",
            'place_holder': self.set_value_if_exist(str(self.BaseView.data.weight)+' kg','value in kg'),
            'grid_data': [2, 1, 1, 1]
        })

        self.from_section.append({
            'type': 'label',
            'name': 'ethnicity',
            'place_holder': 'Ethnicity',
            'grid_data': [3, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'combo_box',
            'name': 'ethnicity',
            'data_type': 'string',
            'combo_box_list': [self.BaseView.data.ethnicity, 'Black', 'Asian', 'Arab', 'White'],
            'validation': "[a-z]+.?[a-z]+.?[A-Z]+.?[A-Z]{,2}",
            'place_holder': '',
            'grid_data': [3, 1, 1, 1]
        })


        self.from_section.append({
            'type': 'label',
            'name': 'hair_color',
            'place_holder': 'Hair color',
            'grid_data': [4, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'combo_box',
            'name': 'hair_color',
            'data_type': 'string',
            'validation': "[a-z]+.?[a-z]+.?[A-Z]+.?[A-Z]{,2}",
            'place_holder': '',
            'grid_data': [4, 1, 1, 1],
            'combo_box_list': [self.BaseView.data.hair_color, 'Black', 'Gray', 'Brown', 'Blond']
        })

        self.from_section.append({
            'type': 'label',
            'name': 'date_of_birth',
            'place_holder': 'Date of birth',
            'grid_data': [5, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'calendar',
            'name': 'date_of_birth',
            'data_type': 'data',
            'validation': "[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]",
            'place_holder':'',
            'grid_data': [5, 1, 1, 1]
        })


        self.from_section.append({
            'type': 'label',
            'name': 'dir_label',
            'place_holder': 'Dir location',
            'grid_data': [6, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'dir_edit_line',
            'data_type': 'dir',
            'validation': "",
            'place_holder': self.set_value_if_exist(self.BaseView.data.dir,'Location dir with data'),
            'grid_data': [6, 1, 1, 1]
        })

        if self.BaseView.data.dir:

            self.from_section.append({
                'type': 'label',
                'name': 'avatar_label',
                'place_holder': 'Avatar',
                'grid_data': [7, 0, 1, 1]
            })

            self.from_section.append({
                'type': 'combo_box',
                'name': 'avatar_edit_line',
                'data_type': 'combo_box_dir',
                'validation': "",
                'place_holder': self.set_value_if_exist(self.BaseView.data.avatar,'Avator'),
                'grid_data': [7, 1, 1, 1],
                'combo_box_list': self.get_files_in_dir(self.BaseView.data.avatar)
            })

            self.from_section.append({
                'type': 'label',
                'name': 'none_edit_line_label',
                'place_holder': 'None avatar',
                'grid_data': [8, 0, 1, 1]
            })

            self.from_section.append({
                'type': 'combo_box',
                'name': 'none_edit_line',
                'data_type': 'combo_box_dir',
                'validation': "",
                'place_holder': self.set_value_if_exist(self.BaseView.data.none,'None dir avator'),
                'grid_data': [8, 1, 1, 1],
                'combo_box_list': self.get_files_in_dir(self.BaseView.data.none)
            })

            self.from_section.append({
                'type': 'label',
                'name': 'singles_edit_line_label',
                'place_holder': 'Singles avatar',
                'grid_data': [9, 0, 1, 1]
            })

            self.from_section.append({
                'type': 'combo_box',
                'name': 'singles_edit_line',
                'data_type': 'combo_box_dir',
                'validation': "",
                'place_holder': self.set_value_if_exist(self.BaseView.data.singles,'Singles dir avator'),
                'grid_data': [9, 1, 1, 1],
                'combo_box_list': self.get_files_in_dir(self.BaseView.data.singles)
            })
            self.from_section.append({
                'type': 'button',
                'obj_name': 'add_tags',
                'name': 'Add Tags',
                'place_holder': 'Tags',
                'grid_data': [10, 1, 1, 1],
                'click' : self.add_method(self.BaseView.add_tag,'add_tag'),
                'arguments': []
            })
                
            self.from_section.append({
                'type': 'button_submit',
                'obj_name': 'submit',
                'name': 'Submit',
                'place_holder': 'Submit',
                'grid_data': [11, 1, 1, 1],
                'click': self.add_method(self.BaseView.submit_click,'submit_click'),
                'arguments': []
            })



