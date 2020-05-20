from neural_networks import WaterCounterDetector, NumberDetector, NeuralNet
from preprocessing import PreProprocessor
from PIL import Image
from utils import ResultsProcessor
import os
import cv2


class Detector:

    def __init__(self):

        # Initialize neural networks
        counters_net = NeuralNet(
            confidence_thresh=0.2,
            NMS_thresh=0.5,
            network_resolution=608,
            path_config=r"C:\Users\Evgenii\Desktop\Python_Programming\Python_Projects\WaterMeter\dependencies\yolo_meters.cfg",
            path_weights=r"C:\Users\Evgenii\Desktop\Python_Programming\Python_Projects\WaterMeter\dependencies\yolo_meters.weights"
        )
        numbers_net = NeuralNet(
            confidence_thresh=0.2,
            NMS_thresh=0.5,
            network_resolution=608,
            path_config=r"C:\Users\Evgenii\Desktop\Python_Programming\Python_Projects\WaterMeter\dependencies\yolo_numbers.cfg",
            path_weights=r"C:\Users\Evgenii\Desktop\Python_Programming\Python_Projects\WaterMeter\dependencies\yolo_numbers.weights"
        )

        # Initialize detectors
        self.counter_detector = WaterCounterDetector(net=counters_net)
        self.numbers_detector = NumberDetector(net=numbers_net)

    def predict(self, image: Image) -> list:
        """

        :param image:
        :return:
        """
        # STEP 1 - detect water meter on the image
        counter = self.counter_detector.detect_meter(image)
        if len(counter) == 0:
            return []

        # STEP 2 - proprocess images by rotating them
        rotated_meter = PreProprocessor.orient_numbers(counter)
        processed_meter = PreProprocessor.finalize(rotated_meter)

        # STE3 3 - predict numbers, sort appearance left to right
        predictions = self.numbers_detector.detect_numbers(processed_meter)
        predictions.sort(key=lambda e: e[2])

        # STEP 4 - post process number predictions, draw BB, write classes
        image_out = ResultsProcessor.visualise_results(predictions, processed_meter)
        numbers_out = [e[0] for e in predictions]

        # cv2.imshow('', image_out)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return numbers_out
