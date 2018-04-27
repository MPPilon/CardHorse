from django.db import models

##
# This file holds all of the lookup models for this app. It is referenced primarily by models in card_models.py in
#  order to define fields with a static list of available options, but will also be referenced by various views when
#  they want to refer to a specific constant these classes contain (which point to the appropriate lookup table
#  entry...or at least that's the theory)
##


class GameSet(models.Model):
    ##
    # Lookup table for card sets; Premier, Canterlot Nights, and so on
    ##

    PREMIER = 1
    CANTERLOT_NIGHTS = 2
    CRYSTAL_GAMES = 3
    ABSOLUTE_DISCORD = 4
    EQUESTRIAN_ODYSSEYS = 5
    HIGH_MAGIC = 6
    MARKS_IN_TIME = 7
    DEFENDERS_OF_EQUESTRIA = 8
    SEAQUESTRIA_AND_BEYOND = 9

    # These sets are separate from block sets, but technically belong in certain blocks as denoted by the first number
    # in their numbers, followed by a 0, followed by a unique ID. The exception to this is the generic promotional set,
    # which will be numbered 999 as it can (and has!) cards considered to be in various sets, and thus blocks
    ROCK_AND_RAVE = 101
    CELESTIAL_SOLSTICE = 102
    SANDS_OF_TIME = 201  # Used for two cards which are not legal as of yet
    GENERIC_SET = 999

    set_name = models.CharField(max_length=100)
    short_code = models.CharField(max_length=3, unique=True)


class Colour(models.Model):
    ##
    # Lookup table for colours, in the order that they are normally presented by card number. Not-colours are also
    #  provided in the case of problems, in the same order.
    ##
    BLUE = 1
    ORANGE = 2
    PINK = 3
    PURPLE = 4
    WHITE = 5
    YELLOW = 6

    # Not-colours for problems
    NOT_BLUE = 7
    NOT_ORANGE = 8
    NOT_PINK = 9
    NOT_PURPLE = 10
    NOT_WHITE = 11
    NOT_YELLOW = 12

    # Wild for the sake of being explicit
    WILD = 13

    colour = models.CharField(max_length=10)


class CardRarity(models.Model):
    ##
    # Lookup table for card rarities, from common to ultra rare. Royal Rares and promos will have their own entry
    #  alongside their normal counterparts.
    ##
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    SUPER_RARE = 4
    ULTRA_RARE = 5
    ROYAL_RARE = 6
    PROMO = 7
    FOIL = 8  # For the first few sets, there were foil cards of other rarities instead of super rares.

    rarity_name = models.CharField(max_length=15)


class CardType(models.Model):
    ##
    # This is the lookup table for card types, which is just a good idea to explicitly define
    ##
    FRIEND = 1
    EVENT = 2
    RESOURCE = 3
    TROUBLEMAKER = 4
    MANE = 5
    PROBLEM = 6

    type = models.CharField(max_length=15)


class Trait(models.Model):
    ##
    # This is the lookup table for available traits in the game. They are not listed in any particular order, but are
    #  categorized by card type.
    # As far as I have discovered, this is the full list of traits in alphabetical order:
    # Accessory, Ahuizotl, Alicorn, Ally, Armor, Artifact, Asset, Breezie, Buffalo, Changeling, Chaotic, Condition, Cow,
    # Crystal, Dilemma, Donkey, Draconequus, Dragon, Earth Pony, Elder, Epic, Foal, Griffon, Gotcha, Location, Mailbox,
    # Minotaur, Pegasus, Performer, Pirate, Pony Tone, Report, Rock, Royalty, Sea Serpent, Seapony, Seashell, Showdown,
    # Siren, Song, Storm, Tree, Unicorn, Unique, Yak, Zebra
    ##
    EARTH_PONY = 1
    PEGASUS = 2
    UNICORN = 3
    ALICORN = 4
    CRITTER = 5
    ROCK = 6
    DRAGON = 7
    DRACONEQUUS = 8  # Literally just Discord
    ALLY = 9  # This is a catch-all trait that seems to have no rhyme or reason to it
    AHUIZOTL = 10  # Ahuizotl literally gets his own trait because of course he does
    ROYALTY = 11  # Fun Fact: The only Alicorn that doesn't have this trait is Big Mac, Princess for a Night!
    CHANGELING = 12
    SEASHELL = 13  # Only exists on tokens at the moment
    COW = 14  # There is one card that uses this: Bessie, Bathtime
    TREE = 15  # On only a single card: Bloomberg, Deep Roots
    ELDER = 16  # Granny Smith and a few others use this one
    FOAL = 17
    MINOTAUR = 18  # Pretty much just limited to Iron Will cards
    ZEBRA = 19  # Pretty much just limited to Zecora cards
    BUFFALO = 20
    CRYSTAL = 21
    BREEZIE = 22
    DONKEY = 23
    GRIFFON = 24
    SEA_SERPENT = 25  # Pretty much just Steven Magnet
    YAK = 26  # Pretty much just Prince Rutherford
    PIRATE = 27
    STORM = 28
    SEAPONY = 29  # But no hippogriff? EP pls
    PONY_TONE = 30  # This trait is also found on a resource (Singing Barrel)
    CHAOTIC = 31  # This can theoretically show up on any card that has a chaos effect

    UNIQUE = 32  # This is available on any non-event card types

    # EVENT = # All events have the event trait, so skip it
    GOTCHA = 33  # This trait doesn't show up on modern cards
    SHOWDOWN = 34
    SONG = 35

    # RESOURCE = # All resources have the resource trait, so skip it
    ACCESSORY = 36
    LOCATION = 37
    ASSET = 38
    CONDITION = 39
    REPORT = 40
    ARTIFACT = 41
    MAILBOX = 42  # Two cards use this trait, and one of them is banned
    DILEMMA = 43

    # TROUBLEMAKER = # All troublemakers have the troublemaker trait, so skip it
    EPIC = 44  # Villain is a rules text keyword!

    # Traits added under this line were forgotten in the initial setup or added after Seaquestria and Beyond. Don't
    #  forget to add the trait to the table itself, and its associated fixture!
    PERFORMER = 45
    ARMOR = 46
    SIREN = 47

    trait_name = models.CharField(max_length=30)
