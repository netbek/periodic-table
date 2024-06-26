class Category:
    ALKALI_METAL = "alkali_metal"
    ALKALINE_EARTH_METAL = "alkaline_earth_metal"
    TRANSITION_METAL = "transition_metal"
    POST_TRANSITION_METAL = "post_transition_metal"
    METALLOID = "metalloid"
    POLYATOMIC_NON_METAL = "polyatomic_non_metal"
    DIATOMIC_NON_METAL = "diatomic_non_metal"
    NOBLE_GAS = "noble_gas"
    LANTHANIDE = "lanthanide"
    ACTINIDE = "actinide"
    HYDROGEN = "hydrogen"
    UNKNOWN_PROPERTIES = "unknown_properties"


categories = {
    Category.ALKALI_METAL: "Alkali metal",
    Category.ALKALINE_EARTH_METAL: "Alkali earth metal",
    Category.TRANSITION_METAL: "Transition metal",
    Category.POST_TRANSITION_METAL: "Post-transition metal",
    Category.METALLOID: "Metalloid",
    Category.POLYATOMIC_NON_METAL: "Polyatomic nonmetal",
    Category.DIATOMIC_NON_METAL: "Diatomic nonmetal",
    Category.NOBLE_GAS: "Noble gas",
    Category.LANTHANIDE: "Lanthanide",
    Category.ACTINIDE: "Actinide",
    Category.HYDROGEN: "Hydrogen",
    Category.UNKNOWN_PROPERTIES: "Unknown properties",
}

groups = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "11",
    12: "12",
    13: "13",
    14: "14",
    15: "15",
    16: "16",
    17: "17",
    18: "18",
}

element_columns = {
    "atomic_number": "Atomic number",
    "symbol": "Symbol",
    "name": "Name",
    "atomic_mass": "Relative atomic mass",
    "electronegativity": "Electronegativity",
    "work_function": "Work function",
    "block": "Block",
    "group": "Group",
    "period": "Period",
    "category": "Category",
}

elements = {
    "H": {
        "atomic_number": 1,
        "symbol": "H",
        "name": "Hydrogen",
        "atomic_mass": 1.008,
        "electronegativity": 2.2,
        "block": "s",
        "group": 1,
        "period": 1,
        "category": Category.HYDROGEN,
        "show_at_default": True,
    },
    "He": {
        "atomic_number": 2,
        "symbol": "He",
        "name": "Helium",
        "atomic_mass": 4.002602,
        "electronegativity": None,
        "block": "s",
        "group": 18,
        "period": 1,
        "category": Category.NOBLE_GAS,
        "show_at_default": True,
    },
    "Li": {
        "atomic_number": 3,
        "symbol": "Li",
        "name": "Lithium",
        "atomic_mass": 6.94,
        "electronegativity": 0.98,
        "block": "s",
        "group": 1,
        "period": 2,
        "category": Category.ALKALI_METAL,
        "show_at_default": True,
    },
    "Be": {
        "atomic_number": 4,
        "symbol": "Be",
        "name": "Beryllium",
        "atomic_mass": 9.0121831,
        "electronegativity": 1.57,
        "block": "s",
        "group": 2,
        "period": 2,
        "category": Category.ALKALINE_EARTH_METAL,
        "show_at_default": True,
    },
    "B": {
        "atomic_number": 5,
        "symbol": "B",
        "name": "Boron",
        "atomic_mass": 10.81,
        "electronegativity": 2.04,
        "block": "p",
        "group": 13,
        "period": 2,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "C": {
        "atomic_number": 6,
        "symbol": "C",
        "name": "Carbon",
        "atomic_mass": 12.011,
        "electronegativity": 2.55,
        "block": "p",
        "group": 14,
        "period": 2,
        "category": Category.POLYATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "N": {
        "atomic_number": 7,
        "symbol": "N",
        "name": "Nitrogen",
        "atomic_mass": 14.007,
        "electronegativity": 3.04,
        "block": "p",
        "group": 15,
        "period": 2,
        "category": Category.POLYATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "O": {
        "atomic_number": 8,
        "symbol": "O",
        "name": "Oxygen",
        "atomic_mass": 15.999,
        "electronegativity": 3.44,
        "block": "p",
        "group": 16,
        "period": 2,
        "category": Category.POLYATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "F": {
        "atomic_number": 9,
        "symbol": "F",
        "name": "Fluorine",
        "atomic_mass": 18.998403163,
        "electronegativity": 3.98,
        "block": "p",
        "group": 17,
        "period": 2,
        "category": Category.DIATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Ne": {
        "atomic_number": 10,
        "symbol": "Ne",
        "name": "Neon",
        "atomic_mass": 20.1797,
        "electronegativity": None,
        "block": "p",
        "group": 18,
        "period": 2,
        "category": Category.NOBLE_GAS,
        "show_at_default": True,
    },
    "Na": {
        "atomic_number": 11,
        "symbol": "Na",
        "name": "Sodium",
        "atomic_mass": 22.98976928,
        "electronegativity": 0.93,
        "block": "s",
        "group": 1,
        "period": 3,
        "category": Category.ALKALI_METAL,
        "show_at_default": True,
    },
    "Mg": {
        "atomic_number": 12,
        "symbol": "Mg",
        "name": "Magnesium",
        "atomic_mass": 24.305,
        "electronegativity": 1.31,
        "block": "s",
        "group": 2,
        "period": 3,
        "category": Category.ALKALINE_EARTH_METAL,
        "show_at_default": True,
    },
    "Al": {
        "atomic_number": 13,
        "symbol": "Al",
        "name": "Aluminium",
        "atomic_mass": 26.9815385,
        "electronegativity": 1.61,
        "block": "p",
        "group": 13,
        "period": 3,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Si": {
        "atomic_number": 14,
        "symbol": "Si",
        "name": "Silicon",
        "atomic_mass": 28.085,
        "electronegativity": 1.9,
        "block": "p",
        "group": 14,
        "period": 3,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "P": {
        "atomic_number": 15,
        "symbol": "P",
        "name": "Phosphorus",
        "atomic_mass": 30.973761998,
        "electronegativity": 2.19,
        "block": "p",
        "group": 15,
        "period": 3,
        "category": Category.POLYATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "S": {
        "atomic_number": 16,
        "symbol": "S",
        "name": "Sulfur",
        "atomic_mass": 32.06,
        "electronegativity": 2.58,
        "block": "p",
        "group": 16,
        "period": 3,
        "category": Category.POLYATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Cl": {
        "atomic_number": 17,
        "symbol": "Cl",
        "name": "Chlorine",
        "atomic_mass": 35.45,
        "electronegativity": 3.16,
        "block": "p",
        "group": 17,
        "period": 3,
        "category": Category.DIATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Ar": {
        "atomic_number": 18,
        "symbol": "Ar",
        "name": "Argon",
        "atomic_mass": 39.948,
        "electronegativity": None,
        "block": "p",
        "group": 18,
        "period": 3,
        "category": Category.NOBLE_GAS,
        "show_at_default": True,
    },
    "K": {
        "atomic_number": 19,
        "symbol": "K",
        "name": "Potassium",
        "atomic_mass": 39.0983,
        "electronegativity": 0.82,
        "block": "s",
        "group": 1,
        "period": 4,
        "category": Category.ALKALI_METAL,
        "show_at_default": True,
    },
    "Ca": {
        "atomic_number": 20,
        "symbol": "Ca",
        "name": "Calcium",
        "atomic_mass": 40.078,
        "electronegativity": 1.0,
        "block": "s",
        "group": 2,
        "period": 4,
        "category": Category.ALKALINE_EARTH_METAL,
        "show_at_default": True,
    },
    "Sc": {
        "atomic_number": 21,
        "symbol": "Sc",
        "name": "Scandium",
        "atomic_mass": 44.955908,
        "electronegativity": 1.36,
        "block": "d",
        "group": 3,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ti": {
        "atomic_number": 22,
        "symbol": "Ti",
        "name": "Titanium",
        "atomic_mass": 47.867,
        "electronegativity": 1.54,
        "block": "d",
        "group": 4,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "V": {
        "atomic_number": 23,
        "symbol": "V",
        "name": "Vanadium",
        "atomic_mass": 50.9415,
        "electronegativity": 1.63,
        "block": "d",
        "group": 5,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Cr": {
        "atomic_number": 24,
        "symbol": "Cr",
        "name": "Chromium",
        "atomic_mass": 51.9961,
        "electronegativity": 1.66,
        "block": "d",
        "group": 6,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Mn": {
        "atomic_number": 25,
        "symbol": "Mn",
        "name": "Manganese",
        "atomic_mass": 54.938044,
        "electronegativity": 1.55,
        "block": "d",
        "group": 7,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Fe": {
        "atomic_number": 26,
        "symbol": "Fe",
        "name": "Iron",
        "atomic_mass": 55.845,
        "electronegativity": 1.83,
        "block": "d",
        "group": 8,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Co": {
        "atomic_number": 27,
        "symbol": "Co",
        "name": "Cobalt",
        "atomic_mass": 58.933194,
        "electronegativity": 1.88,
        "block": "d",
        "group": 9,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ni": {
        "atomic_number": 28,
        "symbol": "Ni",
        "name": "Nickel",
        "atomic_mass": 58.6934,
        "electronegativity": 1.91,
        "block": "d",
        "group": 10,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Cu": {
        "atomic_number": 29,
        "symbol": "Cu",
        "name": "Copper",
        "atomic_mass": 63.546,
        "electronegativity": 1.9,
        "block": "d",
        "group": 11,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Zn": {
        "atomic_number": 30,
        "symbol": "Zn",
        "name": "Zinc",
        "atomic_mass": 65.38,
        "electronegativity": 1.65,
        "block": "d",
        "group": 12,
        "period": 4,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ga": {
        "atomic_number": 31,
        "symbol": "Ga",
        "name": "Gallium",
        "atomic_mass": 69.723,
        "electronegativity": 1.81,
        "block": "p",
        "group": 13,
        "period": 4,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ge": {
        "atomic_number": 32,
        "symbol": "Ge",
        "name": "Germanium",
        "atomic_mass": 72.63,
        "electronegativity": 2.01,
        "block": "p",
        "group": 14,
        "period": 4,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "As": {
        "atomic_number": 33,
        "symbol": "As",
        "name": "Arsenic",
        "atomic_mass": 74.921595,
        "electronegativity": 2.18,
        "block": "p",
        "group": 15,
        "period": 4,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "Se": {
        "atomic_number": 34,
        "symbol": "Se",
        "name": "Selenium",
        "atomic_mass": 78.971,
        "electronegativity": 2.55,
        "block": "p",
        "group": 16,
        "period": 4,
        "category": Category.POLYATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Br": {
        "atomic_number": 35,
        "symbol": "Br",
        "name": "Bromine",
        "atomic_mass": 79.904,
        "electronegativity": 2.96,
        "block": "p",
        "group": 17,
        "period": 4,
        "category": Category.DIATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Kr": {
        "atomic_number": 36,
        "symbol": "Kr",
        "name": "Krypton",
        "atomic_mass": 83.798,
        "electronegativity": None,
        "block": "p",
        "group": 18,
        "period": 4,
        "category": Category.NOBLE_GAS,
        "show_at_default": True,
    },
    "Rb": {
        "atomic_number": 37,
        "symbol": "Rb",
        "name": "Rubidium",
        "atomic_mass": 85.4678,
        "electronegativity": 0.82,
        "block": "s",
        "group": 1,
        "period": 5,
        "category": Category.ALKALI_METAL,
        "show_at_default": True,
    },
    "Sr": {
        "atomic_number": 38,
        "symbol": "Sr",
        "name": "Strontium",
        "atomic_mass": 87.62,
        "electronegativity": 0.95,
        "block": "s",
        "group": 2,
        "period": 5,
        "category": Category.ALKALINE_EARTH_METAL,
        "show_at_default": True,
    },
    "Y": {
        "atomic_number": 39,
        "symbol": "Y",
        "name": "Yttrium",
        "atomic_mass": 88.90584,
        "electronegativity": 1.22,
        "block": "d",
        "group": 3,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Zr": {
        "atomic_number": 40,
        "symbol": "Zr",
        "name": "Zirconium",
        "atomic_mass": 91.224,
        "electronegativity": 1.33,
        "block": "d",
        "group": 4,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Nb": {
        "atomic_number": 41,
        "symbol": "Nb",
        "name": "Niobium",
        "atomic_mass": 92.90637,
        "electronegativity": 1.6,
        "block": "d",
        "group": 5,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Mo": {
        "atomic_number": 42,
        "symbol": "Mo",
        "name": "Molybdenum",
        "atomic_mass": 95.95,
        "electronegativity": 2.16,
        "block": "d",
        "group": 6,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Tc": {
        "atomic_number": 43,
        "symbol": "Tc",
        "name": "Technetium",
        "atomic_mass": 97.90721,
        "electronegativity": 2.1,
        "block": "d",
        "group": 7,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ru": {
        "atomic_number": 44,
        "symbol": "Ru",
        "name": "Ruthenium",
        "atomic_mass": 101.07,
        "electronegativity": 2.2,
        "block": "d",
        "group": 8,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Rh": {
        "atomic_number": 45,
        "symbol": "Rh",
        "name": "Rhodium",
        "atomic_mass": 102.9055,
        "electronegativity": 2.28,
        "block": "d",
        "group": 9,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Pd": {
        "atomic_number": 46,
        "symbol": "Pd",
        "name": "Palladium",
        "atomic_mass": 106.42,
        "electronegativity": 2.2,
        "block": "d",
        "group": 10,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ag": {
        "atomic_number": 47,
        "symbol": "Ag",
        "name": "Silver",
        "atomic_mass": 107.8682,
        "electronegativity": 1.93,
        "block": "d",
        "group": 11,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Cd": {
        "atomic_number": 48,
        "symbol": "Cd",
        "name": "Cadmium",
        "atomic_mass": 112.414,
        "electronegativity": 1.69,
        "block": "d",
        "group": 12,
        "period": 5,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "In": {
        "atomic_number": 49,
        "symbol": "In",
        "name": "Indium",
        "atomic_mass": 114.818,
        "electronegativity": 1.78,
        "block": "p",
        "group": 13,
        "period": 5,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Sn": {
        "atomic_number": 50,
        "symbol": "Sn",
        "name": "Tin",
        "atomic_mass": 118.71,
        "electronegativity": 1.96,
        "block": "p",
        "group": 14,
        "period": 5,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Sb": {
        "atomic_number": 51,
        "symbol": "Sb",
        "name": "Antimony",
        "atomic_mass": 121.76,
        "electronegativity": 2.05,
        "block": "p",
        "group": 15,
        "period": 5,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "Te": {
        "atomic_number": 52,
        "symbol": "Te",
        "name": "Tellurium",
        "atomic_mass": 127.6,
        "electronegativity": 2.1,
        "block": "p",
        "group": 16,
        "period": 5,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "I": {
        "atomic_number": 53,
        "symbol": "I",
        "name": "Iodine",
        "atomic_mass": 126.90447,
        "electronegativity": 2.66,
        "block": "p",
        "group": 17,
        "period": 5,
        "category": Category.DIATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Xe": {
        "atomic_number": 54,
        "symbol": "Xe",
        "name": "Xenon",
        "atomic_mass": 131.293,
        "electronegativity": 2.6,
        "block": "p",
        "group": 18,
        "period": 5,
        "category": Category.NOBLE_GAS,
        "show_at_default": True,
    },
    "Cs": {
        "atomic_number": 55,
        "symbol": "Cs",
        "name": "Cesium",
        "atomic_mass": 132.90545196,
        "electronegativity": 0.79,
        "block": "s",
        "group": 1,
        "period": 6,
        "category": Category.ALKALI_METAL,
        "show_at_default": True,
    },
    "Ba": {
        "atomic_number": 56,
        "symbol": "Ba",
        "name": "Barium",
        "atomic_mass": 137.327,
        "electronegativity": 0.89,
        "block": "s",
        "group": 2,
        "period": 6,
        "category": Category.ALKALINE_EARTH_METAL,
        "show_at_default": True,
    },
    "La": {
        "atomic_number": 57,
        "symbol": "La",
        "name": "Lanthanum",
        "atomic_mass": 138.90547,
        "electronegativity": 1.1,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Ce": {
        "atomic_number": 58,
        "symbol": "Ce",
        "name": "Cerium",
        "atomic_mass": 140.116,
        "electronegativity": 1.12,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Pr": {
        "atomic_number": 59,
        "symbol": "Pr",
        "name": "Praseodymium",
        "atomic_mass": 140.90766,
        "electronegativity": 1.13,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Nd": {
        "atomic_number": 60,
        "symbol": "Nd",
        "name": "Neodymium",
        "atomic_mass": 144.242,
        "electronegativity": 1.14,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Pm": {
        "atomic_number": 61,
        "symbol": "Pm",
        "name": "Promethium",
        "atomic_mass": 144.91276,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Sm": {
        "atomic_number": 62,
        "symbol": "Sm",
        "name": "Samarium",
        "atomic_mass": 150.36,
        "electronegativity": 1.17,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Eu": {
        "atomic_number": 63,
        "symbol": "Eu",
        "name": "Europium",
        "atomic_mass": 151.964,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Gd": {
        "atomic_number": 64,
        "symbol": "Gd",
        "name": "Gadolinium",
        "atomic_mass": 157.25,
        "electronegativity": 1.2,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Tb": {
        "atomic_number": 65,
        "symbol": "Tb",
        "name": "Terbium",
        "atomic_mass": 158.92535,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Dy": {
        "atomic_number": 66,
        "symbol": "Dy",
        "name": "Dysprosium",
        "atomic_mass": 162.5,
        "electronegativity": 1.22,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Ho": {
        "atomic_number": 67,
        "symbol": "Ho",
        "name": "Holmium",
        "atomic_mass": 164.93033,
        "electronegativity": 1.23,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Er": {
        "atomic_number": 68,
        "symbol": "Er",
        "name": "Erbium",
        "atomic_mass": 167.259,
        "electronegativity": 1.24,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Tm": {
        "atomic_number": 69,
        "symbol": "Tm",
        "name": "Thulium",
        "atomic_mass": 168.93422,
        "electronegativity": 1.25,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Yb": {
        "atomic_number": 70,
        "symbol": "Yb",
        "name": "Ytterbium",
        "atomic_mass": 173.045,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Lu": {
        "atomic_number": 71,
        "symbol": "Lu",
        "name": "Lutetium",
        "atomic_mass": 174.9668,
        "electronegativity": 1.0,
        "block": "d",
        "group": 3,
        "period": 6,
        "category": Category.LANTHANIDE,
        "show_at_default": True,
    },
    "Hf": {
        "atomic_number": 72,
        "symbol": "Hf",
        "name": "Hafnium",
        "atomic_mass": 178.49,
        "electronegativity": 1.3,
        "block": "d",
        "group": 4,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ta": {
        "atomic_number": 73,
        "symbol": "Ta",
        "name": "Tantalum",
        "atomic_mass": 180.94788,
        "electronegativity": 1.5,
        "block": "d",
        "group": 5,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "W": {
        "atomic_number": 74,
        "symbol": "W",
        "name": "Tungsten",
        "atomic_mass": 183.84,
        "electronegativity": 1.7,
        "block": "d",
        "group": 6,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Re": {
        "atomic_number": 75,
        "symbol": "Re",
        "name": "Rhenium",
        "atomic_mass": 186.207,
        "electronegativity": 1.9,
        "block": "d",
        "group": 7,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Os": {
        "atomic_number": 76,
        "symbol": "Os",
        "name": "Osmium",
        "atomic_mass": 190.23,
        "electronegativity": 2.2,
        "block": "d",
        "group": 8,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Ir": {
        "atomic_number": 77,
        "symbol": "Ir",
        "name": "Iridium",
        "atomic_mass": 192.217,
        "electronegativity": 2.2,
        "block": "d",
        "group": 9,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Pt": {
        "atomic_number": 78,
        "symbol": "Pt",
        "name": "Platinum",
        "atomic_mass": 195.084,
        "electronegativity": 2.2,
        "block": "d",
        "group": 10,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Au": {
        "atomic_number": 79,
        "symbol": "Au",
        "name": "Gold",
        "atomic_mass": 196.966569,
        "electronegativity": 2.4,
        "block": "d",
        "group": 11,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Hg": {
        "atomic_number": 80,
        "symbol": "Hg",
        "name": "Mercury",
        "atomic_mass": 200.592,
        "electronegativity": 1.9,
        "block": "d",
        "group": 12,
        "period": 6,
        "category": Category.TRANSITION_METAL,
        "show_at_default": True,
    },
    "Tl": {
        "atomic_number": 81,
        "symbol": "Tl",
        "name": "Thallium",
        "atomic_mass": 204.38,
        "electronegativity": 1.8,
        "block": "p",
        "group": 13,
        "period": 6,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Pb": {
        "atomic_number": 82,
        "symbol": "Pb",
        "name": "Lead",
        "atomic_mass": 207.2,
        "electronegativity": 1.8,
        "block": "p",
        "group": 14,
        "period": 6,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Bi": {
        "atomic_number": 83,
        "symbol": "Bi",
        "name": "Bismuth",
        "atomic_mass": 208.9804,
        "electronegativity": 1.9,
        "block": "p",
        "group": 15,
        "period": 6,
        "category": Category.POST_TRANSITION_METAL,
        "show_at_default": True,
    },
    "Po": {
        "atomic_number": 84,
        "symbol": "Po",
        "name": "Polonium",
        "atomic_mass": 209.0,
        "electronegativity": 2.0,
        "block": "p",
        "group": 16,
        "period": 6,
        "category": Category.METALLOID,
        "show_at_default": True,
    },
    "At": {
        "atomic_number": 85,
        "symbol": "At",
        "name": "Astatine",
        "atomic_mass": 210.0,
        "electronegativity": 2.2,
        "block": "p",
        "group": 17,
        "period": 6,
        "category": Category.DIATOMIC_NON_METAL,
        "show_at_default": True,
    },
    "Rn": {
        "atomic_number": 86,
        "symbol": "Rn",
        "name": "Radon",
        "atomic_mass": 222.0,
        "electronegativity": None,
        "block": "p",
        "group": 18,
        "period": 6,
        "category": Category.NOBLE_GAS,
        "show_at_default": True,
    },
    "Fr": {
        "atomic_number": 87,
        "symbol": "Fr",
        "name": "Francium",
        "atomic_mass": 223.0,
        "electronegativity": 0.7,
        "block": "s",
        "group": 1,
        "period": 7,
        "category": Category.ALKALI_METAL,
        "show_at_default": True,
    },
    "Ra": {
        "atomic_number": 88,
        "symbol": "Ra",
        "name": "Radium",
        "atomic_mass": 226.0,
        "electronegativity": 0.9,
        "block": "s",
        "group": 2,
        "period": 7,
        "category": Category.ALKALINE_EARTH_METAL,
        "show_at_default": True,
    },
    "Ac": {
        "atomic_number": 89,
        "symbol": "Ac",
        "name": "Actinium",
        "atomic_mass": 227.0,
        "electronegativity": 1.1,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Th": {
        "atomic_number": 90,
        "symbol": "Th",
        "name": "Thorium",
        "atomic_mass": 232.0377,
        "electronegativity": 1.3,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Pa": {
        "atomic_number": 91,
        "symbol": "Pa",
        "name": "Protactinium",
        "atomic_mass": 231.03588,
        "electronegativity": 1.5,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "U": {
        "atomic_number": 92,
        "symbol": "U",
        "name": "Uranium",
        "atomic_mass": 238.02891,
        "electronegativity": 1.7,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Np": {
        "atomic_number": 93,
        "symbol": "Np",
        "name": "Neptunium",
        "atomic_mass": 237.0,
        "electronegativity": 1.3,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Pu": {
        "atomic_number": 94,
        "symbol": "Pu",
        "name": "Plutonium",
        "atomic_mass": 244.0,
        "electronegativity": 1.3,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Am": {
        "atomic_number": 95,
        "symbol": "Am",
        "name": "Americium",
        "atomic_mass": 243.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Cm": {
        "atomic_number": 96,
        "symbol": "Cm",
        "name": "Curium",
        "atomic_mass": 247.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Bk": {
        "atomic_number": 97,
        "symbol": "Bk",
        "name": "Berkelium",
        "atomic_mass": 247.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Cf": {
        "atomic_number": 98,
        "symbol": "Cf",
        "name": "Californium",
        "atomic_mass": 251.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Es": {
        "atomic_number": 99,
        "symbol": "Es",
        "name": "Einsteinium",
        "atomic_mass": 252.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Fm": {
        "atomic_number": 100,
        "symbol": "Fm",
        "name": "Fermium",
        "atomic_mass": 257.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Md": {
        "atomic_number": 101,
        "symbol": "Md",
        "name": "Mendelevium",
        "atomic_mass": 258.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "No": {
        "atomic_number": 102,
        "symbol": "No",
        "name": "Nobelium",
        "atomic_mass": 259.0,
        "electronegativity": None,
        "block": "f",
        "group": None,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Lr": {
        "atomic_number": 103,
        "symbol": "Lr",
        "name": "Lawrencium",
        "atomic_mass": 262.0,
        "electronegativity": None,
        "block": "d",
        "group": 3,
        "period": 7,
        "category": Category.ACTINIDE,
        "show_at_default": True,
    },
    "Rf": {
        "atomic_number": 104,
        "symbol": "Rf",
        "name": "Rutherfordium",
        "atomic_mass": 267.0,
        "electronegativity": None,
        "block": "d",
        "group": 4,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Db": {
        "atomic_number": 105,
        "symbol": "Db",
        "name": "Dubnium",
        "atomic_mass": 268.0,
        "electronegativity": None,
        "block": "d",
        "group": 5,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Sg": {
        "atomic_number": 106,
        "symbol": "Sg",
        "name": "Seaborgium",
        "atomic_mass": 271.0,
        "electronegativity": None,
        "block": "d",
        "group": 6,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Bh": {
        "atomic_number": 107,
        "symbol": "Bh",
        "name": "Bohrium",
        "atomic_mass": 274.0,
        "electronegativity": None,
        "block": "d",
        "group": 7,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Hs": {
        "atomic_number": 108,
        "symbol": "Hs",
        "name": "Hassium",
        "atomic_mass": 269.0,
        "electronegativity": None,
        "block": "d",
        "group": 8,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Mt": {
        "atomic_number": 109,
        "symbol": "Mt",
        "name": "Meitnerium",
        "atomic_mass": 276.0,
        "electronegativity": None,
        "block": "d",
        "group": 9,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Ds": {
        "atomic_number": 110,
        "symbol": "Ds",
        "name": "Darmstadtium",
        "atomic_mass": 281.0,
        "electronegativity": None,
        "block": "d",
        "group": 10,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Rg": {
        "atomic_number": 111,
        "symbol": "Rg",
        "name": "Roentgenium",
        "atomic_mass": 281.0,
        "electronegativity": None,
        "block": "d",
        "group": 11,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Cn": {
        "atomic_number": 112,
        "symbol": "Cn",
        "name": "Copernicium",
        "atomic_mass": 285.0,
        "electronegativity": None,
        "block": "d",
        "group": 12,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Nh": {
        "atomic_number": 113,
        "symbol": "Nh",
        "name": "Nihonium",
        "atomic_mass": 286.0,
        "electronegativity": None,
        "block": "p",
        "group": 13,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Fl": {
        "atomic_number": 114,
        "symbol": "Fl",
        "name": "Flerovium",
        "atomic_mass": 289.0,
        "electronegativity": None,
        "block": "p",
        "group": 14,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Mc": {
        "atomic_number": 115,
        "symbol": "Mc",
        "name": "Moscovium",
        "atomic_mass": 288.0,
        "electronegativity": None,
        "block": "p",
        "group": 15,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Lv": {
        "atomic_number": 116,
        "symbol": "Lv",
        "name": "Livermorium",
        "atomic_mass": 293.0,
        "electronegativity": None,
        "block": "p",
        "group": 16,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Ts": {
        "atomic_number": 117,
        "symbol": "Ts",
        "name": "Tennessine",
        "atomic_mass": 294.0,
        "electronegativity": None,
        "block": "p",
        "group": 17,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
    "Og": {
        "atomic_number": 118,
        "symbol": "Og",
        "name": "Oganesson",
        "atomic_mass": 294.0,
        "electronegativity": None,
        "block": "p",
        "group": 18,
        "period": 7,
        "category": Category.UNKNOWN_PROPERTIES,
        "show_at_default": True,
    },
}
