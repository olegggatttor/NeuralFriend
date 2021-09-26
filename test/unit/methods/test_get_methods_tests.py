import random
import unittest

from endpoints.methods.get_methods import get_root_message, format_prediction_message, get_prediction
from endpoints.methods.model_instance import predictor


class GetMethodsTestCase(unittest.TestCase):
    def setUp(self):
        predictor.reset()

    def test_root_message_eq(self):
        result = get_root_message()
        self.assertEqual(result, "Hi! Talk to me please!")

    def test_root_message_not_eq(self):
        result = get_root_message()
        self.assertNotEqual(result, "Something else")

    def test_root_message_determinism(self):
        result1 = get_root_message()
        result2 = get_root_message()
        self.assertEqual(result1, result2)

    def test_format_prediction_message_eq(self):
        for i in range(100):
            x, y = random.randint(0, 100), random.randint(0, 100)
            result = format_prediction_message(x, y)
            self.assertEqual(result, 'Predicted y={} for x={}'.format(y, x))

    def test_format_prediction_message_not_eq(self):
        for i in range(100):
            x, y = random.randint(0, 100), random.randint(200, 300)
            result = format_prediction_message(x, y)
            self.assertNotEqual(result, 'Predicted y={} for x={}'.format(x, y))

    def test_format_prediction_message_determinism(self):
        for i in range(100):
            x, y = random.randint(0, 100), random.randint(0, 100)
            result1 = format_prediction_message(x, y)
            result2 = format_prediction_message(x, y)
            self.assertEqual(result1, result2)

    def test_get_prediction_eq(self):
        for i in range(100):
            x = random.randint(0, 100)
            y = x + 1
            result = get_prediction(x)
            self.assertEqual(result, y)

    def test_get_prediction_not_eq(self):
        for i in range(100):
            x = random.randint(0, 100)
            y = x + 2
            result = get_prediction(x)
            self.assertNotEqual(result, y)

    def test_get_prediction_determinism(self):
        for i in range(100):
            x = random.randint(0, 100)
            result1 = get_prediction(x)
            result2 = get_prediction(x)
            self.assertEqual(result1, result2)
