import csv

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
diffListNine = []

# Uncomment the commented lines to print out every single case with its corresponding data points
# (May take a while)
for item in caseReader:
        if item[0] == "":
            break
        if item[51] != "majVotes":
            numCases += 1
#            print(item[14] + "\t(" + item[51] + "-" + item[52] + ")")
#            print("Majority votes: " + item[51] + "\tMinority votes: " + item[52] +
#                  "\tDifference: " + str(int(item[51]) - int(item[52])) + "\tTotal votes: " + str(int(item[51]) + int(item[52])))
            totalDiff += int(item[51]) - int(item[52])
            diffList.append(int(item[51]) - int(item[52]))
            if int(item[51]) + int(item[52]) == 9:
                diffListNine.append(int(item[51]) - int(item[52]))
                totalDiffNine += int(item[51]) - int(item[52])
                numCasesNine += 1
#            print("----------------------------------------------------------")

#print("==============================================================")

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


input("Press ENTER to exit")
