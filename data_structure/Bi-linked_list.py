class ObjList:

    def __init__(self, data):
        self.__next = self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:

    def __init__(self):
        self.__data = []
        self.head = self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = obj

        if not (self.tail is None):
            obj.set_prev(self.tail)
            obj.get_prev().set_next(obj)

        self.tail = obj
        self.__data.append(obj.get_data())

    def remove_obj(self):
        self.__data.pop()

        if not self.__data:
            self.head = None

        self.tail = self.tail.get_prev()

    def get_data(self):
        return self.__data
