from neural_networks import WaterCounterDetector, NumberDetector, NeuralNet
from preprocessing import PreProprocessor
from utils import ResultsProcessor
import os
import cv2


def main():
    test_dir = r"C:\Users\Evgenii\Downloads\test_images"
    # Initialize neural nets
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
    counter_detector = WaterCounterDetector(net=counters_net)
    numbers_detector = NumberDetector(net=numbers_net)

    show = False
    for file in os.listdir(test_dir):
        path_to_file = os.path.join(test_dir, file)

        # Check if image and we can open it
        if not any(file.endswith(ext.lower()) for ext in [".jpg", ".jpeg", ".png"]):
            continue

        # Attempt image decoding. Continue if failed
        try:
            image = cv2.imread(path_to_file)
        except Exception as e:
            print(f"Failed during decoding an image: {file}. Error: {e}")
            continue

        # STEP 1 - detect water meter on the image
        counter = counter_detector.detect_meter(image)
        if len(counter) == 0:
            print(f"No water meter detected for: {file}. Skipping")
            continue

        # STEP 2 - proprocess images by rotating them
        rotated_meter = PreProprocessor.orient_numbers(counter)
        processed_meter = PreProprocessor.finalize(rotated_meter)

        # STE3 3 - predict numbers
        number_predictions = numbers_detector.detect_numbers(processed_meter)

        # STEP 4 - post process number predictions, draw BB, write classes
        image_out = ResultsProcessor.visualise_results(number_predictions, processed_meter)

        if show:
            cv2.imshow('', image_out)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()