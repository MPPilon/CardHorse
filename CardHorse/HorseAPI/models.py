from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class GameState(models.Model):
    ###
    # This model represents the entirety of the game state, that is to say that this object contains
    # all of the zones, areas, cards, and active modifiers at the moment. All public information should be included!
    # This model also needs to be tied to the user who submitted it. No anonymous requests!
    ###
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PlayZone(models.Model):
    ###
    # This model represents the play zone of the game, where cards exist while in play.
    ###
    game = models.OneToOneField(GameState, on_delete=models.CASCADE)


class HandZone(models.Model):
    ###
    # This model represents the hand of the player taking the action. It might be relevant to some cards, such as
    # Gummy, Lap Gator where it can be put into play upon moving a character. This information should not be returned
    # to the players, even if it's just the player who sent it.
    ###
    game = models.OneToOneField(GameState, on_delete=models.CASCADE)


class GamePlayArea(models.Model):
    ###
    # This model represents one of the areas in the Play Zone: the active player's home, the non-active player's home,
    # the active player's problem, the non-active player's problem, and any additional problems in play (Dilemmas).
    # Dilemmas can be assigned any ID greater than 4 as long as it is consistent with cards that are present.
    ###

    zone = models.OneToOneField(PlayZone, on_delete=models.CASCADE)
    area_id = models.PositiveSmallIntegerField()


class Card(models.Model):
    ###
    # This model represents a card. Any card. It could be a friend, could be a problem, could be a troublemaker.
    # It lists off all the computer-relevant details of the card like set, card number, colour, power, etc.
    # Notice that rules text is not stored: This is not a card lookup model!
    ###
    card_set = models.SmallIntegerField()
    card_number = models.SmallIntegerField()
    power = models.IntegerField()
    cost = models.IntegerField()
    traits = ArrayField(models.PositiveSmallIntegerField, null=True)
    colour = ArrayField(models.PositiveSmallIntegerField, null=True)

    # TODO: Colour requirements are currently the same power for all colours, but this could change! How to handle?
    requirement_power = models.PositiveSmallIntegerField(null=True)
    requirement_colours = ArrayField(models.PositiveSmallIntegerField, null=True)


class Problem(models.Model):
    ###
    # I decided to break this out into its own model because it made the Card model too messy. A resource becoming
    # a problem shouldn't matter as long as we receive valid data from the sender. This is huge because there are
    # various colour combinations with varying values, up to Fire When Ready which has all colours.
    # Maybe switch this to lookup requirements instead?
    ###
    area = models.ForeignKey(GamePlayArea, on_delete=models.CASCADE)
    card_set = models.SmallIntegerField()
    card_number = models.SmallIntegerField()

    # Owning player's confront requirements
    owner_confront_requirement_colour_1 = models.SmallIntegerField(null=True)
    owner_confront_requirement_power_1 = models.SmallIntegerField()
    owner_confront_requirement_colour_2 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_power_2 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_colour_3 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_power_3 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_colour_4 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_power_4 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_colour_5 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_power_5 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_colour_6 = models.SmallIntegerField(null=True, default=None)
    owner_confront_requirement_power_6 = models.SmallIntegerField(null=True, default=None)

    # Opponent's confront requirements
    opponent_confront_requirement_colour_1 = models.SmallIntegerField(null=True)
    opponent_confront_requirement_power_1 = models.SmallIntegerField()
    opponent_confront_requirement_colour_2 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_power_2 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_colour_3 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_power_3 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_colour_4 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_power_4 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_colour_5 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_power_5 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_colour_6 = models.SmallIntegerField(null=True, default=None)
    opponent_confront_requirement_power_6 = models.SmallIntegerField(null=True, default=None)


class PlayerAction(models.Model):
    ###
    # This is the action the player is requesting.
    # Possible actions include main phase actions, activating abilities, and playing cards.
    ###
    action_type = models.PositiveSmallIntegerField()
