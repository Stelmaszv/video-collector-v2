from core.datamanipulation import Data as Data
class BaseInfo:
    data_info=[]
    def __init__(self, Obj=None, methods=[]):
        if Obj is not None:
            self.BaseView=Obj.BaseView
            self.list=Obj.list

class SingleSectionInfo(BaseInfo):

    def set_obj(self,Obj):
        self.Obj=Obj

    def return_data(self):
        return  [
            {"itemNmae" : "Year","itemName2" :"anser1"},
            {"itemNmae" : "anser2","itemName2" :"anser2"},
            {"itemNmae": "anser3","itemName2" :"anser2"}
        ]

class InfoSection(BaseInfo):
    def return_data(self):
        self.data_info.append({})
        return  self.data_info


class StarInfoSection(BaseInfo):
    def return_data(self):
        self.data_info=[]
        self.add_date_of_birth()
        self.add_height_and_weight()
        self.if_data(self.BaseView.data.ethnicity,'Ethnicity')
        self.if_data(self.BaseView.data.hair_color, 'Hair color')
        self.add_series_and_movies()
        self.add_views_and_likes()
        self.if_data(str(self.BaseView.data.favourite), 'Favourite')
        return  self.data_info

    def add_date_of_birth(self):
        DataObj=None
        if self.BaseView.data.date_of_birth:
            DataObj = Data(self.BaseView.data.date_of_birth)

        if DataObj is not None:
            self.data_info.append({
                "itemNmae": "Date of birth / Age",
                "itemName2": DataObj.show() + ' / ' + DataObj.get_age()
            })

    def add_height_and_weight(self):

        if self.BaseView.data.height and self.BaseView.data.weight:
            self.data_info.append({
                "itemNmae": "Height / Weight",
                "itemName2": str(self.BaseView.data.height) + ' cm  / ' + str(self.BaseView.data.weight) + ' kg'
            })

    def add_series_and_movies(self):

        self.data_info.append({
            "itemNmae": "Movies / Series",
            "itemName2": self.count_series() + ' / ' + self.count_movies()
        })

    def is_method(self, method):
        return callable(getattr(self.BaseView, method, None))

    def add_views_and_likes(self):
        self.data_info.append({
            "itemNmae": "Views / Likes",
            "itemName2": str(self.BaseView.data.views) + ' / ' + str(self.BaseView.data.likes)
        })

    def if_data(self,data,name):

        if data:
            self.data_info.append({
                "itemNmae":  name,
                "itemName2": data
            })

    def count_series(self):
        return str(len(self.list))

    def count_movies(self):
        count = 0;
        for item in self.list:
            count = count + len(item['movies'])
        return str(count)







