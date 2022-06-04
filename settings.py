import presets

class Settings:
    def __init__(self, width, height, xWidth, yWidth, centrePos, iterations, palette, rowsPerOutput, selectedPresetName = None):
        # Mandelbrot generation settings
        self.width = width
        self.height = height
        self.xWidth = xWidth
        self.yWidth = yWidth
        self.centrePos = centrePos
        self.iterations = iterations
        self.palette = palette
        self.rowsPerOutput = rowsPerOutput

        # Other info (used for file directory, etc)
        self.selectedPresetName = selectedPresetName

def inputSettings():
    width = int(input("Enter width in pixels: "))
    height = width

    iterations = int(input("Enter max iterations (recommended = 500): "))

    print("Preset list:")
    for key in presets.presets.keys():
        print(" - " + key)
    print(" - custom")
    selectedPresetName = input("Enter preset name: ")
    while not selectedPresetName in presets.presets.keys():
        selectedPresetName = input("Invalid preset name. Enter a valid preset name: ")
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

    return Settings(width, height, xWidth, yWidth, centrePos, iterations, palette, rowsPerOutput, selectedPresetName)