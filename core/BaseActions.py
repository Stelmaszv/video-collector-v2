from app.db.models import session
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

    def add_favourite(self):

        if self.obj.data.favourite is True:
            stan=False
        else:
            stan=True

        self.obj.data.favourite = stan;
        self.session.commit()

