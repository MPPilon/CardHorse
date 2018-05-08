from django.db import IntegrityError
from django.http import HttpResponse
import urllib.request
import json

from django.template.response import TemplateResponse

from HorseDB.db_utils import parse_colour_to_model, parse_traits_to_model, parse_req_power_to_model, \
    parse_mane_start_power, parse_mane_boosted_power, parse_mane_start_traits_to_model, \
    parse_mane_boosted_traits_to_model, parse_mane_start_flavour_text, parse_mane_start_rules_text, \
    parse_mane_boosted_rules_text, parse_mane_boosted_flavour_text, parse_mane_boosted_title, \
    parse_mane_boosted_subtitle, parse_mane_start_title, parse_mane_start_subtitle, parse_card_rarity_to_model, \
    resolve_card_type, resolve_card_rarity, resolve_card_set_by_short_code
from HorseDB.models import GameSet, CardFriend, CardEvent, CardResource, CardMane, CardTroublemaker, CardProblem, \
    CardType, CardDilemma, Colour, Card


def database_homepage(request):
    ##
    # This view sends the user to the card database homepage
    ##

    return TemplateResponse(request, 'index.html')


def database_admin_acquire_card_list(request):
    ##
    # This view is admin-only and can only be accessed if a correct password is submitted with the request. It grabs
    #  all of the cards in the game from Aracat's MLPCCG API at http://www.ferrictorus.com/mlpapi1/
    ##
    return None
    api_domain = 'http://www.ferrictorus.com/mlpapi1/'
    query = 'cards?query=allids:""'
    print("Attempting to get card list from " + api_domain + query)
    response = urllib.request.urlopen(api_domain + query).read()
    json_data = json.loads(response)
    for card in json_data["data"]:
        # Load initial name, rules and flavour text (Manes will tend to change this)
        rules_text = card["gametext"]
        flavour_text = card["flavortext"]
        title = card["title"]
        subtitle = card["subtitle"]
        if card["type"] == "Friend":
            new_card = CardFriend(
                card_type=resolve_card_type(CardType.FRIEND),
                power=int(card["power"]),
                cost=card["cost"],
                colour=parse_colour_to_model(card["color"]),
                requirement_colour=parse_colour_to_model(card["color"]),
                requirement_power=parse_req_power_to_model(card['req']),
                trait=parse_traits_to_model(card["traits"])
            )

        elif card["type"] == "Event":
            new_card = CardEvent(
                card_type=resolve_card_type(CardType.EVENT),
                power=int(card["power"]),
                cost=card["cost"],
                requirement_colour=parse_colour_to_model(card["color"]),
                requirement_power=parse_req_power_to_model(card['req']),
                trait=parse_traits_to_model(card["traits"])
            )

        elif card["type"] == "Resource":
            if "Dilemma" in card["traits"]:
                new_card = CardDilemma(
                    bonus=card["bonus"],
                    owner_requirement_colour=[Colour.WILD],
                    owner_requirement_power=[card["prireq"]],
                    opposing_requirement_colour=[Colour.WILD],
                    opposing_requirement_power=[card["wildreq"]]
                )
            else:
                new_card = CardResource()
            new_card.card_type = resolve_card_type(CardType.RESOURCE)
            new_card.power = int(card["power"])
            new_card.cost = card["cost"]
            new_card.requirement_colour = parse_colour_to_model(card["color"])
            new_card.requirement_power = parse_req_power_to_model(card['req'])
            new_card.trait = parse_traits_to_model(card["traits"])

        elif card["type"] == "Mane":
            new_card = CardMane(
                card_type=resolve_card_type(CardType.MANE),
                power=parse_mane_start_power(card['power']),
                boosted_power=parse_mane_boosted_power(card['power']),
                colour=parse_colour_to_model(card["color"]),
                trait=parse_mane_start_traits_to_model(card["traits"]),
                boosted_trait=parse_mane_boosted_traits_to_model(card["traits"]),
                boosted_rules_text=parse_mane_boosted_rules_text(rules_text),
                boosted_flavour_text=parse_mane_boosted_flavour_text(flavour_text),
                boosted_title=parse_mane_boosted_title(title),
                boosted_subtitle=parse_mane_boosted_subtitle(subtitle)
            )
            rules_text = parse_mane_start_rules_text(rules_text)
            flavour_text = parse_mane_start_flavour_text(flavour_text)
            title = parse_mane_start_title(title)
            subtitle = parse_mane_start_subtitle(subtitle)

        elif card["type"] == "Troublemaker":
            new_card = CardTroublemaker(
                card_type=resolve_card_type(CardType.TROUBLEMAKER),
                power=int(card["power"]),
                bonus=int(card["bonus"]),
                trait=parse_traits_to_model(card["traits"])
            )

        elif card["type"] == "Problem":
            prireq = int(card["prireq"])
            secreq = int(card["secreq"])
            owner_colour = parse_colour_to_model(card["color"], True)
            if secreq == 0 and len(owner_colour) > 1:
                owner_colour = [owner_colour[0]]  # Some blue problems have only a blue requirement

            if len(owner_colour) == 6:  # Check for Fire When Ready
                owner_power = [5, 5, 5, 5, 5, 5]
                opposing_colour = owner_colour
                opposing_power = owner_power
            else:
                if len(owner_colour) > 1:
                    owner_power = [prireq, secreq]
                else:
                    owner_power = [prireq]
                opposing_colour = [Colour.WILD]
                opposing_power = [int(card["wildreq"])]

            new_card = CardProblem(
                card_type=resolve_card_type(CardType.PROBLEM),
                owner_requirement_colour=owner_colour,
                owner_requirement_power=owner_power,
                opposing_requirement_colour=opposing_colour,
                opposing_requirement_power=opposing_power,
                bonus=int(card["bonus"])
            )

        new_card.card_set = resolve_card_set_by_short_code(card["set"])
        number = card["number"]
        new_card.card_rarity = resolve_card_rarity(parse_card_rarity_to_model(card["rarity"]))
        if "p" in number or "f" in number or "d" in number:
            number = number.replace("p", "")
            number = number.replace("f", "")
            number = number.replace("d", "")
            # This is a promo card, override the original rarity
            new_card.card_rarity = resolve_card_rarity(parse_card_rarity_to_model("P"))
        new_card.card_number = int(number)

        new_card.card_title = title
        new_card.card_subtitle = subtitle
        new_card.card_rules_text = rules_text
        new_card.card_flavour_text = flavour_text
        if card["status"] == "Banned":
            new_card.card_banned = True
        try:
            new_card.save()
        except IntegrityError:
            print("Card already in DB: " + str(new_card.card_set.short_code) + str(new_card.card_number) + str(new_card.card_rarity.rarity_name))

    return HttpResponse(200)


def ajax_fetch_all_cards(request):
    ##
    # This view is an AJAX-only view accessed by background workers to fetch all cards from the database. It should
    #  probably avoid being used unless absolutely necessary.
    ##
    return HttpResponse(200)


def ajax_fetch_simple_filtered_list(request):
    return HttpResponse(200)


def ajax_fetch_advanced_filtered_list(request):
    return HttpResponse(200)
