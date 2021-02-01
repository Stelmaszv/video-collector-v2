from app.db.models import session
from PyQt5 import QtGui,QtCore, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from datetime import datetime
from core.datamanipulation import DataValidator
from app.db.models import Tags

class ViewBaseAction:

    def __init__(self,obj):
        self.session = session
        self.obj=obj

    def update_view(self):
        self.obj.data.views=self.obj.data.views+1;
        self.session.commit()

    def add_like(self):
        self.obj.data.likes = self.obj.data.likes + 1;
        self.session.commit()
        self.reset()

    def edit(self):
        self.obj.close()
        self.obj.BaseView.load_view('edit_star',self.obj.data)
        return True;

    def add_favourite(self):

        if self.obj.data.favourite is True:
            stan=False
        else:
            stan=True

        self.obj.data.favourite = stan;
        self.session.commit()
        self.reset()

    def reset(self):
        self.obj.close()
        self.obj.BaseView.load_view('stars',self.obj.data)
        return True;

class AddTag:

    model=Tags

    def __init__(self,data,Obj_data):
        self.data=data
        self.Obj=Obj_data
        self.session = session

    def add(self):
        value = self.data[0]['value']

        add=False

        for item in self.Obj.tags:
            if item.name == value:
                add=True

        in_db=False
        query=self.session.query(self.model).filter(self.model.name==value).first()

        if query:
            in_db = True;

        if in_db is False and add is False:
            self.add_tag_to_db(value)
            self.add_tag_from_db(value)

        if in_db is True and add is False:
            self.add_tag_from_db(value)

    def add_tag_to_db(self,value):
        self.session.add_all([self.model(name=value)])
        self.session.commit()

    def add_tag_from_db(self,value):
        item = self.session.query(self.model).filter(self.model.name == value).first()
        self.Obj.tags.append(item)


class Submit:

    def __init__(self,Model,Data,Obj):
        self.Model = Model(Data)
        self.Obj   = Obj

    def set_data(self,values):
        self.data=values

    def run(self):
        error = []
        for item in self.data:
            if item['data-type'] == 'data':
                ymd = item['value'].split('-')
                if len(ymd)==3:
                    DV = DataValidator()
                    DV.error=[]
                    DV.set_data(int(ymd[0]),ymd[1],int(ymd[2]))
                    DV.validate_data()

                    if len(DV.error)==0:
                        item['value']=datetime(DV.year,DV.mount,DV.day)
                    else:
                        for error_from_DV in DV.error:
                            error.append(error_from_DV)
                else:
                    if len(ymd[0])>0:
                        if len(ymd) == 1 or len(ymd) == 2:
                            error.append('Data is invalid')

        if len(error) == 0:
            self.add_data_to_model()

        if len(error) > 0:
            data =[
                'Errors in form',
                self.form_to_string(error),
                ''
            ]
            self.Obj.BaseView.Massage.show(data)


    def form_to_string(self,errors):

        string="<html><head/><body>";
        for error in errors:
            string+=error+'<br>'
        string +='</body></html>'
        return str(string)

    def add_data_to_model(self):
        self.Model.add_data(self.data)
        self.Obj.close()
        self.Obj.BaseView.load_view('stars', self.Obj.data)
        return True;

class FormSection:

    def __init__(self,obj):
        self.obj=obj

    def form_section(self, data, buttons=[]):
        self.widget_edit_section = QtWidgets.QWidget(self.obj)
        self.widget_edit_section.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.widget_edit_section.setObjectName("widget_edit_section")
        self.edit_section_grid = QtWidgets.QGridLayout(self.widget_edit_section)
        self.edit_section_grid.setContentsMargins(0, 0, 0, 0)
        self.edit_section_grid.setObjectName("edit_section_grid")
        grid_array = []
        for item in buttons:
            if item['type'] == 'button':
                self.button(
                    item,
                    self.edit_section_grid
                )

            if item['type'] == 'label':
                self.label(
                    [item['name'], item['place_holder']],
                    item['grid_data'],
                    self.edit_section_grid
                )

            if item['type'] == 'edit_line':
                edit_line = self.edit_line2(
                    item['place_holder'],
                    item['grid_data'],
                    self.edit_section_grid,
                    item['validation'],
                )
                grid_array.append(
                    {
                        'item': item,
                        'button': edit_line
                    }
                )

        submit = self.faind_submit(buttons)
        self.button_submit(
            submit,
            self.edit_section_grid,
            grid_array
        )

    def button (self,info,grid):
        button = QtWidgets.QPushButton(self.obj)
        button.setObjectName(info['obj_name'])
        button.setText(info['name'])
        grid.addWidget(
            button,
            info['grid_data'][0],
            info['grid_data'][1],
            info['grid_data'][2],
            info['grid_data'][3]
        )
        button.clicked.connect(lambda: info['click']('data'))

    def button_submit(self,submit,grid,grid_array):
        button = QtWidgets.QPushButton(self.obj)
        button.setObjectName(submit['obj_name'])
        button.setText(submit['name'])

        grid.addWidget(
            button,
            submit['grid_data'][0],
            submit['grid_data'][1],
            submit['grid_data'][2],
            submit['grid_data'][3]
        )

        button.clicked.connect(lambda :submit['click'](self.get_values(grid_array)))

    def label(self,info,data,grid,el=None):
        if el is not None:
            el=self.obj

        label = QtWidgets.QLabel(el)
        label.setObjectName(info[0])
        label.setText(info[1])
        grid.addWidget(label, data[0], data[1], data[2], data[3])
        return label

    def edit_line2(self,placeholder,data,grid,validator):
        from PyQt5.QtGui import QIntValidator
        line = QtWidgets.QLineEdit(self.obj)
        line.setPlaceholderText(placeholder)
        if validator:
            reg_ex = QRegExp(validator)
            validator_obj = QRegExpValidator(reg_ex, line)
            line.setValidator(validator_obj)

        grid.addWidget(line,data[0], data[1], data[2], data[3])
        return line

    def get_values(self,grid):
        values=[]
        for item in grid:
            values.append(
                {
                    'name' :item['item']['place_holder'],
                    'value':item['button'].text(),
                    'data-type':item['item']['data_type'],
                    'DB': item['item']['DB']
                }
            )
        return values;

    def faind_submit(self,buttons):
        for item in buttons:
            if item['type'] == 'button_submit':
                return item


