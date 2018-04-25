from django.db import models
from django.contrib.postgres.fields import ArrayField
from HorseDB.models import lookup_models


##
# This file holds all of the card-related models for this app, which is to say anything that isn't a lookup table. It
#  also holds any specific validation related to the card type in question, things like cards having requirement power
#  set if requirement colour is set, problems having appropriate array lengths for confront requirements, etc.
##


class Card(models.Model):
    ##
    # This model is the supertype for all cards in the game, primarily lists attributes that are common among all
    #  cards: set, number, rarity, type, title, rules text, and flavour text. Cards are also unique based on set,
    #  number, and rarity (so as to account for Royal Rares and Promo cards, which share set and number).
    ##

    class Meta:
        # Card set, number, and rarity determine the card, and together each must be unique to any other
        unique_together = ('card_set', 'card_number', 'card_rarity')

    card_set = models.ForeignKey(lookup_models.GameSet, on_delete=models.CASCADE)
    card_number = models.SmallIntegerField()
    card_rarity = models.ForeignKey(lookup_models.CardRarity, on_delete=models.CASCADE)
    card_type = models.ForeignKey(lookup_models.CardType, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=100)
    card_subtitle = models.CharField(max_length=100, null=True)
    card_rules_text = models.CharField(max_length=500, null=True)
    card_flavour_text = models.CharField(max_length=300, null=True)
    card_banned = models.BooleanField(default=False)


class CardFriend(Card):
    ##
    # This is the Friend model, inheriting the universal Card model attributes
    ##
    power = models.SmallIntegerField()
    cost = models.SmallIntegerField()
    colour = ArrayField(models.SmallIntegerField(), null=True)
    requirement_colour = ArrayField(models.SmallIntegerField(), null=True)
    requirement_power = models.SmallIntegerField(default=0)
    trait = ArrayField(models.SmallIntegerField(), null=True)


class CardEvent(Card):
    ##
    # This is the Event model, inheriting the universal Card model attributes
    ##
    power = models.SmallIntegerField()
    cost = models.SmallIntegerField()
    requirement_colour = ArrayField(models.SmallIntegerField(), null=True)
    requirement_power = models.SmallIntegerField(default=0)
    trait = ArrayField(models.SmallIntegerField(), null=True)


class CardResource(Card):
    ##
    # This is the Resource model, inheriting the universal Card model attributes
    ##
    power = models.SmallIntegerField()
    cost = models.SmallIntegerField()
    requirement_colour = ArrayField(models.SmallIntegerField(), null=True)
    requirement_power = models.SmallIntegerField(default=0)
    trait = ArrayField(models.SmallIntegerField(), null=True)


class CardDilemma(CardResource):
    ##
    # This the dilemma model, a further subtype of Resource cards that include problem-like attributes.
    # This model would normally inherit from CardProblem as well, but because multiple inheritance is kind of messy I
    #  decided to save myself the headache and just make this inherit from only CardResource instead.
    # Similarly to the CardProblem model, care should be taken to ensure that colour and power requirement indices
    #  match up between the arrays so that they can be processed properly when displaying the card's attributes.
    ##
    owner_requirement_colour = ArrayField(models.SmallIntegerField())
    owner_requirement_power = ArrayField(models.SmallIntegerField())
    opposing_requirement_colour = ArrayField(models.SmallIntegerField())
    opposing_requirement_power = ArrayField(models.SmallIntegerField())
    bonus = models.SmallIntegerField()


class CardTroublemaker(Card):
    ##
    # This is the Troublemaker model, inheriting the universal Card model attributes
    ##
    power = models.SmallIntegerField()
    bonus = models.SmallIntegerField()
    trait = ArrayField(models.SmallIntegerField(), null=True)


class CardProblem(Card):
    ##
    # This is the Problem model, inheriting the universal Card model attributes
    # Care must be taken when using this model! The indices of the requirement power must be the same as the requirement
    #  colour so that it can match up colour to power with two arrays instead of having fourteen attributes describing
    #  how much of each colour is needed for each side. Nobody wants that many attributes on a table. NOBODY.
    # The length of the colour array must be equal to the length of the power array.
    ##
    owner_requirement_colour = ArrayField(models.SmallIntegerField())
    owner_requirement_power = ArrayField(models.SmallIntegerField())
    opposing_requirement_colour = ArrayField(models.SmallIntegerField())
    opposing_requirement_power = ArrayField(models.SmallIntegerField())
    bonus = models.SmallIntegerField()


class CardMane(Card):
    ##
    # This is the Mane character model, inheriting the universal Card model attributes. Manes are unique in that they
    #  have a boosted side to them, meaning they have additional "boosted" power, text, and traits (which can all be
    #  different from the start side!).
    ##
    power = models.SmallIntegerField()
    boosted_power = models.SmallIntegerField()
    trait = ArrayField(models.SmallIntegerField())
    boosted_trait = ArrayField(models.SmallIntegerField())
    boosted_rules_text = models.CharField(max_length=200, null=True)
    boosted_flavour_text = models.CharField(max_length=200, null=True)