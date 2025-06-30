def get_element_at_index(lst, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range.")
    return lst[index]

my_list = ['a', 'b', 'c', 'd']
print(get_element_at_index(my_list, 2))
print(get_element_at_index(my_list, 5))

"""
| Exception             | When to Raise It                                                                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `ValueError`          | When a function receives a value that has the right type but an inappropriate value. <br>*e.g., `k` is too small or too large for the array.* |
| `TypeError`           | When a function receives an argument of the wrong type. <br>*e.g., `k` is a string instead of an integer.*                                    |
| `IndexError`          | When trying to access an index that is out of the list’s bounds. <br>*Typically raised by Python itself.*                                     |
| `KeyError`            | When trying to access a dictionary key that doesn’t exist.                                                                                    |
| `ZeroDivisionError`   | When attempting to divide by zero.                                                                                                            |
| `FileNotFoundError`   | When trying to open a file that doesn’t exist.                                                                                                |
| `AssertionError`      | When an `assert` statement fails.                                                                                                             |
| `RuntimeError`        | For errors that don’t fit other categories but occur during runtime.                                                                          |
| `NotImplementedError` | To indicate that a method is expected to be implemented in a subclass.                                                                        |
| `AttributeError`      | When an invalid attribute is accessed on an object.                                                                                           |
| `OverflowError`       | When a numeric operation exceeds the limits of the data type.                                                                                 |
| `StopIteration`       | To signal the end of an iterator (usually automatically raised).                                                                              |
"""