import pytest
import System

#Test 1:
#Test to see if the student akend3 can login
def test_login(grading_system):
    username = "akend3"
    password = "123454321"
    grading_system.login(username, password)
    assert(grading_system.usr.name == username)


#Test 2:
#Test to check if the system can check if the password matches
def test_check_password(grading_system):
    
    assert(grading_system.check_password('akend3', '123454321') and
            grading_system.check_password('hdjsr7', 'pass1234') and
            grading_system.check_password('yted91', 'imoutofpasswordnames') and
            grading_system.check_password('calyam', '#yeet') and
            grading_system.check_password('goggins', 'augurrox') and
            grading_system.check_password('saab', 'boomr345') and
            grading_system.check_password('cmhbf5', 'bestTA'))


#Test 3:
#Tests if a grade can be changed
def test_change_grade(staff_test):

   # user = "akend3"
   # course = "comp_sci"
   # assignment = "assignment1"
    grade = 50
    staff_test.usr.change_grade('akend3', 'comp_sci', 'assignment1', grade)
    assert(staff_test.usr.check_grades('akend3', 'comp_sci')[0][1] == grade)



#Test 4:
#Tests if the TA cmhbf5 can create a new assignment
def test_create_assignment(grading_system, staff_test):
    exec(open("./RestoreData.py").read())
    assign_date = "5/23/20"
    staff_test.usr.create_assignment("New Assignment", assign_date, 'comp_sci')
    courses = grading_system.load_course_db()
    assert(courses['comp_sci']['assignments']["New Assignment"]["due_date"] == assign_date)



#Test 5:
#Test to add the user 'akend3' to the software_engineering course
def test_add_student(grading_system, proffessor_test):
    proffessor_test.usr.add_student("akend3", "software_engineering")
    user = grading_system.load_user_db()
    assert(user["akend3"]["courses"]["software_engineering"])



#Test 6:
#Test to drop the user 'akend3' from the comp_sci course
def test_drop_student(grading_system, proffessor_test):
    proffessor_test.usr.drop_student("akend3", "comp_sci")
    user = grading_system.load_user_db()
    assert("comp_sci" not in user["akend3"]["courses"])



#Test 7:
#testing a student submission for the user akend3
def test_student_submit(student_test):
    student_test.users["akend3"]["courses"]["comp_sci"]["assignment1"] = ""
    submission_test = "TEST"
    student_test.usr.submit_assignment("comp_sci", "assignment1", submission_test, "2/1/20")
    assert(student_test.users["akend3"]["courses"]["comp_sci"]["assignment1"]["submission"] == submission_test)



#Test 8:
#Testing if the student submission for the user akend3 detects if its ontime
def test_student_submit(student_test):
    #check_ontime(submitDate, dueDate)
    assert(student_test.usr.check_ontime("2/2/20", "2/1/20") == False and
        student_test.usr.check_ontime("1/23/20", "2/1/20") == True and
        student_test.usr.check_ontime("2/1/20", "2/1/20") == True)



#Test 9:
#Testing if the student akend3 can check their grades
def test_student_submit(student_test):
    exec(open("./RestoreData.py").read())
    grades = student_test.usr.check_grades("comp_sci")
    print(grades)
    #checking if the grades are accurate
    assert(grades["assignment1"] == 99 and
            grades["assignment2"] == 66)



#Test 10:
#Testing if the student akend3 can view their assignments
def test_student_submit(student_test):
    assignments = student_test.usr.view_assignments("comp_sci")
    print(assignments)
    #checking for the correct assignments
    assert(assignments[0][1] == "2/1/20" and
            assignment[0][0] == "assignment1" and 
            assignments[1][1] == "2/8/20" and 
            assignment[1][0] == "assignment2")


#Custom Fail Tests:

#Test 11:
#Testing for if a teacher drops a student who isn't registered in the course
def test_teacher_drops_outside_student(proffessor_test):
    drop_class = "software_engineering"
    users = proffessor_test.load_user_db()
    #If the student is registered for the course it will remove them
    if(drop_class in users["akend3"]["courses"]) == True:
        proffessor_test.usr.drop_student("akend3", "software_engineering")
    else: #if they arn't registered for the course it gives assertion error
        assert(drop_class in users["akend3"]["courses"])



#Test 12:
#Testing for if a teacher drops a student from a course they don't own
def test_teacher_drops_from_unowned_course(proffessor_test):
    drop_class = "comp_sci"
    users = proffessor_test.load_user_db()
    if(drop_class in users["goggins"]["courses"]) == True:
        proffessor_test.usr.drop_student("akend3", "comp_sci")
    else: #if they don't own the course it gives assertion error
        assert(drop_class in users["goggins"]["courses"])
    
    


#Test 13:
#Testing for if a proffessor changes grades in an unowned course
def test_proffessor_change_unowned_course_grade(proffessor_test):
    exec(open("./RestoreData.py").read())
    selected_course = "comp_sci"
    users = proffessor_test.load_user_db()
    if(selected_course in users["goggins"]["courses"]) == True:
        proffessor_test.usr.change_grade("akend3", "comp_sci", "assignment1", 33)
    else: #if they don't own the course it gives assertion error
        assert(selected_course in users["goggins"]["courses"])


#Test 14:
#Tests if the TA can check grades in an unowned course
def test_ta_check_unowned_course_grades(staff_test):
    selected_course ="comp_sci"
    users = staff_test.load_user_db
    if(selected_course in users["cmhbf5"]["courses"]) == True:
        grades = staff_test.usr.check_grades("akend3", "comp_sci")
        print(grades)
    else:
        assert(selected_course in users["cmhbf5"]["courses"])


#Test 15:
#Testing to see if the ta is creating a duplicate assignment
def test_ta_add_duplicate_assignment(staff_test, grading_system):
    exec(open("./RestoreData.py").read())
    add_assignment = "assignment1"
    assign_date = "5/23/20"
    courses = grading_system.load_course_db()
    if(add_assignment not in courses["comp_sci"]["assignments"]):
        staff_test.usr.create_assignment(add_assignment, assign_date, 'comp_sci')
    else:
        assert(add_assignment not in courses["comp_sci"]["assignments"])





@pytest.fixture
def proffessor_test():
    grading_system = System.System()
    grading_system.load_data()
    #logging in as professor to access functions
    grading_system.login('goggins', 'augurrox')
    return(grading_system)


@pytest.fixture
def staff_test():
    grading_system = System.System()
    grading_system.load_data()
    #login with TA credentials to access function
    grading_system.login('cmhbf5', 'bestTA')
    return(grading_system)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

@pytest.fixture
def student_test():
    grading_system = System.System()
    grading_system.load_data()
    #logging in as student to access functions
    grading_system.login('akend3', '123454321')
    return(grading_system)