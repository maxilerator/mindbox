from abc import abstractmethod, ABC


# All inheritors of the class must have an area method
# We
class Figure(ABC):

    @abstractmethod
    def area(self):
        pass
