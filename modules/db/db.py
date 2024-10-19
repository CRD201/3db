from abc import ABC, abstractmethod
from typing import List
from .model.car import Car


class Db(ABC):

    @abstractmethod
    def insert_element(self, car: Car):
        pass


    @abstractmethod
    def insert_elements(self, cars: List[Car]):
        pass
