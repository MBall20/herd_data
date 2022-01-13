'''
Author: Mitchell Ball
Date: 1/13/22
Project: Relational Database
'''

#import needed libraries
import sqlite3

# Connect to database, creates new if not already present
connection = sqlite3.connect('cattle_database.db')
cursor = connection.cursor()

# Display menu options
choice = None
while choice != 6:
    print('1) Select Herd')
    print('2) Display Livestock')
    print('3) Add Livestock')
    print('4) Update Livestock')
    print('5) Delete Livestock')
    print('6) Quit')

    
'''    
First table columns:
ID, ear tag, birth date,  gender, breed, polled, location
create a link to an additional table with vaccine list
create a link to additional table with medications
decide how to record pedegree

'''


