from abc import ABC, abstractmethod


class Addable(ABC):  # class of classes which has an add method

    @abstractmethod
    def __add__(self, other):
        return NotImplemented  # add that doesnt know how to add

    @classmethod
    def __subclasshook__(cls, C):  # declare ourselves to be a parent class of other classes, cls = our class, cls instead of self for convention
        if cls is not Addable:  # boiler plate
            return NotImplemented  # if subclasshook called on a subclass, no say on whether smth is a subclass of the subclass
        for B in C.__mro__:  # for subclass in C's method-resolution-order,
            if "__add__" in B.__dict__:  # dict of a class contains all attributes and methods that are live on that class
                if B.__dict__["__add__"] is None:  # B doesn't implement add, add is not allowed
                    return NotImplemented
                return True  # found add somewhere
        return NotImplemented  # went through method resolution order and haven't found an add
