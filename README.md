# Result_Management
DESCRIPTION

The College Result Management System is a web-based application designed to manage student results efficiently. It provides functionality for adding, updating, and viewing results for students, along with managing user accounts for staff and students. The system ensures secure handling of sensitive information like passwords using encryption and follows best practices in web development and database management.

FEATURES

1.User Management:
Staff and student roles.
Secure password storage using bcrypt.

2.Student Management:
Add and manage student details like name, roll number, and class.

3. Management:
Add, update, and view results for students.
View results based on student ID, subjects, and marks.

4.Foreign Key Constraints:
Results are linked to students via a foreign key relationship, ensuring referential integrity in the database.

TECHNOLOGIES USED

Backend: Flask (Python), Flask-Bcrypt (for password hashing), Flask-MySQLdb (for database interaction).

Database: MySQL

Frontend: HTML, CSS (with Jinja2 templates for dynamic content rendering).

Authentication: Flask-Login for session management.

INSTALLATION

1.Clone the repository:
git clone https://github.com/your-username/college-result-management.git

2.Install the required Python dependencies:
pip install -r requirements.txt

Set up MySQL database:
3.Create a database named college_results.
Run the SQL scripts (or queries) from the /database directory to create the necessary tables.

4.Set up configuration:
Edit the config.py file to include your MySQL database credentials.

5.Run the application:
python app.py

6.Access the application on your browser:
http://127.0.0.1:5000

USAGE

Admin/Staff: Can log in to add and manage students and their results.

Students: Can view their results by logging in with their credentials.

CONTRIBUTING

Feel free to fork this repository and make your own contributions. Pull requests are welcome!
