from datetime import datetime, time

from models.educator import Educator
from models.learning_style import LearningStyle
from models.lesson import Lesson
from models.student import Student
from models.subject import Subject

import repositories.educator_repository as educator_repository
import repositories.lesson_repository as lesson_repository
import repositories.student_repository as student_repository
import repositories.subject_repository as subject_repository
import repositories.learning_style_repository as learning_style_repository

# delete all ---> keeps database clean when running multiple times
learning_style_repository.delete_all()
educator_repository.delete_all()
lesson_repository.delete_all()
student_repository.delete_all()
subject_repository.delete_all()


# Add learning_styles to learning_styles table
learning_style1 = LearningStyle("In person")
learning_style_repository.save(learning_style1)

learning_style2 = LearningStyle("Online")
learning_style_repository.save(learning_style2)

# select all learning_styles
learning_styles = learning_style_repository.select_all()

# select learning_style by id
learning_style_repository.select(learning_style2.id)

# Add subjects to subjects table
subject1 = Subject("Painting Trees", learning_style1)
subject_repository.save(subject1)

subject2 = Subject("Writing", learning_style2)
subject_repository.save(subject2)

# select all subjects
subjects = subject_repository.select_all()
# for subject in subjects:
#     print(subject.subject_name)

# select subject by id
subject = subject_repository.select(subject2.id)

# update / edit subject
subject3 = Subject("Cooking with EGGS", learning_style1)
subject_repository.save(subject3)
subject3.subject_name = "Cooking with eggs"
subject_repository.update(subject3)

# Add educators to educators table
educator1 = Educator("Bob", "Ross", subject1, learning_style1)
educator_repository.save(educator1)

educator2 = Educator("Julia", "Donaldson", subject2, learning_style2)
educator_repository.save(educator2)

# select all educators
educators = educator_repository.select_all()
# for educator in educators:
#     print(educator.first_name)

# select educator by id
educator = educator_repository.select(educator1.id)
# print(educator.first_name)

# update educator
educator3 = Educator("Jamie", "OLIVER", subject3, learning_style1)
educator_repository.save(educator3)
educator3.last_name = "Oliver"
educator_repository.update(educator3)

# Add students to students table
student1 = Student("Sharky", "George", subject1, learning_style1,
                   "Diligent, all intervention tasks completed")
student_repository.save(student1)

student2 = Student("Ben", "Buckle", subject2, learning_style2, None)
student_repository.save(student2)

# select all students
students = student_repository.select_all()
# for student in students:
#     print(student.first_name)

# select student by id
student = student_repository.select(student1.id)
# print(student.first_name)

# update student
student3 = Student("Humpty", "DUMPTY", subject3, learning_style1,
                   "A good egg")
student_repository.save(student3)
student3.last_name = "Dumpty"
student_repository.update(student3)

# Add lesson to lessons table
lesson1date = datetime(2024, 5, 23)
lesson1time = datetime.strptime('15:00', '%H:%M').time()
lesson1 = Lesson(lesson1date, lesson1time, educator1,
                 subject1, learning_style1)
lesson_repository.save(lesson1)

lesson2date = datetime(2024, 5, 25)
lesson2time = datetime.strptime('09:00', '%H:%M').time()
lesson2 = Lesson(lesson2date, lesson2time, educator2,
                 subject2, learning_style2)
lesson_repository.save(lesson2)

# update a lesson
lesson2.lesson2date = (2024, 6, 25)
lesson_repository.update(lesson2)

# select lesson by id
lesson = lesson_repository.select(lesson2.id)
# print("over here --->", lesson.date, lesson.subject.subject_name)

# subjects for student
students_subjects = student_repository.subjects_for_student(student1)
# for subject in students_subjects:
#     print(subject.subject_name)

# subjects for educator
educators_subjects = educator_repository.subjects_for_educator(educator1)
# for subject in educators_subjects:
#     print(subject.subject_name)

# search for student
found_students = student_repository.search_for_student("Ben")
# found_student = found_students[0]
# print(found_student.first_name)

# delete by id
# lesson_repository.delete(1)
# student_repository.delete(1)
# educator_repository.delete(1)
# subject_repository.delete(1)
# learning_style_repository.delete(1)

# all upcoming lessons
lesson1date = datetime(2023, 1, 22)
lesson1time = datetime.strptime('15:00', '%H:%M').time()
lesson1 = Lesson(lesson1date, lesson1time, educator2,
                 subject2, learning_style2)
lesson_repository.save(lesson1)
upcoming_lessons = lesson_repository.select_all_upcoming_lessons()
# for lesson in upcoming_lessons:
#     print(lesson.date, lesson.subject.subject_name)

# select all lessons
all_lessons = lesson_repository.select_all()
# for lesson in all_lessons:
#     print("over here --->",lesson.subject.subject_name, lesson.date)

# add student to lesson
student_in_lesson1 = lesson_repository.add_student_to_lesson(student1.id, lesson1.id)
# print(student1.first_name, lesson1.id)


# select all students for a lesson
lesson_repository.add_student_to_lesson(student2.id, lesson1.id)
classlist = lesson_repository.students_for_lesson(lesson1)
# for student in classlist:
#     print("over here ---> ", student.first_name)
