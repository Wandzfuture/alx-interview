# Rotate 2D Matrix

This project contains a Python function that rotates an n x n 2D matrix 90 degrees clockwise in-place.

## Requirements

- Python 3.8.10
- Ubuntu 20.04 LTS

## Usage

```python
#!/usr/bin/python3
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

## Function Description

```python
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (List[List[int]]): The input n x n 2D matrix.

    Returns:
    None. The matrix is edited in-place.
    """
```

## File Descriptions

- `0-rotate_2d_matrix.py`: Contains the `rotate_2d_matrix` function.

## Coding Style

This project follows the `pycodestyle` style guide (version 2.8.0).

## Author

[Your Name]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
