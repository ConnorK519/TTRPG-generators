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
    "class_data": {
        "Artificer": {
            "hit dice": 8,
            "cantrips": 2,
            "features": {
                "Magical Tinkering": "",
                "Spellcasting": ""
            }
        },
        "Barbarian": {
            "hit dice": 12
        },
        "Bard": {
            "hit dice": 8
        },
        "Cleric": {
            "hit dice": 8
        },
        "Druid": {
            "hit dice": 8
        },
        "Fighter": {
            "hit dice": 10
        },
        "Monk": {
            "hit dice": 8
        },
        "Paladin": {
            "hit dice": 10
        },
        "Ranger": {
            "hit dice": 10
        },
        "Rogue": {
            "hit dice": 8
        },
        "Sorcerer": {
            "hit dice": 6
        },
        "Warlock": {
            "hit dice": 8
        },
        "Wizard": {
            "hit dice": 6
        }
    },
    "alignment_data": {
        "order": ["Lawful", "Neutral", "Chaotic"],
        "morality": ["Good", "Neutral", "Evil"]
    },
    "trait_data": {
        "alignment_traits": {
            "order": {
                "Lawful": {
                    "Disciplined": "Follows rules and procedures strictly.",
                    "Methodical": "Approaches tasks in a slow, systematic, and orderly manner.",
                    "Reliable": "Can be trusted to fulfill duties and promises.",
                    "Rigid": "Inflexible in thought or action; adheres strictly to tradition."
                },
                "Chaotic": {
                    "Impulsive": "Acts quickly based on instinct or feeling, ignoring consequences.",
                    "Unpredictable": "Behavior is erratic and difficult to anticipate.",
                    "Spontaneous": "Loves unplanned action and thrives on novelty.",
                    "Turbulent": "Prone to sudden, violent, or intense internal disorder."
                },
                "Neutral": {
                    "Flexible": "Easily adapts to changing circumstances or rules.",
                    "Uncommitted": "Reluctant to take firm sides or bind themselves to a cause.",
                    "Situational": "Decisions are made based on the current context rather than abstract rules.",
                    "Moderate": "Prefers balance and avoids extremes in action or ideology."
                },
            },
            "morality": {
                "Good": {
                    "Pious": "Devoted to the pursuit of moral excellence or divine will.",
                    "Just": "Dedicated to fairness and equality in application of ethics.",
                    "Virtuous": "Possessing high moral standards and righteousness.",
                    "Compassionate": "Always Strives to help the poor, downtrodden or those in need."
                },
                "Evil": {
                    "Ruthless": "Lacking pity or compassion; cruel and uncompromising.",
                    "Vindictive": "Having a strong desire for revenge in the most harsh way possible.",
                    "Egoist": "Focused entirely on self-interest; treats others as means to an end.",
                    "Destructive": "Revels in destruction of the property, home or mental state of others."
                },
                "Neutral": {
                    "Pragmatic": "Deals with things sensibly and realistically, focusing on practical outcomes.",
                    "Observant": "Attentive to surroundings and keen on noticing details.",
                    "Indifferent": "Lacking interest, sympathy, or concern.",
                    "Detached": "Emotionally separated from situations, people, or outcomes."
                }
            },
            "alignment": {
                "Lawful Good": {
                    "Heroic": "Committed absolutely to their highest ideals, they are willing to fight to the death to "
                              "protect the innocent and uphold their sacred code of justice."
                },
                "Neutral Good": {
                    "Moral Calculus": "Willing to break laws and sacrifice a few to achieve the greatest good for the "
                                      "majority with cold calculation of number of lives saved.",
                    "Vigilante": "Committed to delivering justice efficiently; breaks flawed laws and bypasses corrupt "
                                 "institutions when the greatest good demands immediate action."
                },
                "Chaotic Good": {
                    "Martyr to Ideals": "Driven by absolute conviction, they impulsively sacrifice everything, even "
                                        "their life, to uphold their ideals.",
                    "Pure Insanity": "This character upholds absolute good using unhinged, unpredictable and "
                                     "unconventional means."
                },
                "Lawful Neutral": {
                    "Unbending Precedent": "Bound solely by established laws, contracts, or the dictates of their "
                                           "organization. Personal feelings are irrelevant; the code must be upheld, "
                                           "even if unjust.",
                    "The Greater Order": "Dedicated to abstract cosmic order, logic, and efficiency. Views all chaos, "
                                         "regardless of moral alignment, as a threat to long-term stability that must "
                                         "be pruned."
                },
                "True Neutral": {
                    "Primal Balance": "Dedicated to universal equilibrium. Actively intervenes to prevent Good or Evil "
                                      "from becoming dominant, seeing all extremism as a threat to stability.",
                    "Total Apathy": "Possesses profound indifference to mortal affairs, caring only for nature's cycles"
                                    " or abstract observation. Views life and death academically."
                },
                "Chaotic Neutral": {
                    "Maddening Whim": "Driven purely by impulse, self-interest, and amusement. Acts with total "
                                      "disregard for promises or consequences.",
                    "Selective Disregard": "Adheres only to one strange, personal principle (e.g., 'always steal shiny "
                                           "objects'). Breaks all other rules without hesitation."
                },
                "Lawful Evil": {
                    # Needs moving
                    "Veiled Tyrant": "Aims to wields laws, contracts, and wealth like weapons; they commit grave evil, "
                                     "yet remain technically within the letter of the law."
                },
                "Neutral Evil": {
                    # Needs moving
                    "Master Mind": "Tries to wear the mask of other alignments to manipulate people towards "
                                   "their goals."
                },
                "Chaotic Evil": {
                    "Twisted by darkness": "Are their acts guided by a malignant external force, or are they merely "
                                           "the result of deep psychological trauma and a fractured mind?"
                },
            }
        },
        "ego": {
            "high": {
                "Arrogant": "",
                "Self-assured": "",
                "Bold": "",
                "Overconfident": ""
            },
            "medium": {
                "Humble": "",
                "Balanced": "",
                "Modest": "",
                "Realistic": ""
            },
            "low": {
                "Insecure": "",
                "Timid": "",
                "Self-doubting": "",
                "Submissive": ""
            },
        },
        "social": {

        }
    }
}


def set_valid_name_data_keys():
    gender_to_genre = {}
    gender_to_race = {}
    genre_to_race = {}
    for race in GENERATION_DATA["name_data"]:
        for genre in GENERATION_DATA["name_data"][race]:
            if genre not in genre_to_race.keys():
                genre_to_race[genre] = set()
            genre_to_race[genre].add(race)
            for gender in GENERATION_DATA["name_data"][race][genre]:
                if gender == "Surnames":
                    continue
                if gender not in gender_to_genre.keys():
                    gender_to_genre[gender] = set()
                gender_to_genre[gender].add(genre)
                if gender not in gender_to_race.keys():
                    gender_to_race[gender] = set()
                gender_to_race[gender].add(race)
    for gender in gender_to_genre:
        gender_to_genre[gender] = list(gender_to_genre[gender])
    for genre in genre_to_race:
        genre_to_race[genre] = list(genre_to_race[genre])
    for gender in gender_to_race:
        gender_to_race[gender] = list(gender_to_race[gender])
    GENERATION_DATA["validation_data"]["name_data"]["gender_to_genre"] = gender_to_genre
    GENERATION_DATA["validation_data"]["name_data"]["gender_to_race"] = gender_to_race
    GENERATION_DATA["validation_data"]["name_data"]["genre_to_race"] = genre_to_race


set_valid_name_data_keys()
