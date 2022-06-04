from mandelbrot import generateMandelbrot
from PIL import Image
from settings import inputSettings
import time
import os

IMAGE_FOLDER = "images" # if changing, also update gitignore

settings = inputSettings()

image = Image.new("RGB", (settings.width, settings.height))
pixels = []

startTime = time.time()

pixels = generateMandelbrot(settings)

print("Saving image")

image.putdata(pixels)

imageDirectory = f"{IMAGE_FOLDER}/{settings.selectedPresetName}.png"
if not os.path.exists(IMAGE_FOLDER):
    os.mkdir(IMAGE_FOLDER)

image.save(imageDirectory)

print(f"Image saved to {imageDirectory}.")
print("Total Elapsed: " + str(time.time() - startTime))