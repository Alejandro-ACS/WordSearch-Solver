# Crossword-Solver
Solve any word search puzzle in a matter of milliseconds.

# Requeriments
In order to run the program, the following libraries must be installed: **Pygame, pillow, pandas, csv and argparse**. To install all libraries you need to run the following commands.
```bash
pip install pygame

pip install pandas

pip install pillow

pip install csv-reader

pip install argparse
```

# Run file
To execute the file, you must have an image file that contains the crossword and replace it in the folder with the one that comes by default called "Crossword.png".In order for the program to scan the alphabet soup, you have to manually type each row and each column of the puzzle in the "crossword.csv" file and write the words you want it to search for in the "list.csv" file. Then execute the following command in the path where the program is located the following command.
```bash
python solver.py
```
