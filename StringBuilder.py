class StringBuilder:
    def __init__(self):
        self.workingArray = []

    def add(self, value):
        self.workingArray.append(value)

    def __str__(self):
        return "".join(self.workingArray)

if __name__ == '__main__':
    stringbuilder = StringBuilder()
    stringbuilder.add("abel")
    stringbuilder.add("nahome")
    stringbuilder.add("zeku")
    print(stringbuilder)
