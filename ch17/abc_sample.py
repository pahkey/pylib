from abc import ABCMeta, abstractmethod


class Bird(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()
