from datetime import datetime
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

        if mount == 10:
            return 'October'

        if mount == 5:
            return 'May'

    def get_age(self):
        difrence=datetime.now()-self.data
        age=difrence/365;
        return str(age.days)

    def show(self):
        return str(self.get_day())+' '+self.get_mount()+' '+str(self.get_year())


class DataValidator:

    error=[]

    def __init__(self):
        self.now=datetime.now()

    def set_data(self,year,mount,day):
        self.year=year
        self.mount=mount
        self.day=day

    def validate_data(self):
        self.valid_year()
        self.valid_mount()
        self.valid_day()

    def valid_day(self):
        def get_mount(number):
            switcher = {
                1:  31,
                2:  29,
                3:  31,
                4:  30,
                5:  31,
                6:  30,
                7:  31,
                8:  31,
                9:  30,
                10: 30,
                11: 30,
                12: 31
            }

            return  switcher.get(number, "Invalid mount");

        days= get_mount(self.mount);

        if self.day > days:
            self.error.append('day is invalid !')

    def valid_mount(self):

        if self.mount >12 or self.mount<1:
            self.error.append('mount is invalid !')
        else:
            if self.day==29 and self.mount == 2 :
                if self.year % 4 !=0 :
                    self.error.append('mount is invalid !')

    def valid_year(self):
        if self.year > self.now.year:
            self.error.append('Year is invalid !')



