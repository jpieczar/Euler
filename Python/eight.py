myFile = open("eight_resources", 'r')
myList = ""
for line in myFile:
    myList += line.strip()
myFile.close()
myArr = []
for i in myList:
  myArr.append(int(i))  

def thirteen(numArr):
    total = 1
    for i in range(len(numArr)):
        total *= numArr[i]
    return total

hold_you = []
hold_me = 0
for j in range(len(myArr)):
    if j + 12 == len(myArr):
        break
    for k in range(0, 13):
        hold_you.append(myArr[j + k])

    if thirteen(hold_you) >= hold_me:
        hold_me = thirteen(hold_you)
    hold_you = []

print(hold_me)
