import random
from data import GENERATION_DATA

NAME_DATA = GENERATION_DATA["name_data"]
NAME_DATA_VALIDATION = GENERATION_DATA["validation_data"]["name_data"]
CLASS_DATA = GENERATION_DATA["class_data"]
ALIGNMENT_DATA = GENERATION_DATA["alignment_data"]
PERSONALITY_DATA = GENERATION_DATA["trait_data"]


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


def validate_data(args):
    # Normalize inputs to Title Case for case-insensitive dictionary lookup.
    race = args.get("race").title() if args.get("race") else None
    genre = args.get("genre").title() if args.get("genre") else None
    gender = args.get("gender").title() if args.get("gender") else None

    # Assign defaults for 'order' and 'morality' if not provided.
    order = args.get("order").title() if args.get("order") else roll_order()
    morality = args.get("morality").title() if args.get("morality") else roll_morality()

    validated_data = {
        "firstname": args.get("firstname").title() if args.get("firstname") else None,
        "surname": args.get("surname").title() if args.get("surname") else None
    }

    if order and not check_order_exists(order):
        raise ValueError(f"Invalid order axis: {order}. Valid orders: {ALIGNMENT_DATA["order"]}")

    validated_data["order"] = order

    if morality and not check_morality_exists(morality):
        raise ValueError(f"Invalid morality axis: {morality}. Valid moralities: {ALIGNMENT_DATA["morality"]}")

    validated_data["morality"] = morality

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
                genders = [gender_key for gender_key in list(NAME_DATA[race][genre].keys()) if gender != "Surnames"]
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
            valid_genre_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"].get(validated_data["genre"])
            valid_races = [race_key for race_key in valid_genre_to_race_keys if race_key in valid_genre_to_race_keys and race_key in valid_gender_to_race_keys]
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
            valid_genres = [genre_key for genre_key in genres if genre in valid_gender_to_genre_keys]

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

    # name_data_set = False
    #
    # Handles the case when a full set of valid data is passed.
    # if race and genre and gender:
    #     valid_race = check_race_exists(race)
    #     if not valid_race:
    #         raise ValueError(f"Invalid race: {race} for generator. Valid races: {list(NAME_DATA.keys())}.")
    #     valid_genre = check_genre_exists(race, genre)
    #     if not valid_genre:
    #         raise ValueError(f"Invalid genre: {genre} for race: {race}. Valid races: {list(NAME_DATA[race].keys())}.")
    #     valid_gender = check_gender_exists(race, genre, gender)
    #     if not valid_gender:
    #         raise ValueError()
    #     validated_data["race"] = race
    #     validated_data["genre"] = genre
    #     validated_data["gender"] = gender
    #     name_data_set = True
    #
    # # Retrieve pre-defined validation sets from global data structures.
    # if gender and not name_data_set:
    #     valid_gender_to_genre_keys = GENERATION_DATA["validation_data"]["name_data"]["gender_to_genre"].get(gender)
    #     valid_gender_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["gender_to_race"].get(gender)
    #     if not valid_gender_to_genre_keys:
    #         raise ValueError()
    #
    #     if genre and genre not in valid_gender_to_genre_keys:
    #         raise ValueError()
    #     elif genre and not race:
    #         validated_data["genre"] = genre
    #         races = GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"].get(genre)
    #         valid_races = [race for race in races if race in valid_gender_to_race_keys]
    #         validated_data["race"] = roll_race(valid_races=valid_races)
    #
    #     if not valid_gender_to_race_keys:
    #         raise ValueError()
    #
    #     if race and race not in valid_gender_to_race_keys:
    #         raise ValueError()
    #     elif race and not genre:
    #         validated_data["race"] = race
    #         genres = list(NAME_DATA[race].keys())
    #         valid_genres = [genre for genre in genres if genre in valid_gender_to_genre_keys]
    #         validated_data["genre"] = roll_genre(race=race, valid_genres=valid_genres)
    #
    #     if gender and not race and not genre:
    #         validated_data["genre"] = random.choice(valid_gender_to_genre_keys)
    #         races = GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"].get(validated_data["genre"])
    #         valid_races = [race for race in races if race in valid_gender_to_race_keys]
    #         validated_data["race"] = roll_race(valid_races=valid_races)
    #     validated_data["gender"] = gender
    #
    # if genre and not gender and not name_data_set:
    #     valid_genre_to_race_keys = GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"].get(genre)
    #     if not valid_genre_to_race_keys:
    #         raise ValueError()
    #     if race and race not in valid_genre_to_race_keys:
    #         raise ValueError()
    #     elif race:
    #         validated_data["race"] = race
    #         validated_data["genre"] = genre
    #         validated_data["gender"] = roll_gender(validated_data["race"], validated_data["genre"])
    #     else:
    #         validated_data["race"] = roll_race(valid_races=valid_genre_to_race_keys)
    #         validated_data["genre"] = genre
    #         validated_data["gender"] = roll_gender(validated_data["race"], validated_data["genre"])
    #
    # no_genre_or_gender = not genre and not gender
    # only_race = race and no_genre_or_gender
    # no_params = not race and no_genre_or_gender
    # if only_race and not check_race_exists(race):
    #     raise ValueError(f"Invalid race: {race} for generator. Valid races: {list(NAME_DATA.keys())}.")
    # if only_race or no_params:
    #     validated_data["race"] = race if race else roll_race()
    #     validated_data["genre"] = roll_genre(validated_data["race"])
    #     validated_data["gender"] = roll_gender(validated_data["race"], validated_data["genre"])
    return validated_data


def generate_name(race=None, genre=None, gender=None, firstname=None, surname=None):
    name_data = GENERATION_DATA["name_data"]
    firstname_part = firstname if firstname else random.choice(name_data[race][genre][gender]["full_firstnames"])
    surname_part = surname if surname else random.choice(name_data[race][genre]["Surnames"]["full_surnames"])
    full_name = f"{firstname_part} {surname_part}"
    return full_name


def generate_stats():
    stats = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }
    for stat in stats.keys():
        lowest_roll = 7
        total = 0
        for i in range(0, 4):
            roll = random.choice(range(1, 7))
            total += roll
            if roll < lowest_roll:
                lowest_roll = roll
        stats[stat] = total - lowest_roll
    return stats


def generate_traits(order=None, morality=None, alignment=None):
    alignment_traits = PERSONALITY_DATA["alignment_traits"]
    traits = {
        "order traits": {

        },
        "morality traits": {

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

    order = validated_data.get("order")
    morality = validated_data.get("morality")
    alignment = "True Neutral" if order == "Neutral" and morality == "Neutral" else f"{order} {morality}"

    name = generate_name(race=race, genre=genre, gender=gender, firstname=firstname, surname=surname)
    stats = generate_stats()
    traits = generate_traits(order=order, morality=morality, alignment=alignment)
    npc = {
        "name": name,
        "race": race,
        "genre": genre,
        "gender": gender,
        "alignment": alignment,
        "stats": stats,
        "traits": traits,
    }
    return npc


race = ""
genre = ""
gender = "N/A"

# Race
# Race and Genre
# Race, Genre and Gender
# Gender
# Gender and Genre
# Gender and Race
# Genre
# No data
# All
# Bad Genre data with All > Fixed error message bug
# Bad Race data with All
# Bad Gender data with All > Fixed an issue where Surnames was included in the gender list due to data structure
# Bad Race only
# Bad Genre with Race
# Bad Gender with Race > Fixed an error where I didn't check the gender in only race and gender
# Bad Race with Gender
# Bad Genre with Gender
# Bad Gender with Genre > Fixed an error where I didn't check the gender in only genre and gender


# for _ in range(1, 1001):
#     npc = generate_npc({"race": race, "genre": genre, "gender": gender})
#     print(npc)
#     if (npc["race"] != race and race) or (genre and npc["genre"] != genre) or (gender and npc["gender"] != gender):
#         print("Npc not aligned with params critical error!")
#         break

# print(generate_npc({"gender": "female"}))
