from abc import ABCMeta


class ObjectDetector(metaclass=ABCMeta):

    @abstractmethod
    def calculate_distance_to_object_in_front():
        pass