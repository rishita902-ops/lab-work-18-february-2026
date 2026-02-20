import math

# ---------------- CUBE ----------------
def cube_surface_area(side):
    return 6 * side * side

def cube_volume(side):
    return side ** 3


# ---------------- CUBOID ----------------
def cuboid_surface_area(length, breadth, height):
    return 2 * (length*breadth + breadth*height + height*length)

def cuboid_volume(length, breadth, height):
    return length * breadth * height


# ---------------- CYLINDER ----------------
def cylinder_curved_surface_area(radius, height):
    return 2 * math.pi * radius * height

def cylinder_total_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius * radius * height


# ---------------- CONE ----------------
def cone_curved_surface_area(radius, height):
    l = math.sqrt(radius**2 + height**2)   # slant height
    return math.pi * radius * l

def cone_total_surface_area(radius, height):
    l = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + l)

def cone_volume(radius, height):
    return (1/3) * math.pi * radius * radius * height


# ---------------- SPHERE ----------------
def sphere_surface_area(radius):
    return 4 * math.pi * radius * radius

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


# ---------------- HEMISPHERE ----------------
def hemisphere_curved_surface_area(radius):
    return 2 * math.pi * radius * radius

def hemisphere_total_surface_area(radius):
    return 3 * math.pi * radius * radius

def hemisphere_volume(radius):
    return (2/3) * math.pi * radius**3


