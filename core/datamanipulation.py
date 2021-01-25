class Data:
    LANG= "eng";

    def __init__(self,data):
        self.data=data

    def get_mount(self):
        return self.convert_mount(self.data.month);

    def get_year(self):
        return self.data.year;

    def get_day(self):
        return self.data.day;

    def convert_mount(self,mount):
        if mount == 8:
            return 'August'

    def show(self):
        return str(self.get_day())+' '+self.get_mount()+' '+str(self.get_year())


