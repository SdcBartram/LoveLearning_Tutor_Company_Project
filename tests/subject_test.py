import unittest
from models.subject import Subject


class TestSubject(unittest.TestCase):

    def setUp(self):
        self.subject = Subject("wheels 101", "online", 2)

    def test_subject_has_a_name(self):
        self.assertEqual("wheels 101", self.subject.subject_name)

    def test_subject_has_a_learning_style(self):
        self.assertEqual("online", self.subject.learning_style)
    
    def test_subject_has_id(self):
        self.assertEqual(2, self.subject.id)
