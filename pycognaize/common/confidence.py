from collections.abc import dict_keys
from typing import Union


class Confidence:
    """
    This class is used by tag object to store confidence values
    of possible classes.
    """

    def __init__(self, confidences=None):
        """
        Initialize class with confidence scores.
        :param confidences: dictionary of class names and their confidence
        """
        self._is_finalized = False
        if confidences and isinstance(confidences, dict):
            self.confidences = confidences
            self.finalize()
        else:
            self.confidences = {}

    def add_class(self, class_name: str,
                  confidence: Union[float, int]) -> None:
        """Add new class for confidence scores
        :param class_name: name of the class
        :param confidence: confidence score for the class
        """
        self.confidences[class_name] = confidence

    def number_of_classes(self) -> int:
        """Returns number of classes"""
        return len(self.confidences)

    def class_names(self) -> dict_keys:
        """Returns class names"""
        return self.confidences.keys()

    def get_confidence(self) -> dict:
        """Returns confidence scores if finalized"""
        if not self._is_finalized:
            raise ValueError('Confidence scores have to be finalized.')
        return self.confidences

    @property
    def is_finalized(self) -> bool:
        return self._is_finalized

    def finalize(self) -> None:
        """Finalize confidence scores by checking if all scores sum to 1"""
        if not sum(self.confidences.values()) == 1:
            raise ValueError('Confidence scores have to sum up to 1.')
        self._is_finalized = True

    def __getitem__(self, item: str) -> Union[float, int]:
        if not self._is_finalized:
            raise ValueError('Confidence scores have to be finalized.')
        if item in self.confidences:
            return self.confidences[item]
        else:
            raise KeyError(f'Class {item} not found in confidence scores.')

    def __setitem__(self, key, value) -> None:
        self.confidences[key] = value
