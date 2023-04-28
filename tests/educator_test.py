import unittest
from models.educator import Educator


class TestEducator(unittest.TestCase):

    def setUp(self):
        self.educator = Educator("Knowe", "Itall", "wheels 101", "online", 3)

    def test_educator_has_first_name(self):
        self.assertEqual("Knowe", self.educator.first_name)

    def test_educator_has_last_name(self):
        self.assertEqual("Itall", self.educator.last_name)

    def test_educator_has_subject(self):
        self.assertEqual("wheels 101", self.educator.subject)

    def test_educator_has_learning_style(self):
        self.assertEqual("online", self.educator.learning_style)

    def test_educator_has_id(self):
        self.assertEqual(3, self.educator.id)
