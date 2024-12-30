"""
Given the coordinates of two points, determine if the points lie on the same line (horizontal, vertical, or diagonal).
"""
point1 = (10, 0)
point2 = (5, 0)

print("Output:")
if point1[0] == 0 and point2[0] == 0:
    print("Horizontal line")
elif point1[1] == 0 and point2[1] == 0:
    print("Vertical line")
else:
    print("Diagonal Line")