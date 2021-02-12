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
            if value:
                raise NameError()
        except NameError:
            print(error)
            if exit_var:
                exit()

