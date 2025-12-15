import math
import random
from data import GENERATION_DATA

NAME_DATA = GENERATION_DATA["name_data"]
NAME_DATA_VALIDATION = GENERATION_DATA["validation_data"]["name_data"]

CLASS_DATA = GENERATION_DATA["class_data"]

RACE_DATA = GENERATION_DATA["race_data"]

ALIGNMENT_DATA = GENERATION_DATA["alignment_data"]

TRAIT_DATA = GENERATION_DATA["trait_data"]


def roll_race(valid_races=None):
    race = random.choice(valid_races or list(NAME_DATA.keys()))
    return race


def check_race_exists(race):
    return race in NAME_DATA.keys()


def roll_genre(race, valid_genres=None):
    genre = random.choice(valid_genres or list(NAME_DATA[race].keys()))
    return genre


def check_genre_exists(race, genre):
    return genre in NAME_DATA[race].keys()


def roll_gender(race, genre):
    genders = [gender for gender in NAME_DATA[race][genre].keys() if gender != "Surnames"]
    return random.choice(genders)


def check_gender_exists(race, genre, gender):
    return gender in NAME_DATA[race][genre].keys() and not gender == "Surnames"


def roll_order():
    return random.choice(ALIGNMENT_DATA["order"])


def check_order_exists(order):
    return order in ALIGNMENT_DATA["order"]


def roll_morality():
    return random.choice(ALIGNMENT_DATA["morality"])


def check_morality_exists(morality):
    return morality in ALIGNMENT_DATA["morality"]


def roll_class():
    return random.choice(list(CLASS_DATA.keys()))


def roll_stat_values():
    stat_value_list = []
    for _ in range(1, 7):
        lowest_roll = 7
        total = 0
        for i in range(0, 4):
            roll = random.choice(range(1, 7))
            total += roll
            if roll < lowest_roll:
                lowest_roll = roll
        stat_value_list.append(total - lowest_roll)
    return stat_value_list


def validate_data(args):
    # Normalize inputs to Title Case for case-insensitive dictionary lookup.
    race = args.get("race").title() if args.get("race") else None
    genre = args.get("genre").title() if args.get("genre") else None
    gender = args.get("gender").title() if args.get("gender") else None

    # Assign defaults for 'order' and 'morality' if not provided.
    order = args.get("order").title() if args.get("order") else roll_order()
    morality = args.get("morality").title() if args.get("morality") else roll_morality()

    class_ = args.get("class").title() if args.get("class") else None
    assign_class = bool(args.get("assign-class"))

    # Adds names to the validated data if present.
    validated_data = {
        "firstname": args.get("firstname").title() if args.get("firstname") else None,
        "surname": args.get("surname").title() if args.get("surname") else None,
        "opt_stats": bool(args.get("opt-stats"))
    }

    # Checks order axis is present and if so validates it.
    if order and not check_order_exists(order):
        raise ValueError(f"Invalid order axis: {order}. Valid orders: {ALIGNMENT_DATA["order"]}")

    validated_data["order"] = order

    # Checks morality axis is present and if so validates it.
    if morality and not check_morality_exists(morality):
        raise ValueError(f"Invalid morality axis: {morality}. Valid moralities: {ALIGNMENT_DATA["morality"]}")

    validated_data["morality"] = morality

    if class_ and class_ not in CLASS_DATA.keys():
        raise ValueError(f"Invalid class: {class_}. Valid classes: {list(CLASS_DATA.keys())}")

    if class_:
        validated_data["class"] = {"name": class_} | CLASS_DATA[class_]["class data"]
    elif not class_ and assign_class:
        new_class = roll_class()
        validated_data["class"] = {"name": new_class} | CLASS_DATA[new_class]["class data"]
    elif not class_ and random.choice(range(1, 101)) <= 50:
        new_class = roll_class()
        validated_data["class"] = {"name": new_class} | CLASS_DATA[new_class]["class data"]
    else:
        validated_data["class"] = class_

    # Sets the match pattern for how to validate the data
    name_data_pattern = (bool(race), bool(genre), bool(gender))

    match name_data_pattern:
        case (False, False, False) | (True, False, False) | (True, True, False) | (True, True, True):
            race = race or roll_race()
            valid_race = check_race_exists(race)
            if not valid_race:
                raise ValueError(f"Invalid race: {race}. Valid races: {list(NAME_DATA.keys())}.")
            genre = genre or roll_genre(race)
            valid_genre = check_genre_exists(race, genre)
            if not valid_genre:
                raise ValueError(
                    f"Invalid genre: {genre} for race: {race}. Valid genres: {list(NAME_DATA[race].keys())}.")
            gender = gender or roll_gender(race, genre)
            valid_gender = check_gender_exists(race, genre, gender)
            if not valid_gender:
                genders = [key for key in NAME_DATA[race][genre].keys() if key != "Surnames"]
                raise ValueError(
                    f"Invalid gender: {gender} for race: {race} and genre: {genre}, combination. Valid genders {genders}.")
            validated_data["race"] = race
            validated_data["genre"] = genre
            validated_data["gender"] = gender
            pass
        case (False, False, True) | (False, True, True):
            valid_gender_to_genre_keys = GENERATION_DATA["validation_data"]["name_data"]["gender_to_genre"].get(gender)
            valid_gender_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["gender_to_race"].get(gender)

            if not valid_gender_to_genre_keys:
                raise ValueError(f"Invalid Gender: {gender}. Gender is not recognized.")

            if genre and genre not in valid_gender_to_genre_keys:
                raise ValueError(
                    f"Invalid pairing of gender: {gender} and genre: {genre}. Valid genres for gender: {list(valid_gender_to_genre_keys)}.")

            validated_data["genre"] = genre or random.choice(valid_gender_to_genre_keys)
            valid_genre_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"].get(
                validated_data["genre"])
            valid_races = [race_key for race_key in valid_genre_to_race_keys if
                           race_key in valid_genre_to_race_keys and race_key in valid_gender_to_race_keys]
            validated_data["race"] = roll_race(valid_races=valid_races)
            validated_data["gender"] = gender
            pass
        case (True, False, True):
            valid_race = check_race_exists(race)
            valid_gender_to_genre_keys = GENERATION_DATA["validation_data"]["name_data"]["gender_to_genre"].get(gender)
            valid_gender_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["gender_to_race"].get(gender)

            if not valid_gender_to_race_keys:
                raise ValueError(f"Invalid Gender: {gender}. Gender is not recognized.")

            if not valid_race:
                raise ValueError(f"Invalid race: {race}. Valid races: {list(NAME_DATA.keys())}.")

            if race not in valid_gender_to_race_keys:
                raise ValueError(
                    f"Invalid race: {race} for gender: {gender}. Valid races: {valid_gender_to_race_keys} for {gender}")

            genres = list(NAME_DATA[race].keys())
            valid_genres = [genre_key for genre_key in genres if genre_key in valid_gender_to_genre_keys]

            if not valid_genres:
                raise ValueError(f"No compatible genres found for race: {race} and gender: {gender}. Check your data "
                                 f"configuration.")

            validated_data["race"] = race
            validated_data["gender"] = gender
            validated_data["genre"] = roll_genre(race=race, valid_genres=valid_genres)
            pass
        case (False, True, False):
            valid_genre_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"].get(genre)

            if not valid_genre_to_race_keys:
                raise ValueError(f"Invalid genre: {genre}. Genre does not exist in the data.")

            validated_data["race"] = roll_race(valid_races=valid_genre_to_race_keys)
            validated_data["genre"] = genre
            validated_data["gender"] = roll_gender(validated_data["race"], validated_data["genre"])
            pass
    return validated_data


def generate_name(race=None, genre=None, gender=None, firstname=None, surname=None):
    name_data = GENERATION_DATA["name_data"]
    firstname_part = firstname if firstname else random.choice(name_data[race][genre][gender]["full_firstnames"])
    surname_part = surname if surname else random.choice(name_data[race][genre]["Surnames"]["full_surnames"])
    full_name = f"{firstname_part} {surname_part}"
    return full_name


def generate_stats(race, class_=None, opt_stats=None):
    stats = {
    }
    race_stat_bonuses = RACE_DATA[race]["stat bonuses"]
    class_data = CLASS_DATA.get(class_)
    stat_list = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    if class_data:
        main_stat = class_data["main stat"].copy()
        secondary_stats = class_data["secondary stats"].copy()
        dump_stats = class_data["dump stats"].copy()
        main_stat_pool = class_data.get("main stat pooling", []).copy()
        secondary_stat_pool = class_data.get("secondary stats pooling", []).copy()
        if main_stat_pool:
            random.shuffle(main_stat_pool)
            main_stat += [main_stat_pool.pop(0)]
            secondary_stats += main_stat_pool
        if secondary_stat_pool:
            random.shuffle(main_stat)
            random.shuffle(secondary_stat_pool)
            secondary_stats += [secondary_stat_pool.pop(0)]
            dump_stats += secondary_stat_pool
        random.shuffle(secondary_stats)
        random.shuffle(dump_stats)
        stat_list = main_stat + secondary_stats + dump_stats
    stat_values = roll_stat_values()
    if opt_stats:
        stat_values.sort(reverse=True)
    else:
        random.shuffle(stat_list)
    for i in range(0, 6):
        stat = stat_list[i]
        value = stat_values[i]
        racial_bonus = race_stat_bonuses.get(stat, 0)
        final_value = value + racial_bonus
        stats[stat] = {
            "value": final_value,
            "modifier": math.floor((final_value - 10) / 2),
            "race bonus": racial_bonus
        }
    return stats


def calculate_hp(class_data=None, con_bonus=None):
    base_hp = class_data['hit dice'] if class_data else random.choice(range(5, 11))
    return base_hp + con_bonus


def generate_traits(order=None, morality=None, alignment=None):
    alignment_traits = TRAIT_DATA["alignment_traits"]
    ego_traits = TRAIT_DATA["ego"]

    traits = {
        "order traits": {

        },
        "morality traits": {

        },
        "alignment trait": {

        },
        "ego trait": {

        }
    }
    order_trait_count = 1
    morality_trait_count = 1

    order_trait_threshold = 600
    morality_trait_threshold = 600

    order_data = alignment_traits["order"][order]
    available_order_keys = list(order_data.keys())

    morality_data = alignment_traits["morality"][morality]
    available_morality_keys = list(morality_data.keys())

    alignment_data = alignment_traits["alignment"][alignment]
    available_alignment_keys = list(alignment_data.keys())

    alignment_key = random.choice(available_alignment_keys)
    traits["alignment trait"][alignment_key] = alignment_data[alignment_key]

    ego_level = random.choice(list(ego_traits.keys()))
    ego_level_data = ego_traits[ego_level]
    available_ego_keys = list(ego_traits[ego_level].keys())

    ego_key = random.choice(available_ego_keys)
    traits["ego trait"][ego_key] = ego_level_data[ego_key]

    while len(traits["order traits"].keys()) < order_trait_count:
        unpicked_order_traits = set(available_order_keys) - set(traits["order traits"].keys())

        order_trait_key = random.choice(list(unpicked_order_traits))

        traits["order traits"][order_trait_key] = order_data[order_trait_key]

        order_trait_roll = random.choice(range(1, 1001))

        if order_trait_roll > order_trait_threshold:
            order_trait_count += 1
            order_trait_threshold += 200

    while len(traits["morality traits"].keys()) < morality_trait_count:
        unpicked_morality_traits = set(available_morality_keys) - set(traits["morality traits"].keys())

        morality_trait_key = random.choice(list(unpicked_morality_traits))

        traits["morality traits"][morality_trait_key] = morality_data[morality_trait_key]

        morality_trait_roll = random.choice(range(1, 1001))

        if morality_trait_roll > morality_trait_threshold:
            morality_trait_count += 1
            morality_trait_threshold += 200
    return traits


def generate_npc(args):
    try:
        validated_data = validate_data(args)
    except ValueError as e:
        raise e
    race = validated_data["race"]
    genre = validated_data["genre"]
    gender = validated_data["gender"]

    firstname = validated_data.get("firstname")
    surname = validated_data.get("surname")
    name = generate_name(race=race, genre=genre, gender=gender, firstname=firstname, surname=surname)

    order = validated_data.get("order")
    morality = validated_data.get("morality")
    alignment = "True Neutral" if order == "Neutral" and morality == "Neutral" else f"{order} {morality}"

    class_data = validated_data["class"]
    class_name = None

    if class_data:
        class_name = class_data["name"]

    stats = generate_stats(race=race, class_=class_name, opt_stats=validated_data["opt_stats"])
    traits = generate_traits(order=order, morality=morality, alignment=alignment)
    hp = calculate_hp(class_data=class_data, con_bonus=stats["constitution"]["modifier"])

    npc = {
        "name": name,
        "hp": hp,
        "race": race,
        "genre": genre,
        "gender": gender,
        "class": class_data,
        "alignment": alignment,
        "stats": stats,
        "traits": traits,
    }
    return npc


def get_field_data():
    NAME_VALIDATION_DATA = GENERATION_DATA["validation_data"]["name_data"]
    data = {
        "RACE": {
            "all_races": list(GENERATION_DATA["name_data"].keys()),
            "race_to_genre": NAME_VALIDATION_DATA["race_to_genre"],
            "race_to_gender": NAME_VALIDATION_DATA["race_to_gender"]
        },
        "GENRE": {
            "all_genres": list(NAME_VALIDATION_DATA["genre_to_race"].keys()),
            "genre_to_race": NAME_VALIDATION_DATA["genre_to_race"],
            "genre_to_gender": NAME_VALIDATION_DATA["genre_to_gender"]
        },
        "GENDER": {
            "all_genders": list(NAME_VALIDATION_DATA["gender_to_race"].keys()),
            "gender_to_genre": NAME_VALIDATION_DATA["gender_to_genre"],
            "gender_to_race": NAME_VALIDATION_DATA["gender_to_race"]
        },
        "ALIGNMENT": {
            "order": ALIGNMENT_DATA["order"],
            "morality": ALIGNMENT_DATA["morality"]
        },
        "CLASS": {
            "all_classes": list(CLASS_DATA.keys())
        }
    }
    return data


