from django.test import TestCase

from HorseDB.models import *


def create_test_cards():
    CardFriend.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=101,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.FRIEND,
        card_title='Test Card',
        card_subtitle='Please Ignore',
        card_rules_text='Random. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Friend attributes
        power=1,
        cost=8,
        colour=[Colour.PINK],
        requirement_colour=[Colour.PINK],
        requirement_power=4,
        trait=[Trait.CRYSTAL, Trait.TREE],
    )
    CardFriend.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=102,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.FRIEND,
        card_title='Test Card 2',
        card_subtitle='Please Ignore',
        card_rules_text='Stubborn. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Friend attributes
        power=2,
        cost=7,
        colour=[Colour.ORANGE],
        requirement_colour=[Colour.ORANGE],
        requirement_power=4,
        trait=[Trait.YAK, Trait.ALLY],
    )
    CardFriend.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=103,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.FRIEND,
        card_title='Test Card 3',
        card_subtitle='Please Ignore',
        card_rules_text='Swift. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Friend attributes
        power=3,
        cost=6,
        colour=[Colour.BLUE],
        requirement_colour=None,
        requirement_power=0,
        trait=[Trait.PEGASUS, Trait.PERFORMER],
    )
    CardEvent.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=104,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.EVENT,
        card_title='Test Card 4',
        card_subtitle='Please Ignore',
        card_rules_text='Chaos: You win the game. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Friend attributes
        power=4,
        cost=5,
        requirement_colour=[Colour.ORANGE],
        requirement_power=4,
        trait=[Trait.SONG, Trait.CHAOTIC],
    )
    CardEvent.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=105,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.EVENT,
        card_title='Test Card 5',
        card_subtitle='Please Ignore',
        card_rules_text='Immediate: You lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Event attributes
        power=5,
        cost=4,
        requirement_colour=None,
        requirement_power=None,
        trait=None,
    )
    CardResource.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=106,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.RESOURCE,
        card_title='Test Card 6',
        card_subtitle='Please Ignore',
        card_rules_text='Play on a problem. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Resource attributes
        power=6,
        cost=3,
        requirement_colour=[Colour.YELLOW],
        requirement_power=1,
        trait=[Trait.LOCATION],
    )
    CardResource.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=107,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.RESOURCE,
        card_title='Test Card 7',
        card_subtitle='Please Ignore',
        card_rules_text='Play on a friend. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Resource attributes
        power=7,
        cost=2,
        requirement_colour=[Colour.YELLOW, Colour.BLUE],
        requirement_power=3,
        trait=[Trait.ACCESSORY, Trait.ARTIFACT],
    )
    CardDilemma.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=108,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.RESOURCE,
        card_title='Test Card 8',
        card_subtitle='Please Ignore',
        card_rules_text='When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Resource attributes
        power=8,
        cost=1,
        requirement_colour=[Colour.WHITE, Colour.PURPLE],
        requirement_power=2,
        trait=[Trait.DILEMMA],

        # Dilemma Attributes
        owner_requirement_colour=[Colour.WHITE, Colour.PURPLE, Colour.WILD],
        owner_requirement_power=[1, 1, 3],
        opposing_requirement_colour=[Colour.WILD],
        opposing_requirement_power=[10],
        bonus=2,
    )
    CardTroublemaker.objects.create(
        # Card attributes
        card_set=GameSet.ABSOLUTE_DISCORD,
        card_number=109,
        card_rarity=CardRarity.PROMO,
        card_type=CardType.FRIEND,
        card_title='Test Card 9',
        card_subtitle='Please Ignore',
        card_rules_text='Villain. When this card is in your hand, reveal it and you lose the game.',
        card_flavour_text='Dreddit is recruiting.',

        # Troublemaker attributes
        power=9,
        bonus=2,
        trait=[Trait.EPIC, Trait.UNIQUE],
    )


class SearchByPower(TestCase):
    def setUp(self):
        create_test_cards()

    def test_search_by_exact_power(self):
        pass