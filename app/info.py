from core.datamanipulation import Data as Data
class BaseInfo:
    data_info=[]
    def __init__(self, Obj=None, methods=[]):
        if Obj is not None:
            self.BaseView=Obj.BaseView
            self.list=Obj.list

class SingleSectionInfo(BaseInfo):

    def set_obj(self,Obj,item):
        self.Obj=Obj
        self.item=item

    def return_data(self):
        self.data_info = []
        info_item = None
        for el in self.Obj.sezons:
            if int(el.name)==int(self.item):
                info_item=el
        count = self.count_in_seazon(info_item)
        stars_in_seazom= self.stars_to_string(self.count_star(info_item))

        if info_item.year:
            self.data_info.append({
                "itemNmae": "Year",
                "itemName2": info_item.year
            })
        if count>1:
            self.data_info.append({
                "itemNmae": "Movies",
                "itemName2": str(count)
            })
            if info_item.sezon_name:
                self.data_info.append({
                    "itemNmae": "Name",
                    "itemName2": info_item.sezon_name
                })

        if stars_in_seazom:
            self.data_info.append({
                "itemNmae": "Stars",
                "itemName2": stars_in_seazom
            })
        return self.data_info

    def stars_to_string(self,stars):
        stars_str=''
        count=0
        for el in stars:
            if count>1:
                stars_str=stars_str+' , '
            stars_str=stars_str+str(el.name)
            count=count+1

        return stars_str
    def count_star(self,seazon):
        stars=[]
        def add_if_not_exist(Star):
            stan=False
            for item in stars:
                if item.id == Star.id:
                    stan=True

            if stan is False:
                stars.append(Star)

        for item in self.Obj.movies:
            if int(seazon.name) == item.sezon:
                for star in item.stars:
                    add_if_not_exist(star)

        return stars

    def count_in_seazon(self,seazon):
        count=0
        for item in self.Obj.movies:
            if int(seazon.name) == item.sezon:
                count=count+1
        return count

class InfoSection(BaseInfo):

    def return_data(self):
        self.data_info=[]
        if self.BaseView.data.years:
            self.data_info.append({
                "itemNmae": "Year",
                "itemName2": self.BaseView.data.years
            })
        if len(self.BaseView.data.sezons) != len(self.BaseView.data.movies):
            self.data_info.append({
                "itemNmae": "Sezons",
                "itemName2": str(len(self.BaseView.data.sezons))
            })
        self.data_info.append({
            "itemNmae": "Movies",
            "itemName2": str(len(self.BaseView.data.movies))
        })
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







