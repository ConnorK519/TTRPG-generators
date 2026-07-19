from names import HUMAN_MALE_FANTASY_NAMES, HUMAN_FEMALE_FANTASY_NAMES, HUMAN_FANTASY_SURNAMES

GENERATION_DATA = {
    "validation_data": {
        "name_data": {}
    },
    "name_data": {
        "Human": {
            "Fantasy": {
                "Male": {
                    "full_firstnames": HUMAN_MALE_FANTASY_NAMES,
                    "generate_firstname": {},
                }, "Female": {
                    "full_firstnames": HUMAN_FEMALE_FANTASY_NAMES,
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": HUMAN_FANTASY_SURNAMES,
                    "generate_surname": {

                    }
                }
            },
            "Sci-Fi": {
                "Male": {
                    "full_firstnames": ["HuSciM"],
                    "generate_firstname": {},
                },
                "Female": {
                    "full_firstnames": ["HuSciF"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            },
            "Modern": {
                "Male": {
                    "full_firstnames": ["HuModM"],
                    "generate_firstname": {},
                },
                "Female": {
                    "full_firstnames": ["HuModF"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            }
        },
        "Elf": {
            "Fantasy": {
                "Male": {
                    "full_firstnames": ["ElFaM"],
                    "generate_firstname": {},
                },
                "Female": {
                    "full_firstnames": ["ElFaf"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            }
        },
        "Dwarf": {
            "Fantasy": {
                "Male": {
                    "full_firstnames": ["DwaFaM"],
                    "generate_firstname": {},
                },
                "Female": {
                    "full_firstnames": ["DwaFaF"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            }
        },
        "Android": {
            "Sci-Fi": {
                "N/A": {
                    "full_firstnames": ["S4TURN"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            }
        },
        "Cyborg": {
            "Sci-Fi": {
                "Male": {
                    "full_firstnames": ["CySciM"],
                    "generate_firstname": {},
                },
                "Female": {
                    "full_firstnames": ["CySciF"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            }
        },
        "Alien": {
            "Sci-Fi": {
                "Male": {
                    "full_firstnames": ["AliSciM"],
                    "generate_firstname": {},
                },
                "Female": {
                    "full_firstnames": ["AliSciF"],
                    "generate_firstname": {},
                },
                "N/A": {
                    "full_firstnames": ["AliSciN/A"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["Sur"],
                    "generate_surname": {}
                }
            }
        },
        "Old One": {
            "Fantasy": {
                "N/A": {
                    "full_firstnames": ["Old"],
                    "generate_firstname": {},
                },
                "Surnames": {
                    "full_surnames": ["One"],
                    "generate_surname": {}
                }
            }
        }
    },
    "race_data": {
        "Human": {
            "stat bonuses": {
                "strength": 1,
                "dexterity": 1,
                "constitution": 1,
                "intelligence": 1,
                "wisdom": 1,
                "charisma": 1
            }
        },
        "Elf": {
            "stat bonuses": {
                "strength": 0,
                "dexterity": 2,
                "constitution": 0,
                "intelligence": 0,
                "wisdom": 0,
                "charisma": 0
            }
        },
        "Dwarf": {
            "stat bonuses": {
                "strength": 0,
                "dexterity": 0,
                "constitution": 2,
                "intelligence": 0,
                "wisdom": 0,
                "charisma": 0
            }
        },
        "Android": {
            "stat bonuses": {
                "strength": 0,
                "dexterity": 0,
                "constitution": 0,
                "intelligence": 0,
                "wisdom": 0,
                "charisma": 0
            }
        },
        "Cyborg": {
            "stat bonuses": {
                "strength": 0,
                "dexterity": 0,
                "constitution": 0,
                "intelligence": 0,
                "wisdom": 0,
                "charisma": 0
            }
        },
        "Alien": {
            "stat bonuses": {
                "strength": 0,
                "dexterity": 0,
                "constitution": 0,
                "intelligence": 0,
                "wisdom": 0,
                "charisma": 0
            }
        },
        "Old One": {
            "stat bonuses": {
                "strength": 0,
                "dexterity": 0,
                "constitution": 0,
                "intelligence": 0,
                "wisdom": 0,
                "charisma": 0
            }
        },
    },
    "class_data": {
        "Artificer": {
            "main stat": ["intelligence"],
            "secondary stats": ["dexterity", "constitution"],
            "dump stats": ["wisdom", "charisma", "strength"],
            "cantrips limit": 2,
            "class cantrips": [
                {
                    "Name": "Acid Splash",
                    "School": "Conjuration",
                    "Stats": {"Casting time": "1 Action", "Range": "60ft", "Duration": "Instantaneous",
                              "Components": ["V", "S"]},
                },
                {
                    "Name": "Booming Blade",
                    "School": "Evocation",
                    "Stats": {"Casting time": "1 Action", "Range": "Self (5-foot radius)", "Duration": "1 Round",
                              "Components": ["S", "M"]},
                },
                {
                    "Name": "",
                    "School": "",
                    "Stats": {"Casting time": "", "Range": "", "Duration": "",
                              "Components": []},
                }
            ],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Magical Tinkering": "",
                    "Spellcasting": ""
                }
            }
        },
        "Barbarian": {
            "main stat": ["strength"],
            "secondary stats": ["dexterity", "constitution"],
            "dump stats": ["wisdom", "charisma", "intelligence"],
            "cantrips limit": 0,
            "class cantrips": [],
            "class data": {
                "hit dice": 12,
                "features": {
                    "Rage": "",
                    "Unarmored Defense": ""
                }
            }
        },
        "Bard": {
            "main stat": ["charisma"],
            "secondary stats": ["dexterity", "constitution"],
            "dump stats": ["strength", "wisdom", "intelligence"],
            "cantrips limit": 2,
            "class cantrips": [],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Spellcasting": "",
                    "Bardic Inspiration": ""
                }
            }
        },
        "Cleric": {
            "main stat": ["wisdom"],
            "secondary stats": ["constitution", "strength"],
            "dump stats": ["intelligence", "dexterity", "charisma"],
            "cantrips limit": 3,
            "class cantrips": [],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Spellcasting": "",
                    "Divine Domain": ""
                }
            }
        },
        "Druid": {
            "main stat": ["wisdom"],
            "secondary stats": ["dexterity", "constitution"],
            "dump stats": ["intelligence", "charisma", "strength"],
            "cantrips limit": 2,
            "class cantrips": [],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Druidic": "",
                    "Spellcasting": ""
                }
            }
        },
        "Fighter": {
            "main stat pooling": ["strength", "dexterity"],
            "main stat": [],
            "secondary stats": ["constitution"],
            "dump stats": ["intelligence", "wisdom", "charisma"],
            "cantrips limit": 0,
            "class cantrips": [],
            "class data": {
                "hit dice": 10,
                "features": {
                    "Fighting Style": "",
                    "Second Wind": ""
                }
            }
        },
        "Monk": {
            "main stat pooling": ["dexterity", "wisdom"],
            "main stat": [],
            "secondary stats": ["constitution"],
            "dump stats": ["intelligence", "strength", "charisma"],
            "cantrips limit": 0,
            "class cantrips": [],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Unarmored Defense": "",
                    "Martial Arts": ""
                }
            }
        },
        "Paladin": {
            "main stat": ["charisma", "strength"],
            "secondary stats pooling": ["wisdom", "dexterity"],
            "secondary stats": ["constitution"],
            "dump stats": ["intelligence"],
            "cantrips limit": 0,
            "class cantrips": [],
            "class data": {
                "hit dice": 10,
                "features": {
                    "Divine Sense": "",
                    "Lay on Hands": ""
                }
            }
        },
        "Ranger": {
            "main stat": ["dexterity"],
            "secondary stats": ["wisdom", "constitution"],
            "dump stats": ["intelligence", "charisma", "strength"],
            "cantrips limit": 0,
            "class cantrips": [],
            "class data": {
                "hit dice": 10,
                "features": {
                    "Favored Enemy": "",
                    "Natural Explorer": ""
                }
            }
        },
        "Rogue": {
            "main stat": ["dexterity"],
            "secondary stats": ["constitution"],
            "dump stats": ["intelligence", "charisma", "strength", "wisdom"],
            "cantrips limit": 0,
            "class cantrips": [],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Expertise": "",
                    "Sneak Attack": "",
                    "Thieves’ Cant": ""
                }
            }
        },
        "Sorcerer": {
            "main stat": ["charisma"],
            "secondary stats": ["constitution", "dexterity"],
            "dump stats": ["intelligence", "strength", "wisdom"],
            "cantrips limit": 4,
            "class cantrips": [],
            "class data": {
                "hit dice": 6,
                "features": {
                    "Spellcasting": "",
                    "Sorcerous Origin": ""
                }
            }
        },
        "Warlock": {
            "main stat": ["charisma"],
            "secondary stats": ["constitution", "dexterity"],
            "dump stats": ["intelligence", "strength", "wisdom"],
            "cantrips limit": 2,
            "class cantrips": [],
            "class data": {
                "hit dice": 8,
                "features": {
                    "Otherworldly Patron": "",
                    "Pact Magic": ""
                }
            }
        },
        "Wizard": {
            "main stat": ["intelligence"],
            "secondary stats": ["constitution", "dexterity"],
            "dump stats": ["charisma", "strength", "wisdom"],
            "cantrips limit": 3,
            "class cantrips": [],
            "class data": {
                "hit dice": 6,
                "features": {
                    "Spellcasting": "",
                    "Arcane Recovery": ""
                }
            }
        }
    },
    "alignment_data": {
        "order": ["Lawful", "Neutral", "Chaotic"],
        "morality": ["Good", "Neutral", "Evil"]
    },
    "trait_data": {
        "ego": {
            "high": {
                "Arrogant": "Has an exaggerated sense of their importance and/or abilities.",
                "Self-assured": "Confident in their own abilities and/or character.",
                "Bold": "Willing to take risks while being confident and courageous.",
                "Overconfident": "Is unjustifiably confident and cocky."
            },
            "medium": {
                "Humble": "Confident in their abilities but avoids boasting or taking credit for shared success.",
                "Balanced": "Isn't over or under confident.",
                "Modest": "Unassuming in the estimation of their abilities and/or achievements.",
                "Realistic": "Takes things as they come knowing they can only do whats within their ability range."
            },
            "low": {
                "Insecure": "Uncertain and/or anxious about themself and their abilities.",
                "Timid": "Lacks courage and/or confidence and is easily scared.",
                "Self-doubting": "Questions their ability to do anything of value.",
                "Submissive": "Folds to the will and whims of others easily even doing stuff they don't want to."
            },
        },
        "temperament": {
            "positive": {
                "Jovial": "Consistently cheerful, friendly, and good-humored, regardless of minor setbacks.",
                "Sanguine": "Optimistic and enthusiastic; treats every situation, even negative ones, as an "
                            "opportunity or adventure.",
                "Ebullient": "Characterized by high enthusiasm, exuberance, and bubbling energy."
            },
            "neutral": {
                "Phlegmatic": "Calm, slow to anger, and generally placid; maintains an even emotional keel under "
                              "pressure.",
                "Stoic": "Endures pain, hardship, or emotional distress without showing feelings or complaining.",
                "Mellow": "Relaxed, easygoing, and agreeable; rarely becomes anxious or highly motivated."
            },
            "negative": {
                "Volatile": "Prone to sudden, unpredictable, and intense emotional changes or outbursts.",
                "Irascible": "Easily provoked to anger or irritability; has a quick temper.",
                "Melancholy": "Pensive, reflective, and prone to thoughtful sadness or a state of quiet depression."
            }
        }
    }
}


def set_valid_name_data_keys():
    gender_to_race = {}
    gender_to_genre = {}
    genre_to_race = {}
    genre_to_gender = {}
    race_to_genre = {}
    race_to_gender = {}
    for race in GENERATION_DATA["name_data"]:
        race_to_genre[race] = list(GENERATION_DATA["name_data"][race].keys())
        if race not in race_to_gender.keys():
            race_to_gender[race] = set()
        for genre in GENERATION_DATA["name_data"][race]:
            if genre not in genre_to_race.keys():
                genre_to_race[genre] = set()
            if genre not in genre_to_gender.keys():
                genre_to_gender[genre] = set()
            genre_to_race[genre].add(race)
            for gender in GENERATION_DATA["name_data"][race][genre]:
                if gender == "Surnames":
                    continue
                genre_to_gender[genre].add(gender)
                if gender not in gender_to_genre.keys():
                    gender_to_genre[gender] = set()
                gender_to_genre[gender].add(genre)
                if gender not in gender_to_race.keys():
                    gender_to_race[gender] = set()
                gender_to_race[gender].add(race)
                race_to_gender[race].add(gender)
    for gender in gender_to_race:
        gender_to_race[gender] = list(gender_to_race[gender])
    for gender in gender_to_genre:
        gender_to_genre[gender] = list(gender_to_genre[gender])
    for genre in genre_to_race:
        genre_to_race[genre] = list(genre_to_race[genre])
    for genre in genre_to_gender:
        genre_to_gender[genre] = list(genre_to_gender[genre])
    for race in race_to_gender:
        race_to_gender[race] = list(race_to_gender[race])
    GENERATION_DATA["validation_data"]["name_data"]["gender_to_race"] = gender_to_race
    GENERATION_DATA["validation_data"]["name_data"]["gender_to_genre"] = gender_to_genre
    GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"] = genre_to_race
    GENERATION_DATA["validation_data"]["name_data"]["genre_to_gender"] = genre_to_gender
    GENERATION_DATA["validation_data"]["name_data"]["race_to_genre"] = race_to_genre
    GENERATION_DATA["validation_data"]["name_data"]["race_to_gender"] = race_to_gender


set_valid_name_data_keys()
