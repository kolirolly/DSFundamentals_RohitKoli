def readName(string):
    with open("/content/drive/MyDrive/DS_foundation/assignment_3/names.csv") as file:
        string.append(file.read())

def loadMatrix(string,new):
    new.extend(string[0].strip().split('\n'))


def convertToColumnMajor(new):
    temp = []
    n = max([len(i) for i in new])
    for i in range(n):
        res = ""
        for j in range(len(new)):
            try:
                res += new[j][i]

            except Exception as e:
                res += " "
        temp.append(res)
    new.clear()
    new.extend(temp)


def calculateCharacterLength(new):
    res = 0
    for i in new:
        res += len(i.replace(" ",""))
    print(res)

def storeListAsString(new):
    convertToColumnMajor(new)
    with open("output.txt","wt") as file:
        for i in new:
            file.write(i.strip())


def main():
    string = []
    new = []
    readName(string)
    loadMatrix(string,new)
    print("load matrix:",new)
    convertToColumnMajor(new)
    print("Column major:",new)
    calculateCharacterLength(new)
    storeListAsString(new)

main()