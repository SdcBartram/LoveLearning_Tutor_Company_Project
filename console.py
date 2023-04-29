import datetime

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

learning_style_repository.delete_all()
educator_repository.delete_all()
lesson_repository.delete_all()
student_repository.delete_all()
subject_repository.delete_all()

learning_style1 = LearningStyle("In person")
learning_style_repository.save(learning_style1)

subject1 = Subject("Painting Trees", learning_style1)
subject_repository.save(subject1)

educator1 = Educator("Bob", "Ross", subject1, learning_style1)
educator_repository.save(educator1)

student1 = Student("Sharky", "George", subject1, learning_style1, "Diligent, all intervention tasks completed")
student_repository.save(student1)

lesson1date = (2023, 5, 23)
lesson1time = datetime.strptime('15:00', '%H:%M').time()
lesson1 = Lesson(lesson1date, lesson1time, educator1, student1, subject1, learning_style1)
lesson_repository.save(lesson1)


