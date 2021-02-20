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
counter = 0                 # Counter
myList = []                 # Our List

# Opening the file
file = open("input.txt", "r")

# Detect the value inside the '
# <-- returns the value
def getNestedValue(raw):
    flag = False            # Flag
    nestedValue = ""        # Nested value

    for index in raw:
        if index == key:
            if flag:
                flag = False
            else:
                flag = True
                continue
        if flag:
            nestedValue += index

    return nestedValue

# Check the value's length, create a new record
# & append to the list
def createNewRecord(line, text):
    if len(text) > 1:
        newRecord = Record(line, text)
        myList.append(newRecord)

# Count the ' in the line
def countTheApost(line):
    miniCounter = 0
    for index in line:
        if index == key:
            miniCounter += 1
    return miniCounter

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

# Reading line by line the txt files
for line in lines:
    counter += 1    # Counts the lines
    if key in line:
        #countTheApost(line)
        value = getNestedValue(line)
        createNewRecord(counter, value)

# Loop at list to print the stored elements
for obj in myList:
    print(obj.line , " - ", obj.value )

# Call the writting func
writeToXls()

# TODO Create a new excel file and store the object 
# list that has been extraxted

# Closing the file
file.close()
