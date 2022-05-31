from mandelbrot import generateMandelbrot
from PIL import Image
import presets
import time

width = int(input("Enter width in pixels: "))
height = width
image = Image.new("RGB", (width, height))
pixels = []

iterations = int(input("Enter max iterations (recommended = 500): "))

print("Preset list:")
for key in presets.presets.keys():
    print(" - " + key)
print(" - custom")
selectedPresetName = input("Enter preset name: ")
if selectedPresetName != "custom":
    selectedPreset = presets.presets[selectedPresetName]

    xWidth = selectedPreset["xWidth"]
    yWidth = selectedPreset["yWidth"]
    centrePos = selectedPreset["centrePos"]
    palette = selectedPreset["palette"]
else:
    xWidth = float(input("Enter xWidth: "))
    yWidth = float(input("Enter yWidth: "))
    centrePos = (float(input("Enter centrePosX: ")), float(input("Enter centrePosY: ")))
    
    print("Palette preset list:")
    for key in presets.presets.keys():
        if presets.presets[key]["showInPaletteList"]:
            print(" - " + key)
    selectedPaletteName = input("Enter palette preset name: ")
    palette = presets.presets[selectedPaletteName]["palette"]

rowsPerOutput = int(input("Enter rows per console output: "))

startTime = time.time()

pixels = generateMandelbrot(width, height, xWidth, yWidth, centrePos, iterations, palette, rowsPerOutput, startTime)

print("Fractal completed - saving image")
print("Elapsed: " + str(time.time() - startTime))

image.putdata(pixels)

imageDirectory = f"images/{selectedPresetName}.png"
image.save(imageDirectory)

print(f"Image saved to {imageDirectory}.")
print("Total Elapsed: " + str(time.time() - startTime))