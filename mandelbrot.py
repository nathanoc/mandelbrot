from PIL import Image
import math
import time
import presets

width = int(input("Enter width in pixels: "))
height = width
image = Image.new("RGB", (width, height))
pixels = []

iterations = int(input("Enter max iterations (recommended = 500): "))

print("Preset list:")
for key in presets.presets.keys():
    print(key)
print("custom")
selectedPresetName = input("Enter preset name: ")
if selectedPresetName != "custom":
    selectedPreset = presets.presets[selectedPresetName]

    xWidth = selectedPreset["xWidth"]
    yWidth = selectedPreset["yWidth"]
    centrePos = selectedPreset["centrePos"]
    redWeight = selectedPreset["redWeight"]
    redPow = selectedPreset["redPow"]
    greenWeight = selectedPreset["greenWeight"]
    greenPow = selectedPreset["greenPow"]
    blueWeight = selectedPreset["blueWeight"]
    bluePow = selectedPreset["bluePow"]
else:
    xWidth = float(input("Enter xWidth: "))
    yWidth = float(input("Enter yWidth: "))
    centrePos = (float(input("Enter centrePosX: ")), float(input("Enter centrePosY: ")))
    redWeight = float(input("Enter redWeight: "))
    redPow = float(input("Enter redPow: "))
    greenWeight = float(input("Enter greenWeight: "))
    greenPow = float(input("Enter greenPow: "))
    blueWeight = float(input("Enter blueWeight: "))
    bluePow = float(input("Enter bluePow: "))

rowsPerOutput = 256
startTime = time.time()

for yInt in range(int(width/2), int(-width/2), -1):
    y = centrePos[1] + (yInt / height * yWidth)
    for xInt in range(int(-width/2), int(width/2)):
        x = centrePos[0] + (xInt / width * xWidth)

        Z = (0, 0)
        C = (x, y)

        for iteration in range(1, iterations + 1):
            a = Z[0]
            b = Z[1]
            c = C[0]
            d = C[1]

            calc = (a ** 2 - b ** 2 + c, 2 * a * b + d)
            Z = calc

            if Z[0] ** 2.0 + Z[1] ** 2.0 > 4.0:
                break
        if Z[0] ** 2.0 + Z[1] ** 2.0 < 4.0:
            pixels.append((0,0,0))
        else:
            pixels.append((
                int(math.pow(float(iteration) / float(iterations), redPow) * 255.0 * redWeight),
                int(math.pow(float(iteration) / float(iterations), greenPow) * 255.0 * greenWeight),
                int(math.pow(float(iteration) / float(iterations), bluePow) * 255.0 * blueWeight)
            ))
    if yInt % rowsPerOutput == 0 and height - int(height/2 + yInt) != 0:
        rowsRemaining = int(height/2 + yInt)
        rowsCompleted = height - int(height/2 + yInt)
        
        elapsed = time.time() - startTime
        etr = elapsed / rowsCompleted * rowsRemaining

        print(str(rowsRemaining) + " rows remaining.\tElapsed: " + str(elapsed) + "\tRemaining: " + str(etr))

print("Fractal completed - saving image")
print("Elapsed: " + str(time.time() - startTime))

image.putdata(pixels)
image.save("mandelbrot.png")

print("Image saved.")
print("Total Elapsed: " + str(time.time() - startTime))