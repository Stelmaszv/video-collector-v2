from PyQt5.QtWidgets import QWidget

from app.db.models import Series
from app.forms import AdvanceSearchForm
from core.setings import series_defult, show_limit, stars_defult, tags_defult
from core.view import AbstractBaseView
from view.menu.menu import Menu

from .add_tag_advance_search import (AddStarsAdvnaceSearchView,
                                     AddTagAdvnaceSearchView)


class AdvanceSearch(QWidget,AbstractBaseView):
    FormSchema = AdvanceSearchForm
    model_view_off = True
    show_elemnts = ['Title', 'Info', 'Galery', 'Nav', 'Avatar','List']
    resolution_index = 'advande_search'
    window_title = 'Advance Search'
    reset_view = 'advance_search'
    criterions = {'Tags':tags_defult[1:],'Stars':stars_defult[1:],'Series':series_defult[1:]}
    Menu=Menu(0)
    limit=show_limit

    def add_star(self,values):
        self.close()
        ATASV = AddStarsAdvnaceSearchView()
        ATASV.data_array = list(self.criterions['Stars'])
        ATASV.run_window()

    def add_tag(self,values):
        self.close()
        ATASV=AddTagAdvnaceSearchView()
        ATASV.data_array=list(self.criterions['Tags'])
        ATASV.run_window()

    def set_up(self):
        def set_rage(array, limit):
            if len(array) > limit:
                return limit
            else:
                return len(array)
        def array_list(array):

            string=''
            counter=0
            range_var=set_rage(array,self.limit)

            for item in range(0,range_var):
                string=string+array[counter]
                if counter>-1 and counter<range_var-1:
                    string=string+', '
                counter=counter+1

            if range_var < len(array):
                string = string+' and others '+str(len(array)-range_var)
            return string

        tags=array_list(self.criterions['Tags'])
        self.custom_title('Tags', 'tags_name')
        text ="< html > < head / > < body > < p align =\"left\">"+str(tags)+"</body></html>"
        self.custum_description('tags','tags_limit',text)

        self.custom_title('Stars', 'star_name')
        stars = array_list(self.criterions['Stars'])
        text = "< html > < head / > < body > < p align =\"left\">" + str(stars) + "</body></html>"
        self.custum_description('stars', 'stars_limit', text)

    def valid_series(self,value):
        data = self.session.query(Series).filter(Series.name == value).first()
        if data == None:
            data = [
                "Not Found series " + value + " !",
                '',
                ''
            ]
            self.BaseView.Massage.show(data)
            return False
        else:
            array = list(self.criterions['Series'])
            array.append(value)
            self.criterions['Series']=array
            return True

    def submit_click(self,values):
        error=True
        series=None
        def convert_to_bool(value):
            if len(value):
                if value == 'True':
                    value = True
                elif value == 'False':
                    value = False
                elif value == '' or value == 'None':
                    value = None
                return value
            return None

        def set_serch_in(value):
            if value:
                return value
            return self.Menu.search_in


        if len(values[8]['value']):
            error=self.valid_series(values[8]['value'])
            if error:
                series=[values[8]['value']]

        if error:
            self.close()
            self.Menu.close()
            self.Menu.search_in = set_serch_in(values[1]['value'])
            self.Menu.AdvandeSearchCriteria.favourite=convert_to_bool(values[2]['value'])
            self.Menu.AdvandeSearchCriteria.order_by = values[3]['value']

            if len(values[4]['value']) and len(values[5]['value']):
                self.Menu.AdvandeSearchCriteria.min = [values[4]['value'],int(values[5]['value'])]

            if len(values[6]['value']) and len(values[7]['value']):
                self.Menu.AdvandeSearchCriteria.max = [values[6]['value'], int(values[7]['value'])]

            self.Menu.AdvandeSearchCriteria.series = tuple(self.criterions['Series'])
            self.Menu.AdvandeSearchCriteria.tags  = tuple(self.criterions['Tags'])
            self.Menu.AdvandeSearchCriteria.stars = tuple(self.criterions['Stars'])
            self.Menu.run_window()

