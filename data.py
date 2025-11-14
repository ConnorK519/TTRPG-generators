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
            "hit dice": 12,
            "cantrips": 0,
            "features": {
                "Rage": "",
                "Unarmored Defense": ""
            }
        },
        "Bard": {
            "hit dice": 8,
            "cantrips": 0,
            "features": {
                "Spellcasting": "",
                "Bardic Inspiration": ""
            }
        },
        "Cleric": {
            "hit dice": 8,
            "cantrips": 0,
            "features": {
                "Spellcasting": "",
                "Divine Domain": ""
            }
        },
        "Druid": {
            "hit dice": 8,
            "cantrips": 0,
            "features": {
                "Druidic": "",
                "Spellcasting": ""
            }
        },
        "Fighter": {
            "hit dice": 10,
            "cantrips": 0,
            "features": {
                "Fighting Style": "",
                "Second Wind": ""
            }
        },
        "Monk": {
            "hit dice": 8,
            "cantrips": 0,
            "features": {
                "Unarmored Defense": "",
                "Martial Arts": ""
            }
        },
        "Paladin": {
            "hit dice": 10,
            "cantrips": 0,
            "features": {
                "Divine Sense": "",
                "Lay on Hands": ""
            }
        },
        "Ranger": {
            "hit dice": 10,
            "cantrips": 0,
            "features": {
                "Favored Enemy": "",
                "Natural Explorer": ""
            }
        },
        "Rogue": {
            "hit dice": 8,
            "cantrips": 0,
            "features": {
                "Expertise": "",
                "Sneak Attack": "",
                "Thieves’ Cant": ""
            }
        },
        "Sorcerer": {
            "hit dice": 6,
            "cantrips": 0,
            "features": {
                "Spellcasting": "",
                "Sorcerous Origin": ""
            }
        },
        "Warlock": {
            "hit dice": 8,
            "cantrips": 0,
            "features": {
                "Otherworldly Patron": "",
                "Pact Magic": ""
            }
        },
        "Wizard": {
            "hit dice": 6,
            "cantrips": 0,
            "features": {
                "Spellcasting": "",
                "Arcane Recovery": ""
            }
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
                    "Grim Utility": "Will reluctantly abandon procedure to secure the greatest good, choosing the path "
                                    "that saves the most lives.",
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
                                           "objects'). Breaks all other rules without hesitation.",
                    "Sovereign Ego": "Prioritizes total personal autonomy; acts purely by their own will and reacts "
                                     "aggressively to any perceived threat."
                },
                "Lawful Evil": {
                    "Masked Devil": "Stays within the confines of the law committing evils where they can get away "
                                    "with it."
                },
                "Neutral Evil": {
                    "Calculating Shadow": "Hides the evil they commit with a balanced, flexible and adaptable mind."
                },
                "Chaotic Evil": {
                    "Twisted by darkness": "Are their acts guided by a malignant external force, or are they merely "
                                           "the result of deep psychological trauma and a fractured mind?",
                    "Chaos Incarnate": "They leave a trail of chaos and corpses of people who displease them "
                                       "wherever they go."
                },
            }
        },
        "ego": {
            "high": {
                "Arrogant": "Has an an exaggerated sense of their importance and/or abilities.",
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
