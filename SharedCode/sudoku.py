def sudoku(input):
    """Solve Sudoku"""
    values = convert(input)
    solve(values)
    return values

def solve(values, x=0, y=0):
    """Solve Sudoku"""

    if y > 8:
        return True
    elif values[y][x] != 0: # solved
        if x == 8:
            if solve(values, 0, y + 1): # next row
                return True
        else:
            if solve(values, x + 1, y): # next column
                return True
    else:
        for i in range(1, 10): # check 1-9
            if check(values, x, y, i):
                values[y][x] = i
                if x == 8:
                    if solve(values, 0, y + 1): # next row
                        return True
                else:
                    if solve(values, x + 1, y): # next column
                        return True
        values[y][x] = 0 # unsolved
        return False

def check(values, x, y, i):
    """Check if the digit can be placed"""

    if row(values, y, i) and column(values, x, i) and block(values, x, y, i):
        return True
    return False

def row(values, y, i):
    """Check the row"""

    return all(True if i != values[y][_x] else False for _x in range(9))

def column(values, x, i):
    """Check the column"""

    return all(True if i != values[_y][x] else False for _y in range(9))

def block(values, x, y, i):
    """Check the 3x3 block"""

    xblock = (x // 3) * 3
    yblock = (y // 3) * 3
    return all(True if i != values[_y][_x] else False
            for _y in range(yblock, yblock + 3)
                for _x in range(xblock, xblock + 3))

def convert(input):
    """Create a nested list from input"""

    values = []
    digits = "123456789"

    chars = [c for c in input if c in digits or c in '0.']
    assert len(chars) == 81
    input_int = map(lambda x: int(x) if x != "." else 0, chars)

    count = 0
    row = []
    for i in input_int:
        row.append(i)
        count += 1
        if count % 9 == 0:
            values.append(row)
            row = []

    return values

if __name__ == "__main__":
    import sys, pprint
    values = sudoku(sys.argv[1])
    pprint.pprint(values)
