"""
    This file is part of flatlib - (C) FlatAngle
    Author: João Ventura (flatangleweb@gmail.com)
    

    This module defines some properties of Traditional Astrology core
    elements.
    
    It defines qualities of temperaments, orbs and genders of planets,
    if a house is cardinal, angular or succedent, among others.
    
    To keep things simple, properties are divided in types, such as 
    base properties, planet properties, house properties, etc. Each 
    property type is defined as a lowercased python class so that we 
    can mimic different namespaces in a single python module.
    
"""

from calendar import SATURDAY
from . import const



# ------------------- #
#   Base Properties   #
# ------------------- #

class base:
    
    # The four elements
    elements = [
        const.FIRE,
        const.EARTH,
        const.AIR,
        const.WATER
    ]

    # The four temperaments
    temperaments = [
        const.CHOLERIC,
        const.MELANCHOLIC,
        const.SANGUINE,
        const.PHLEGMATIC
    ]
    
    # Genders
    genders = [
        const.MASCULINE,
        const.FEMININE
    ]
    
    # Factions
    factions = [
        const.DIURNAL, 
        const.NOCTURNAL
    ]
    
    # Sun seasons
    sunseasons = [
        const.SPRING,
        const.SUMMER,
        const.AUTUMN, 
        const.WINTER
    ]

    # Element to Temperament
    elementTemperament = {
        const.FIRE: const.CHOLERIC,
        const.EARTH: const.MELANCHOLIC,
        const.AIR: const.SANGUINE,
        const.WATER: const.PHLEGMATIC
    }
    
    # Temperament to Element
    temperamentElement = {
        const.CHOLERIC: const.FIRE,
        const.MELANCHOLIC: const.EARTH,
        const.SANGUINE: const.AIR,
        const.PHLEGMATIC: const.WATER                     
    }

    # Qualities of elements
    elementQuality = {
        const.FIRE: [const.HOT, const.DRY],
        const.EARTH: [const.COLD, const.DRY],
        const.AIR: [const.HOT, const.HUMID],
        const.WATER: [const.COLD, const.HUMID]
    }

    # Qualities of temperaments
    temperamentQuality = {
        const.CHOLERIC: [const.HOT, const.DRY],
        const.MELANCHOLIC: [const.COLD, const.DRY],
        const.SANGUINE: [const.HOT, const.HUMID],
        const.PHLEGMATIC: [const.COLD, const.HUMID]
    }

    # Moon Phase Elements
    moonphaseElement = {
        const.MOON_FIRST_QUARTER: const.AIR,
        const.MOON_SECOND_QUARTER: const.FIRE,
        const.MOON_THIRD_QUARTER: const.EARTH,
        const.MOON_LAST_QUARTER: const.WATER
    }

    # Sun Season Elements
    sunseasonElement = {
        const.SPRING: const.AIR,
        const.SUMMER: const.FIRE,
        const.AUTUMN: const.EARTH,
        const.WINTER: const.WATER
    }


# ------------------- #
#   Sign Properties   #
# ------------------- #

class sign:
    
    _signs = const.LIST_SIGNS
    
    # Modes
    _modes = [const.CARDINAL, const.FIXED, const.MUTABLE]
    mode = dict(zip(_signs, _modes * 4))
    
    # Sun Season
    _sunseasons = [[season] * 3 for season in base.sunseasons]
    _sunseasons = sum(_sunseasons, [])
    sunseason = dict(zip(_signs, _sunseasons))
    
    # Simple properties
    gender = dict(zip(_signs, base.genders * 6))
    faction = dict(zip(_signs, base.factions * 6))
    element = dict(zip(_signs, base.elements * 3))
    temperament = dict(zip(_signs, base.temperaments * 3))
        
    # Fertilities
    fertility = {
        const.ARIES: const.SIGN_MODERATELY_STERILE,
        const.TAURUS: const.SIGN_MODERATELY_FERTILE,
        const.GEMINI: const.SIGN_STERILE,
        const.CANCER: const.SIGN_FERTILE,
        const.LEO: const.SIGN_STERILE,
        const.VIRGO: const.SIGN_STERILE,
        const.LIBRA: const.SIGN_MODERATELY_FERTILE,
        const.SCORPIO: const.SIGN_FERTILE,
        const.SAGITTARIUS: const.SIGN_MODERATELY_FERTILE,
        const.CAPRICORN: const.SIGN_MODERATELY_STERILE,
        const.AQUARIUS: const.SIGN_MODERATELY_STERILE,
        const.PISCES: const.SIGN_FERTILE
    }
    
    # Sign number
    number = dict((sign, i+1) for (i, sign) in enumerate(_signs))
    
    # Sign figure properties
    figureBestial = [
        const.ARIES,
        const.TAURUS,
        const.LEO,
        const.SAGITTARIUS,
        const.CAPRICORN
    ]
    
    figureHuman = [
        const.GEMINI,
        const.VIRGO,
        const.LIBRA,
        const.AQUARIUS
    ]
    
    figureWild = [
        const.LEO
    ]


# --------------------- #
#   Object Properties   #
# --------------------- #

class object:
    
    # Mean daily motions
    meanMotion = {
        const.NO_PLANET: 0,
        const.SUN: 0.9833,
        const.MOON: 13.1833,
        const.MERCURY: 0.9833,
        const.VENUS: 0.9833,
        const.MARS: 0.5166,
        const.JUPITER: 0.0833,
        const.SATURN: 0.0333,
        const.URANUS: 0.001,
        const.NEPTUNE: 0.0001,
        const.PLUTO: 0.00001,
        const.CHIRON: 0.00001,
        const.NORTH_NODE: 13.1833,
        const.SOUTH_NODE: 13.1833,
        const.SYZYGY: 0.0
    }
    
    # Object orbs
    orb = {
        const.NO_PLANET: 0,
        const.SUN: 15,
        const.MOON: 12,
        const.MERCURY: 7,
        const.VENUS: 7,
        const.MARS: 8,
        const.JUPITER: 9,
        const.SATURN: 9,
        const.URANUS: 5,
        const.NEPTUNE: 5,
        const.PLUTO: 5,
        const.CHIRON: 5,
        const.NORTH_NODE: 12,
        const.SOUTH_NODE: 12,
        const.SYZYGY: 0,
        const.PARS_FORTUNA: 0
    }
    
    # Planet elements
    element = {
        const.SATURN: const.EARTH,
        const.JUPITER: const.AIR,
        const.MARS: const.FIRE,
        const.SUN: const.FIRE,
        const.VENUS: const.AIR,
        const.MERCURY: const.EARTH,
        const.MOON: const.WATER
    }
    
    # Planet temperaments
    temperament = {
        const.SATURN: const.MELANCHOLIC,
        const.JUPITER: const.SANGUINE,
        const.MARS: const.CHOLERIC,
        const.SUN: const.CHOLERIC,
        const.VENUS: const.SANGUINE,
        const.MERCURY: const.MELANCHOLIC,
        const.MOON: const.PHLEGMATIC
    }
    
    # Planet genders
    gender = {
        const.SATURN: const.MASCULINE,
        const.JUPITER: const.MASCULINE,
        const.MARS: const.MASCULINE,
        const.SUN: const.MASCULINE,
        const.VENUS: const.FEMININE,
        const.MERCURY: const.NEUTRAL,
        const.MOON: const.FEMININE
    }
    
    # Planet factions
    faction = {
        const.SATURN: const.DIURNAL,
        const.JUPITER: const.DIURNAL,
        const.MARS: const.NOCTURNAL,
        const.SUN: const.DIURNAL,
        const.VENUS: const.NOCTURNAL,
        const.MERCURY: const.NEUTRAL,
        const.MOON: const.NOCTURNAL
    }
    
    # Sign joy of planets
    signJoy = {
        const.SATURN: const.AQUARIUS,
        const.JUPITER: const.SAGITTARIUS,
        const.MARS: const.SCORPIO,
        const.SUN: const.LEO,
        const.VENUS: const.TAURUS,
        const.MERCURY: const.VIRGO,
        const.MOON: const.CANCER
    }
    
    # House joy of planets
    houseJoy = {
        const.SATURN: const.HOUSE12,
        const.JUPITER: const.HOUSE11,
        const.MARS: const.HOUSE6,
        const.SUN: const.HOUSE9,
        const.VENUS: const.HOUSE5,
        const.MERCURY: const.HOUSE1,
        const.MOON: const.HOUSE3
    }

    #sign ruler
    signRuler = {
        'Aries': const.MARS,
        'Taurus': const.VENUS,
        'Gemini': const.MERCURY,
        'Cancer': const.MOON,
        'Leo': const.SUN,
        'Virgo': const.MERCURY,
        'Libra': const.VENUS,
        'Scorpio': const.MARS,
        'Sagittarius': const.JUPITER,
        'Capricorn': const.SATURN,
        'Aquarius': const.SATURN,
        'Pisces': const.JUPITER
    }
    

    #nakshatra ruler
    nakshatraRuler = {
        'Ashwini': const.SOUTH_NODE,
        'Bharani': const.VENUS,
        'Krittika': const.SUN,
        'Rohini': const.MOON,
        'Mrigshira': const.MARS,
        'Aardra': const.NORTH_NODE,
        'Punarvasu': const.JUPITER,
        'Pushya': const.SATURN,
        'Ashlesha': const.MERCURY,

        'Magha': const.SOUTH_NODE,
        'Purva Phalguni': const.VENUS,
        'Uttara Phalguni': const.SUN,
        'Hasta':const.MOON,
        'Chitra': const.MARS,
        'Swati': const.NORTH_NODE,
        'Vishaka': const.JUPITER,
        'Anuradha': const.SATURN,
        'Jyeshta': const.MERCURY,

        'Mula': const.SOUTH_NODE,
        'Purva Ashadha': const.VENUS,
        'Uttara Ashadha': const.SUN,
        'Shravana': const.MOON,
        'Dhanishta': const.MARS,
        'Shatabhisha':const.NORTH_NODE,
        'Purva Bhadrapada': const.JUPITER,
        'Uttara Bhadrapada': const.SATURN,
        'Revati': const.MERCURY
    }


# -------------------- #
#   House Properties   #
# -------------------- #

class house:
    
    _houses = const.LIST_HOUSES
    
    # House conditions
    _conditions = [const.ANGULAR, const.SUCCEDENT, const.CADENT]
    condition = dict(zip(_houses, _conditions * 4))
    
    # House genders
    gender = dict(zip(_houses, base.genders * 4))
    
    # Houses above and below horizon
    aboveHorizon = [
        const.HOUSE7, const.HOUSE8, const.HOUSE9,
        const.HOUSE10, const.HOUSE11, const.HOUSE12
    ]
    
    belowHorizon = [
        const.HOUSE1, const.HOUSE2, const.HOUSE3,
        const.HOUSE4, const.HOUSE5, const.HOUSE6
    ]

    houseVariables = {
        'House 1': const.HOUSE1,
        'House 2': const.HOUSE2,
        'House 3': const.HOUSE3,
        'House 4': const.HOUSE4,
        'House 5': const.HOUSE5,
        'House 6': const.HOUSE6,
        'House 7': const.HOUSE7,
        'House 8': const.HOUSE8,
        'House 9': const.HOUSE9,
        'House 10': const.HOUSE10,
        'House 11': const.HOUSE11,
        'House 12': const.HOUSE12,
    }


# --------------------- #
#   Aspect Properties   #
# --------------------- #

class aspect:
    
    # Names
    name = {
        # Major Aspects
        const.NO_ASPECT: 'None',
        const.CONJUNCTION: 'Conjunction',
        const.SEXTILE: 'Sextile',
        const.SQUARE: 'Square',
        const.TRINE: 'Trine',
        const.OPPOSITION: 'Opposition',
        
        # Minor Aspects
        const.SEMISEXTILE: 'Semisextile',
        const.SEMIQUINTILE: 'Semiquintile',
        const.SEMISQUARE: 'Semisquare',
        const.QUINTILE: 'Quintile',
        const.SESQUIQUINTILE: 'Sesquiquintile',
        const.SESQUISQUARE: 'Sesquisquare',
        const.BIQUINTILE: 'Biquintile',
        const.QUINCUNX: 'Quincunx'
    }


# ------------------------- #
#   Fixed Star Properties   #
# ------------------------- #

class fixedStar:
    pass


# ------------------------- #
#   House Sys. Properties   #
# ------------------------- #

class houseSystem:
    pass
