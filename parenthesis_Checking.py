from ListStack import ArrayStack
class checkTag:
    def __init__(self,listOfTag):
        self.listOfTag = listOfTag
        self.open = ["(","[","{"]
        self.close = [")","]","}"]
        self.stack = ArrayStack()
    def addOpenTag(self,Tag):
        self.stack.push(Tag)
    def removeTag(self,Tag):
        self.stack.pop()
    def is_opposite(self,tag):
        tagIndex = self.close.index(tag)
        tagIndex2 = self.open[tagIndex]
        try:
            if self.stack.peak()==tagIndex2:
                return True
        except IndexError:
            print("Incorrect tag = ",tag)

        return False
    def run(self):
        for tags in self.listOfTag:
            if tags in self.open:
                self.addOpenTag(tags)
                print("tag added")
            elif tags in self.close:
                if self.is_opposite(tags):
                    self.removeTag(tags)
                    print("tag removed good")
        self.verify()
    def verify(self):
        if self.stack.isEmpty():
            print("correct")
        else:
            print("incorrect left over(s)")
            while self.stack.isEmpty()==False:
                print(self.stack.pop())




# ["(",")","(","(",")",")","{","(","[","(",")","]",")","}","[","]"]
checkTag = checkTag(["{","(","(",")",')',']'])
checkTag.run()
