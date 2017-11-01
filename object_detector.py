from abc import ABC, abstractmethod


class ObjectDetector(ABC):

    @abstractmethod
    def calculate_distance_to_object_in_front(x):
        """
        Calculate distance to object
        :param x: int deinstalation
        :return int distance to object
        """
        pass
