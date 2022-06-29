import time

def generateMandelbrot(settings):
    width = settings.width
    height = settings.height
    xWidth = settings.xWidth
    yWidth = settings.yWidth
    centrePos = settings.centrePos
    iterations = settings.iterations
    palette = settings.palette
    rowsPerOutput = settings.rowsPerOutput

    startTime = time.time()
    pixels = []
    for yInt in range(int(width/2), int(-width/2), -1):
        y = centrePos[1] + (yInt / height * yWidth)
        for xInt in range(int(-width/2), int(width/2)):
            x = centrePos[0] + (xInt / width * xWidth)

            Z = (0, 0)
            C = (x, y)

            for iteration in range(1, iterations + 1):
                zx2 = Z[0] ** 2
                zy2 = Z[1] ** 2

                Z = (zx2 - zy2 + C[0], 2 * Z[0] * Z[1] + C[1])

                if zx2 + zy2 > 4.0:
                    break
            if zx2 + zy2 < 4.0:
                pixels.append((0,0,0))
            else:
                pixels.append(
                    palette.getColour(iteration, iterations)
                )

        if rowsPerOutput != 0:
            if yInt % rowsPerOutput == 0 and height - int(height/2 + yInt) != 0:
                rowsRemaining = int(height/2 + yInt)
                rowsCompleted = height - int(height/2 + yInt)
                elapsed = time.time() - startTime
                etr = elapsed / rowsCompleted * rowsRemaining
                print(str(rowsRemaining) + " rows remaining.\tElapsed: " + str(elapsed) + "\tRemaining: " + str(etr))
    
    print("Generation complete")
    elapsed = time.time() - startTime
    print("Total elapsed: " + str(elapsed))
    return pixels