import csv


def write_student_data():
    # get number of students
    num_students = int(input("Enter the number of students: "))

    # open the CSV file for writing
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # write the header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # loop to get student data
        for _ in range(num_students):
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # write the student data to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Data has been written to grades.csv")


def read_and_display_data():
    # open the CSV file for reading
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)

        # read and print the header
        header = next(reader)
        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        # read each row of data and print it in formatted columns
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


def main():
    # write data to the CSV file
    write_student_data()

    # read from the CSV file and display the data
    print("\nDisplaying the data from grades.csv:\n")
    read_and_display_data()


if __name__ == "__main__":
    main()
