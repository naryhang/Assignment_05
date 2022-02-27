#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# NHang, 2022-Feb-26, Adding code
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {} # list of lists with list of dicts
lstRow = [] # list of data row
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
        # Add the functionality of loading existing data
        # Clear existing table
        lstTbl.clear()
        # Read data
        objFile = open(strFileName, 'r')
        for row in objFile:
          # Creating a dictionary out of the file
          lstRow = row.strip().split(',') 
          # Columns
          dicRow = {'ID': lstRow[0], 'CD TITLE': lstRow[1], 'ARTIST': lstRow[2]}
          lstTbl.append(dicRow)
        objFile.close()
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        # Dictionary 
        dicRow = {'ID': intID, 'CD TITLE': strTitle, 'ARTIST': strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD TITLE, ARTIST')
        # Cycling and unpacking
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print('ID, CD TITLE, ARTIST')
        # Displaying list 
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        # Creating variable deletion and asking for ID input
        lstDel = input('What CD would you like to delete?')
        for row in lstTbl:
            if row['ID'] == lstDel:
                del lstDel
        # Code is not working. Input is working and stores ID in row['ID']
                
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            # Empty file cabinet
            strRow = ''
            # Process
            for item in row.values():
                strRow += str(item) + ','
            # Cutting trailing comma
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!')

