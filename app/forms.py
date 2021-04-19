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
        db = self.set_db(details)
        if 'validation' in details:
            validation = details['validation']
        return {
            'data_type': 'data',
            'type': 'calendar',
            'db': db,
            'name': details['name'],
            'validation' :validation,
            'place_holder': details['place_holder'],
            'grid_data': self.create_grid(details)
        }

    def combo_box(self,details):
        self.field_valid(details)
        Error.throw_error_bool('combo_box_list is not exist', 'combo_box_list' in details)
        db = self.set_db(details)
        return {
            'db': db,
            'type': 'combo_box',
            'data_type': "",
            'name': details['name'],
            'place_holder': details['place_holder'],
            'combo_box_list' :details['combo_box_list'],
            'grid_data': self.create_grid(details)
        }

    def photo_loop(self,details):

        def photo_to_loop(el,details,row):
           return {
               "db" :el.id,
               "row": True,
               "coll": True,
               'type': 'combo_box',
               'name': el.id,
               'place_holder': el.id,
               'data_type': 'combo_box_dir',
               'combo_box_list': self.BaseFormShema.get_files_from_dir(
                   getattr(el, details['photo_index']),
                   self.BaseFormShema.BaseView.data,
                   details['dir_set']
               ),
               'grid_data': [row,2,1,1]
            }
        photos=[]
        loop = getattr(self.BaseFormShema.BaseView.data, details['index'])
        row=0
        for el in loop:
            photos.append({
                'type':"label",
                'name':el.name+' label',
                'place_holder': "Sezon name " + str(el.name),
                'grid_data': [row, 0, 1, 1]
            })
            photos.append({
                    'db'          : el.id,
                    'type'        : 'edit_line',
                    'name'        : el.id,
                    'data_type'   : 'photo_location',
                    'validation'  : '',
                    'place_holder': "Custum locataion for photo " + str(el.name),
                    'grid_data': [row, 1, 1, 1]
            })
            #photos.append(photo_to_loop(el, details, row))
            row=row+1
        self.row=row
        self.coll=2
        return {
            'loop' :photos
        }

    def photo(self,details):
        self.field_valid(details)
        db=self.set_db(details)
        return {
            'db'  : db,
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
        Error.throw_error_bool(
            'Object do not have atribut '+details['name'],
            hasattr(self.BaseFormShema.BaseView.data,details['name']) is False
        )
        Error.throw_error_bool(
            details['name']+' is not method',
            self.BaseFormShema.is_method(details['name'])
        )

        def set_disabled(details):
            if 'disabled' in details:
                return details['disabled']
            return True

        name= 'button'
        self.field_valid(details)
        if 'is_submit' in details:
            name = 'button_submit'

        return {
            'disabled':set_disabled(details),
            'type': name,
            'data_type':"string",
            'name': details['place_holder'],
            'obj_name': details['name'],
            'place_holder': details['place_holder'],
            'grid_data': self.create_grid(details),
            'click': getattr(self.BaseFormShema.BaseView, details['name']),
            'arguments': []
        }

    def if_model(self,details):
        if 'model' in details and details['model'] is False:
            return True
        return False

    def set_db(self,details):
        if 'db' in details:
            if hasattr(self.BaseFormShema.BaseView.data,details['db']):
                return details['db']
        return ''

    def set_placeholder(self,details):
        place_holder = ''
        if  hasattr(self.BaseFormShema.BaseView.data,details['name']):
            place_holder = self.BaseFormShema.set_value_if_exist(
                    getattr(self.BaseFormShema.BaseView.data,details['name']),details['name']
            )
            if self.if_model(details) and 'custum_name' in details:
                Error.throw_error_bool(
                    details['custum_name'] + ' not exist in object ' + str(self.BaseFormShema.BaseView.data),
                    'custum_name' in details
                )

                place_holder = details['custum_name']
        else:
            place_holder = details['custum_name']
        return place_holder

    def edit_line(self,details):
        self.field_valid(details)
        db=self.set_db(details)
        required= False

        data_type = 'data_type'
        validation= ''

        if 'required' in details:
            required = details['required']

        if 'data_type' in details:
            data_type = details['data_type']

        if 'validation' in details:
            validation = details['validation']

        return {
            'db'          : db,
            'required'    : required,
            'type'        : 'edit_line',
            'name'        : details['name'],
            'data_type'   : data_type,
            'validation'  : validation,
            'place_holder': self.set_placeholder(details),
            'grid_data': self.create_grid(details)
        }

class BaseFormShema:
    from_section=[]
    def __init__(self, BaseView):
        self.BaseView = BaseView
        self.ElmentsShema=FormConstract(self)
        self.form()

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

    def check_if_value_exist(self,args,defult,arry=False):
        hasattr_var = hasattr(args[0], args[1])
        if hasattr_var:
            new_value=getattr(args[0],args[1])
            if new_value:
                if arry:
                    return new_value[0]
                else:
                    return new_value
        return defult

    def set_value_if_exist(self,value,empty):
        if value is None :
            return empty
        return str(value)

    def return_from_section(self):
        return self.from_section

    def is_method(self, method):
        return callable(getattr(self.BaseView, method, None))

    def add_iten(self,item,details):
        if hasattr(self.ElmentsShema,item):
            method=getattr(self.ElmentsShema,item)
            method=method(details)
            if 'loop' in method:
                for el in method['loop']:
                    self.from_section.append(el)
            else:
                self.from_section.append(method)

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
            'db'  : 'name',
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
            'db': 'avatar',
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
            'db'  :'country',
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
            'db': 'year',
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
            'place_holder': 'Edit Galery',
            'name': 'edit_galery',
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

class MenuPaginationForm(BaseFormShema):
    def form(self):
        self.from_section = []
        self.add_iten('button', {
            'place_holder': 'Previous Page',
            'name': 'previous_page',
            "disabled" : self.BaseView.previous,
            "row"      : True,
            "coll"     : True
        })
        self.add_iten('button', {
            'place_holder': 'Next Page',
            'name': 'next_page',
            "disabled": self.BaseView.next,
            "row": False,
            "coll": True,
        })

class AdvanceSearchForm(BaseFormShema):
    def form(self):
        self.from_section = []
        self.add_iten('label', {
            'place_holder': 'Serch fraze',
            'name': 'name',

            "row": False,
            "coll": False
        })
        self.add_iten('edit_line', {
            'place_holder': 'Hukaj',
            'custum_name': self.check_if_value_exist([self.BaseView.Menu,'search_faze'],'Hukaj'),
            'model' : False,
            'name': 'name',
            "row": False,
            "coll": True
        })
        self.add_iten('label', {
            'place_holder': 'Serch in',
            'name': 'name',
            "row": True,
            "coll": False,
            'new_row': True
        })
        self.add_iten('combo_box', {
            'place_holder': 'search_in',
            'name': 'search_in',
            'combo_box_list': [self.BaseView.Menu.search_in,'series', 'stars', 'movies'],
            "row": False,
            "coll": True
        })
        self.add_iten('label', {
            'place_holder': 'Favarite',
            'name': 'name',
            "row": True,
            "coll": False,
            'new_row': True
        })
        self.add_iten('combo_box', {
            'place_holder': 'Favaraite_var',
            'name': 'search_in',
            'combo_box_list': [str(self.BaseView.Menu.AdvandeSearchCriteria.favourite),'','True','False'],
            "row": False,
            "coll": True
        })
        self.add_iten('label', {
            'place_holder': 'Order by',
            'name': 'name',
            "row": True,
            "coll": False,
            'new_row': True
        })
        self.add_iten('combo_box', {
            'place_holder': 'Order by',
            'name': 'search_in',
            'combo_box_list': [str(self.BaseView.Menu.AdvandeSearchCriteria.order_by),'year','likes','views'],
            "row": False,
            "coll": True
        })
        self.add_iten('label', {
            'place_holder': 'Mini',
            'name': 'name',
            "row": True,
            "coll": False,
            'new_row': True
        })
        self.add_iten('combo_box', {
            'place_holder': 'min Order by',
            'name': 'min_order_by',
            'combo_box_list': ['','year','likes','views'],
            "row": False,
            "coll": True
        })
        self.add_iten('edit_line', {
            'place_holder': 'mini',
            'custum_name':'Mini Var',
            'model':False,
            'name': 'name',
            "row": True,
            "coll": True,
            'new_row': True
        })
        self.add_iten('label', {
            'place_holder': 'Max',
            'name': 'name',
            "row": True,
            "coll": False,
            'new_row': True
        })
        self.add_iten('combo_box', {
            'place_holder': 'max_place',
            'name': 'search_in',
            'combo_box_list': ['','year','likes','views'],
            "row": False,
            "coll": True
        })
        self.add_iten('edit_line', {
            'place_holder': 'max_place_var',
            'custum_name':'Max Value',
            'model':False,
            'name': 'name',
            "row": True,
            "coll": True,
            'new_row': True
        })
        self.add_iten('label', {
            'place_holder': 'Series',
            'name': 'name',
            "row": True,
            "coll": False,
            'new_row': True
        })
        self.add_iten('edit_line', {
            'place_holder': 'series_var',
            'custum_name':self.check_if_value_exist([self.BaseView.Menu.AdvandeSearchCriteria,'series'],'Series Name',True),
            'model':False,
            'name': 'name',
            "row": False,
            "coll": True
        })
        self.add_iten('button', {
            'place_holder': 'Add Tag',
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
            "is_submit": True,
            'new_row': True
        })

class MenuFormSchena(BaseFormShema):

    def form(self):
        self.from_section = []
        self.add_iten('label', {
            'place_holder': 'Name',
            'name': 'name',
            "row": False,
            "coll": False
        })

        self.add_iten('edit_line', {
            'place_holder': 'Szukaj',
            'custum_name':self.check_if_value_exist([self.BaseView,'search_faze'],'Hukaj'),
            'name': 'name',
            "row": False,
            "coll": True
        })

        self.add_iten('combo_box', {
            'place_holder': 'search_in',
            'name': 'search_in',
            'combo_box_list': [self.BaseView.search_in, 'series', 'stars', 'movies'],
            "row": False,
            "coll": True
        })

        self.add_iten('button', {
            'place_holder': 'Advance',
            'name': 'advance',
            "row": True,
            "coll": True,
            'new_row': True
        })

        self.add_iten('button', {
            'place_holder': 'Reset',
            'name': 'reset',
            "row": True,
            "coll": True,
            'new_row': True
        })

        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            "row": True,
            "coll": True,
            "is_submit": True,
            'new_row': True
        })

class AddStarToModelForm(BaseFormShema):

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
            'custum_name':'Star name',
            'model':False,
            'name': 'name',
            "row": False,
            "coll": True
        })
        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            "row": False,
            "coll": True,
            "is_submit": True,
        })

class SetPhotoToSeriesForm(AbstractBaseFormShema):

    avatar_dir = '/photo'

    def form(self):
        self.from_section = []
        self.add_iten('photo_loop', {
            'index'      : 'sezons',
            'photo_index': 'src',
            'dir_set'    : self.avatar_dir
        })

        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            "row": True,
            "coll": True,
            "is_submit": True,
            'new_row': True
        })

class JSONDataConfigForm(AbstractBaseFormShema):
    def form(self):
        self.from_section = []
        self.add_iten('label', {
            'place_holder': 'Stars dir',
            'name': 'stars_dir',
            "row": False,
            "coll": False
        })

        self.add_iten('edit_line', {
            'place_holder': 'Stars dir edit label',
            'custum_name':'Stars dir edit label',
            'required' : True,
            'data_type':'dir',
            'model':False,
            'name': 'stars_edit',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Series dir',
            'name': 'series_label',
            'new_row': True,
            "row": True,
            "coll": False
        })

        self.add_iten('edit_line', {
            'place_holder': 'Series dir edit label',
            'custum_name':'Stars dir edit label',
            'required': True,
            'data_type': 'dir',
            'model':False,
            'name': 'series_edit',
            "row": False,
            "coll": True
        })

        self.add_iten('label', {
            'place_holder': 'Movies Photos',
            'name': 'movies_photos_label',
            'new_row': True,
            "row": True,
            "coll": False
        })

        self.add_iten('edit_line', {
            'place_holder': 'Series dir edit label',
            'custum_name':'Stars dir edit label',
            'required': True,
            'data_type': 'dir',
            'model':False,
            'name': 'movies_photos_edit',
            "row": False,
            "coll": True
        })

        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            'new_row': True,
            "row": True,
            "coll": True,
            "is_submit": True,
        })

class TagsForm(BaseFormShema):

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
            'custum_name':'Tag name',
            'model':False,
            'name': 'name',
            "row": False,
            "coll": True
        })
        self.add_iten('button', {
            'place_holder': 'Submit',
            'name': 'submit_click',
            "row": False,
            "coll": True,
            "is_submit": True,
        })

class TagsFormAddToSearch(TagsForm):
    def form(self):
        super().form()
        self.add_iten('button', {
            'place_holder': 'save',
            'name': 'save_click',
            "row": False,
            "coll": True,
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
            'db': 'height',
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
            'db': 'weight',
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
            'db': 'ethnicity',
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
            'db': 'hair_color',
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
            'db': 'date_of_birth',
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
            'db': 'none',
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
            'db': 'singles',
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




