
error_array = {
    #JSON_ERORS
    1: "Error 1: Invalid JSONDATA File check instruction!",
    2: "Error 2: Drive {{data}} not exist please check if is crypt !",
    #View_errror
    3: 'class self.model is not subclass of BaseModel',
    4: 'class self.Info is not subclass of BaseInfo',
    5: 'class self.Nav is not subclass of BaseNav',
    6: 'class self.FormSchema is not subclass of BaseFormSection',
    #form_errror
    7:  'Index click_btm_info not found array data',
    8:  'Index res not found array data',
    9:  'Index method not found array data',
    10: 'Invalid index "font" check instruction!',
    11: 'Index "objets" not found array data'
}

class Error:

    @staticmethod
    def throw_error_is_none(error,value,exit_var=True):
        try:
            if value is None:
                raise NameError()
        except NameError:
            print(error)
            if exit_var:
                exit()

    @staticmethod
    def throw_error_bool(error,value,exit_var=True):
        try:
            if value is False:
                raise NameError()
        except NameError:
            print(error)
            if exit_var:
                exit()

    @staticmethod
    def throw_error(error,exit_var=True):
        try:
            raise NameError()
        except NameError:
            print(error)
            if exit_var:
                exit()

    @staticmethod
    def add_data_to_error(error,index,DATA):
        return error.replace(index,DATA)

    @staticmethod
    def get_error(index):
        return error_array[index]
