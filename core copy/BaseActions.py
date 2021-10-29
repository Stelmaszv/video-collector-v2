import os
from app.db.models import session
from PyQt5 import QtGui,QtCore, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from datetime import datetime
from core.datamanipulation import DataValidator
from core.dir import AddStarViaDir, set_dir_for_star
from app.db.models import Tags,Stars
from core.custum_errors import Error
from pathlib import Path
from abc import ABC,abstractmethod
from core.setings import photo_ext,with_size_defult,height_size_defult

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
        if hasattr(self.obj, 'edit_view'):
            self.obj.BaseView.load_view(self.obj.edit_view,self.obj.data)
        else:
            Error.throw_error(self.obj.__class__.__name__+' do not have atter "edit_view" ',False)

    def add_favourite(self):
        if self.obj.data.favourite is True:
            stan = False
        else:
            stan = True

        self.obj.data.favourite = stan;
        self.session.commit()
        self.reset()

    def reset(self):
        if hasattr(self.obj,'reset_view'):
            self.obj.close()
            self.obj.BaseView.load_view(self.obj.reset_view,self.obj.data)
        else:
            Error.throw_error(self.obj.__class__.__name__+' do not have atter "reset_view" ',False)

class AbstractAddToModel(ABC):

    Model=None
    field = ''
    dialog_mes='Dialog'

    def __init__(self,data,Obj):
        self.data=data
        self.Obj=Obj.data
        Error.throw_error_bool(
            self.Obj.__class__.__name__+' do not have atter "'+self.field+'" ',
            hasattr(self.Obj,self.field)
        )
        self.field=getattr(self.Obj,self.field)
        self.Obj_var = Obj
        self.session = session
        self.ViewBaseAction=ViewBaseAction(Obj)

    def faind_item(self,var):
        add = False
        for item in self.field:
            if item.name == var:
                add = True
        return add

    def remove(self, Star):
        add=self.faind_item(Star.name)

        if add:
            self.field.remove(Star)

    def set_new_dialog(self,mess):
        if str(mess) and len(mess):
            return mess
        else:
            return self.dialog_mes

    def add(self):
        self.value = self.data[0]['value']
        self.dialog_mes=self.set_new_dialog(
            self.set_dialog_mess()
        )
        self.in_db = False
        add = self.faind_item(self.value)
        self.AddObj = self.session.query(self.Model).filter(self.Model.name == self.value).first()

        if self.AddObj:
            self.in_db = True

        if len(self.value) > 0:
            if self.in_db is False and add is False:
                self.Obj_var.BaseView.Massage.set_resolution(self.Obj_var.get_dialog_location())
                self.Obj_var.BaseView.Massage.dialog(
                    self.dialog_mes,
                    self.accept,
                    self.cancel
                )
            else:
                self.in_db = True

        if self.in_db is True and add is False:
            self.add_to_object()
            self.ViewBaseAction.reset()

    @abstractmethod
    def add_to_object(self):
        pass

    def cancel(self):
        pass

    @abstractmethod
    def accept(self):
        pass

    @abstractmethod
    def set_dialog_mess(self):
        pass

class AddStar(AbstractAddToModel):

    field='stars'
    Model = Stars

    def add_to_object(self):
        self.Obj.stars.append(self.AddObj)

    def set_dialog_mess(self):
        return '<h2>Star "' + self.value + '" no exist in db do you wont to add ?</h2>'

    def accept(self):
        ASVD = AddStarViaDir(set_dir_for_star(self.value))
        self.AddObj = ASVD.star
        self.in_db = True

class AddTag(AbstractAddToModel):
    field = 'tags'
    Model = Tags

    def add_to_object(self):
        self.Obj.tags.append(self.AddObj)

    def set_dialog_mess(self):
        return '<h2>Tag "' + self.value + '" no exist in db do you wont to add ?</h2>'

    def accept(self):
        Tag=self.Model(name=self.value)
        self.session.add_all([Tag])
        self.session.commit()
        self.AddObj = Tag
        self.in_db = True

class Submit:

    Model = None
    Obj   = None
    auto_model =True
    data  = []

    def __init__(self,Model=None,Data=[],Obj=None):
        self.Model = Model(Data)
        self.Obj   = Obj

    def set_data(self,values):
        self.data=values

    def run(self):
        self.error = []
        for item in self.data:
            if 'required' in item:
                if len(item['value']) == 0 and item['required'] is True:
                    self.error.append("<b>" + item['error'] + "</b> is required !")

            if 'data-type' in item:
                if item['data-type'] == 'dir_create':
                    if os.path.isdir(item['value']) is False:
                        if item['value']:
                            os.mkdir(item['value'])

                if item['data-type'] == 'photo_location':
                    if len(item['value']) > 0:
                        if Path(item['value']).is_file() is False:
                            self.error.append(item['value']+" is not a file")
                        else:
                            if item['value'].endswith(photo_ext) is False:
                                self.error.append('File '+item['value']+' is not photo '+str(photo_ext))

                if item['data-type'] == 'dir':
                    if len(item['value']) > 0:
                        if os.path.isdir(item['value']) is False:
                            self.error.append("Invalid dir location in <b>"+item['error']+"</b>")

                if item['data-type'] == 'data':
                    ymd = item['value'].split('-')
                    if len(ymd) == 3:
                        DV = DataValidator()
                        DV.error = []
                        DV.set_data(int(ymd[0]), ymd[1], int(ymd[2]))
                        DV.validate_data()
                        item['value'] = datetime(DV.year, DV.mount, DV.day)

        if len(self.error) == 0:
            if self.auto_model:
                self.add_data_to_model()

        if len(self.error) > 0:
            data = [
                'Errors in form',
                self.form_to_string(self.error),
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
            if hasattr(self.Obj, 'submit_view'):
                self.Obj.BaseView.load_view(self.Obj.submit_view, self.Obj.data)
            else:
                Error.throw_error(self.Obj.__class__.__name__ + ' do not have atter "submit_view" ')
        return True

class Form:

    run=0

    def __init__(self, BaseView):
        self.BaseView=BaseView

    def buttom_genarator(self,list,fuction,id):
        self.run=self.run+1
        if self.run == 1:
            for button in list.buttons():
                if button is list.button(id):
                    fuction(list.button(id).data)

    def button_loop(self, el, grid, item, data, info, index,size=[]):
        button = QtWidgets.QPushButton(el)
        with_size=with_size_defult
        height_size=height_size_defult
        if size:
            with_size =size[0]
            height_size  =size[1]
        button.setMinimumSize(QtCore.QSize(with_size, height_size))
        button.setObjectName("InfoButton")
        button.setText(info[0])
        button.data = item
        grid.addWidget(button, data[0], data[1], data[2], data[3])
        self.buttons_loop[index]['obejct'].addButton(button)
        self.buttons_loop[index]['obejct'].buttonClicked[int].connect(self.buttons_loop[index]['button'])

    def button (self,info,grid=None,list=[]):
        button = QtWidgets.QPushButton(self.BaseView)
        button.setObjectName(info['obj_name'])
        button.setText(info['name'])
        button.setEnabled(info['disabled'])
        if grid is not None:
            grid.addWidget(
                button,
                info['grid_data'][0],
                info['grid_data'][1],
                info['grid_data'][2],
                info['grid_data'][3]
            )
        if grid is None:
            button.setGeometry(info['grid_data'][0],info['grid_data'][1],info['grid_data'][2],info['grid_data'][3])
        button.clicked.connect(lambda: info['click'](list))

    def combo_box(self,data,combo_list,grid=None):
        combo_box = QtWidgets.QComboBox(self.BaseView)
        combo_box.addItems(combo_list)
        if grid is not None:
            grid.addWidget(combo_box,data[0], data[1], data[2], data[3])
        return combo_box

    def photo(self,data,grid,photo_url,size,el=None):
        if el is not None:
            el=self.BaseView
        item = QtWidgets.QLabel(el)
        item.setMaximumSize(QtCore.QSize(size[0],size[1]))
        item.setText("")
        item.setPixmap(QtGui.QPixmap(photo_url))
        item.setScaledContents(True)
        item.setObjectName("galeryItem")
        grid.addWidget(item, data[0], data[1], data[2], data[3])

    def label(self,info,data,grid,el=None):
        if el is not None:
            el=self.BaseView

        label = QtWidgets.QLabel(el)
        label.setObjectName(info[0])
        label.setText(info[1])
        grid.addWidget(label, data[0], data[1], data[2], data[3])
        return label

    def edit_line(self,placeholder,data,grid,validator):
        from PyQt5.QtGui import QIntValidator
        line = QtWidgets.QLineEdit(self.BaseView)
        line.setPlaceholderText(placeholder)
        if validator:
            reg_ex = QRegExp(validator)
            validator_obj = QRegExpValidator(reg_ex, line)
            line.setValidator(validator_obj)

        grid.addWidget(line,data[0], data[1], data[2], data[3])
        return line


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

        calender = QtWidgets.QCalendarWidget(self.BaseView)
        calender.setMaximumDate(QtCore.QDate(currentYear,currentMonth,currentDay))
        date = calender.selectedDate()
        calender.clicked[QtCore.QDate].connect(show_date)
        grid.addWidget(calender,data[0], data[1], data[2], data[3])
        return calender

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
                    'name': item['item']['name'],
                    'place_holder' :item['item']['place_holder'],
                    'value':str(show_value(item)),
                    'data-type':item['item']['data_type']
                }
            )
        return values

class FormSection:

    def __init__(self, BaseView):
        self.BaseView=BaseView
        self.Form=Form(self.BaseView)

    def faind_clandar_value(self,buttons):
        clendar_value=None
        for item in buttons:
            if item['type'] == "calendar_value":
                clendar_value=item
        return clendar_value

    def form_section(self, data, buttons=[]):
        self.widget_edit_section = QtWidgets.QWidget(self.BaseView)
        self.widget_edit_section.setGeometry(QtCore.QRect(data[0], data[1], data[2], data[3]))
        self.widget_edit_section.setObjectName("widget_edit_section")
        self.edit_section_grid = QtWidgets.QGridLayout(self.widget_edit_section)
        self.edit_section_grid.setContentsMargins(0, 0, 0, 0)
        self.edit_section_grid.setObjectName("edit_section_grid")
        grid_array = []
        for item in buttons:
            if item['type'] == 'button':
                self.Form.button(
                    item,
                    self.edit_section_grid,
                    grid_array
                )

            if item['type'] == 'combo_box':
                combo=self.Form.combo_box(
                    item['grid_data'],
                    item['combo_box_list'],
                    self.edit_section_grid
                )
                grid_array.append(
                    {
                        'item': item,
                        'value_show' : combo.currentText(),
                        'button': combo
                    }
                )

            if item['type'] == "calendar":
                edit_line = self.Form.edit_line(
                    item['place_holder'],
                    item['grid_data'],
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

                self.Form.calendar(
                    item['grid_data'],
                    self.edit_section_grid,
                    edit_line
                )

            if item['type'] == 'label':
                self.Form.label(
                    [item['name'], item['place_holder']],
                    item['grid_data'],
                    self.edit_section_grid
                )

            if item['type'] == 'edit_line':
                edit_line = self.Form.edit_line(
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
    def button_submit(self,submit,grid,grid_array):
        button = QtWidgets.QPushButton(self.BaseView)
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

    def get_values(self,grid):
        values=[]
        def show_value(data):

            if data['item']['type'] == 'edit_line' or data['item']['type'] == 'calendar':
                return  data['button'].text()

            if data['item']['type'] == 'combo_box':
                return  data['button'].currentText()

        def set_requierd(item):
            if 'required' in item['item']:
                return item['item']['required']
            return None

        for item in grid:
            db = ''
            if 'db' in item['item']:
                db=item['item']['db']
            values.append(
                {
                    'required' : set_requierd(item),
                    'name'     : item['item']['place_holder'],
                    'error'    : item['item']['name'],
                    'value'    : str(show_value(item)),
                    'data-type': item['item']['data_type'],
                    'db'       : db
                }
            )

        return values;

    def faind_submit(self,buttons):
        for item in buttons:
            if item['type'] == 'button_submit':
                return item


