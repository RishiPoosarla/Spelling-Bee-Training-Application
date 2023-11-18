import tkinter as tk
from random import shuffle
from gtts import gTTS
from playsound import playsound

# List of words (you can modify this list with your words)
words = [ "abbreviate", "abdicate", "abode",
    "abstraction", "abundant", "abusive",
    "abyss", "accomplice", "accordion",
    "accumulate", "acerbate", "acetone",
    "acme", "acolyte", "acoustic",
    "acquittal", "acumen", "adequacy",
    "adroitness", "advocate", "affidavit",
    "affluent", "aggregate", "agitation",
    "agriculture", "agronomy", "aisle",
    "alabaster", "alkaline", "allay",
    "allegory", "alleviate", "alliance",
    "alligator", "alloy", "alluvium",
    "almanac", "alpinist", "alteration",
    "amateur", "ambrosia", "amiable",
    "analyze", "anarchy", "anchovy",
    "angstroms", "anomaly", "antenna",
    "antics", "antonym", "anxiety",
    "aortic", "appreciate", "arrogance",
    "arsenal", "aspersion", "austere",
    "axiom", "bachelor", "bailiff",
    "basalt", "basilica", "bastion",
    "battalion", "bauble", "bayonet",
    "bayou", "beatific", "bedazzle",
    "behemoth", "beneficence", "beret",
    "berserk", "betrothal", "bevy",
    "bibelot", "bifurcate", "bilious",
    "blatant", "blithe", "blunder",
    "boar", "bogus", "boloney",
    "bolshevism", "bonhomie", "brogan",
    "brouhaha", "buoyant", "bureaucracy",
    "burgundy", "buttress",
    "cachet", "calibrate", "calypso",
    "candor", "caramel", "carbine",
    "careen", "caribou", "caricature",
    "castanets", "cathartic", "cauliflower",
    "chambray", "champagne", "chapeau",
    "charisma", "chateau", "chic",
    "chimera", "chivalry", "choreographer",
    "chromatic", "cicada", "clairvoyance",
    "clavicle", "clemency", "coincidence",
    "collage", "collateral", "colloquial",
    "cologne", "colossal", "comatose",
    "concierge", "confabulate", "confetti",
    "confidence", "conspiracy", "constraint",
    "construe", "consultant", "contagious",
    "contempt", "contour", "contradict",
    "contrary", "contrive", "convoluted",
    "corrupt", "countenance", "covenant",
    "cranium", "crimson", "crotchety",
    "crucible", "cruelty", "crypt",
    "cuckoo", "cyanide", "dazzle",
    "declination", "decrepit", "delirious",
    "delta", "despotism", "deterrent",
    "detonate", "detriment", "dexterous",
    "dichotomy", "diesel", "digit",
    "disintegration", "dismantle", "disquietude",
    "dissident", "distraught", "diversify",
    "dormancy", "dour", "druid",
    "ductile", "dungeon", "duplicate",
    "duress", "elocution", "elysian",
    "emancipation", "embassy", "embellish",
    "embodiment", "embryonic", "emollient",
    "emphasis", "emphatic", "emporium",
    "emulate", "enamel", "endorse",
    "enmity", "enthusiasm", "enumerate",
    "environment", "epidermis", "equanimity",
    "equestrian", "equivocation", "erratic",
    "espionage", "ethnic", "euphoric",
    "exaggerate", "exhilarated", "exhume",
    "exigent", "exodus", "exotic",
    "expatriate", "expertise", "expatiate",
    "explicit", "exponential", "extinguish",
    "extortion", "extraneous", "fabricate",
    "facile", "factitious", "falderal",
    "fallacy", "feasible", "fedora",
    "felicitation", "femur", "ferocity",
    "festoon", "fidelity", "filament",
    "filibuster", "finesse", "flagrant",
    "flourish", "fluctuate", "fluid",
    "flummery", "foppish", "forfeit",
    "formulation", "forte", "fractious",
    "fragility", "franchise", "fraternize",
    "friar", "frivolous", "frugal",
    "fumigate", "galaxy", "galleon",
    "garlic", "garrison", "garrote",
    "gauche", "gendarme", "germane",
    "ghastly", "gladiator", "globule",
    "googol", "gossamer", "gradient",
    "graffiti", "gratitude", "gravitate",
    "grievance", "guarantee", "hacienda",
    "halcyon", "harbinger", "haughtily",
    "heifer", "heirloom", "hemisphere",
    "hermit", "hilarity", "homburg",
    "hooligan", "horde", "howitzer",
    "huckleberry", "humorous", "hurricane",
    "hyphenate", "hysterical", "icicle",
    "igneous", "ignominy", "immaculate",
    "impasse", "impassive", "impenetrable",
    "impertinent", "impromptu", "impropriety",
    "improvisational", "impulse", "inaugural",
    "incendiary", "incisiveness", "incoherent",
    "incongruous", "incredulous", "indelible",
    "indigent", "indivisible", "indolent",
    "indulgent", "inept", "infatuation",
    "infectious", "innate", "inorganic",
    "interference", "interrogate", "intimidate",
    "intrepid", "jaundice", "jeopardy",
    "jettison", "jocund", "jostle",
    "jubilant", "kerosene", "kinesiology",
    "knavery", "kudos", "lambaste",
    "languid", "lantern", "larceny",
    "largesse", "lassitude", "league",
    "legume", "lightning", "liturgy",
    "loafer", "loathe", "lobster",
    "localize", "lubricate", "lucrative",
    "lummox", "luster", "macabre",
    "magenta", "magisterial", "malediction",
    "malicious", "malleable", "mandible",
    "manganese", "mantilla", "marathon",
    "marionette", "marzipan", "massacre",
    "masticate", "mauve", "mediocre",
    "melancholy", "melanoma", "meliorate",
    "metamorphosis", "migratory", "mimeograph",
    "mimic", "miscellaneous", "misconception",
    "miserable", "mitigate", "monotonous",
    "multiplier", "nectar", "negativism",
    "negligence", "nettlesome", "neurologist",
    "nocuous", "nomad", "nomenclature",
    "nonchalant", "notorious", "nourishment",
    "nullify", "oblivion", "occupancy",
    "occurrence", "ocelot", "odious",
    "odometer", "officious", "ointment",
    "oligarchy", "onus", "optimistic",
    "oscillation", "ostrich", "outrageous",
    "oxidize", "oxymoron", "pachyderm",
    "palaver", "palfrey", "palooka",
    "panache", "paprika", "paralyze",
    "parenthesis", "pastry", "pathetic",
    "patrician", "patriotism", "pavilion",
    "peccadillo", "pecuniary", "pedigree",
    "peculate", "pellucid", "peninsula",
    "penury", "perceptible", "perennial",
    "perilous", "perpetrator", "perplex",
    "pertinence", "peruse", "pessimistic",
    "pheasant", "piteous", "placard",
    "placid", "plateau", "platitude",
    "plausible", "plebeian", "plenitude",
    "pliancy", "plutonic", "pneumatic",
    "podiatrist", "poignant", "poltroon",
    "polymer", "pomegranate", "pomposity",
    "porcelain", "portentous", "posthumous",
    "postulate", "pragmatic", "praline",
    "precipitation", "predator", "predecessor",
    "predicament", "predilection", "premonition",
    "primitive", "privy", "procrastinate",
    "procurement", "prodigal", "progeny",
    "prognosis", "prologue", "promontory",
    "prompt", "pronouncement", "propaganda",
    "propolis", "prosaic", "protoplasm",
    "psyche", "pugilist", "pullet",
    "pulpit", "pursuit", "purulence",
    "purveyor", "queasy", "quench",
    "querulous", "quintet", "quintuplet",
    "quorum", "raiment", "rampant",
    "ramshackle", "raspberry", "reassurance",
    "receptacle", "rectitude", "redolent",
    "regalia", "regurgitate", "remnant",
    "renegade", "repatriate", "repertoire",
    "reprisal", "reprobate", "requiem",
    "residue", "resonance", "restitution",
    "reticence", "retrieval", "rhetoric",
    "rheumatic", "rhizome", "rhythm",
    "ridiculous", "rigorous", "risotto",
    "sabotage", "sacrifice", "satirical",
    "sayonara", "scaffold", "scald",
    "sciatica", "scrawny", "selenium",
    "sentry", "sepia", "serviceable",
    "shrapnel", "shrewd", "siege",
    "simulate", "sinew", "singular",
    "sirloin", "skirmish", "sojourn",
    "solemn", "sorcerer", "souvenir",
    "spasmodic", "spatula", "spigot",
    "sporadic", "squalid", "stagnant",
    "stalwart", "stenography", "stevedore",
    "strafe", "strategy", "stratocumulus",
    "strictly", "stroganoff", "sublimation",
    "subservience", "subsidiary", "sumo",
    "superstition", "suspensory", "suspiciously",
    "syndrome", "tabernacle", "talisman",
    "tarantula", "tenacious", "testimony",
    "theatrical", "therapeutic", "thievery",
    "threshold", "timbre", "timorous",
    "topaz", "tragedy", "tranquilizer",
    "transparent", "treacherous", "trepidation",
    "triceratops", "trough", "turban",
    "turbulence", "turret", "tutelage",
    "typhoid", "ulcerated", "ullage",
    "ultimatum", "ululate", "umbrage",
    "upholstery", "urbane", "urgency",
    "usurer", "usurper", "utility",
    "utopian", "valedictory", "vandalism",
    "velocity", "vestibule", "veterans",
    "viable", "vigil", "vindicate",
    "virago", "viscera", "viscous",
    "visualization", "vocalize", "vocation",
    "vogue", "volunteer", "voracity",
    "vortex", "vulgarity", "vulpine",
    "wainscot", "wallop", "waltz",
    "wampum", "weevil", "wheelbarrow",
    "whimsical", "wizardry", "wreckage",
    "wrought", "yearling", "zealot",
    "zeppelin", "zilch", "zodiac",
    "zoologist", "zwieback", "zygote",
    "zymurgy"

]
words2 = ["accommodate", "abstain", "accumulate",
    "accustomed", "acoustics", "acquaintance",
    "acquisition", "acquittal", "adolescence",
    "adolescent", "advantageous", "aerial",
    "amateur", "amnesty", "anecdote",
    "annoyance", "anonymous", "antecedent",
    "antidote", "antiseptic", "anxious",
    "apology", "apostrophe", "appendixes",
    "applicant", "approximate", "archaic",
    "architect", "arrangement", "asphalt",
    "asterisk", "asthma", "awkward",
    "bachelor", "bankruptcy", "barometer",
    "belligerent", "berserk", "besieged",
    "biannual", "bimonthly", "biographical",
    "brilliance", "budge", "burglary",
    "cameos", "capably", "caricature",
    "catastrophe", "chameleon", "chandelier",
    "characteristic", "chauffeur", "chrysanthemum",
    "circumference", "collaborate", "collateral",
    "colleague", "colonel", "confiscate",
    "confiscation", "conscious", "consequence",
    "considerable", "contagious", "controversy",
    "continuous", "correlation", "council",
    "counsel", "criticism", "criticize",
    "critique", "crypt", "cylinder",
    "deficiency", "desirable", "desolate",
    "deterrent", "diagnosis", "dialogue",
    "dilemma", "disbursement", "discernible",
    "discrepancy", "dominance", "embargo",
    "endeavor", "envious", "epidemic",
    "equilibrium", "erroneous", "escalator",
    "excessive", "existence", "extremity",
    "extricate", "façade", "fashionable",
    "fiasco", "fibrous", "fiery",
    "flamboyant", "forgery", "frivolous",
    "frostbitten", "glamorous", "gorgeous",
    "grotesque", "gymnasium", "haphazard",
    "hazardous", "headquarters", "honorary",
    "horrific", "hospitality", "incidentally",
    "inconvenience", "indulgence", "inept",
    "inevitable", "innumerable", "insistent",
    "insufficient", "integrity", "intermittent",
    "internally", "interrogate", "jewelry",
    "legitimate", "leisure", "lieutenant",
    "longevity", "lucrative", "lunar",
    "luncheon", "luxurious", "malady",
    "malicious", "malignant", "melodious",
    "mercenary", "mesmerize", "meteor",
    "meticulous", "metropolitan", "minimize",
    "miscellaneous", "mischievous", "misdemeanor",
    "Ezoic",
    "necessity", "negligence", "neutral",
    "newsstand", "nostalgia", "noticeable",
    "obesity", "obscure", "obsolete",
    "obstinate", "occurred", "ominous",
    "optimism", "optimistic", "outrageous",
    "pageant", "parachute", "paralysis",
    "parliament", "penitentiary", "perceive",
    "permeate", "perseverance", "personality",
    "personification", "persuade", "phenomenon",
    "plaintiff", "pneumonia", "politician",
    "potential", "precipice", "precocious",
    "predecessor", "preferably", "prestigious",
    "procrastinate", "propeller", "prosperous",
    "protein", "pseudonym", "psychiatrist",
    "questionnaire", "radioactive", "rampage",
    "recurrent", "rehearsal", "relevant",
    "religious", "roommate", "sacrifice",
    "sacrificial", "sanctuary", "scandalized",
    "schedule", "scheme", "schism",
    "scholar", "semester", "serviceable",
    "shrine", "shuddering", "sieve",
    "snobbery", "solitary", "sophomore",
    "studious", "subtlety", "suburban",
    "surmise", "susceptible", "suspicious",
    "taboo", "technically", "technology",
    "tyranny", "unacceptable", "unconscious",
    "undernourished", "unduly", "unenforceable",
    "unique", "universal", "unpredictable",
    "unsanitary", "utopia", "vaccinate",
    "vacillate", "venom", "vertigo",
    "vessel", "vigilant", "villain",
    "vitamin", "vivacious", "vocalize",
    "voracious", "voucher", "vulnerable",
    "withhold"]
incorrect_words2 = ["purulence", "aggregate", "emollient", "sporadic", "propolis", "elysian", "decrepit", "indolent", "pellucid"]
incorrect_words3 = ["chauffeur", "melodious", "belligerent", "precipice", "conscious", "burglary", 
    "glamorous", "deficiency", "discernible", "adolescence", "withhold", "disbursement", 
    "malady", "precocious", "amnesty", "advantageous", "abstain", "susceptible", 
    "accommodate", "mischievous", "perseverance", "antecedent", "unacceptable", 
    "lieutenant", "protein", "schism", "counsel", "extricate", "penitentiary", 
    "sieve", "vacillate", "bankruptcy", "obstinate", "acquaintance", "questionnaire", 
    "erroneous", "discrepancy", "innumerable"]
# Shuffle the list of words to randomize the order
shuffle(words)
shuffle(words2)
shuffle(words3)
shuffle(incorrect_words)
shuffle(incorrect_words2)
shuffle(incorrect_words3)
# Count of the number of words done in the session
count = 0

def get_random_word(event=None):
    if words:
        word = words.pop()
        app.word_to_display = word  # Store the word in the app object
    else:
        app.word_to_display = "No words left"

def read_aloud(event=None):
    if hasattr(app, 'word_to_display'):
        word = app.word_to_display
        if word != "No words left":
            tts = gTTS(text=word, lang='en')
            tts.save("word.mp3")
            playsound("word.mp3")

def display_word(event=None):
    global count
    if hasattr(app, 'word_to_display'):
        word_label.config(text=app.word_to_display)
    count += 1
    empty_label.config(text=str(count))

app = tk.Tk()
app.title("Spelling Bee Training App")
app.word_to_display = None  # Initialize the word storage

# Create the label in the middle
label = tk.Label(app, text="", font=("Helvetica", 24))
label.pack(pady=20)

# Create the "Get Word" button
get_word_button = tk.Button(app, text="Get Word", command=get_random_word)
get_word_button.pack()

# Create the "Read Aloud" button
read_aloud_button = tk.Button(app, text="Read Aloud", command=read_aloud)
read_aloud_button.pack()

# Create the "Finished" button
finished_button = tk.Button(app, text="Finished", command=display_word)
finished_button.pack()

# Create a label to display the word when the "Finished" button is clicked
word_label = tk.Label(app, text="", font=("Helvetica", 24))
word_label.pack(pady=20)

# Create an empty label on the middle-right
empty_label = tk.Label(app, text="", font=("Helvetica", 24))
empty_label.pack(side=tk.RIGHT)

# Bind keys to functions
app.bind("<space>", get_random_word)  # Spacebar for "Get Word"
app.bind("<m>", read_aloud)  # Letter 'm' for "Read Aloud"
app.bind("<n>", display_word)  # Letter 'n' for "Finished"

app.mainloop()
