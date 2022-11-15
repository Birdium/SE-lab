class Element:

    def get_type(self):
        return self.__type__

    def get_lower(self):
        return self.__lower__

    def get_upper(self):
        return self.__upper__

    def __init__(self, item : tuple):
        self.__type__ = item[0]
        if item[0] == "int" or item[0] == "string":
            self.__lower__ = int(item[1])
            self.__upper__ = int(item[2])
