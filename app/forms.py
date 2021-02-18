from core.view import BaseFormShema

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
                'click': self.BaseView.add_tag,
                'arguments': []
            })
                
            self.from_section.append({
                'type': 'button_submit',
                'obj_name': 'submit',
                'name': 'Submit',
                'place_holder': 'Submit',
                'grid_data': [11, 1, 1, 1],
                'click': self.BaseView.submit_click,
                'arguments': []
            })



