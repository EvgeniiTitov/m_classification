import numpy as np

class WaterCounterDetector:
    def __init__(self, net):
        # Initialize the net provided
        self.net = net
        print("Water counter detector initialized")

    def detect_meter(self, image: np.ndarray) -> list:
        """

        :param image:
        :return:
        """
        predictions = self.net.predict(image)
        original_image = image.copy()

        serial_number = list()

        # Pick only the serial number
        if predictions:
            for element in predictions:
                if element[0] == 0:
                    cropped = original_image[element[3]-15:element[5]+15, element[2]-15:element[4]+15]
                    serial_number.append(cropped)

        # As per requirements, there will be only one serial number on the photo
        if len(serial_number) > 1:
            print("Something went wrong. More than 1 serial number detected on the photo")
            return serial_number[0]

        return serial_number
