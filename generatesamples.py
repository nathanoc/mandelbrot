from PIL import Image
import presets
import time
from mandelbrot import generateMandelbrot

width = 1024
height = 1024
iterations = 1000
rowsPerOutput = 64

for key in presets.presets.keys():
    preset = presets.presets[key]
    xWidth = preset["xWidth"]
    yWidth = preset["yWidth"]
    centrePos = preset["centrePos"]
    palette = preset["palette"]

    print(f"! Starting generation for preset {key}")
    pixels = generateMandelbrot(
        width = width,
        height = height,
        xWidth = xWidth,
        yWidth = yWidth,
        centrePos = centrePos,
        iterations = iterations,
        palette = palette,
        rowsPerOutput = rowsPerOutput,
        startTime = time.time()
    )
    print(f"! Completed generation - saving...")
    image = Image.new("RGB", (width, height))
    image.putdata(pixels)
    image.save(f"samples/{key}.png")
    print("! Saved")

print("Generation complete")