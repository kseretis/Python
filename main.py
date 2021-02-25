My Drive
#------------------------------------------------------------#
# This is demo program has been developed by @kseretis for
# business purposes. 
# --> (input) a txt file that contains abap code
# <-- (output) a xlsx file that contains the lines and the 
# values were inside '
#------------------------------------------------------------#

from Record import Record   # Importing class from Record.py
import xlsxwriter
key = "'"                   # Global keyword
stopKeyword = "STOP"        # Stop param
counter = 0                 # Counter
myList = []                 # Our List
exceps = []                 # Exceptions List

# Opening the file
file = open("input.txt", "r")

# Detect the value inside the '
# <-- returns the value
def getNestedValue(raw):
    flag = False            # Flag
    nestedValue = ""        # Nested value
    valuesList = []

    for index in raw:
        if index == key:
            if flag:
                flag = False
                valuesList.append(nestedValue)
                nestedValue = ""
            else:
                flag = True
                continue
        if flag:
            nestedValue += index

    return valuesList

# exceptions
def checkForKeywords(text):
    exceps.append("SE11")
    exceps.append("BKPF")
    exceps.append("VBPA")
    exceps.append("MKPF")
    exceps.append("VF11")
    exceps.append("VBRK")
    exceps.append("BSET")
    exceps.append("AG")
    exceps.append("WE")
    exceps.append("E1EDKA1")
    exceps.append("E1EDK03")

    if text in exceps:
        return False
    return True

def setExceptions():
    stopParam = True
    print("Enter exceptions: ")
    while stopParam:
        tmpInput = input()
    
        if tmpInput == stopKeyword:
            stopParam = False
        exceps.append(tmpInput)
    

# Check the value's length, create a new record
# & append to the list
def createNewRecord(line, text):
    if len(text) > 1 and checkForKeywords(text):
        newRecord = Record(line, text)
        myList.append(newRecord)

# Create new xls file and write the new data
def writeToXls():
    workbook = xlsxwriter.Workbook("Results.xlsx")
    worksheet = workbook.add_worksheet()
    index = 0
    for obj in myList:
        worksheet.write(index, 0, obj.line)
        worksheet.write(index, 1, obj.value)
        index += 1

    workbook.close()

# Reading the lines from the txt file
lines = file.readlines()
setExceptions()

# Reading line by line the txt files
for line in lines:
    counter += 1    # Counts the lines
    if key in line:
        if "CALL FUNCTION" not in line:
            #countTheApost(line)
            valueList = getNestedValue(line)
            for index in valueList:
                createNewRecord(counter, index)
        

# Loop at list to print the stored elements
for obj in myList:
    print(obj.line , " - ", obj.value )

# Call the writting func
writeToXls()

# Closing the file
file.close()
