from core.db.config import cur,con
class abstractModel:

    def __init__(self):
        self.table=self.getTablename()
        self.cur=cur
        self.con=con

    def all(self):
        self.cur.execute('SELECT * FROM '+self.table+'')
        return self.cur.fetchall()

    def insert(self,array):
        fieldsLenght= len(array[0])
        fields='?,'
        for x in range(fieldsLenght):
            fields=fields+str('?')
            if x < fieldsLenght-1:
                fields = fields + str(',')

        insertList=[]
        items=''

        for item in array:

            field=[None]
            for x in range(fieldsLenght):
                field.append(item[x])
            insertList.append(field)

        query='INSERT INTO '+self.table+' VALUES('+fields+')'
        self.con.executemany(query, insertList)
        self.con.commit()

    def dropTable(self):
        self.cur.execute('DROP TABLE IF EXISTS '+self.table+';')
        self.migration.shema()
        self.con.commit()

    @classmethod
    def getTablename(cls):
        return cls.__name__
