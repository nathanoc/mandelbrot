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
    },

    "loopingred": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            (0, 0, 0),
            (255, 0, 0)
        ], increment = 0.02)
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
    },

    "loopingcyan": {
        "xWidth": 4.0,
        "yWidth": 4.0,
        "centrePos": (0, 0),

        "palette": Palette([
            (0, 0, 0),
            (0, 255, 255)
        ], increment = 0.02)
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
    },
}