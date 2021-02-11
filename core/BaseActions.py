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
        self.obj.BaseView.load_view(self.obj.edit_view,self.obj.data)
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
        self.obj.BaseView.load_view(self.obj.reset_view,self.obj.data)
        return True;

class AddTag:

    model=Tags

    def __init__(self,data,Obj):
        self.data=data
        self.Obj=Obj.data
        self.session = session
        self.ViewBaseAction=ViewBaseAction(Obj)

    def remove_tag(self,tag):
        value=tag.name
        add=False
        for item in self.Obj.tags:
            if item.name == value:
                add=True

        if add:
            self.Obj.tags.remove(tag)
            self.ViewBaseAction.reset()

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

        self.ViewBaseAction.reset()

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
                if len(ymd) == 3:
                    DV = DataValidator()
                    DV.error = []
                    DV.set_data(int(ymd[0]), ymd[1], int(ymd[2]))
                    DV.validate_data()
                    item['value'] = datetime(DV.year, DV.mount, DV.day)

        if len(error) == 0:
            self.add_data_to_model()

        if len(error) > 0:
            data = [
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
        if self.Obj.data is not None:
            self.Obj.BaseView.load_view(self.Obj.submit_view, self.Obj.data)
        return True

class FormSection:

    def __init__(self,obj):
        self.obj=obj

    def faind_clandar_value(self,buttons):
        clendar_value=None
        for item in buttons:
            if item['type'] == "calendar_value":
                clendar_value=item
        return clendar_value

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

            if item['type'] == 'combo_box':
                combo=self.combo_box(
                    item['grid_data'],
                    self.edit_section_grid,
                    item['combo_box_list']
                )
                grid_array.append(
                    {
                        'item': item,
                        'value_show' : combo.currentText(),
                        'button': combo
                    }
                )

            if item['type'] == "calendar":

                edit_line = self.edit_line2(
                    item['place_holder'],
                    [6, 1, 1, 1],
                    self.edit_section_grid,
                    item['validation'],
                )
                grid_array.append(
                    {
                        'item': item,
                        'value_show' : edit_line.text(),
                        'button': edit_line
                    }
                )

                self.calendar(
                    item['grid_data'],
                    self.edit_section_grid,
                    edit_line
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
                        'value_show': edit_line.text(),
                        'button': edit_line
                    }
                )
        submit = self.faind_submit(buttons)
        if submit is not None:
            submit = self.faind_submit(buttons)
            self.button_submit(
                submit,
                self.edit_section_grid,
                grid_array
            )

    def combo_box(self,data,grid,combo_list):
        combo_box = QtWidgets.QComboBox(self.obj)
        combo_box.addItems(combo_list)
        grid.addWidget(combo_box,data[0], data[1], data[2], data[3])
        return combo_box

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

    def calendar(self,data,grid,label=False):

        def convert_data(number):
            if number < 10:
                return '0'+str(number)
            return str(number)

        def show_date(date):
            data= str(date.year())+'-'+convert_data(date.month())+'-'+convert_data(date.day())
            label.setText(data)

        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        currentDay   = datetime.now().day

        calender = QtWidgets.QCalendarWidget(self.obj)
        calender.setMaximumDate(QtCore.QDate(currentYear,currentMonth,currentDay))
        date = calender.selectedDate()
        calender.clicked[QtCore.QDate].connect(show_date)
        grid.addWidget(calender,data[0], data[1], data[2], data[3])
        return calender

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

        def show_value(data):

            if data['item']['type'] == 'edit_line' or data['item']['type'] == 'calendar':
                return  data['button'].text()

            if data['item']['type'] == 'combo_box':
                return  data['button'].currentText()

        for item in grid:
            values.append(
                {
                    'name' :item['item']['place_holder'],
                    'value':str(show_value(item)),
                    'data-type':item['item']['data_type']
                }
            )
        return values;

    def faind_submit(self,buttons):
        for item in buttons:
            if item['type'] == 'button_submit':
                return item


