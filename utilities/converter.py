xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ymin = float(input("Enter ymin: "))
ymax = float(input("Enter ymax: "))

width = xmax - xmin
height = ymax - ymin
xCentre = (xmin + xmax) / 2
yCentre = (ymin + ymax) / 2

print("Width: " + str(width))
print("Height: " + str(height))
print(f"Centre: ({xCentre}, {yCentre})")

if abs(width - height) > 0.001:
    print("Warning: non-square aspect ratio. Use one value for both xWidth and yWidth for a square aspect ratio.")