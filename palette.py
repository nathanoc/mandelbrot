class Palette:
    coloursAtPercentages = [] # ((r, g, b), frac)

    def __init__(self, coloursAtPercentages, increment = 0):        
        if increment == 0:
            self.coloursAtPercentages = coloursAtPercentages
        else:
            coloursAtPercentages = coloursAtPercentages * int(1 / (increment * len(coloursAtPercentages)))
            coloursAtPercentages.append(coloursAtPercentages[1])
            for i in range(len(coloursAtPercentages)):
                coloursAtPercentages[i] = (coloursAtPercentages[i], i * increment)
            coloursAtPercentages[-1] = (coloursAtPercentages[-1][0], 1)
            self.coloursAtPercentages = coloursAtPercentages
                

    def getColour(self, iteration, iterations):
        frac = iteration / iterations
        i = 0
        while self.coloursAtPercentages[i][1] < frac and i < len(self.coloursAtPercentages):
            i += 1
        i -= 1
        
        if i != len(self.coloursAtPercentages) - 1:
            lerpRightWeight = (self.coloursAtPercentages[i + 1][1] - frac) / (self.coloursAtPercentages[i + 1][1] - self.coloursAtPercentages[i][1])

            leftColour = self.coloursAtPercentages[i][0]
            rightColour = self.coloursAtPercentages[i + 1][0]
            lerpedColour = (
                int(leftColour[0] + ((rightColour[0] - leftColour[0]) * (1 - lerpRightWeight))),
                int(leftColour[1] + ((rightColour[1] - leftColour[1]) * (1 - lerpRightWeight))),
                int(leftColour[2] + ((rightColour[2] - leftColour[2]) * (1 - lerpRightWeight)))
            )
        else:
            lerpedColour = self.coloursAtPercentages[i][0]

        return lerpedColour