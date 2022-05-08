from palette import Palette

presets = {
    "grayscale": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((0, 0, 0), 0),
            ((255, 255, 255), 1)
        ], power = 0.6),

        "showInPaletteList": True,
    },

    "loopinggrayscale": {
        "xWidth": 4,
        "yWidth": 4,
        "centrePos": (0,0),

        "palette": Palette([
            (0,0,0),
            (255,255,255)
        ], increment = 0.02),

        "showInPaletteList": True,
    },

    "invertedgrayscale": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((255, 255, 255), 0),
            ((0, 0, 0), 1)
        ], power = 0.25),

        "showInPaletteList": True,
    },

    "red": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((0, 0, 0), 0),
            ((255, 0, 0), 1)
        ], power = 0.5),

        "showInPaletteList": True,
    },

    "loopingred": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            (0, 0, 0),
            (255, 0, 0)
        ], increment = 0.02),

        "showInPaletteList": True,
    },

    "cyan": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((0, 0, 0), 0),
            ((0, 255, 255), 1)
        ], power = 0.5),
        
        "showInPaletteList": True,
    },

    "loopingcyan": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            (0, 0, 0),
            (0, 255, 255)
        ], increment = 0.02),

        "showInPaletteList": True,
    },

    "rainbow": {
        "xWidth": 4,
        "yWidth": 4,
        "centrePos": (0,0),

        "palette": Palette([
            (255,0,0),
            (255,255,0),
            (0,255,0),
            (0,255,255),
            (0,0,255),
            (255,0,255)
        ], increment = 0.028),

        "showInPaletteList": True,
    },

    "seahorsevalleyrainbow": {
        "xWidth": 0.00865394444,
        "yWidth": 0.00865394444,
        "centrePos": (-0.746619028, 0.108934389),

        "palette": Palette([
            (255,0,0),
            (255,255,0),
            (0,255,0),
            (0,255,255),
            (0,0,255),
            (255,0,255)
        ], increment = 0.01),

        "showInPaletteList": False,
    },

    "seahorsevalleygreen": {
        "xWidth": 0.00865394444,
        "yWidth": 0.00865394444,
        "centrePos": (-0.745619028, 0.108934389),

        "palette": Palette([
            (40, 40, 0),
            (30, 100, 30)
        ], increment = 0.025),

        "showInPaletteList": False,
    },

    "hell": {
        "xWidth": 2.977893334699111e-08,
        "yWidth": 2.977893334699111e-08,
        "centrePos": (0.14770400828146663, -0.6478217646645333),

        "palette": Palette([
            (0, 0, 0),
            (255, 0, 0)
        ], increment = 0.02),

        "showInPaletteList": False,
    },

    "blackhole": {
        "xWidth": 7.838257820580452e-12,
        "yWidth": 7.838257820580452e-12,
        "centrePos": (-0.1664602000144797, 1.0406697632671256),

        "palette": Palette([
            (255,0,0),
            (255,255,0),
            (0,255,0),
            (0,255,255),
            (0,0,255),
            (255,0,255)
        ], increment = 0.024),

        "showInPaletteList": False,
    },

    "paths": {
        "xWidth": 1.496466788708517e-06,
        "yWidth": 1.496466788708517e-06,
        "centrePos": (-1.4742905518400689, -0.00341624010717357),

        "palette": Palette([
            (0, 0, 0),
            (255, 255, 255)
        ], increment = 0.125),

        "showInPaletteList": False,
    }
}