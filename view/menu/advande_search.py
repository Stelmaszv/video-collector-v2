from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.forms import AdvanceSearchForm
from view.menu.menu import Menu
from app.db.models import Series
from  .add_tag_advance_search import AddTagAdvnaceSearchView,AddStarsAdvnaceSearchView
class AdvanceSearch(QWidget,AbstractBaseView):
    FormSchema = AdvanceSearchForm
    model_view_off = True
    show_elemnts = ['Title', 'Info', 'Galery', 'Nav', 'Avatar','List']
    resolution_index = 'advande_search'
    window_title = 'Advance Search'
    reset_view = 'advance_search'
    criterions = {'Tags':[],'Stars':[]}
    Menu=Menu(0)
    limit=5

    def add_star(self,values):
        self.close()
        ATASV = AddStarsAdvnaceSearchView()
        ATASV.data_array = self.criterions['Stars']
        ATASV.run_window()

    def add_tag(self,values):
        self.close()
        ATASV=AddTagAdvnaceSearchView()
        ATASV.data_array=self.criterions['Tags']
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

    def submit_click(self,values):
        error=True
        series=None
        def convert_to_bool(value):
            if len(value):
                if value == 'True':
                    value = 1
                else:
                    value = 0
                print(value)
                return value
            return ''

        def set_serch_in(value):
            if value:
                return value
            return self.Menu.search_in
        def valid_series(value):
            data = self.session.query(Series).filter(Series.name == value).first()
            if data==None:
                data = [
                    "Not Found series "+value+" !",
                    '',
                    ''
                ]
                self.BaseView.Massage.show(data)
                return False
            return True

        if len(values[8]['value']):
            error=valid_series(values[8]['value'])
            if error:
                series=[values[8]['value']]
        if error:
            self.close()
            self.Menu.close()
            self.Menu.search_in = set_serch_in(values[1]['value'])
            self.Menu.AdvandeSearchCriteria.favourite=convert_to_bool(values[2]['value'])
            self.Menu.AdvandeSearchCriteria.order_by = values[3]['value']
            self.Menu.AdvandeSearchCriteria.series=series

            if len(values[4]['value']) and len(values[5]['value']):
                self.Menu.AdvandeSearchCriteria.min = [values[4]['value'],int(values[5]['value'])]

            if len(values[6]['value']) and len(values[7]['value']):
                self.Menu.AdvandeSearchCriteria.max = [values[6]['value'], int(values[7]['value'])]

            self.Menu.AdvandeSearchCriteria.stars = tuple(self.criterions['Stars'])
            self.Menu.AdvandeSearchCriteria.tags  =tuple(self.criterions['Tags'])
            self.Menu.run_window()

