from core.custum_errors import Error

class BaseNav:
    base_nav=[]
    row=0
    coll=-1
    def __init__(self,AbstractBaseView):
        self.BaseActions =  AbstractBaseView.BaseActions
        self.data        =  AbstractBaseView.data
        self.AbstractBaseView = AbstractBaseView

    def set_name_for_favorits(self):
        name= 'Add to favorits'
        if self.data.favourite:
            name= 'Remove from favorits'
        return name

    def set_data(self,data):
        self.data = data
        self.set_base_nav()

    def set_nav(self):
        return self.base_nav

    def click(self,data):
        Error.throw_error_bool(
            'Function '+data['function']+' not found in '+data['obj'].__class__.__name__+'',
            hasattr(data['obj'],data['function'])
        )
        return getattr(data['obj'],data['function'])

    def add_button(self,data):
       self.coll = self.coll + 1
       return {
            "name": data['name'],
            "disabled" :True,
            "obj_name": data['obj_name'],
            "grid_data": [0, self.coll, 1, 1],
            "click": self.click(data['click']),
            'arguments': [],
        }


    def set_base_nav(self):
        self.base_nav =[
            self.add_button({
                "name": self.set_name_for_favorits(),
                "obj_name": "add_to_favorits",
                "click": {"obj": self, "function": 'add_favorits'}
            }),
            self.add_button({
                "name": "Add like",
                "obj_name": "add_like",
                "click": {"obj": self, "function": 'add_like'}
            }),
            self.add_button({
                "name": "Edit",
                "obj_name": "edit",
                "click": {"obj": self, "function": 'edit'}
            }),
            self.add_button({
                "name": "Reset",
                "obj_name": "reset",
                "click": {"obj": self, "function": 'reset'}
            })
        ]

    def add_favorits(self,argumants):
        self.BaseActions.add_favourite()

    def add_like(self,argumants):
        self.BaseActions.add_like()

    def edit(self,argumants):
        self.BaseActions.edit()

    def reset(self,argumants):
        self.BaseActions.reset()


class MovieNav(BaseNav):

    def set_nav(self):
        new=self.add_button({
            "name": "Open",
            "obj_name": "open",
            "click": {"obj": self, "function": 'open'}
        })
        self.base_nav.append(new)
        return self.base_nav

    def open(self,argumants):
        self.AbstractBaseView.BaseView.load_view('play', self.data)

class MovieGaleryNav(BaseNav):

    def set_base_nav(self):
        self.base_nav =[
            self.add_button({
                "name"      : "Remove all photos create new",
                "obj_name"  : "remove_all_photos_create_new",
                "click"     : {"obj":self.AbstractBaseView,"function":'remove_all_photos_create_new'}
            }),
            self.add_button({
                "name": "Create missing photos",
                "obj_name": "create_missing_photos",
                "click": {"obj": self.AbstractBaseView, "function": 'create_missing_photos'}
            })
        ]
        return self.base_nav

class StarNav(BaseNav):

    pass

class SeriesNav(BaseNav):

    pass

class NavPoducent(BaseNav):

    pass


