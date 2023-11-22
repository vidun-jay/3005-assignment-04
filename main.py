import psycopg2

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    NC = '\033[0m'

# database parameters
params = {
    'host': 'localhost',
    'database': 'assignment-04',
    'user': 'postgres',
    'password': 'postgres'
}

table_name = 'students'

def getAllStudents():
    """ Return all students from the database """

    try:
        # connect to the database and create cursor to run queries
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # sql query to select all students
        query = f'SELECT * FROM {table_name};'
        cursor.execute(query) # execute query

        records = cursor.fetchall()

        print('\n')
        for record in records:
            print(record)
        print('\n')

    except psycopg2.Error as e:
        print(f'{colors.RED}Error connecting to the database: {e}{colors.NC}')

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """Add student to the database

    Args:
        first_name (string): student's first name
        last_name (string): student's last name
        email (string): student's email
        enrollment_date (string): date of enrollment
    """

    try:
        # connect to the database and create cursor to run queries
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # sql query to insert student
        query = f'''
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
        '''
        cursor.execute(query, (first_name, last_name, email, enrollment_date)) # execute query

        # commit the changes to the database
        connection.commit()

        print(f'Student {colors.YELLOW}{first_name} {last_name}{colors.NC} has been added to the database {colors.GREEN}successfully!{colors.NC}')

    except psycopg2.Error as e:
        print(f'{colors.RED}Error adding student: {e}{colors.NC}')

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def updateStudentEmail(student_id, new_email):
    """Update a student's email in the database

    Args:
        student_id (string): student id
        new_email (string): updated email
    """

    try:
        # connect to the database and create cursor to run queries
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # sql query to update student email
        query = 'UPDATE students SET email = %s WHERE student_id = %s;'
        cursor.execute(query, (new_email, student_id)) # execute query

        # commit the changes to the database
        connection.commit()

        print(f'Email address for student with id {colors.YELLOW}{student_id}{colors.NC} updated {colors.GREEN}successfully!{colors.NC}')

    except psycopg2.Error as e:
        print(f'{colors.RED}\nError adding student: {e}{colors.NC}')

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def deleteStudent(student_id):
    """Delete a student from the database

    Args:
        student_id (string): student id
    """

    try:
        # connect to the database and create cursor to run queries
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # sql query to update student email
        query = 'DELETE FROM students WHERE student_id = %s'
        cursor.execute(query, (student_id,)) # execute query

        # commit the changes to the database
        connection.commit()

        print(f'\nStudent with id {colors.YELLOW}{student_id}{colors.NC} deleted {colors.GREEN}successfully!{colors.NC}\n')

    except psycopg2.Error as e:
        print(f'{colors.RED}\nError deleting student: {e}{colors.NC}')

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def printMenu():
    """ Prints the menu """
    print(f'''
What would you like to do?

    1) Get all students
    2) Add a student
    3) Update a student's email
    4) Delete a student\n''')

def main():

    print(f'''
+--------------------------+
| STUDENTS DATABASE - MENU |
+--------------------------+''')

    while True:

        # check validity of input
        while True:
            printMenu()
            choice = input('Select an option: ')

            # check if the input is one of the valid options
            if choice in ['1', '2', '3', '4']:
                break  # exit the loop if the input is valid
            else:
                print(f'\n{colors.RED}Please select a valid option and try again.{colors.NC}')

        if choice == '1':
            getAllStudents()
        elif choice == '2':
            student = input('Enter the student details (first_name, last_name, email, enrollment_date): ').split(', ')
            addStudent(*student)
        elif choice == '3':
            email = input('Enter the student id and updated email (student_id, updated_email): ').split(', ')
            updateStudentEmail(*email)
        elif choice == '4':
            student_id = input('Enter the student id of the student to delete: ')
            deleteStudent(student_id)

        quit = input("Would you like to close the program? (y/n): ")
        if quit == 'y':
            break

if __name__ == '__main__':
    main()