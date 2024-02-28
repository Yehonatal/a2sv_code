class Element:
    def __init__(self, data=None):
        self.data = data


class ArrayList:
    def __init__(self):
        self.length = 0

    def prepend(self, element):
        ...

    def insertAt(self, element, idx):
        ...

    def append(self, element):
        ...

    def remove(self, element):
        ...

    def get(self, idx):
        ...

    def removeAt(self, idx):
        ...

    def see_array(self):
        ...


array = ArrayList()
array.prepend(1)
array.append(2)
array.append("Three")
array.prepend(0)
array.append("Five")
array.append("six")
array.see_array()
array.remove("Five")
array.get(2)
array.insertAt("zero", 0)
array.see_array()
