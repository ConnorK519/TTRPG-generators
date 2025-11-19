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
                "dexterity": 0,
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
                "constitution": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 2,
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
            "class data": {
                "hit dice": 12,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 10,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 10,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 10,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 6,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 8,
                "cantrips": 0,
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
            "class data": {
                "hit dice": 6,
                "cantrips": 0,
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
                    "Merciful": "Shows mercy to their enemies.",
                    "Forgiving": "Tends to forgive any wrongs committed against them fast.",
                    "Virtuous": "Adheres to a strict personal moral code, often prioritizing principle over expediency "
                                "or personal gain.",
                    "Compassionate": "Always Strives to help the poor, downtrodden or those in need."
                },
                "Evil": {
                    "Ruthless": "Lacking pity or compassion; cruel and uncompromising.",
                    "Vindictive": "Having a strong desire for revenge in the most harsh way possible.",
                    "Exploitative": "Sees every other individual purely as a resource to be used and discarded for "
                                    "personal gain.",
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
