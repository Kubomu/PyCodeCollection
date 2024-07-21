import random

class MazeGenerator:
    """
    A class to generate a random maze.

    Attributes:
        rows (int): The number of rows in the maze.
        cols (int): The number of columns in the maze.
        maze (list): A 2D list representing the maze, where "#" represents a wall and " " represents an empty space.

    Methods:
        display_maze(): Prints the generated maze to the console.
    """

    def __init__(self, rows, cols):
        """
        Initializes the MazeGenerator with the specified number of rows and columns.

        Args:
            rows (int): The number of rows in the maze.
            cols (int): The number of columns in the maze.
        """
        self.rows = rows
        self.cols = cols
        self.maze = [[random.choice(["#", " "]) for _ in range(cols)] for _ in range(rows)]

    def display_maze(self):
        """
        Prints the generated maze to the console.

        Example:
            >>> maze_generator = MazeGenerator(10, 20)
            >>> maze_generator.display_maze()
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
            # # # # # # # # # # # # # # # # # # # # # # #
        """
        for row in self.maze:
            print("".join(row))

# Example of using the maze generator
maze_generator = MazeGenerator(10, 20)

print("Generated Maze:")
maze_generator.display_maze()