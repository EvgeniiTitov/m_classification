import cv2
import numpy


class ResultsProcessor:

    @staticmethod
    def save_processed_image(image: numpy.ndarray) -> None:
        raise NotImplementedError

    @staticmethod
    def visualise_results(elements: list, image: numpy.ndarray) -> numpy.ndarray:
        """

        :param elements:
        :param image:
        :return:
        """
        for element in elements:
            color = (204, 0, 102)
            left = element[2]
            top = element[3]
            right = element[4]
            bot = element[5]
            formatting = cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2

            if element[0] == 0:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '0', (left, top + 50), *formatting)
            elif element[0] == 1:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '1', (left, top + 50), *formatting)
            elif element[0] == 2:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '2', (left, top + 50), *formatting)
            elif element[0] == 3:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '3', (left, top + 50), *formatting)
            elif element[0] == 4:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '4', (left, top + 50), *formatting)
            elif element[0] == 5:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '5', (left, top + 50), *formatting)
            elif element[0] == 6:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '6', (left, top + 50), *formatting)
            elif element[0] == 7:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '7', (left, top + 50), *formatting)
            elif element[0] == 8:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '8', (left, top + 50), *formatting)
            elif element[0] == 9:
                cv2.rectangle(image, (left, top), (right, bot), color, 2)
                cv2.putText(image, '9', (left, top + 50), *formatting)

        return image
