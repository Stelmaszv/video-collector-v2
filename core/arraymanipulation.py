class ArrayManipulation:

    @staticmethod
    def faind_index_in_array(array,index) ->bool:
        stan=True
        for item in array:
            if index==item:
                return False
        return stan