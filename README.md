![](https://img.shields.io/badge/python-3.9-blue)

# Database Interaction with PostgreSQL and Application Programming

## Table Setup and Initialization
First, ensure that the PostGresql is running on the local host. Then, create a database in pgAdmin called `assignment-04` and run the following SQL query to create the table:


```sql
CREATE TABLE students (
    student_id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text NOT NULL UNIQUE,
    enrollment_date date
);
```


Then, insert the initial data to the table using the following query:


```sql
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```


## Compiling and Running
This project requires the `psycopg2` library, which is installed in the virtual environment provided. To activate it, run:

```
.\venv\Scripts\activate
```
on Windows systems, or
```shell
source venv/bin/activate
```
on Unix-based systems.

Once inside the venv, run
```shell
python main.py
```
to run the program.

## Functions
### `getAllStudents()`
**Description:** Retrieves all students from the database and displays them.
**Usage:** Call this function to fetch and display all student records from the students table.

### `addStudent(first_name, last_name, email, enrollment_date)`
**Description:** Adds a new student to the database.
**Parameters:**
first_name (string): The first name of the student.
last_name (string): The last name of the student.
email (string): The email address of the student.
enrollment_date (string): The date the student enrolled.
**Usage:** Provide the student's details to insert a new record into the students table.

### `updateStudentEmail(student_id, new_email)`
**Description:** Updates the email address for a specific student in the database.
**Parameters:**
student_id (string): The ID of the student whose email needs to be updated.
new_email (string): The new email address.
**Usage:** Call this function with the student's ID and new email to update their email in the database.

### `deleteStudent(student_id)`
**Description:** Deletes a student's record from the database.
**Parameters:**
student_id (string): The ID of the student to be deleted.
**Usage:** Use this function to remove a student's record from the database.

### `printMenu()`
**Description:** Displays the menu options for the application.
**Usage:** Invoked to show the main menu options to the user.
