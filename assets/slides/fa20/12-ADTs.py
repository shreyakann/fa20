def point(x, y): # constructor
        return (x, y)

x = lambda point: point[0] # selector, could easily be a normal function
y = lambda point: point[1]

def subtract(p1, p2): # Operator
    return point(x(p2) - x(p1), y(p2) - y(p1))

def distance(p1, p2): # Operator
    """Pythagorean theorem between 2 points"""
    difference = subtract(p1, p2)
    return (x(difference)**2 + y(difference)**2) ** 0.5


# Using our new ADT
origin = point(0, 0)
my_house = point(5, 5) # Random values, for illustration.
campus = point(8, 9)

distance_to_campus = distance(my_house, campus)

print(distance_to_campus)
