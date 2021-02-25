from Record import Record       # Importing class from Record.py
import os, xlsxwriter           # libs

# This function checks line by line the code
# (input) --> line, list of exceptions
# (output) <-- True if there is not a * or a keyword in the line
def checkLineByLine(line, exceptionList):

    # this part of code checks if the line is a comment
    subString = line[0:3]
    if "*" in subString:
        return False  
    if inExceptionsList(line, exceptionList):
        return False
    return True

# This function scans the exceptions list
# (input) --> line, list of exceptions
# (output) <-- True if there is a keyword in the line
def inExceptionsList(line, exceptionList):
    for exceps in exceptionList:
        if exceps in line:
            return True
    return False

# Detect the value inside the ' ' 
# (input) --> line, key
# (output) <-- Returns the list filled with values
def getNestedValue(line, key):
    flag = False            # Flag
    nestedValue = ""        # Nested value
    valuesList = []         # Nested values list

    for index in line:
        if index == key:
            if flag:
                flag = False
                if len(nestedValue) > 1:
                    valuesList.append(nestedValue)
                nestedValue = ""
            else:
                flag = True
                continue
        if flag:
            nestedValue += index

    return valuesList

# Check the value's length, create a new record
# & append it to the list
# (input) --> line number, the value
# (output) <-- New object
def createNewRecord(line, value):
    newRecord = Record(line, value)
    return newRecord
    
# This function checks if the excel file with results already exists
# if yes the script replace it with a new one
# (input) --> the list
def checkIfResultsExist(myList):
    if os.path.exists("Results.xlsx"):
        os.remove("Results.xlsx")
        print("Old excel file deleted!")
    writeToXlsx(myList)

# Create new xls file and write the new data
# (input) --> the list
def writeToXlsx(myList):
    workbook = xlsxwriter.Workbook("Results.xlsx")
    worksheet = workbook.add_worksheet()
    index = 0
    for obj in myList:
        worksheet.write(index, 0, obj.line)
        worksheet.write(index, 1, obj.value)
        index += 1

    workbook.close()