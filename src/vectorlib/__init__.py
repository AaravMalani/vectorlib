from __future__ import annotations
from collections.abc import Iterable
from itertools import zip_longest

class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            raise Exception("Invalid argument length: 0")
        if isinstance(args[0], Iterable) and all(map(lambda x: isinstance(x, float) or isinstance(x, int), args[0])):
            self.__data: list[float] = [float(i) for i in args[0]]
        else:
            self.__data: list[float] = [float(i) for i in args]

    @property
    def magnitude(self) -> float:
        """The magnitude of the vector

        Returns:
            float: The magnitude
        """
        return sum(map(lambda x: x**2, self.__data))**0.5

    @property
    def dim(self) -> tuple:
        """The dimension of the vector

        Returns:
            tuple: The dimension
        """
        return (len(self.__data),)

    @property
    def direction(self) -> Vector:
        """A unit vector in the direction of the vector

        Returns:
            Vector: The direction vector
        """
        return self/self.magnitude
        
    def __add__(self, other):
        if not type(other) is Vector:
            raise Exception('You can only add vectors')
        return Vector(list(map(sum, zip_longest(self.__data, other.__data, fillvalue=0))))

    def __sub__(self, other):
        if not type(other) is Vector:
            raise Exception('You can only add vectors')
        return Vector(list(map(lambda x: x[0]-x[1], zip_longest(self.__data, other.__data, fillvalue=0))))

    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only multiply scalars')
        return Vector(list(map(lambda x: x*other, self.__data)))
    def __rmul__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only multiply scalars')
        return Vector(list(map(lambda x: x*other, self.__data)))
    def __iter__(self):
        for i in self.__data:
            yield i

    def __truediv__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only divide scalars')
        return Vector(list(map(lambda x: x/other, self.__data)))

    def __floordiv__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only divide scalars')
        return Vector(list(map(lambda x: x//other, self.__data)))

    def __mod__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use modulus with scalars')
        return Vector(list(map(lambda x: x % other, self.__data)))

    def __pow__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use powers with scalars')
        return Vector(list(map(lambda x: x**other, self.__data)))

    def __lshift__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use left-shift with scalars')
        return Vector(list(map(lambda x: x << other, self.__data)))

    def __rshift__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use right-shift with scalars')
        return Vector(list(map(lambda x: x >> other, self.__data)))

    def __and__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use AND with scalars')
        return Vector(list(map(lambda x: x & other, self.__data)))

    def __or__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use OR with scalars')
        return Vector(list(map(lambda x: x | other, self.__data)))

    def __xor__(self, other):
        if type(other) not in [int, float]:
            raise Exception('You can only use XOR with scalars')
        return Vector(list(map(lambda x: x ^ other, self.__data)))

    def dot(self, other: Vector) -> Vector:
        """Returns the dot product of the two vectors

        Args:
            other (Vector): The second operand

        Returns:
            Vector: The result of the dot product
        """
        return sum((map(lambda x: x[0]*x[1], zip_longest(self.__data, other.__data, fillvalue=0))))

    def cross(self, other : Vector) -> Vector:
        """Returns the cross product of the two vectors (only 3D x 3D for now)

        Args:
            other (Vector): The second operand

        Raises:
            Exception: Throws if the vectors are not 3-dimensional

        Returns:
            Vector: The result of the cross product
        """
        if self.dim != other.dim or self.dim != (3,):
            raise Exception("Can only take 3D cross product for now")

        # Add n-dimensional cross products
        return Vector(self.__data[1]*other.__data[2]-self.__data[2]*other.__data[1], -self.__data[0]*other.__data[2]+self.__data[2]*other.__data[0], self.__data[0]*other.__data[1]-self.__data[1]*other.__data[0])
    
    def __repr__(self):
        return 'Vector'+str(tuple(self.__data))
    def __eq__(self, other):
        return isinstance(other, Vector) and self.__data == other.__data
