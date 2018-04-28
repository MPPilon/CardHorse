from HorseDB.models import Colour, Trait, DBErrorLog, CardRarity, CardType, GameSet


def parse_colour_to_model(data, problem=False):
    output = []
    split_data = data.split("/")
    if "None" in split_data:
        return None
    if "Blue" in split_data:
        output.append(Colour.BLUE)
    if "Orange" in split_data:
        output.append(Colour.ORANGE)
    if "Pink" in split_data:
        output.append(Colour.PINK)
    if "Purple" in split_data:
        output.append(Colour.PURPLE)
    if "White" in split_data:
        output.append(Colour.WHITE)
    if "Yellow" in split_data:
        output.append(Colour.YELLOW)
    if "Wild" in split_data:
        output.append(Colour.WILD)

    # Problems have weird parsing, colour will be "COLOUR/Wild" if it has a wild requirement instead of a not-colour.
    if problem:
        if len(split_data) == 1 and "Wild" not in split_data:
            if "Blue" in split_data:
                output.append(Colour.NOT_BLUE)
            if "Orange" in split_data:
                output.append(Colour.NOT_ORANGE)
            if "Pink" in split_data:
                output.append(Colour.NOT_PINK)
            if "Purple" in split_data:
                output.append(Colour.NOT_PURPLE)
            if "White" in split_data:
                output.append(Colour.NOT_WHITE)
            if "Yellow" in split_data:
                output.append(Colour.NOT_YELLOW)

        # For "Fire When Ready"
        if "Rainbow" in split_data:
            output.append(Colour.BLUE)
            output.append(Colour.ORANGE)
            output.append(Colour.PINK)
            output.append(Colour.PURPLE)
            output.append(Colour.WHITE)
            output.append(Colour.YELLOW)

    return output


def parse_card_rarity_to_model(data):
    if data == "C":
        return CardRarity.COMMON
    elif data == "U":
        return CardRarity.UNCOMMON
    elif data == "R":
        return CardRarity.RARE
    elif data == "SR":
        return CardRarity.SUPER_RARE
    elif data == "UR":
        return CardRarity.ULTRA_RARE
    elif data == "RR":
        return CardRarity.ROYAL_RARE
    elif data == "F":
        return CardRarity.FIXED
    elif data == "P":
        return CardRarity.PROMO
    else:
        return None


def parse_req_power_to_model(data):
    return str(data).split("/")[0]


def parse_traits_to_model(data):
    output = []
    split_data = data.split(', ')
    for trait in split_data:
        output.append(Trait()[trait])

    return output


def parse_problem_owner_colours(data):
    output = []
    split_data = data.split("/")
    for colour in split_data:
        output.append()


# The following methods parse traits specific to manes (start and boosted side)
def parse_mane_start_power(data):
    return data.split("/")[0]


def parse_mane_boosted_power(data):
    return data.split("/")[1]


def parse_mane_start_traits_to_model(data):
    output = []
    start_traits = data.split("/")[0].split(", ")
    for trait in start_traits:
        output.append(Trait()[trait])

    return output


def parse_mane_boosted_traits_to_model(data):
    output = []
    if len(data.split("/")) > 1:
        start_traits = data.split("/")[1].split(", ")
    else:
        return [Trait()[data.split("/")[0]]]
    for trait in start_traits:
        output.append(Trait()[trait])

    return output


def parse_mane_start_rules_text(data):
    if data:
        front_text = data.split("Back:")[0]
        return front_text.split("Front:")[1]
    else:
        return None


def parse_mane_boosted_rules_text(data):
    if data:
        return data.split("Back:")[1]
    else:
        return None


def parse_mane_start_flavour_text(data):
    if data:
        return data.split(" / ")[0]
    else:
        return None


def parse_mane_boosted_flavour_text(data):
    if data:
        return data.split(" / ")[1]
    else:
        return None


def parse_mane_start_title(data):
    return data.split("/")[0]


def parse_mane_boosted_title(data):
    split_data = data.split("/")
    if len(split_data) > 1:
        return split_data[1]
    else:
        return split_data[0]


# These two parse methods are provided for future expansion, should they ever be needed
def parse_mane_start_subtitle(data):
    return data


def parse_mane_boosted_subtitle(data):
    return data


# The following methods resolve an instance of a lookup model
def resolve_card_type(id):
    return CardType.objects.get(pk=id)


def resolve_card_rarity(id):
    return CardRarity.objects.get(pk=id)


def resolve_card_colour(id):
    return Colour.objects.get(pk=id)


def resolve_card_set_by_id(id):
    return GameSet.objects.get(pk=id)


def resolve_card_set_by_short_code(short_code):
    return GameSet.objects.get(short_code=short_code)


def resolve_card_trait(id):
    return Trait.objects.get(pk=id)
