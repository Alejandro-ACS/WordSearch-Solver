from PIL import Image # To get the dimensions of the image

import pygame # To start and manage game

import argparse # To set arguments

import csv # To open and read csv files

import pandas as pd

# Add arguments

parser = argparse.ArgumentParser(description='Crossword cheats')

parser.add_argument("--crossword", help="Put the location of your crossword", default="./Crossword.png")

parser.add_argument("--puzzle", help="Put the location of the CSV crossword file", default="./crossword.csv")

parser.add_argument("--words", help="Put the location of the CSV list of words of the crosswords file", default="./list.csv")

args = parser.parse_args()

# Get puzzle dimensions

image = Image.open(args.crossword)

width, height = image.size

width1, height1 = width, height

# Functions to count lines and rows

def color(columns, rows):
    
    X = rows*box_width

    Y = columns*box_height

    s = pygame.Surface((box_width,box_height))

    s.set_alpha(128)

    s.fill((255,0,0))

    screen.blit(s, (X,Y))

    pygame.display.update()

def count_rows(fileName : str):
    num_rows = 0

    for row in open(fileName):
        num_rows += 1

    return num_rows + 1

def count_columns(fileName : str):

    results = pd.read_csv(fileName)
    
    return len(results) + 1

def coordinates(iw, ih):

    global box_height
    
    global box_width

    box_height = ih / count_columns(args.puzzle)

    box_width = iw / count_rows(args.puzzle)

def crossWord(args : str):

    class Puzzle:

        def __init__(self, args):

            self.puzzle = self.parse_puzzle(args.puzzle)

            self.words = self.parse_words(args.words)

            self.solved = []

        def parse_puzzle(self, puzzle_name):

            puzzle = []

            with open(puzzle_name, 'r') as pfile:

                p_reader = csv.reader(pfile)

                for p_row in p_reader:

                    puzzle.append(p_row)

            return puzzle

        def parse_words(self, list_name):

            words = []

            with open(list_name, 'r') as cfile:

                c_reader = csv.reader(cfile)

                for c_row in c_reader:

                    words.append(str(c_row[0]).replace(' ', '')) 

            return words 

        def output_cli(self):

            for ri, row in enumerate(self.puzzle):

                for chi, ch in enumerate(row[0]):

                    if (ri, chi) in self.solved:

                        color(ri, chi)

        def find_word(self):

            for word in self.words:

                if self.find_horizontal(word):

                    continue

                if self.find_vertical(word):

                    continue

                if self.find_diagonal(word):

                    continue

        def find_horizontal(self, word):

            for ri, row in enumerate(self.puzzle):

                if word in str(row):

                    for i in range(0, len(word)):

                        self.solved.append((ri, str(row).find(word) - 2 + i))

                    return True

                row_r = str(row)[::-1]

                if word in row_r:

                    for i in range(0, len(word)):

                        self.solved.append((ri, len(row_r) - str(row_r).find(word) - 3 - i))

                    return True

            return False

        def find_vertical(self, word):

            for char in range(len(self.puzzle[0][0])):

                temp = []

                for col in range(len(self.puzzle)):

                    temp.append(self.puzzle[col][0][char])

                temp = ''.join(temp)

                temp_r = temp[::-1]

                if word in str(temp):

                    for i in range(0, len(word)):

                        self.solved.append((str(temp).find(word) + i, char))

                    return True

                if word in str(temp_r):

                    for i in range(0, len(word)):

                        self.solved.append((len(temp_r) - str(temp_r).find(word) - 1 - i, char))

                    return True

            return False

        def find_diagonal(self, word):

            for a in range(0, len(self.puzzle[0][0])):

                diagonal = count_columns(args.puzzle) - 1

                temp = [[] for i in range(8)]

                ranges = [[] for i in range(8)]

                i = 0

                while ((a - i) >= 0) and (i < len(self.puzzle)):

                    coords = [[i, a-i],[diagonal-i, a-i], [diagonal-i, diagonal-(a-i)], [i, diagonal-(a-i)]]

                    for cx, c in enumerate(coords):

                        temp[cx].append(self.puzzle[c[0]][0][c[1]])

                        ranges[cx].append((c[0], c[1]))

                        ranges[cx+4].append((c[1], c[0]))

                    i+=1


                for ti in range(4):

                    temp[ti] = ''.join(temp[ti])

                    temp[ti+4] = temp[ti][::-1]


                for tx, t in enumerate(temp):

                    if word in str(t):

                        for i in range(0, len(word)):

                            self.solved.append(ranges[tx][str(t).find(word) + i])

                        return True

            return False

    p = Puzzle(args)

    p.output_cli()

    p.find_word()

    p.output_cli()

# Pygame

coordinates(width, height)

pygame.display.set_caption('Crossword cheat (' + args.crossword.replace("./","") + ')')

clock = pygame.time.Clock()

screen = pygame.display.set_mode([width, height])

done = False

background = pygame.image.load(args.crossword).convert()

z = 1

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

    if z != 0:

        screen.blit(background, [0, 0])

        crossWord(args)

        pygame.display.flip()

        z = 0

    
pygame.quit()