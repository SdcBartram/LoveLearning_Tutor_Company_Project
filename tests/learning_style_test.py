import unittest

from models.learning_style import LearningStyle


class TestLearningStyle(unittest.TestCase):

    def setUp(self):
        self.learning_style = LearningStyle("online", 2)

    def test_learning_style_has_a_learning_style(self):
        self.assertEqual("online", self.learning_style.learning_style)

    def test_learning_style_has_id(self):
        self.assertEqual(2, self.learning_style.id)
