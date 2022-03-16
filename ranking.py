class FileProcessor:
    def __init__(self):
        self.rankList = []

    def rankFile(self,name):
        with open(name) as f:
            contents = f.readlines()
            for index, line in enumerate(contents):
                if index <6 : continue
                self.rankList.append((index,)+tuple(line.strip().split(',')))
                # print("Line {}: {}".format(index, line.strip()))
            # print(contents[6:])
        self.rankList.sort(key= lambda x:x[2])

    def printRank(self):
        for value in self.rankList:
            print("line:{}     points:{} name:{}".format(value[0], value[2],value[4]))

    def writeRankToFile(self):
        with open('ranking.txt', 'w') as f:
            for value in self.rankList:
                f.write("line:{}     points:{} name:{} \n".format(value[0], value[2],value[4]))

Processor = FileProcessor()
Processor.rankFile('Books_2')
Processor.printRank()
Processor.writeRankToFile()