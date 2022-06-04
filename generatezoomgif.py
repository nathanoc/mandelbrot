import imageio
from PIL import Image
from settings import Settings, inputSettings
import os
from mandelbrot import generateMandelbrot
import shutil
from pygifsicle import optimize

INITIAL_WIDTH = 4

frameCount = int(input("Enter frame count: "))
fps = int(input("Enter frames per second: "))
savedFileName = input("Enter a file name for the generated GIF: ")
finalFrameSettings = inputSettings()

if os.path.exists("tempFramesStorage"):
    shutil.rmtree("tempFramesStorage")
os.mkdir("tempFramesStorage")

gifFrames = []

exponentBase = finalFrameSettings.xWidth ** (1/frameCount)
for frameNumber in range(frameCount):
    print(f"Generating frame {frameNumber} of {frameCount}")

    frameImage = Image.new("RGB", (finalFrameSettings.width, finalFrameSettings.height))

    xWidth = INITIAL_WIDTH * (finalFrameSettings.xWidth / INITIAL_WIDTH) ** ((frameNumber + 1) / frameCount)

    frame = generateMandelbrot(Settings(
        finalFrameSettings.width,
        finalFrameSettings.height,
        xWidth,
        xWidth * (finalFrameSettings.yWidth / finalFrameSettings.xWidth),
        finalFrameSettings.centrePos,
        finalFrameSettings.iterations,
        finalFrameSettings.palette,
        finalFrameSettings.rowsPerOutput
    ))

    frameImage.putdata(frame)
    frameImage.save(f"tempFramesStorage/{frameNumber}.png")

    gifFrames.append(imageio.imread(f"tempFramesStorage/{frameNumber}.png"))

# Have the gif stay on the last frame for a few seconds
for i in range(fps * 3):
    gifFrames.append(imageio.imread(f"tempFramesStorage/{frameCount - 1}.png"))

if not os.path.exists("images"):
    os.mkdir("images")
imageio.mimsave(f"images/{savedFileName}.gif", gifFrames, fps = fps)
optimize(f"images/{savedFileName}.gif")
shutil.rmtree("tempFramesStorage")
print("GIF successfully saved.")