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
    def random(length) ->str :
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str




