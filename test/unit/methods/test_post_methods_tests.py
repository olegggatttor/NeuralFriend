import unittest

from endpoints.methods.model_instance import predictor
from endpoints.methods.post_methods import update_model, format_update_message


class PostMethodsTestCase(unittest.TestCase):
    def setUp(self):
        predictor.reset()

    def test_format_update_message_eq(self):
        result = format_update_message(123, 2, "message")
        self.assertEqual(result, "Thanks, 123! You set new inc value for model: 2. Your reversed message: egassem")

    def test_format_update_message_determinism(self):
        result1 = format_update_message(123, 2, "message")
        result2 = format_update_message(123, 2, "message")
        self.assertEqual(result1, result2)

    def test_update_model(self):
        result = update_model(123, 2, "message")
        self.assertEqual(result, "Thanks, 123! You set new inc value for model: 2. Your reversed message: egassem")

    def test_update_model_exception_if_zero_inc(self):
        self.assertRaises(ValueError, update_model, 123, 0, "message")
