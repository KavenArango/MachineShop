from flask import Blueprint
from flask import render_template,g
from apps.accounts.models import Users
from apps.StudentPage.models import Student, majors, Levels
from apps.StaffPage.forms import Staff_Student
from apps.Machine.models import machines

Staff_View = Blueprint('Staff_View', __name__)

@Staff_View.route('/staff')
def staff():
    template = "StaffPage/staff.html"
    title = "staff"
    return render_template(template, title=title)

@Staff_View.route('/studentsearch')
def student_search():
    template = "StaffPage/StudentSearch.html"
    title = "Student Search"
    form = Staff_Student()
    students = Student.query.distinct(Users.email).group_by(Users.email).filter(Student.user_id == Users.id).join(
        Users, Users.id == Student.user_id
    ).join(
        machines, machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        majors.major_name.label("major_name"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("level")
    ).all()
    return render_template(template, title=title, students=students, form=form)

@Staff_View.route('/studentdetail/<student_id>')
def student_detail(student_id):
    template = "StaffPage/studentdetail.html"
    title = "Student Detail"
    form =Staff_Student()
    post = Student.query.filter(Student.id == student_id).join(
        Users, Users.id == Student.user_id
    ).join(
        machines, machines.id == Student.machine_id
    ).join(
        majors, majors.id == Student.major_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        Student.id.label("id"),
        Users.first_name.label("first_name"),
        Users.last_name.label("last_name"),
        Users.email.label("email"),
        majors.major_name.label("major_name"),
        machines.machine_name.label("machine_name"),
        Levels.description.label("description"),
        Users.id.label("User_id")
    ).first()
    form.first_name.data = post.first_name
    form.last_name.data = post.last_name
    form.email.data = post.email
    form.major.data = post.major_name

    detail = Student.query.filter(Student.user_id == post.User_id).join(
        machines, machines.id == Student.machine_id
    ).join(
        Levels, Levels.id == Student.level_id
    ).with_entities(
        machines.machine_name.label("machine_name"),
        Levels.description.label("description")
    ).all()

    return render_template(template, title=title, form=form, detail=detail)



