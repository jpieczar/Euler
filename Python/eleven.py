hold = 0

myFile = open("resources/eleven_resources.txt", 'r')
myList = myFile.readlines()
myFile.close()

myArr = []
for i in myList:
    myArr.append(i.split(' '))

for line in range(0, 20):
    for index in range(0, 20):
        myArr[line][index] = int(myArr[line][index])

def productCheck(a, b, c, d):
    global hold
    product = a*b*c*d
    if hold < product:
        hold = product

def runThrough(arr):
    for line in range(0, 20):
        for index in range(0, 17):
            productCheck(arr[line][index], arr[line][index + 1], arr[line][index + 2], arr[line][index + 3])
            '''
            print(">>>>>>>>>>>>>>")
            print("--- ", line, " --- ", index)
            print(arr[line][index])
            print(arr[line][index + 1])
            print(arr[line][index + 2])
            print(arr[line][index + 3])
            print(">>>>>>>>>>>>>>")
            '''
           

def jumpThrough(arr):
    for line in range(0, 17):
        for index in range(0, 20):
            productCheck(arr[line][index], arr[line + 1][index], arr[line + 2][index], arr[line + 3][index])
            '''
            print(">>>>>>>>>>>>>>")
            print("--- ", line, " --- ", index)
            print(arr[line][index])
            print(arr[line + 1][index])
            print(arr[line + 2][index])
            print(arr[line + 3][index])
            print(">>>>>>>>>>>>>>")
'''

def diagonalRight(arr):
    for line in range(0, 17):
        for index in range(0, 17):
            productCheck(arr[line][index], arr[line + 1][index + 1], arr[line + 2][index + 2], arr[line + 3][index + 3])
            '''
            print(">>>>>>>>>>>>>>")
            print(arr[line][index])
            print(arr[line + 1][index + 1])
            print(arr[line + 2][index + 2])
            print(arr[line + 3][index + 3])
            print(">>>>>>>>>>>>>>")
'''
def diagonalLeft(arr):
    for line in range(0, 17):
        for index in reversed(range(3, 20)):
            productCheck(arr[line][index], arr[line + 1][index - 1], arr[line + 2][index - 2], arr[line + 3][index - 3])
            '''
            print(">>>>>>>>>>>>>>")
            print(arr[line][index])
            print(arr[line + 1][index - 1])
            print(arr[line + 2][index - 2])
            print(arr[line + 3][index - 3])
            print(">>>>>>>>>>>>>>")
            '''

diagonalLeft(myArr)
diagonalRight(myArr)
runThrough(myArr)
jumpThrough(myArr)

print(hold)
