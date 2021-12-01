
error_array = {
    1: "Error 1: Invalid JSONDATA File check instruction!",
    2: "Error 2: Drive {{data}} not exist please check if is crypt !"
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
