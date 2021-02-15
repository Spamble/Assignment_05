#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# BEagle-jack, 2021-Feb-12, Modify script to replace the inner data structure by dictionaries.
# BEagle-jack, 2021-Feb-12, Add the functionality of loading existing data
# BEagle-jack, 2021-Feb-13, Add functionality of deleting an entry.
# BEagle-jack, 2021-Feb-13, Change display functionality to unpack dictionaries
# BEagle-jack, 2021-Feb-13, Change save functionality to change dictionaries to strings for writing
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstDict = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        #1. functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            lstDict = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(lstDict)
        objFile.close()
        pass
    elif strChoice == 'a':  
        # 2. Add data to the table (2d-list) each time the user wants to add data
        lstDict['id'] = int(input('Enter an ID: '))
        lstDict['title'] = input('Enter the CD\'s Title: ')
        lstDict['artist'] = input('Enter the Artist\'s Name: ')
        lstTbl.append(lstDict)
        print()
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['id'], row['title'], row['artist'])
        print()
    elif strChoice == 'd':
        # 4. functionality of deleting an entry
        if len(lstTbl) > 0:
            print('There are ' + str(len(lstTbl)) + ' lines of inventory.')
            delList = int(input('Enter inventory line to delete: '))
            try: 
                del lstTbl[delList - 1]
            except: 
                print('Line number does not exist.')
        print()
        pass
    elif strChoice == 's':
        # 5. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strDict = ''
            for val in row.values():
                val = str(val)
                strDict += val + ','
            objFile.write(strDict[:-1] + '\n')
            strDict = ''
        objFile.close()
        lstTbl = []
    else:
        print('Please choose either l, a, i, d, s or x!')

