class StarsForm:

    def __init__(self,BaseView):
        self.BaseView=BaseView
        self.set_form()

    def set_form(self):
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
            'combo_box_list': ['', 'Black', 'Asian', 'Arab', 'White'],
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
            'combo_box_list': ['', 'Black', 'Gray', 'Brown', 'Blond']
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

        self.from_section.append({
            'type': 'label',
            'name': 'none_label',
            'place_holder': 'None avatar',
            'grid_data': [7, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'none_edit_line',
            'data_type': 'dir',
            'validation': "",
            'place_holder': self.set_value_if_exist(self.BaseView.data.none,'None dir avator'),
            'grid_data': [7, 1, 1, 1]
        })

        self.from_section.append({
            'type': 'label',
            'name': 'singles_edit_line_label',
            'place_holder': 'Singles avatar',
            'grid_data': [8, 0, 1, 1]
        })

        self.from_section.append({
            'type': 'edit_line',
            'name': 'singles_edit_line',
            'data_type': 'dir',
            'validation': "",
            'place_holder': self.set_value_if_exist(self.BaseView.data.singles,'Singles dir avator'),
            'grid_data': [8, 1, 1, 1]
        })

        self.from_section.append({
            'type': 'button',
            'obj_name': 'add_tags',
            'name': 'Add Tags',
            'place_holder': 'Tags',
            'grid_data': [9, 1, 1, 1],
            'click': self.BaseView.add_tag
        })

        self.from_section.append({
            'type': 'button_submit',
            'obj_name': 'submit',
            'name': 'Submit',
            'place_holder': 'Submit',
            'grid_data': [10, 1, 1, 1],
            'click': self.BaseView.submit_click
        })



    def set_value_if_exist(self,value,empty):
        if value is None :
            return empty
        return str(value)

    def return_from_section(self):
        return self.from_section