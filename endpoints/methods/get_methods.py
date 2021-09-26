from endpoints.methods.model_instance import predictor


def format_prediction_message(x, y) -> str:
    return 'Predicted y={} for x={}'.format(y, x)


def get_prediction(x) -> str:
    return predictor.predict(x)


def get_root_message():
    return "Hi! Talk to me please!"
