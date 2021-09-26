class SimpleModel:
    def __init__(self):
        self.value = 1

    def predict(self, x: int) -> int:
        """
        Predictor that returns x + value
        :param x: given x
        :return: predicted y = x + 1
        """
        return x + self.value

    def set_value(self, value):
        if value == 0:
            raise ValueError("0 is forbidden as value parameter.")
        self.value = value

    def reset(self):
        self.value = 1