import random
import string
class stringManipupations:

    @staticmethod
    def short(string,limit) ->str:
        new=''
        if len(string)>limit:
            for letter in range(len(string)):
                if letter<limit:
                    new=new+str(string[letter])
            new = new+' ...'
        else:
            new = string
        return new

    @staticmethod
    def array_to_string(array)->str :
        string=''
        el=1
        for item in array:
            string=string+str(item.name)
            if el<len(array):
                string=string+str(', ')
                if el % 5==0:
                    string = string + str('<br>')
            el=el+1;
        return string

    @staticmethod
    def random(length) ->str :
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str




