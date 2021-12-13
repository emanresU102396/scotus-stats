import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

loop = True
while loop:
    try:
        fileName = input("Enter file path:\n")
        casesFile = open(fileName, errors="ignore")
        loop = False
    except FileNotFoundError:
        print("File not found.", end=" ")

caseReader = csv.reader(casesFile)

totalDiff = 0
totalDiffNine = 0
numCases = 0
numCasesNine = 0

diffList = []
dateList = []
diffListNine = []
dateListNine = []

century = 1900
lastYear = 0

for item in caseReader:
        if item[0] == "":
            break
        if item[51] != "majVotes":
            numCases += 1
            totalDiff += int(item[51]) - int(item[52])
            diffList.append(int(item[51]) - int(item[52]))
            if (century + int(item[4][-2:])) < lastYear - 50:
                century = 2000
            dateList.append(century + int(item[4][-2:]))
            if int(item[51]) + int(item[52]) == 9:
                dateListNine.append(century + int(item[4][-2:]))
                diffListNine.append(int(item[51]) - int(item[52]))
                totalDiffNine += int(item[51]) - int(item[52])
                numCasesNine += 1
            lastYear = dateList[-1]

avgDiff = float(totalDiff)/numCases
avgDiffNine = float(totalDiffNine)/numCasesNine

squaredDiffSum = 0
squaredDiffSumNine = 0

for item in diffList:
    squaredDiffSum += (item - avgDiff) ** 2
for item in diffListNine:
    squaredDiffSumNine += (item - avgDiffNine) ** 2

variance = squaredDiffSum / numCases
varianceNine = squaredDiffSumNine / numCasesNine

stdDev = variance ** 0.5
stdDevNine = varianceNine ** 0.5

print("Total cases:")
print(numCases)
print("Average difference between majority and minority vote count:")
print(avgDiff)
print("Standard deviation:")
print(stdDev)

print()

print("Total nine-justice cases:")
print(numCasesNine)
print("Average difference (including only nine-justice cases):")
print(avgDiffNine)
print("Standard deviation:")
print(stdDevNine)
print()

divisiveList = [4-((x - 1) / 2) for x in diffList]
divisiveListNine = [ 4-((x-1) / 2) for x in diffListNine]

x = np.array(dateListNine)
y = np.array(divisiveListNine)
m, b, r_value, p_value, std_err = stats.linregress(x, y)


plt.plot(x, y, 'ro')
plt.plot(x, m*x + b)

print("Line of best fit: " + str(m)+ "x + " + str(b))
print("R = " + str(r_value))
print("R^2 = " + str(r_value ** 2))

plt.xticks(range(dateListNine[0], dateListNine[-1], 10))
plt.yticks([0,1,2,3,4])

plt.title("Divisiveness of Landmark Supreme Court Decisions Over Time")
plt.xlabel("Year")
plt.ylabel("Divisiveness")

plt.show()
