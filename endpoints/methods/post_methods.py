from endpoints.methods.model_instance import predictor


def update_model(user_id, inc_value, word_param) -> str:
    predictor.set_value(inc_value)
    return format_update_message(user_id, inc_value, word_param)


def format_update_message(user_id, inc_value, word_param) -> str:
    return "Thanks, {}! You set new inc value for model: {}. Your reversed message: {}".format(
        user_id, inc_value, word_param[::-1]
    )
