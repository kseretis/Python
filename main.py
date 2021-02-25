#------------------------------------------------------------#
# This is demo program has been developed by @kseretis for
# business purposes. 
# (input) --> a txt file that contains abap code
# (output) <-- a xlsx file that contains the lines and the 
# values were inside '
#------------------------------------------------------------#

import myModule
key = "'"                   # Global keyword
counter = 0                 # Counter
myList = []                 # Our List
exceptionList = ["CALL FUNCTION", "VALUE", "DATA", 
                "DEFAULT", "AUTHORITY-CHECK", "ID",
                "HAHA", "hana"]                

# Opening the file
file = open("input.txt")
# Reading the lines from the txt file
lines = file.readlines()

# Reading line by line the txt files
for line in lines:
    counter += 1    # Counts the lines
    if key in line and myModule.checkLineByLine(line, exceptionList):
            valueList = myModule.getNestedValue(line, key)
            for index in valueList:
                myList.append(myModule.createNewRecord(counter, index))
        
# Call the writting func
myModule.checkIfResultsExist(myList)
print("File Results.xlsx have created!")
print(len(myList) , " items have found!")

# Closing the file
file.close()