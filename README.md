Jacob Hawkins
10/27/2024

----
Program Description:


----
logical steps:
1. program starts with the main() function
2. prompt user to inter number of students
3. open or create the .csv file
4. write the header foer the .csv file
5. loop through each student to get their info
6. close the file, notify the user
7. open the .csv file for reading
8. read header, then loop through each student
9. close the file

----
variables:
1. num_students: stores the number of students
2. file: represents the file object used to open the .csv file
3. writer: a csv.writer object used to write rows to the grades.csv file
4. first_name: stores the first name of the student being entered
5. last_name: stores the last name of the student being entered
6. exam1: stores the grade for exam 1 for the student being entered.
7. exam2: stores the grade for exam 2 for the student being entered.
8. exam3: stores the grade for exam 3 for the student being entered.
9. reader: a csv.reader object used to read rows from the grades.csv file
10. header: stores the header from the grades.csv file
11. row: represents each row of data from the grades.csv file

----
functions:
1. write_student_data(): collects student data from the user and writes it to a .csv file.
2. read_and_display_data(): reads the data from the .csv file, and displays it.
3. main(): calls the other functions.

----

repository: https://github.com/sometimeslingual/csv
