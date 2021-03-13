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

    def calendar(self,details):
        self.field_valid(details)
        validation=''
        data_type='string'
        if 'validation' in details:
            validation = details['validation']
        if 'data_type' in details:
            data_type = details['data_type']
        return {
            'data_type': data_type,
            'type': 'calendar',
            'name': details['name'],
            'validation' :validation,
            'place_holder': details['place_holder'],
            'grid_data': self.create_grid(details)
        }

    def combo_box(self,details):
        self.field_valid(details)
        Error.throw_error_bool('combo_box_list is not exist', 'combo_box_list' in details)
        return {
            'type': 'combo_box',
            'data_type': "",
            'name': details['name'],
            'place_holder': details['place_holder'],
            'combo_box_list' :details['combo_box_list'],
            'grid_data': self.create_grid(details)
        }

    def photo(self,details):
        self.field_valid(details)
        return {
            'type': 'combo_box',
            'name': details['name'],
            'data_type': 'combo_box_dir',
            'place_holder': details['place_holder'],
            'combo_box_list': self.BaseFormShema.get_files_from_dir(
                getattr(self.BaseFormShema.BaseView.data,details['name']),
                self.BaseFormShema.BaseView.data,
                details['dir_set']
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
        if hasattr(self.BaseFormShema.BaseView.data,details['name']):
            data_type = 'data_type'
            validation= ''
            if 'data_type' in details:
                data_type = details['data_type']
            if 'validation' in details:
                validation = details['validation']

            return {
                'type'        : 'edit_line',
                'name'        : details['name'],
                'data_type'   : data_type,
                'validation'  : validation,
                'place_holder': self.BaseFormShema.set_value_if_exist(
                    getattr(self.BaseFormShema.BaseView.data,details['name']),details['name']),
                'grid_data': self.create_grid(details)
            }
        else:
            Error.throw_error(details['name']+' not exist in object '+str(self.BaseFormShema.BaseView.data)  )

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

    def get_files_from_dir(self,defult,Obj,dir_add):
        dir_loop = []
        dir_loop.append(defult)
        dir=Obj.dir

        if dir_add:
            dir=Obj.dir+''+dir_add

        for item in os.listdir(dir):
            dir_loop_elment=dir + '/' +str(item)
            dir_loop.append(dir_loop_elment)
        return dir_loop

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

class AbstractBaseFormShema(BaseFormShema):

    avatar_dir=''

    def add_forms(self):
        pass

    def form(self):
        self.from_section = []
        self.add_iten('label', {
            'place_holder': 'Name',
            'name': 'name',
            "row": False,
            "coll": False
        })

        self.add_iten('edit_line', {
            'place_holder': 'Name',
            'name': 'name',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Dir Location',
            'name': 'dir',
            'data_type': 'dir',
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

        self.add_iten('photo', {
            'place_holder': 'Avatar',
            'dir_set': self.avatar_dir,
            'name': 'avatar',
            "row": False,
            "coll": True,
        })
        self.add_forms()
        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            "row": True,
            "coll": True,
            "is_submit": True,
            'new_row': True
        })

class MovieEditForm(AbstractBaseFormShema):

    def add_forms(self):

        self.add_iten('label', {
            'place_holder': 'Country',
            'name': 'country',
            "row": True,
            "coll": False,
            'new_row': True
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

class SeriesForm(AbstractBaseFormShema):

    avatar_dir = '/photo'

    def add_forms(self):
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
            'place_holder': 'Set photo for series',
            'name': 'set_photo_for_series',
            "row": True,
            "coll": True,
            'new_row': True
        })

class StarsForm(AbstractBaseFormShema):

    avatar_dir = '/photo'

    def add_forms(self):
        self.add_iten('label', {
            'place_holder': 'Height',
            'name': 'height',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('edit_line', {
            'place_holder': 'Height',
            'name': 'height',
            'data_type': 'int',
            'validation': "[0-9][0-9][0-9]",
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Weight',
            'name': 'weight',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('edit_line', {
            'place_holder': 'Weight',
            'name': 'weight',
            'data_type': 'int',
            'validation': "[0-9][0-9][0-9]",
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Ethnicity',
            'name': 'ethnicity',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('combo_box', {
            'place_holder': 'Weight',
            'name': 'ethnicity',
            'combo_box_list':[self.BaseView.data.ethnicity, 'Black', 'Asian', 'Arab', 'White'],
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Hair color',
            'name': 'hair_color',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('combo_box', {
            'place_holder': 'Hair color',
            'name': 'hair_color',
            'combo_box_list': [self.BaseView.data.hair_color, 'Black', 'Gray', 'Brown', 'Blond'],
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Date of birth',
            'name': 'date_of_birth',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('calendar', {
            'place_holder': 'Date of birth',
            'name': 'date_of_birth',
            'validation': "[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]",
            "row": False,
            "coll": True
        })


        self.add_iten('label', {
            'place_holder': 'None',
            'name': 'none',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('photo', {
            'place_holder': 'None',
            'dir_set': self.avatar_dir,
            'name': 'none',
            "row": False,
            "coll": True,
        })

        self.add_iten('label', {
            'place_holder': 'Singles',
            'name': 'singles',
            "row": True,
            "coll": False,
            'new_row': True
        })

        self.add_iten('photo', {
            'place_holder': 'Singles',
            'dir_set': self.avatar_dir,
            'name': 'singles',
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




