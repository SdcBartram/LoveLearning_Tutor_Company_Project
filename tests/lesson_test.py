import unittest
from models.lesson import Lesson


class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson = Lesson("25-05-2023", "13:00", "Knowe Itall", "wheels 101", "online", 3)

    def test_lesson_has_date(self):
        self.assertEqual("25-05-2023", self.lesson.date)

    def test_lesson_has_time(self):
        self.assertEqual("13:00", self.lesson.time)

    def test_lesson_has_educator(self):
        self.assertEqual("Knowe Itall", self.lesson.educator)

    def test_lesson_has_subject(self):
        self.assertEqual("wheels 101", self.lesson.subject)

    def test_lesson_has_learning_style(self):
        self.assertEqual("online", self.lesson.learning_style)

    def test_lesson_has_id(self):
        self.assertEqual(3, self.lesson.id)
