"""
Abbreviations for currencies in PoE
"""

import re


# Currencies are abbreviated in notes.
# The standard form of a note is this:
PRICE_RE = re.compile(r'\~(price|b\/o)\s+(\S+)\s+([\w\-\']+)')
PRICE_WITH_SPACE_RE = re.compile(r'\~(price|b\/o)\s+(\S+)\s+([ \w\-\']+)')

# The last part of the note is an abbreviated currency name.
# Official currencies are those available in the in-game drop-down menu
OFFICIAL_CURRENCIES = {
    "alch": "Orb of Alchemy",
    "alt": "Orb of Alteration",
    "blessed": "Blessed Orb",
    "chance": "Orb of Chance",
    "chaos": "Chaos Orb",
    "chisel": "Cartographer's Chisel",
    "chrom": "Chromatic Orb",
    "divine": "Divine Orb",
    "exa": "Exalted Orb",
    "fuse": "Orb of Fusing",
    "gcp": "Gemcutter's Prism",
    "jew": "Jeweller's Orb",
    "regal": "Regal Orb",
    "regret": "Orb of Regret",
    "scour": "Orb of Scouring",
    "vaal": "Vaal Orb",
}

# But some players write in their own, and there are several common
# ones in use. See http://currency.poe.trade/tags which I processed
# using the script from scripts/currency_abbreviations.pl
# Then we've added a few seen in the wild (first section)
# Note that some of these appear in the official list, above as well
UNOFFICIAL_CURRENCIES = {
    # Seen in the wild
    "c": "Chaos Orb",
    "p": "Perandus Coin",
    "pc": "Perandus Coin",
    "mirror": "Mirror of Kalandra",
    "fusing": "Orb of Fusing",
    "eshs-breachstone": "Esh's Breachstone",
    "esh-breachstone": "Esh's Breachstone",
    "xophs-breachstone": "Xoph's Breachstone",
    "xoph-breachstone": "Xoph's Breachstone",
    "chayulas-breachstone": "Chayula's Breachstone",
    "chayula-breachstone": "Chayula's Breachstone",
    "tuls-breachstone": "Tul's Breachstone",
    "tul-breachstone": "Tul's Breachstone",
    "uul-netols-breachstone": "Uul-Netol's Breachstone",
    "uul-netol-breachstone": "Uul-Netol's Breachstone",
    "minotaur": "Fragment of the Minotaur",
    "chimera": "Fragment of the Chimera",
    "phoenix": "Fragment of the Phoenix",
    "hydra": "Fragment of the Hydra",
    "wisdom": "Scroll of Wisdom",
    "the-samurais-eye": "The Samurai's Eye",
    "apprentice": "Apprentice Cartographer's Sextant",
    "journeyman": "Journeyman Cartographer's Sextant",
    "master": "Master Cartographer's Sextant",
    # From http://currency.poe.trade/tags, see above
    "alt": "Orb of Alteration",
    "fuse": "Orb of Fusing",
    "fus": "Orb of Fusing",
    "alch": "Orb of Alchemy",
    "alchemy": "Orb of Alchemy",
    "chaos": "Chaos Orb",
    "choas": "Chaos Orb",
    "gemc": "Gemcutter's Prism",
    "gcp": "Gemcutter's Prism",
    "exa": "Exalted Orb",
    "ex": "Exalted Orb",
    "exalted": "Exalted Orb",
    "chrom": "Chromatic Orb",
    "chrome": "Chromatic Orb",
    "jew": "Jeweller's Orb",
    "chance": "Orb of Chance",
    "chanc": "Orb of Chance",
    "chisel": "Cartographer's Chisel",
    "cart": "Cartographer's Chisel",
    "scour": "Orb of Scouring",
    "blesse": "Blessed Orb",
    "regret": "Orb of Regret",
    "regr": "Orb of Regret",
    "regal": "Regal Orb",
    "rega": "Regal Orb",
    "divine": "Divine Orb",
    "div": "Divine Orb",
    "vaal": "Vaal Orb",
    "wis": "Scroll of Wisdom",
    "port": "Portal Scroll",
    "armour": "Armourer's Scrap",
    "blacksmith": "Blacksmith's Whetstone",
    "whetstone": "Blacksmith's Whetstone",
    "glass": "Glassblower's Bauble",
    "bauble": "Glassblower's Bauble",
    "tra": "Orb of Transmutation",
    "aug": "Orb of Augmentation",
    "mir": "Mirror of Kalandra",
    "kal": "Mirror of Kalandra",
    "ete": "Eternal Orb",
    "coin": "Perandus Coin",
    "coins": "Perandus Coin",
    "perandus": "Perandus Coin",
    "silver": "Silver Coin",
    "dusk": "Sacrifice at Dusk",
    "mid": "Sacrifice at Midnight",
    "dawn": "Sacrifice at Dawn",
    "noon": "Sacrifice at Noon",
    "grie": "Mortal Grief",
    "rage": "Mortal Rage",
    "hope": "Mortal Hope",
    "ign": "Mortal Ignorance",
    "eber": "Eber's Key",
    "yriel": "Yriel's Key",
    "inya": "Inya's Key",
    "volkuur": "Volkuur's Key",
    "offer": "Offering to the Goddess",
    "hydra": "Fragment of the Hydra",
    "phoenix": "Fragment of the Phoenix",
    "phenix": "Fragment of the Phoenix",
    "pheon": "Fragment of the Phoenix",
    "minot": "Fragment of the Minotaur",
    "chimer": "Fragment of the Chimera",
    "apprentice-sextant": "Apprentice Cartographer's Sextant",
    "journeyman-sextant": "Journeyman Cartographer's Sextant",
    "master-sextant": "Master Cartographer's Sextant",
    "sacrifice-set": "Sacrifice set",
    "mortal-set": "Mortal set",
    "pale-court-set": "Pale Court set",
    "shaper-set": "Shaper set",
    "splinter-xoph": "Splinter of Xoph",
    "splinter-of-xoph": "Splinter of Xoph",
    "splinter-tul": "Splinter of Tul",
    "splinter-of-tul": "Splinter of Tul",
    "splinter-esh": "Splinter of Esh",
    "splinter-of-esh": "Splinter of Esh",
    "splinter-uul-netol": "Splinter of Uul-Netol",
    "splinter-of-uul-netol": "Splinter of Uul-Netol",
    "splinter-chayula": "Splinter of Chayula",
    "splinter-of-chayula": "Splinter of Chayula",
    "blessing-xoph": "Blessing of Xoph",
    "blessing-of-xoph": "Blessing of Xoph",
    "blessing-tul": "Blessing of Tul",
    "blessing-of-tul": "Blessing of Tul",
    "blessing-esh": "Blessing of Esh",
    "blessing-of-esh": "Blessing of Esh",
    "blessing-uul-netol": "Blessing of Uul-Netol",
    "blessing-of-uul-netol": "Blessing of Uul-Netol",
    "blessing-chayula": "Blessing of Chayula",
    "blessing-of-chayula": "Blessing of Chayula",
    "xophs-breachstone": "Xoph's Breachstone",
    "tuls-breachstone": "Tul's Breachstone",
    "eshs-breachstone": "Esh's Breachstone",
    "uul-netol-breachstone": "Uul-Netol's Breachstone",
    "chayulas-breachstone": "Chayula's Breachstone",
    "essence-of-delirium": "Essence of Delirium",
    "essence-of-horror": "Essence of Horror",
    "essence-of-hysteria": "Essence of Hysteria",
    "essence-of-insanity": "Essence of Insanity",
    "screaming-essence-of-anger": "Screaming Essence of Anger",
    "shrieking-essence-of-anger": "Shrieking Essence of Anger",
    "deafening-essence-of-anger": "Deafening Essence of Anger",
    "screaming-essence-of-anguish": "Screaming Essence of Anguish",
    "shrieking-essence-of-anguish": "Shrieking Essence of Anguish",
    "deafening-essence-of-anguish": "Deafening Essence of Anguish",
    "screaming-essence-of-contempt": "Screaming Essence of Contempt",
    "shrieking-essence-of-contempt": "Shrieking Essence of Contempt",
    "deafening-essence-of-contempt": "Deafening Essence of Contempt",
    "screaming-essence-of-doubt": "Screaming Essence of Doubt",
    "shrieking-essence-of-doubt": "Shrieking Essence of Doubt",
    "deafening-essence-of-doubt": "Deafening Essence of Doubt",
    "screaming-essence-of-dread": "Screaming Essence of Dread",
    "shrieking-essence-of-dread": "Shrieking Essence of Dread",
    "deafening-essence-of-dread": "Deafening Essence of Dread",
    "screaming-essence-of-envy": "Screaming Essence of Envy",
    "shrieking-essence-of-envy": "Shrieking Essence of Envy",
    "deafening-essence-of-envy": "Deafening Essence of Envy",
    "screaming-essence-of-fear": "Screaming Essence of Fear",
    "shrieking-essence-of-fear": "Shrieking Essence of Fear",
    "deafening-essence-of-fear": "Deafening Essence of Fear",
    "screaming-essence-of-greed": "Screaming Essence of Greed",
    "shrieking-essence-of-greed": "Shrieking Essence of Greed",
    "deafening-essence-of-greed": "Deafening Essence of Greed",
    "screaming-essence-of-hatred": "Screaming Essence of Hatred",
    "shrieking-essence-of-hatred": "Shrieking Essence of Hatred",
    "deafening-essence-of-hatred": "Deafening Essence of Hatred",
    "screaming-essence-of-loathing": "Screaming Essence of Loathing",
    "shrieking-essence-of-loathing": "Shrieking Essence of Loathing",
    "deafening-essence-of-loathing": "Deafening Essence of Loathing",
    "screaming-essence-of-misery": "Screaming Essence of Misery",
    "shrieking-essence-of-misery": "Shrieking Essence of Misery",
    "deafening-essence-of-misery": "Deafening Essence of Misery",
    "screaming-essence-of-rage": "Screaming Essence of Rage",
    "shrieking-essence-of-rage": "Shrieking Essence of Rage",
    "deafening-essence-of-rage": "Deafening Essence of Rage",
    "screaming-essence-of-scorn": "Screaming Essence of Scorn",
    "shrieking-essence-of-scorn": "Shrieking Essence of Scorn",
    "deafening-essence-of-scorn": "Deafening Essence of Scorn",
    "screaming-essence-of-sorrow": "Screaming Essence of Sorrow",
    "shrieking-essence-of-sorrow": "Shrieking Essence of Sorrow",
    "deafening-essence-of-sorrow": "Deafening Essence of Sorrow",
    "screaming-essence-of-spite": "Screaming Essence of Spite",
    "shrieking-essence-of-spite": "Shrieking Essence of Spite",
    "deafening-essence-of-spite": "Deafening Essence of Spite",
    "screaming-essence-of-suffering": "Screaming Essence of Suffering",
    "shrieking-essence-of-suffering": "Shrieking Essence of Suffering",
    "deafening-essence-of-suffering": "Deafening Essence of Suffering",
    "screaming-essence-of-torment": "Screaming Essence of Torment",
    "shrieking-essence-of-torment": "Shrieking Essence of Torment",
    "deafening-essence-of-torment": "Deafening Essence of Torment",
    "screaming-essence-of-woe": "Screaming Essence of Woe",
    "shrieking-essence-of-woe": "Shrieking Essence of Woe",
    "deafening-essence-of-woe": "Deafening Essence of Woe",
    "screaming-essence-of-wrath": "Screaming Essence of Wrath",
    "shrieking-essence-of-wrath": "Shrieking Essence of Wrath",
    "deafening-essence-of-wrath": "Deafening Essence of Wrath",
    "screaming-essence-of-zeal": "Screaming Essence of Zeal",
    "shrieking-essence-of-zeal": "Shrieking Essence of Zeal",
    "deafening-essence-of-zeal": "Deafening Essence of Zeal",
    "remnant-of-corruption": "Remnant of Corruption",
    "a-mothers-parting-gift": "A Mother's Parting Gift",
    "abandoned-wealth": "Abandoned Wealth",
    "anarchys-price": "Anarchy's Price",
    "assassins-favour": "Assassin's Favour",
    "atziris-arsenal": "Atziri's Arsenal",
    "audacity": "Audacity",
    "birth-of-the-three": "Birth of the Three",
    "blind-venture": "Blind Venture",
    "boundless-realms": "Boundless Realms",
    "bowyers-dream": "Bowyer's Dream",
    "call-to-the-first-ones": "Call to the First Ones",
    "cartographers-delight": "Cartographer's Delight",
    "chaotic-disposition": "Chaotic Disposition",
    "coveted-possession": "Coveted Possession",
    "death": "Death",
    "destined-to-crumble": "Destined to Crumble",
    "diallas-subjugation": "Dialla's Subjugation",
    "doedres-madness": "Doedre's Madness",
    "dying-anguish": "Dying Anguish",
    "earth-drinker": "Earth Drinker",
    "emperor-of-purity": "Emperor of Purity",
    "emperors-luck": "Emperor's Luck",
    "gemcutters-promise": "Gemcutter's Promise",
    "gift-of-the-gemling-queen": "Gift of the Gemling Queen",
    "glimmer-of-hope": "Glimmer of Hope",
    "grave-knowledge": "Grave Knowledge",
    "her-mask": "Her Mask",
    "heterochromia": "Heterochromia",
    "hope-card": "Hope",
    "house-of-mirrors": "House of Mirrors",
    "hubris": "Hubris",
    "humility": "Humility",
    "hunters-resolve": "Hunter's Resolve",
    "hunters-reward": "Hunter's Reward",
    "jack-in-the-box": "Jack in the Box",
    "lantadors-lost-love": "Lantador's Lost Love",
    "last-hope": "Last Hope",
    "light-and-truth": "Light and Truth",
    "lingering-remnants": "Lingering Remnants",
    "lost-worlds": "Lost Worlds",
    "loyalty": "Loyalty",
    "lucky-connections": "Lucky Connections",
    "lucky-deck": "Lucky Deck",
    "lysahs-respite": "Lysah's Respite",
    "mawr-blaidd": "Mawr Blaidd",
    "merciless-armament": "Merciless Armament",
    "might-is-right": "Might is Right",
    "mitts": "Mitts",
    "pride-before-the-fall": "Pride Before the Fall",
    "prosperity": "Prosperity",
    "rain-tempter": "Rain Tempter",
    "rain-of-chaos": "Rain of Chaos",
    "rats": "Rats",
    "scholar-of-the-seas": "Scholar of the Seas",
    "shard-of-fate": "Shard of Fate",
    "struck-by-lightning": "Struck by Lightning",
    "the-aesthete": "The Aesthete",
    "the-arena-champion": "The Arena Champion",
    "the-artist": "The Artist",
    "the-avenger": "The Avenger",
    "the-battle-born": "The Battle Born",
    "the-betrayal": "The Betrayal",
    "the-body": "The Body",
    "the-brittle-emperor": "The Brittle Emperor",
    "the-calling": "The Calling",
    "the-carrion-crow": "The Carrion Crow",
    "the-cartographer": "The Cartographer",
    "the-cataclysm": "The Cataclysm",
    "the-catalyst": "The Catalyst",
    "the-celestial-justicar": "The Celestial Justicar",
    "the-chains-that-bind": "The Chains that Bind",
    "the-coming-storm": "The Coming Storm",
    "the-conduit": "The Conduit",
    "the-cursed-king": "The Cursed King",
    "the-dapper-prodigy": "The Dapper Prodigy",
    "the-dark-mage": "The Dark Mage",
    "the-demoness": "The Demoness",
    "the-devastator": "The Devastator",
    "the-doctor": "The Doctor",
    "the-doppelganger": "The Doppelganger",
    "the-dragon": "The Dragon",
    "the-dragons-heart": "The Dragon's Heart",
    "the-drunken-aristocrat": "The Drunken Aristocrat",
    "the-encroaching-darkness": "The Encroaching Darkness",
    "the-endurance": "The Endurance",
    "the-enlightened": "The Enlightened",
    "the-ethereal": "The Ethereal",
    "the-explorer": "The Explorer",
    "the-feast": "The Feast",
    "the-fiend": "The Fiend",
    "the-fletcher": "The Fletcher",
    "the-floras-gift": "The Flora's Gift",
    "the-formless-sea": "The Formless Sea",
    "the-forsaken": "The Forsaken",
    "the-fox": "The Fox",
    "the-gambler": "The Gambler",
    "the-garish-power": "The Garish Power",
    "the-gemcutter": "The Gemcutter",
    "the-gentleman": "The Gentleman",
    "the-gladiator": "The Gladiator",
    "the-harvester": "The Harvester",
    "the-hermit": "The Hermit",
    "the-hoarder": "The Hoarder",
    "the-hunger": "The Hunger",
    "the-immortal": "The Immortal",
    "the-incantation": "The Incantation",
    "the-inoculated": "The Inoculated",
    "the-inventor": "The Inventor",
    "the-jester": "The Jester",
    "the-kings-blade": "The King's Blade",
    "the-kings-heart": "The King's Heart",
    "the-last-one-standing": "The Last One Standing",
    "the-lich": "The Lich",
    "the-lion": "The Lion",
    "the-lord-in-black": "The Lord in Black",
    "the-lover": "The Lover",
    "the-lunaris-priestess": "The Lunaris Priestess",
    "the-mercenary": "The Mercenary",
    "the-metalsmiths-gift": "The Metalsmith's Gift",
    "the-oath": "The Oath",
    "the-offering": "The Offering",
    "the-one-with-all": "The One With All",
    "the-opulent": "The Opulent",
    "the-pack-leader": "The Pack Leader",
    "the-pact": "The Pact",
    "the-penitent": "The Penitent",
    "the-poet": "The Poet",
    "the-polymath": "The Polymath",
    "the-porcupine": "The Porcupine",
    "the-queen": "The Queen",
    "the-rabid-rhoa": "The Rabid Rhoa",
    "the-risk": "The Risk",
    "the-road-to-power": "The Road to Power",
    "the-saints-treasure": "The Saint's Treasure",
    "the-scarred-meadow": "The Scarred Meadow",
    "the-scavenger": "The Scavenger",
    "the-scholar": "The Scholar",
    "the-sephirot": "The Sephirot",
    "the-sigil": "The Sigil",
    "the-siren": "The Siren",
    "the-soul": "The Soul",
    "the-spark-and-the-flame": "The Spark and the Flame",
    "the-spoiled-prince": "The Spoiled Prince",
    "the-standoff": "The Standoff",
    "the-stormcaller": "The Stormcaller",
    "the-summoner": "The Summoner",
    "the-sun": "The Sun",
    "the-surgeon": "The Surgeon",
    "the-surveyor": "The Surveyor",
    "the-survivalist": "The Survivalist",
    "the-thaumaturgist": "The Thaumaturgist",
    "the-throne": "The Throne",
    "the-tower": "The Tower",
    "the-traitor": "The Traitor",
    "the-trial": "The Trial",
    "the-twins": "The Twins",
    "the-tyrant": "The Tyrant",
    "the-union": "The Union",
    "the-valkyrie": "The Valkyrie",
    "the-valley-of-steel-boxes": "The Valley of Steel Boxes",
    "the-vast": "The Vast",
    "the-visionary": "The Visionary",
    "the-void": "The Void",
    "the-warden": "The Warden",
    "the-warlord": "The Warlord",
    "the-watcher": "The Watcher",
    "the-web": "The Web",
    "the-wind": "The Wind",
    "the-wolf": "The Wolf",
    "the-wolfs-shadow": "The Wolf's Shadow",
    "the-wolven-kings-bite": "The Wolven King's Bite",
    "the-wolverine": "The Wolverine",
    "the-wrath": "The Wrath",
    "the-wretched": "The Wretched",
    "three-faces-in-the-dark": "Three Faces in the Dark",
    "thunderous-skies": "Thunderous Skies",
    "time-lost-relic": "Time-Lost Relic",
    "tranquillity": "Tranquillity",
    "treasure-hunter": "Treasure Hunter",
    "turn-the-other-cheek": "Turn the Other Cheek",
    "vinias-token": "Vinia's Token",
    "volatile-power": "Volatile Power",
    "wealth-and-power": "Wealth and Power",
    "abyss-map": "Abyss",
    "academy-map": "Academy",
    "acid-lakes-map": "Acid Lakes",
    "arachnid-nest-map": "Arachnid Nest",
    "arachnid-tomb-map": "Arachnid Tomb",
    "arcade-map": "Arcade",
    "arena-map": "Arena",
    "arid-lake-map": "Arid Lake",
    "armoury-map": "Armoury",
    "arsenal-map": "Arsenal",
    "ashen-wood-map": "Ashen Wood",
    "atoll-map": "Atoll",
    "barrows-map": "Barrows",
    "bazaar-map": "Bazaar",
    "beach-map": "Beach",
    "beacon-map": "Beacon",
    "bog-map": "Bog",
    "burial-chambers-map": "Burial Chambers",
    "canyon-map": "Canyon",
    "castle-ruins-map": "Castle Ruins",
    "catacombs-map": "Catacombs",
    "cavern-map": "Cavern",
    "cells-map": "Cells",
    "cemetery-map": "Cemetery",
    "channel-map": "Channel",
    "chateau-map": "Chateau",
    "colonnade-map": "Colonnade",
    "colosseum-map": "Colosseum",
    "core-map": "Core",
    "courtyard-map": "Courtyard",
    "coves-map": "Coves",
    "crematorium-map": "Crematorium",
    "crypt-map": "Crypt",
    "crystal-ore-map": "Crystal Ore",
    "dark-forest-map": "Dark Forest",
    "desert-map": "Desert",
    "dunes-map": "Dunes",
    "dungeon-map": "Dungeon",
    "estuary-map": "Estuary",
    "excavation-map": "Excavation",
    "factory-map": "Factory",
    "forge-of-the-phoenix-map": "Forge of the Phoenix",
    "ghetto-map": "Ghetto",
    "gorge-map": "Gorge",
    "graveyard-map": "Graveyard",
    "grotto-map": "Grotto",
    "high-gardens-map": "High Gardens",
    "ivory-temple-map": "Ivory Temple",
    "jungle-valley-map": "Jungle Valley",
    "lair-map": "Lair",
    "lair-of-the-hydra-map": "Lair of the Hydra",
    "malformation-map": "Malformation",
    "marshes-map": "Marshes",
    "maze-map": "Maze",
    "maze-of-the-minotaur-map": "Maze of the Minotaur",
    "mesa-map": "Mesa",
    "mineral-pools-map": "Mineral Pools",
    "mud-geyser-map": "Mud Geyser",
    "museum-map": "Museum",
    "necropolis-map": "Necropolis",
    "oasis-map": "Oasis",
    "orchard-map": "Orchard",
    "overgrown-ruin-map": "Overgrown Ruin",
    "overgrown-shrine-map": "Overgrown Shrine",
    "palace-map": "Palace",
    "peninsula-map": "Peninsula",
    "phantasmagoria-map": "Phantasmagoria",
    "pier-map": "Pier",
    "pit-map": "Pit",
    "pit-of-the-chimera-map": "Pit of the Chimera",
    "plateau-map": "Plateau",
    "plaza-map": "Plaza",
    "precinct-map": "Precinct",
    "primordial-pool-map": "Primordial Pool",
    "promenade-map": "Promenade",
    "quarry-map": "Quarry",
    "port-map": "Port",
    "racecourse-map": "Racecourse",
    "ramparts-map": "Ramparts",
    "reef-map": "Reef",
    "residence-map": "Residence",
    "scriptorium-map": "Scriptorium",
    "sewer-map": "Sewer",
    "shaped-academy-map": "Shaped Academy",
    "shaped-acid-lakes-map": "Shaped Acid Lakes",
    "shaped-arachnid-nest-map": "Shaped Arachnid Nest",
    "shaped-arachnid-tomb-map": "Shaped Arachnid Tomb",
    "shaped-arcade-map": "Shaped Arcade",
    "shaped-arena-map": "Shaped Arena",
    "shaped-arid-lake-map": "Shaped Arid Lake",
    "shaped-armoury-map": "Shaped Armoury",
    "shaped-arsenal-map": "Shaped Arsenal",
    "shaped-ashen-wood-map": "Shaped Ashen Wood",
    "shaped-atoll-map": "Shaped Atoll",
    "shaped-barrows-map": "Shaped Barrows",
    "shaped-beach-map": "Shaped Beach",
    "shaped-bog-map": "Shaped Bog",
    "shaped-burial-chambers-map": "Shaped Burial Chambers",
    "shaped-canyon-map": "Shaped Canyon",
    "shaped-castle-ruins-map": "Shaped Castle Ruins",
    "shaped-catacombs-map": "Shaped Catacombs",
    "shaped-cavern-map": "Shaped Cavern",
    "shaped-cells-map": "Shaped Cells",
    "shaped-cemetery-map": "Shaped Cemetery",
    "shaped-channel-map": "Shaped Channel",
    "shaped-colonnade-map": "Shaped Colonnade",
    "shaped-courtyard-map": "Shaped Courtyard",
    "shaped-coves-map": "Shaped Coves",
    "shaped-crypt-map": "Shaped Crypt",
    "shaped-crystal-ore-map": "Shaped Crystal Ore",
    "shaped-desert-map": "Shaped Desert",
    "shaped-dunes-map": "Shaped Dunes",
    "shaped-dungeon-map": "Shaped Dungeon",
    "shaped-factory-map": "Shaped Factory",
    "shaped-ghetto-map": "Shaped Ghetto",
    "shaped-graveyard-map": "Shaped Graveyard",
    "shaped-grotto-map": "Shaped Grotto",
    "shaped-jungle-valley-map": "Shaped Jungle Valley",
    "shaped-malformation-map": "Shaped Malformation",
    "shaped-marshes-map": "Shaped Marshes",
    "shaped-mesa-map": "Shaped Mesa",
    "shaped-mud-geyser-map": "Shaped Mud Geyser",
    "shaped-museum-map": "Shaped Museum",
    "shaped-oasis-map": "Shaped Oasis",
    "shaped-orchard-map": "Shaped Orchard",
    "shaped-overgrown-shrine-map": "Shaped Overgrown Shrine",
    "shaped-peninsula-map": "Shaped Peninsula",
    "shaped-phantasmagoria-map": "Shaped Phantasmagoria",
    "shaped-pier-map": "Shaped Pier",
    "shaped-pit-map": "Shaped Pit",
    "shaped-primordial-pool-map": "Shaped Primordial Pool",
    "shaped-promenade-map": "Shaped Promenade",
    "shaped-quarry-map": "Shaped Quarry",
    "shaped-port-map": "Shaped Port",
    "shaped-racecourse-map": "Shaped Racecourse",
    "shaped-ramparts-map": "Shaped Ramparts",
    "shaped-reef-map": "Shaped Reef",
    "shaped-toxic-sewer-map": "Shaped Toxic Sewer",
    "shaped-shore-map": "Shaped Shore",
    "shaped-spider-forest-map": "Shaped Spider Forest",
    "shaped-spider-lair-map": "Shaped Spider Lair",
    "shaped-strand-map": "Shaped Strand",
    "shaped-temple-map": "Shaped Temple",
    "shaped-terrace-map": "Shaped Terrace",
    "shaped-thicket-map": "Shaped Thicket",
    "shaped-tower-map": "Shaped Tower",
    "shaped-tropical-island-map": "Shaped Tropical Island",
    "shaped-underground-river-map": "Shaped Underground River",
    "shaped-vaal-city-map": "Shaped Vaal City",
    "shaped-vaal-pyramid-map": "Shaped Vaal Pyramid",
    "shaped-villa-map": "Shaped Villa",
    "shaped-waste-pool-map": "Shaped Waste Pool",
    "shaped-wharf-map": "Shaped Wharf",
    "shipyard-map": "Shipyard",
    "shore-map": "Shore",
    "shrine-map": "Shrine",
    "spider-forest-map": "Spider Forest",
    "spider-lair-map": "Spider Lair",
    "springs-map": "Springs",
    "strand-map": "Strand",
    "sulphur-wastes-map": "Sulphur Wastes",
    "temple-map": "Temple",
    "terrace-map": "Terrace",
    "thicket-map": "Thicket",
    "torture-chamber-map": "Torture Chamber",
    "tower-map": "Tower",
    "tropical-island-map": "Tropical Island",
    "underground-river-map": "Underground River",
    "underground-sea-map": "Underground Sea",
    "vaal-city-map": "Vaal City",
    "vaal-pyramid-map": "Vaal Pyramid",
    "vaal-temple-map": "Vaal Temple",
    "vault-map": "Vault",
    "villa-map": "Villa",
    "volcano-map": "Volcano",
    "waste-pool-map": "Waste Pool",
    "wasteland-map": "Wasteland",
    "waterways-map": "Waterways",
    "wharf-map": "Wharf",
    "ancient-reliquary-key": "Ancient Reliquary Key",
    "ambush-leaguestone": "Ambush",
    "anarchy-leaguestone": "Anarchy",
    "beyond-leaguestone": "Beyond",
    "bloodlines-leaguestone": "Bloodlines",
    "breach-leaguestone": "Breach",
    "domination-leaguestone": "Domination",
    "essence-leaguestone": "Essence",
    "invasion-leaguestone": "Invasion",
    "nemesis-leaguestone": "Nemesis",
    "onslaught-leaguestone": "Onslaught",
    "perandus-leaguestone": "Perandus",
    "prophecy-leaguestone": "Prophecy",
    "rampage-leaguestone": "Rampage",
    "talisman-leaguestone": "Talisman",
    "tempest-leaguestone": "Tempest",
    "torment-leaguestone": "Torment",
    "warbands-leaguestone": "Warbands",
    "divine-vessel": "Divine Vessel",
    "orb-of-annulment": "Orb of Annulment",
    "orb-of-binding": "Orb of Binding",
    "orb-of-horizons": "Orb of Horizons",
    "harbingers-orb": "Harbinger's Orb",
    "engineers-orb": "Engineer's Orb",
    "ancient-orb": "Ancient Orb",
    "annulment-shard": "Annulment Shard",
    "mirror-shard": "Mirror Shard",
    "exalted-shard": "Exalted Shard",
    "alleyways-map": "Alleyways",
    "ancient-city-map": "Ancient City",
    "basilica-map": "Basilica",
    "belfry-map": "Belfry",
    "bone-crypt-map": "Bone Crypt",
    "cage-map": "Cage",
    "caldera-map": "Caldera",
    "carcass-map": "Carcass",
    "city-square-map": "City Square",
    "conservatory-map": "Conservatory",
    "coral-ruins-map": "Coral Ruins",
    "courthouse-map": "Courthouse",
    "crimson-temple-map": "Crimson Temple",
    "cursed-crypt-map": "Cursed Crypt",
    "defiled-cathedral-map": "Defiled Cathedral",
    "desert-spring-map": "Desert Spring",
    "dig-map": "Dig",
    "fields-map": "Fields",
    "flooded-mine-map": "Flooded Mine",
    "gardens-map": "Gardens",
    "geode-map": "Geode",
    "harbinger-map": "Harbinger",
    "haunted-mansion-map": "Haunted Mansion",
    "iceberg-map": "Iceberg",
    "infested-valley-map": "Infested Valley",
    "laboratory-map": "Laboratory",
    "lava-chamber-map": "Lava Chamber",
    "lava-lake-map": "Lava Lake",
    "leyline-map": "Leyline",
    "lighthouse-map": "Lighthouse",
    "lookout-map": "Lookout",
    "mausoleum-map": "Mausoleum",
    "moon-temple-map": "Moon Temple",
    "park-map": "Park",
    "pen-map": "Pen",
    "relic-chambers-map": "Relic Chambers",
    "sepulchre-map": "Sepulchre",
    "siege-map": "Siege",
    "sulphur-vents-map": "Sulphur Vents",
    "summit-map": "Summit",
    "sunken-city-map": "Sunken City",
    "toxic-sewer-map": "Toxic Sewer",
    "tribunal-map": "Tribunal",
    "the-ruthless-ceinture": "The Ruthless Ceinture",
    "no-traces": "No Traces",
    "the-realm": "The Realm",
    "the-eye-of-the-dragon": "The Eye of the Dragon",
    "the-blazing-fire": "The Blazing Fire",
    "left-to-fate": "Left to Fate",
    "shaped-vault-map": "Shaped Vault",
    "shaped-bazaar-map": "Shaped Bazaar",
    "shaped-haunted-mansion-map": "Shaped Haunted Mansion",
    "shaped-infested-valley-map": "Shaped Infested Valley",
    "shaped-mausoleum-map": "Shaped Mausoleum",
    "shaped-lookout-map": "Shaped Lookout",
    "shaped-alleyways-map": "Shaped Alleyways",
    "shaped-pen-map": "Shaped Pen",
    "shaped-flooded-mine-map": "Shaped Flooded Mine",
    "shaped-iceberg-map": "Shaped Iceberg",
    "shaped-cage-map": "Shaped Cage",
    "shaped-springs-map": "Shaped Springs",
    "shaped-excavation-map": "Shaped Excavation",
    "shaped-leyline-map": "Shaped Leyline",
    "shaped-city-square-map": "Shaped City Square",
    "shaped-relic-chambers-map": "Shaped Relic Chambers",
    "shaped-courthouse-map": "Shaped Courthouse",
    "shaped-chateau-map": "Shaped Chateau",
    "shaped-gorge-map": "Shaped Gorge",
    "shaped-volcano-map": "Shaped Volcano",
    "shaped-lighthouse-map": "Shaped Lighthouse",
    "shaped-conservatory-map": "Shaped Conservatory",
    "shaped-sulphur-vents-map": "Shaped Sulphur Vents",
    "should-not-display": "should-not-display",
    "shaped-ancient-city-map": "Shaped Ancient City",
    "shaped-ivory-temple-map": "Shaped Ivory Temple",
    "shaped-fields-map": "Shaped Fields",
    "shaped-underground-sea-map": "Shaped Underground Sea",
    "shaped-tribunal-map": "Shaped Tribunal",
    "shaped-coral-ruins-map": "Shaped Coral Ruins",
    "shaped-lava-chamber-map": "Shaped Lava Chamber",
    "shaped-residence-map": "Shaped Residence",
    "shaped-bone-crypt-map": "Shaped Bone Crypt",
    "shaped-gardens-map": "Shaped Gardens",
    "shaped-laboratory-map": "Shaped Laboratory",
    "shaped-overgrown-ruin-map": "Shaped Overgrown Ruin",
    "shaped-geode-map": "Shaped Geode",
    "shaped-mineral-pools-map": "Shaped Mineral Pools",
    "shaped-moon-temple-map": "Shaped Moon Temple",
    "shaped-sepulchre-map": "Shaped Sepulchre",
    "shaped-plateau-map": "Shaped Plateau",
    "shaped-estuary-map": "Shaped Estuary",
    "shaped-scriptorium-map": "Shaped Scriptorium",
    "shaped-siege-map": "Shaped Siege",
    "shaped-shipyard-map": "Shaped Shipyard",
    "shaped-belfry-map": "Shaped Belfry",
    "shaped-wasteland-map": "Shaped Wasteland",
    "shaped-precinct-map": "Shaped Precinct",
    "shaped-cursed-crypt-map": "Shaped Cursed Crypt",
    "the-insatiable": "The Insatiable",
    "the-obscured": "The Obscured",
    "the-iron-bard": "The Iron Bard",
    "forbidden-power": "Forbidden Power",
    "the-breach": "The Breach",
    "the-dreamer": "The Dreamer",
    "the-world-eater": "The World Eater",
    "the-deceiver": "The Deceiver",
    "blessing-of-god": "Blessing of God",
    "the-puzzle": "The Puzzle",
    "bestiary-orb": "Bestiary Orb",
    "imprinted-bestiary-orb": "Imprinted Bestiary Orb",
    "simple-rope-net": "Simple Rope Net",
    "reinforced-rope-net": "Reinforced Rope Net",
    "strong-rope-net": "Strong Rope Net",
    "simple-iron-net": "Simple Iron Net",
    "reinforced-iron-net": "Reinforced Iron Net",
    "strong-iron-net": "Strong Iron Net",
    "simple-steel-net": "Simple Steel Net",
    "reinforced-steel-net": "Reinforced Steel Net",
    "strong-steel-net": "Strong Steel Net",
    "thaumaturgical-net": "Thaumaturgical Net",
    "necromancy-net": "Necromancy Net",
    "harbinger's-shard": "Harbinger's Shard",
    "vial-of-dominance": "Vial of Dominance",
    "vial-of-summoning": "Vial of Summoning",
    "vial-of-awakening": "Vial of Awakening",
    "vial-of-the-ritual": "Vial of the Ritual",
    "vial-of-fate": "Vial of Fate",
    "vial-of-consequence": "Vial of Consequence",
    "vial-of-the-ghost": "Vial of the Ghost",
    "vial-of-transcendence": "Vial of Transcendence",
    "vial-of-sacrifice": "Vial of Sacrifice",
    "harmony-of-souls": "Harmony of Souls",
    "immortal-resolve": "Immortal Resolve",
    "perfection": "Perfection",
    "the-admirer": "The Admirer",
    "the-army-of-blood": "The Army of Blood",
    "the-beast": "The Beast",
    "the-celestial-stone": "The Celestial Stone",
    "the-darkest-dream": "The Darkest Dream",
    "the-dreamland": "The Dreamland",
    "the-fathomless-depths": "The Fathomless Depths",
    "the-hale-heart": "The Hale Heart",
    "the-jeweller's-boon": "The Jeweller's Boon",
    "the-master": "The Master",
    "the-mayor": "The Mayor",
    "the-professor": "The Professor",
    "the-rite-of-elements": "The Rite of Elements",
    "the-samurai's-eye": "The Samurai's Eye",
    "the-sword-king's-salute": "The Sword King's Salute",
    "the-undaunted": "The Undaunted",
    "the-undisputed": "The Undisputed",
    "the-witch": "The Witch",
    "three-voices": "Three Voices",
}

# vim: et:sw=4:sts=4:ai:
