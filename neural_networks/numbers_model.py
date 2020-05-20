import numpy as np


class NumberDetector:

    def __init__(self, net):
        self.net = net
        print("Numbers detector initialized")

    def detect_numbers(self, image: np.ndarray) -> list:
        """

        :param image:
        :return:
        """
        try:
            predictions = self.net.predict(image)
        except Exception as e:
            print(f"Number detection failed. Error: {e}")
            return []

        return predictions
