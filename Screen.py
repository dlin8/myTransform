#!~/usr/bin/env python3

# Takes width and height
# Returns a 2D array with given dimensions and the color 0x000000 for each element
def createScreen(width, height):
    screen = []
    for i in range(0, width):
        screen.append([])
        for j in range(0, height):
            screen[i].append([0,0,0])
    return screen

# Sets all screen elements to black
def clearScreen(screen):
    for i in range(0, len(screen)):
        for j in range(0, len(screen[i])):
            screen[i][j] = [0,0,0]

# Plots a point on x y of screen with color
# Does not work if x or y are out of bounds
def plot(screen, x, y, color):
    width = len(screen)
    height = len(screen[0])
    if(x >= width or y >= height):
        print('Out of bounds!')
        return False
    screen[x][y][0] = color[0]
    screen[x][y][1] = color[1]
    screen[x][y][2] = color[2]

# Writes a ppm file based off of a screen with P3 format as fileName.ppm with comment
def writePpmFile(screen, fileName, comment):
    width = len(screen)
    height = len(screen[0])
    file = open('{}.ppm'.format(fileName), 'w')
    file.write('P3\n')
    file.write('{} {} 255\n'.format( width, height ) )
    file.write('#{}\n'.format(comment))
    # Height first because ppm writes an image a row at a time
    # Using row first would increment height within the nested loop
    # This would result in drawing images by the values per column
    for i in range(0, height):
        for j in range(0, width):
            # Spacing to make each pixel stand out
            file.write('{} {} {}  '.format( screen[j][i][0], screen[j][i][1], screen[j][i][2] ) )
    file.close()
