from flask import Flask, render_template, redirect, url_for, flash, request, session
from config import Config
from models import init_db, query_db, execute_db
from forms import LoginForm, StudentForm, MarkForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user = query_db('SELECT * FROM users WHERE id = %s', (user_id,), one=True)
    if user:
        return User(id=user['id'], username=user['username'], role=user['role'])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = query_db('SELECT * FROM users WHERE username = %s', (form.username.data,), one=True)
        if user and user['password'] == form.password.data:
            login_user(User(id=user['id'], username=user['username'], role=user['role']))
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('third_year'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('login'))
    return render_template('adminpage.html')

@app.route('/admin/third-year', methods=['GET', 'POST'])
@login_required
def third_year():
    if current_user.role != 'admin':
        return redirect(url_for('login'))

    student_form = StudentForm()
    mark_form = MarkForm()

    if student_form.validate_on_submit():
        execute_db('INSERT INTO students (name, register_number, password) VALUES (%s, %s, %s)',
                   (student_form.name.data, student_form.register_number.data, student_form.password.data))
        flash('Student added successfully')
        return redirect(url_for('third_year'))

    if mark_form.validate_on_submit():
        execute_db('INSERT INTO marks (register_number, subject, grade) VALUES (%s, %s, %s)',
                   (mark_form.register_number.data, mark_form.subject.data, mark_form.grade.data))
        flash('Mark added successfully')
        return redirect(url_for('third_year'))

    students = query_db('SELECT * FROM students')
    marks = query_db('SELECT * FROM marks')

    return render_template('third-year.html', student_form=student_form, mark_form=mark_form, students=students, marks=marks)

@app.route('/marks')
@login_required
def marks():
    register_number = request.args.get('register')
    name = request.args.get('name')
    student_marks = query_db('SELECT * FROM marks WHERE register_number = %s', (register_number,))
    return render_template('marks.html', name=name, marks=student_marks)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
