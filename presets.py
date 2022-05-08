from palette import Palette

presets = {
    "default": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((0, 0, 0), 0),
            ((144, 144, 144), 0.1),
            ((171, 171, 171), 0.2),
            ((203, 203, 203), 0.4),
            ((224, 224, 224), 0.6),
            ((241, 241, 241), 0.8),
            ((255, 255, 255), 1)
        ])
        "showInPaletteList": True,
        "showInPaletteList": True,
    },

    "red": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((0, 0, 0), 0),
            ((144, 0, 0), 0.1),
            ((171, 0, 0), 0.2),
            ((203, 0, 0), 0.4),
            ((224, 0, 0), 0.6),
            ((241, 0, 0), 0.8),
            ((255, 0, 0), 1)
        ])
        "showInPaletteList": True,
    },

    "loopingred": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            (0, 0, 0),
            (255, 0, 0)
        ], increment = 0.02)
        "showInPaletteList": True,
    },

    "cyan": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((0, 0, 0), 0),
            ((0, 144, 144), 0.1),
            ((0, 171, 171), 0.2),
            ((0, 203, 203), 0.4),
            ((0, 224, 224), 0.6),
            ((0, 241, 241), 0.8),
            ((0, 255, 255), 1)
        ])
        "showInPaletteList": True,
    },

    "loopingcyan": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            (0, 0, 0),
            (0, 255, 255)
        ], increment = 0.02)
        "showInPaletteList": True,
    },

    "seahorsevalley": {
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
        ], increment = 0.01)
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
        ], increment = 0.028)
    },

    "loopinggrayscale": {
        "xWidth": 4,
        "yWidth": 4,
        "centrePos": (0,0),

        "palette": Palette([
            (0,0,0),
            (255,255,255)
        ], increment = 0.02)
        "showInPaletteList": False,
    },

    "invertedgrayscale": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            ((255, 255, 255), 0),
            ((112, 112, 112), 0.1),
            ((84, 84, 84), 0.2),
            ((52, 52, 52), 0.4),
            ((31, 31, 31), 0.6),
            ((14, 14, 14), 0.8),
            ((0, 0, 0), 1)
        ])
        "showInPaletteList": False,
    },

    "hell": {
        "xWidth": 2.977893334699111e-08,
        "yWidth": 2.977893334699111e-08,
        "centrePos": (0.14770400828146663, -0.6478217646645333),

        "palette": Palette([
            (0, 0, 0),
            (255, 0, 0)
        ], increment = 0.02)
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
        ], increment = 0.024)
        "showInPaletteList": False,
    },
        "showInPaletteList": False,
}