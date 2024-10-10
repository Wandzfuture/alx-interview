# Island Perimeter

This project contains a Python function that calculates the perimeter of an island in a grid.

## Description

The main component of this project is the `island_perimeter` function, which takes a 2D grid as input and returns the perimeter of the island represented in the grid. In this context:

- 0 represents water
- 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS

## File Descriptions

- `0-island_perimeter.py`: Contains the `island_perimeter` function.
- `0-main.py`: A main file to test the `island_perimeter` function.

## Usage

To use the `island_perimeter` function:

1. Ensure you have Python 3.4.3 or later installed on your Ubuntu 20.04 LTS system.
2. Clone this repository or copy the `0-island_perimeter.py` file to your local machine.
3. Make the file executable:
   ```
   chmod +x 0-island_perimeter.py
   ```
4. You can then import and use the function in your Python script:
   ```python
   from 0-island_perimeter import island_perimeter

   grid = [
       [0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0]
   ]
   print(island_perimeter(grid))  # Should output: 12
   ```

## Testing

You can use the provided `0-main.py` file to test the function:

1. Ensure both `0-island_perimeter.py` and `0-main.py` are in the same directory.
2. Run the main file:
   ```
   ./0-main.py
   ```
3. The output should be 12, which is the perimeter of the island in the example grid.

## Style and Documentation

- The code follows PEP 8 style guidelines (version 1.7).
- All modules and functions are documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
