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

# Create base table to work with if it does not already exist
cursor.execute("CREATE TABLE IF NOT EXISTS herd (ear_tag INT, birth_date TEXT, gender CHAR, polled CHAR, location TEXT)")

# Display menu options
choice = None
while choice != '6':
    # Choice 1 is displayed so I can make minor changes when it comes time to implement it.

    print('\n1) Select Herd (Inoperable right now)')
    print('2) Display Livestock')
    print('3) Add Livestock')
    print('4) Update Livestock')
    print('5) Delete Livestock')
    print('6) Quit')
    choice = input('> ')
    print('')
    
    '''
    if choice == '1':
        # Select desired herd
        pass
    '''

    if choice == '2':
        # Display contents of herd
        cursor.execute('SELECT * FROM herd')
        print("{:>10}  {:>10}  {:>10} {:>10} {:>10}".format("Ear Tag", "Birth Date", "Gender", "Polled", "Location"))
        for animal in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10} {:>10} {:>10}".format(animal[0], animal[1], animal [2], animal [3], animal[4]))
        

    elif choice == '3':
        # Add animal to herd
        try:
            ear_tag = input('Ear tag: ')
            birth_date = input(int('Date of Birth: '))
            gender = input('Gender (M/F): ')
            polled = input('Polled (Y/N): ')
            location = input('Current Location: ')
            values = (ear_tag, sqlite3.Date(birth_date), gender.upper(), polled.upper(), location.capitalize())

            cursor.execute("INSERT INTO herd VALUES (?,?,?,?,?)", values)

            # IMPORTANT!! This is what saves the information to the data base for future use
            connection.commit()
        except ValueError:
            print('Invalid Information')

    elif choice == '4':
        # Update animal (location)
        try:
            ear_tag = input('Enter ear tag: ')
            location = input('Enter new location: ')
            values = (location.capitalize(), ear_tag)

            cursor.execute("UPDATE herd SET location = ? WHERE ear_tag = ?", values)
            connection.commit()

        except ValueError:
            print("Invalid ear tag")

    elif choice == '5':
        # Delete an animal
        ear_tag = input('Enter ear tag: ')
        values = (ear_tag,)

        cursor.execute("DELETE FROM herd WHERE ear_tag = ?", values)
        connection.commit()

    else:
        print(choice)  



    
'''    
First table columns:
ID, ear tag, birth date,  gender, breed, polled, location

Future Goals:
create a link to an additional table with vaccine list
create a link to additional table with medications
decide how to record pedegree

'''


