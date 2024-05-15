# betterList

`betterList` is a Python class that enhances some limitations of Python lists and adds quality-of-life features for improved list manipulation.

## Features

- **Nested List Support:** Properly handles nested lists, preventing unexpected behavior when working with nested data structures.
- **Immutability:** Supports immutability, preventing accidental modification of lists when immutability is desired.
- **Functional Programming:** Provides methods for applying functions to each element of the list, filtering elements, and mapping values to new ranges.
- **Convenience Methods:** Includes convenience methods for statistical calculations, random sampling, and finding elements in the list.

## Installation

Copy the [betterList.py](betterList.py) in to your project and have fun

## Usage

```python
from betterList import betterList

# Create a betterList instance
my_list = betterList([1, 2, 3, [4, 5]])

# Append an element to the list
my_list.append(6)

# Apply a function to each element
my_list.apply_function(lambda x: x * 2)

# Remove None values from the list
my_list.remove_nones()

# Split the list into chunks
chunks = list(my_list.split_to_chunks(2))

# Find the index of a value in the list
index = my_list.find(4)

# Map values to a new range
my_list.map(0, 10, 0, 100)
```

## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/TheBigBlockPC//betterList).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
