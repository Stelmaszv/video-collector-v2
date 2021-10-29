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
        switcher = {
             1: 'January',
             2: 'February',
             3: 'March',
             4: 'April',
             5: 'May',
             6: 'June',
             7: 'July',
             8: 'August',
             9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        return switcher.get(mount, "Invalid mount");

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
        self.mount=int(mount)
        self.mount_str = mount
        self.day=day

    def validate_data(self):
        self.valid_year()
        self.valid_mount()
        self.valid_day()

    def valid_day(self):
        def get_mount(number):
            switcher = {
                '01':  31,
                '02':  29,
                '03':  31,
                '04':  30,
                '05':  31,
                '06':  30,
                '07':  31,
                '08':  31,
                '09':  30,
                '10':  30,
                '11':  30,
                '12':  31
            }
            return  switcher.get(number, "Invalid mount");

        if self.mount > 12 or self.mount < 1:
            self.error.append('Day is invalid !')
        else:
            days= get_mount(self.mount_str);
            if self.day > days:
                self.error.append('Day is invalid !')


    def valid_mount(self):
        error=False;
        if self.day == 29 and self.mount == 2:
            if self.year % 4 != 0:
                error=True

        if self.mount >12 or self.mount<1:
            error=True

        if error:
            self.error.append('Mount is invalid !')

    def valid_year(self):
        if self.year > self.now.year:
            self.error.append('Year is invalid !')



