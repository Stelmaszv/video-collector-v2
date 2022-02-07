from core.view import AbstractBaseView, BaseView


class StarListAsctions(AbstractBaseView):
    resolution_index = 'Menu'
    show_elemnts = ['Title', 'Info', 'Galery', 'Nav', 'Avatar','List','Description','Tags']

    def run(self,item):
        self.BaseView.load_view('stars', item)
        return True