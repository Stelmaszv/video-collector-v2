class stringManipupations:
    @staticmethod
    def short(string,limit):
        new=''
        if len(string)>limit:
            for letter in range(len(string)):
                if letter<limit:
                    new=new+str(string[letter])
            new = new+' ...'
        else:
            new = string
        return new

