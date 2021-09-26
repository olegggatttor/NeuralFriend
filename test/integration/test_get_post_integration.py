import unittest

from endpoints.methods.get_methods import get_root_message, format_prediction_message, get_prediction
from endpoints.methods.model_instance import predictor
from endpoints.methods.post_methods import update_model
from random import randint, choice
import string


def get_random_params():
    letters = string.ascii_uppercase
    return (randint(1, 100),
            randint(1, 100),
            randint(1, 100),
            ''.join(choice(letters) for _ in range(50)))


class GetPostIntegrationMethodsTestCase(unittest.TestCase):
    def setUp(self):
        predictor.reset()

    def test_get_after_post_eq(self):
        for i in range(100):
            self.setUp()
            user_id, query_value, inc_change_value, message = get_random_params()
            root_msg_prev = get_root_message()
            get_prediction_message_prev = format_prediction_message(query_value, get_prediction(query_value))

            self.assertEqual(root_msg_prev, "Hi! Talk to me please!")
            self.assertEqual(get_prediction_message_prev,
                             'Predicted y={} for x={}'.format(query_value + 1, query_value))

            update_model_message = update_model(user_id, inc_change_value, message)

            self.assertEqual(update_model_message,
                             "Thanks, {}! You set new inc value for model: {}. Your reversed message: {}".format(
                                 user_id, inc_change_value, message[::-1]
                             ))

            root_msg_new = get_root_message()
            get_prediction_message_new = format_prediction_message(query_value, get_prediction(query_value))

            self.assertEqual(root_msg_prev, root_msg_new)
            self.assertEqual(get_prediction_message_new,
                             'Predicted y={} for x={}'.format(query_value + inc_change_value,
                                                              query_value))

    def test_get_integration_with_format(self):
        for i in range(100):
            user_id, query_value, _, _ = get_random_params()
            result = format_prediction_message(query_value, get_prediction(query_value))
            self.assertEqual(result,
                             'Predicted y={} for x={}'.format(query_value + 1, query_value))

