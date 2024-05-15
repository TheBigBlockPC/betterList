from typing import Iterable, SupportsIndex
from random import randint
class betterList(list):
    """
    This class enhances some limitations of Python lists and adds quality-of-life features.
    
    Attributes:
        immutable (bool): Flag indicating whether the betterList is immutable.

    Args:
        L (list, optional): Initial list to initialize the betterList. Defaults to an empty list.
        immutable (bool, optional): Flag to indicate whether the betterList is immutable. Defaults to False.
    """
    
    def __init__(self, L=[], immutable:bool = False):
        """
        Initializes a betterList instance.

        Args:
            L (list, optional): Initial list to initialize the betterList. Defaults to an empty list.
            immutable (bool, optional): Flag to indicate whether the betterList is immutable. Defaults to False.
        
        Raises:
            Exception: If L is not a valid list.
        """
        self.immutable = immutable
        if isinstance(L, list):
            temp = L.copy()
            self.__make_copy_valid__(temp)
            super().__init__(temp)
        else:
            try:
                super().__init__(L)
            except:
                raise Exception("Invalid type for L")

    def append(self, object) -> None:
        """
        Appends an object to the end of the betterList.

        Args:
            object: The object to be appended.
        """
        if isinstance(object, list):
            return super().append(object.copy())
        return super().append(object)

    def copy(self) -> list:
        """
        Returns a shallow copy of the betterList.

        Returns:
            list: A shallow copy of the betterList.
        """
        temp = super().copy()
        self.__make_copy_valid__(temp)
        return temp

    def extend(self, iterable: Iterable) -> None:
        """
        Extends the betterList by appending elements from the iterable.

        Args:
            iterable (Iterable): The iterable to extend the betterList with.
        """
        for i in iterable:
            self.append(i)

    def insert(self, index: SupportsIndex, object) -> None:
        """
        Inserts an object into the betterList at the specified index.

        Args:
            index (SupportsIndex): The index at which to insert the object.
            object: The object to be inserted.
        """
        if isinstance(object, list):
            return super().insert(index, object.copy())
        return super().insert(index, object)

    def __make_copy_valid__(self, L: list) -> list:
        """
        Ensures nested lists are copied properly in the list.

        Args:
            L (list): The list to validate and copy nested lists.

        Returns:
            list: The modified list with nested lists properly copied.
        """
        for index, value in enumerate(L):
            if isinstance(value, list):
                L[index] = value.copy()

    def __setitem__(self, index, value):
        """
        Sets the value of an element in the betterList at the specified index.

        Args:
            index: The index of the element to set.
            value: The value to set.
        
        Raises:
            TypeError: If the betterList is immutable.
        """
        if self.immutable:
            raise TypeError("this betterlist is set to immutable")
        else:
            super().__setitem__(index, value)

    # New features

    def set_immutable(self, immutable: bool):
        """
        Sets the immutability flag for the betterList.

        Args:
            immutable (bool): Flag indicating whether the betterList should be immutable.
        """
        self.immutable = immutable

    def apply_function(self, function: callable):
        """
        Applies a function to each element of the list.

        Args:
            function (callable): The function to be applied to each element.
        
        Returns:
            betterList: The modified betterList.
        """
        for index, value in enumerate(self):
            self[index] = function(value)
        return self

    def apply_function_listarg(self, function: callable):
        """
        Applies a function to each element of the list, passing the list and index as arguments.

        Args:
            function (callable): The function to be applied to each element.
        
        Returns:
            betterList: The modified betterList.
        """
        for index, value in enumerate(self):
            self[index] = function(self, index)
        return self

    def remove_nones(self):
        """
        Removes all None values from the list.
        
        Returns:
            betterList: The modified betterList.
        """
        while None in self:
            self.remove(None)
        return self

    def split_to_chunks(self, size):
        """
        Splits the list into chunks of the specified size.

        Args:
            size (int): The size of each chunk.
        
        Yields:
            betterList: Chunks of the list as betterList instances.
        """
        for i in range(0, len(self), size):
            yield self[i:i + size]

    def random_sample(self):
        """
        Returns a random value from the list.
        
        Returns:
            object: A randomly chosen value from the list.
        """
        return self[randint(0, len(self))]

    def find(self, value):
        """
        Finds the index of the first occurrence of the specified value in the list.

        Args:
            value: The value to search for.
        
        Returns:
            int: The index of the first occurrence of the value, or -1 if not found.
        """
        try:
            return self.index(value)
        except ValueError:
            return -1

    def math_add(self, value):
        """
        Adds a value to each element of the list.

        Args:
            value: The value to add to each element.
        """
        self.apply_function(lambda x: x + value)

    def math_subtract(self, value):
        """
        Subtracts a value from each element of the list.

        Args:
            value: The value to subtract from each element.
        """
        self.apply_function(lambda x: x - value)

    def math_add(self, value):
        """
        Moltiplys each element of the list with a value.

        Args:
            value: The value that each element gets multiplyed with.
        """
        self.apply_function(lambda x: x * value)

    def math_divide(self, value):
        """
        Divides each element of the list by a value.

        Args:
            value: The value that each element gets divided by.
        """
        self.apply_function(lambda x: x / value)

    def __is_numerical__(var):
        """
        Checks if a variable is of numerical type.

        Args:
            var: The variable to check.
        
        Returns:
            bool: True if the variable is of numerical type, False otherwise.
        """
        numerical_types = (int, float, complex)
        return isinstance(var, numerical_types)

    def min(self):
        """
        Finds the minimum value in the list.

        Returns:
            object: The minimum value in the list.
        """
        return min(self)

    def max(self):
        """
        Finds the maximum value in the list.

        Returns:
            object: The maximum value in the list.
        """
        return max(self)

    def average(self):
        """
        Calculates the average of numerical values in the list.

        Returns:
            float: The average of numerical values in the list.
        """
        temp = 0
        count = 0
        for i in self:
            if self.__is_numerical__(i):
                temp += i
                count += 1
        return temp / count if count > 0 else None

    def filter(self, function):
        """
        Filters the list based on a function.

        Args:
            function (callable): The function used for filtering.
        
        Returns:
            betterList: A new betterList containing elements that satisfy the function.
        """
        filtered_list = betterList()
        for item in self:
            if function(item):
                filtered_list.append(item)
        return filtered_list

    def __remap__(value, old_min, old_max, new_min, new_max):
        """
        Remaps a value from one range to another.

        Args:
            value: The value to remap.
            old_min: The minimum value of the old range.
            old_max: The maximum value of the old range.
            new_min: The minimum value of the new range.
            new_max: The maximum value of the new range.
        
        Returns:
            float: The remapped value.
        """
        return (value - old_min) * (new_max - new_min) / (old_max - old_min) + new_min

    def map(self, old_min, old_max, new_min, new_max):
        """
        Maps each value in the list from one range to another.

        Args:
            old_min: The minimum value of the old range.
            old_max: The maximum value of the old range.
            new_min: The minimum value of the new range.
            new_max: The maximum value of the new range.
        """
        self.apply_function(lambda x: self.__remap__(x, old_min, old_max, new_min, new_max))