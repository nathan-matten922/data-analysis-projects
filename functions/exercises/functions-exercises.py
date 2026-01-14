# Part 1 A -- Make a Line
def make_line(size):
    line = ""
    for i in range(size):
        line += "#"
    return(line)
print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = make_rectangle(size,size)
    return square
print(make_square(5))




# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
    rectangle = ""
    for i in range(height):
        rectangle += make_line(width)
        if i < height - 1:
            rectangle += '\n'
    return rectangle
print(make_rectangle(5,3))




# Part 2 A -- Make a Stairs

def make_downward_stairs(size):
    stairs = ""
    for i in range(size):
        stairs += make_line(i+1)
        if i < size -1:
            stairs += '\n'
    return stairs
print(make_downward_stairs(5))


# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    spaces = ""
    chars = make_line(numChars)
    for i in range(numSpaces):
        spaces += " "
    return spaces + chars + spaces
print(make_space_line(3,5))


# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += make_space_line(height - i - 1, (2 * i + 1))
        if i < height - 1: 
            triangle += '\n'
    return triangle

print(make_isosceles_triangle(5))



# Part 3 -- Make a Diamond
def make_diamond(height):
    diamond = ""
    for i in range(height):
        spaces = " " * (height - i - 1)
        hash = "#" * (2 * i + 1)
        diamond += spaces + hash + "\n"

    for i in range(height - 2, -1, -1):
        spaces = " " * (height - i - 1)
        hash = "#" * (2 * i + 1)
        diamond += spaces + hash + "\n"

    return diamond

print(make_diamond(5))

def make_diamond_2(height):
    diamond = make_isosceles_triangle(height) + '\n'
    for i in range(height - 2, -1, -1):
        spaces = " " * (height - i - 1)
        hash = "#" * (2 * i + 1)
        diamond += spaces + hash + "\n"
    return diamond

print(make_diamond_2(5))