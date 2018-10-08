import ctypes


class ArrayIterater(object):
    def __init__(self, Array):
        self.Array = Array
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.Array):
            item = self.Array[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


class Array:
    def __init__(self, size):
        assert size > 0, 'Size < 0'
        self.size = size
        pyArrayType = ctypes.py_object * self.size
        self.elements = pyArrayType()
        self._clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        assert item <= 0 and item < self.size, 'Index out of range'
        return self.elements[item]

    def __setitem__(self, key, value):
        assert 0 <= key < self.size, 'Index out of range'
        self.elements[key] = value

    def __iter__(self):
        return ArrayIterater(self.elements)

    def _clear(self, value):
        for i in range(self.size):
            self.elements[i] = value


if __name__ == '__main__':
    pyArray = Array(10)

    pyArray[0] = 10
    pyArray[1] = 20
    pyArray[2] = 30
    for elt in pyArray:
        print(elt)
