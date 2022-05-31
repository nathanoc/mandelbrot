import time

def generateMandelbrot(width, height, xWidth, yWidth, centrePos, iterations, palette, rowsPerOutput, startTime):
    pixels = []
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
                pixels.append(
                    palette.getColour(iteration, iterations)
                )
        if yInt % rowsPerOutput == 0 and height - int(height/2 + yInt) != 0:
            rowsRemaining = int(height/2 + yInt)
            rowsCompleted = height - int(height/2 + yInt)
            
            elapsed = time.time() - startTime
            etr = elapsed / rowsCompleted * rowsRemaining

            print(str(rowsRemaining) + " rows remaining.\tElapsed: " + str(elapsed) + "\tRemaining: " + str(etr))
        
    return pixels