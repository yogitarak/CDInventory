# -*- coding: utf-8 -*-
#------------------------------------------#
# Title: CDInventory.py
# Desc: create a version of our CD Inventory program that has a menu structure and allows the 
# program
# Change log: *Who, When, What)
# Yogita Rakasi, 2022-Feb-27, Copied code from starter
# Yogita Rakasi, 2022-Feb-27, Replaced list with dictionary
#------------------------------------------#

# 1. Display menu allowing the user to choose: 'Add CD', 'Display Current Inventory', 'Save Inventory to file', 'Exit' strUserInput = ''

#import csv

# Declare variabls

strChoice = '' # User input
lstTbl = [] #list of dictonaries to hold data
# TODO replace list of lists with list of dicts
dicRow = {} # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strRow = ''

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
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            print (row)
        objFile.close()            
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':intID, 'Title':strTitle, 'Atrist':strArtist}
      #  print(dicRow)
        lstTbl.append(dicRow)
        pass   
    elif strChoice == 'i':
         # 3. Display the current data to the user each time the user wants to display the data
            for row in lstTbl:
                print(row)
            pass  
    elif strChoice == 's':
            # 4. Save the data to a text file CDInventory.txt if the user chooses so
         for row in lstTbl:
            print(row) 
            strRow+= str(row) + ','    
            strRow = strRow[:-1] + '\n'
            objFile = open(strFileName, 'w')
            objFile.write(strRow)
            objFile.close()
            print('saved')              
         pass  
    elif strChoice == 'd':
           # TODO Add functionality of deleting an entry
           intDel = input('enter the ID you want to delete')
           print (intDel)
           objFile = open(strFileName, 'r')
           for row in objFile:
               dicRow = row
               print(dicRow)
              # for key, val in row.items():
               print (dicRow.keys())
           objFile.close()   
           
          # lstTbl.del(strDel)
           #print('Deleted' strDel)
           pass  
    else:
        print('Please choose either l, a, i, d, s or x!')

