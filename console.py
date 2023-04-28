from models.educator import Educator
from models.learning_style import LearningStyle
from models.lesson import Lesson
from models.student import Student
from models.subject import Subject

import repositories.educator_repository
import repositories.lesson_repository
import repositories.student_repository
import repositories.subject_repository

educator_repository.delete_all()
lesson_repository.delete_all()
student_repository.delete_all()
subject_repository.delete_all()
