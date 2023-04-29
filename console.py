from datetime import datetime

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

# Add subjects to subjects table
subject1 = Subject("Painting Trees", learning_style1)
subject_repository.save(subject1)

subject2 = Subject("Writing", learning_style2)
subject_repository.save(subject2)

# Add educators to educators table
educator1 = Educator("Bob", "Ross", subject1, learning_style1)
educator_repository.save(educator1)

educator2 = Educator("Julia", "Donaldson", subject2, learning_style2)
educator_repository.save(educator2)

# Add students to students table
student1 = Student("Sharky", "George", subject1, learning_style1,
                   "Diligent, all intervention tasks completed")
student_repository.save(student1)

student2 = Student("Ben", "Buckle", subject2, learning_style2, None)
student_repository.save(student2)

# Add lesson to lessons table
lesson1date = datetime(2023, 5, 23)
lesson1time = datetime.strptime('15:00', '%H:%M').time()
lesson1 = Lesson(lesson1date, lesson1time, educator1,
                 student1, subject1, learning_style1)
lesson_repository.save(lesson1)

# update / edit subject
subject3 = Subject("Cooking with EGGS", learning_style1)
subject_repository.save(subject3)
subject3.subject_name = "Cooking with eggs"
subject_repository.update(subject3)

# update student
student3 = Student("Humpty", "DUMPTY", subject3, learning_style1,
                   "A good egg")
student_repository.save(student3)
student3.last_name = "Dumpty"
student_repository.update(student3)

# update educator
educator3 = Educator("Jamie", "OLIVER", subject3, learning_style1)
educator_repository.save(educator3)
educator3.last_name = "Oliver"
educator_repository.update(educator3)

# update lesson
lesson2date = datetime(2023, 5, 25)
lesson2time = datetime.strptime('09:00', '%H:%M').time()
lesson2 = Lesson(lesson2date, lesson2time, educator2, None, subject2, learning_style2)
lesson_repository.save(lesson2)
lesson2.student = student2
lesson_repository.update(lesson2)



