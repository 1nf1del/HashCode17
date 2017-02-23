class InputParser:
    def __init__(self):
        pass

    def parse(self,filename):
        inputfile = open(filename, 'r')
        firstline = inputfile.readline()
        print(firstline)
        param = firstline[:-1].split(' ')
        print(param)
        rows, columns, minimum, maximum = int(param[0]), int(param[1]), int(param[2]), int(param[3])
        for i in range(rows):
            line = inputfile.readline()
            items = list(line[:-1])
            print(items)
