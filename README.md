# ACME_EMPLOYEES

+++++ABOUT THE PROGRAM+++++


The following program will request the information on the hours of the workers of the ACME company
and will give as a result the number of days that the pairs of employees coincide.

+++++LANGUAGE USED+++++


Python

+++++MODULES USED++++++


datetime: used to create variables of type date to compare them later

+++++EXERCISE++++++


The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00 ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT: ASTRID-RENE: 2 ASTRID-ANDRES: 3 RENE-ANDRES: 2

Example 2:

INPUT: RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00 ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT: RENE-ASTRID: 3

+++++TO RUN THE PROGRAM++++++


This is a console program.


We must open our command console and locate the path where our main file is, we will execute it, 
then the program will ask us to put the name of our .txt file

The file with the .txt extension must be in the same folder as the program for it to work


Example:
- python ACME_EMPLOYEES.py (NAME OF THE FILE.txt)

- python ACME_EMPLOYEES.py lista.txt

+++++ MY SOLUTION+++++++

In order to develop the exercise, the data had to be read from a .txt file, after that it had to be organized in dictionaries to have a primary key that contained the values ​​of the days and hours worked by the employees, after that another dictionary was created where the names of the employees were given as a key and the days of the week as a value, 
after that cycles were used to gather the information to finally compare the data and see which ones coincided to generate the coincidence of the pair of employees
