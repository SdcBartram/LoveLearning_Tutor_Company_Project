import unittest
from models.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Fred", "Flintstone", "wheels 101", "online", "diligent, enrichment exercises completed", 1)

    def test_student_has_first_name(self):
        self.assertEqual("Fred", self.student.first_name)

    def test_student_has_last_name(self):
        self.assertEqual("Flintstone", self.student.last_name)

    def test_student_has_subject(self):
        self.assertEqual("wheels 101", self.student.subject)

    def test_student_has_learning_style(self):
        self.assertEqual("online", self.student.learning_style)
    
    def test_student_has_comment(self):
        self.assertEqual("diligent, enrichment exercises completed", self.student.comment)

    def test_student_has_id(self):
        self.assertEqual(1, self.student.id)
