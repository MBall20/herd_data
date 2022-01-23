# Overview

Databases play an important role in todays world. Creating one is just the first step, then the user needs the ability to interface with it. My goal here was to implement the skills of both creating and interfacing a database with SQLite and Python through a real world application. 

The purpose of this software is to provide farmers with a user friendly way to track important information about their livestock herds. The main focus right now is on key genetic traits and pedegree of each animal. This is a great way for farmers and ranchers to monitor their herd genetics and know what to breed back to to keep the herd at its desired focus (ex: increased milk production, polled, low birth weight, etc.)

The software allows for calves to be entered when they are born, for changes to be made to each calf if something was recorded wrong, or in the rare occasion to completely remove an animal from the data base (This option should rarely be used). Most importantly the desired information of the herd can be displayed and viewed.


{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

As of now, there is only one table being used. This table holds the basic traits and birth date of each animal. 
# Development Environment

* IDE: Visual Studio Code
* Language: Python 3.9.10
* Libraries: SQLite3 (Already provided, only need to import)

# Useful Websites
* Note: SQL and SQLite are very similar but have slight variances, reference both resources as needed.
<br/>

* [Intro to SQLite](https://docs.python.org/3.8/library/sqlite3.html)
* [SQL tutorials](https://www.w3schools.com/sql/default.asp)
* [SQLite Datetime](https://www.geeksforgeeks.org/python-sqlite-working-with-date-and-datetime/)
* [Additional SQLite](https://www.sqlitetutorial.net/)



# Future Work

* I have started down the path, but have not fully sorted it out yet. I want the birth dates to be formated as dates, not strings
* create a table to contain the herd, and connect to the current table with a linking table
* Error handling, prevent user from inputing invalid information. As an example the gender column should only allow for an m or f to be entered. The user will be prompted to retry if anything else is added.