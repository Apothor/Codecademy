# Generator expression using nested range.
def timesTable():
    [print(*(x for x in range(y, 13*y, y))) for y in range(1, 13)]
    
timesTable()

# Generator expression using multiplication.
def oddTimesTables():
    [print(*(x*y for x in range(1, 13, 2))) for y in range(1, 13, 2)]

oddTimesTables()