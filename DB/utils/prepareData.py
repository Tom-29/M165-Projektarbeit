from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true')
db = client['FestivalTracker']

artists = [
    {"name": "Playboi Carti", "country": "US", "genre": "hip hop", "birthdate": "1996-09-13"},
    {"name": "Kris Kross", "country": "US", "genre": "hip hop"},
    {"name": "Billie Eilish", "country": "US", "genre": "pop", "birthdate": "2001-12-18"},
    {"name": "Arctic Monkeys", "country": "UK", "genre": "indie rock"},
    {"name": "Kendrick Lamar", "country": "US", "genre": "rap", "birthdate": "1987-06-17"},
    {"name": "Taylor Swift", "country": "US", "genre": "pop", "birthdate": "1989-12-13"},
    {"name": "Eminem", "country": "US", "genre": "rap", "birthdate": "1972-10-17"},
    {"name": "Beyoncé", "country": "US", "genre": "pop", "birthdate": "1981-09-04"},
    {"name": "Ed Sheeran", "country": "UK", "genre": "pop", "birthdate": "1991-02-17"},
    {"name": "Coldplay", "country": "UK", "genre": "pop"},
    {"name": "Drake", "country": "US", "genre": "rap", "birthdate": "1986-10-24"},
    {"name": "Ariana Grande", "country": "US", "genre": "pop", "birthdate": "1993-06-26"},
    {"name": "The Weeknd", "country": "Canada", "genre": "r&b", "birthdate": "1990-02-16"},
    {"name": "Post Malone", "country": "US", "genre": "hip hop", "birthdate": "1995-07-04"},
    {"name": "Bruno Mars", "country": "US", "genre": "pop", "birthdate": "1985-10-08"},
    {"name": "Rihanna", "country": "Barbados", "genre": "pop", "birthdate": "1988-02-20"},
    {"name": "Queen", "country": "UK", "genre": "rock"},
    {"name": "Justin Bieber", "country": "Canada", "genre": "pop", "birthdate": "1994-03-01"},
    {"name": "Sia", "country": "Australia", "genre": "pop"},
    {"name": "Foo Fighters", "country": "US", "genre": "rock"},
    {"name": "Dr. Dre", "country": "US", "genre": "rap"},
    {"name": "Metallica", "country": "US", "genre": "rock"},
    {"name": "Madonna", "country": "US", "genre": "pop"},
    {"name": "David Guetta", "country": "France", "genre": "electronic"},
    {"name": "Red Hot Chili Peppers", "country": "US", "genre": "rock"},
    {"name": "Lil Wayne", "country": "US", "genre": "rap"},
    {"name": "Nicki Minaj", "country": "Trinidad and Tobago", "genre": "hip hop"},
    {"name": "Jay-Z", "country": "US", "genre": "rap"},
    {"name": "Lady Gaga", "country": "US", "genre": "pop"},
    {"name": "Adele", "country": "UK", "genre": "pop"},
    {"name": "Bob Dylan", "country": "US", "genre": "rock"},
]

artists_collection = db['Artists']
artists_result = artists_collection.insert_many(artists)
print(f"Erfolgreich {len(artists_result.inserted_ids)} Künstler eingefügt")

festivals = [
    {
        "name": "Openair Frauenfeld",
        "country": "CH",
        "genre": "hip hop",
        "date": {"start": "2024-06-11", "end": "2024-06-13"},
        "prices": [
            {"name": "Three day", "price": 302},
            {"name": "Three day plus", "price": 330}
        ],
        "ratings": [
            {"stars": 4.5, "username": "schliingel1234_", "comment": "Tolle Atmosphäre"},
            {"stars": 5, "username": "musiclover123"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[0], "day": "2024-06-11"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-06-12"},
            {"artistId": artists_result.inserted_ids[2], "day": "2024-06-13"},
            {"artistId": artists_result.inserted_ids[3], "day": "2024-06-11"},
            {"artistId": artists_result.inserted_ids[4], "day": "2024-06-12"}
        ]
    },
    {
        "name": "Coachella Valley Music and Arts Festival",
        "country": "US",
        "genre": "mixed",
        "date": {"start": "2024-04-12", "end": "2024-04-21"},
        "prices": [
            {"name": "General Admission", "price": 429},
            {"name": "VIP", "price": 999}
        ],
        "ratings": [
            {"stars": 4.8, "username": "musiclover88", "comment": "Bestes Festival aller Zeiten"},
            {"stars": 4.7, "username": "festivaljunkie"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[5], "day": "2024-04-12"},
            {"artistId": artists_result.inserted_ids[6], "day": "2024-04-13"},
            {"artistId": artists_result.inserted_ids[7], "day": "2024-04-14"},
            {"artistId": artists_result.inserted_ids[8], "day": "2024-04-15"},
            {"artistId": artists_result.inserted_ids[9], "day": "2024-04-16"},
            {"artistId": artists_result.inserted_ids[0], "day": "2024-04-17"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-04-18"}
        ]
    },
    {
        "name": "Glastonbury Festival",
        "country": "UK",
        "genre": "mixed",
        "date": {"start": "2024-06-26", "end": "2024-06-30"},
        "prices": [
            {"name": "Standard", "price": 265},
            {"name": "Campervan", "price": 130}
        ],
        "ratings": [
            {"stars": 4.8, "username": "festivalfanatic"},
            {"stars": 4.7, "username": "musiclover", "comment": "Fantastische Stimmung"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[10], "day": "2024-06-26"},
            {"artistId": artists_result.inserted_ids[11], "day": "2024-06-27"},
            {"artistId": artists_result.inserted_ids[12], "day": "2024-06-28"},
            {"artistId": artists_result.inserted_ids[13], "day": "2024-06-29"},
            {"artistId": artists_result.inserted_ids[14], "day": "2024-06-30"},
            {"artistId": artists_result.inserted_ids[0], "day": "2024-06-27"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-06-28"}
        ]
    },
    {
        "name": "Primavera Sound",
        "country": "ES",
        "genre": "mixed",
        "date": {"start": "2024-05-29", "end": "2024-06-02"},
        "prices": [
            {"name": "Standard Ticket", "price": 250},
            {"name": "VIP Ticket", "price": 500},
            {"name": "Weekend Pass", "price": 350}
        ],
        "ratings": [
            {"stars": 4.6, "username": "musicfanatic", "comment": "Tolle Auswahl an Künstlern"},
            {"stars": 4.9, "username": "livemusiclover", "comment": "Unvergessliche Erfahrung"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[15], "day": "2024-05-29"},
            {"artistId": artists_result.inserted_ids[16], "day": "2024-05-30"},
            {"artistId": artists_result.inserted_ids[17], "day": "2024-05-31"},
            {"artistId": artists_result.inserted_ids[18], "day": "2024-06-01"},
            {"artistId": artists_result.inserted_ids[19], "day": "2024-06-02"},
            {"artistId": artists_result.inserted_ids[0], "day": "2024-05-30"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-05-31"}
        ]
    },
    {
        "name": "Roskilde Festival",
        "country": "DK",
        "genre": "mixed",
        "date": {"start": "2024-07-03", "end": "2024-07-10"},
        "prices": [
            {"name": "Full Festival Ticket", "price": 320},
            {"name": "One Day Ticket", "price": 80},
            {"name": "Camping Ticket", "price": 50}
        ],
        "ratings": [
            {"stars": 4.7, "username": "festivalgoer", "comment": "Tolle Atmosphäre und vielfältige Musik"},
            {"stars": 4.5, "username": "musicloverDK", "comment": "Fantastische Erfahrung"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[20], "day": "2024-07-03"},
            {"artistId": artists_result.inserted_ids[21], "day": "2024-07-04"},
            {"artistId": artists_result.inserted_ids[22], "day": "2024-07-05"},
            {"artistId": artists_result.inserted_ids[8], "day": "2024-07-06"},
            {"artistId": artists_result.inserted_ids[6], "day": "2024-07-07"},
            {"artistId": artists_result.inserted_ids[0], "day": "2024-07-04"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-07-05"}
        ]
    },
    {
        "name": "Tomorrowland",
        "country": "BE",
        "genre": "electronic",
        "date": {"start": "2024-07-19", "end": "2024-07-21"},
        "prices": [
            {"name": "Full Madness Pass", "price": 400},
            {"name": "Comfort Pass", "price": 600},
            {"name": "VIP Pass", "price": 1000}
        ],
        "ratings": [
            {"stars": 4.9, "username": "raver4life", "comment": "Unbelievable atmosphere and lineup!"},
            {"stars": 4.8, "username": "edmlover", "comment": "Best festival experience ever!"},
            {"stars": 4.7, "username": "musicfanatic"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[0], "day": "2024-07-19"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-07-20"},
            {"artistId": artists_result.inserted_ids[2], "day": "2024-07-21"},
            {"artistId": artists_result.inserted_ids[3], "day": "2024-07-19"},
            {"artistId": artists_result.inserted_ids[4], "day": "2024-07-20"}
        ]
    },
    {
        "name": "Ultra Music Festival",
        "country": "US",
        "genre": "electronic",
        "date": {"start": "2024-03-29", "end": "2024-03-31"},
        "prices": [
            {"name": "General Admission", "price": 300},
            {"name": "VIP", "price": 800},
            {"name": "Ultra Experience", "price": 1500}
        ],
        "ratings": [
            {"stars": 4.8, "username": "ultrafanatic", "comment": "Mind-blowing production and energy!"},
            {"stars": 4.6, "username": "edmlife"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[5], "day": "2024-03-29"},
            {"artistId": artists_result.inserted_ids[6], "day": "2024-03-30"},
            {"artistId": artists_result.inserted_ids[7], "day": "2024-03-31"},
            {"artistId": artists_result.inserted_ids[8], "day": "2024-03-29"},
            {"artistId": artists_result.inserted_ids[9], "day": "2024-03-30"}
        ]
    },
    {
        "name": "Reading Festival",
        "country": "UK",
        "genre": "rock",
        "date": {"start": "2024-08-23", "end": "2024-08-25"},
        "prices": [
            {"name": "Weekend Ticket", "price": 250},
            {"name": "VIP Pass", "price": 500},
            {"name": "Camping Pass", "price": 50}
        ],
        "ratings": [
            {"stars": 4.7, "username": "rockfanatic", "comment": "Epic lineup and great vibes!"},
            {"stars": 4.5, "username": "musicloverUK"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[10], "day": "2024-08-23"},
            {"artistId": artists_result.inserted_ids[11], "day": "2024-08-24"},
            {"artistId": artists_result.inserted_ids[12], "day": "2024-08-25"},
            {"artistId": artists_result.inserted_ids[13], "day": "2024-08-23"},
            {"artistId": artists_result.inserted_ids[14], "day": "2024-08-24"}
        ]
    },
    {
        "name": "Sziget Festival",
        "country": "HU",
        "genre": "mixed",
        "date": {"start": "2024-08-07", "end": "2024-08-13"},
        "prices": [
            {"name": "Full Week Pass", "price": 300},
            {"name": "VIP Pass", "price": 700},
            {"name": "Day Pass", "price": 80}
        ],
        "ratings": [
            {"stars": 4.6, "username": "szigetlover", "comment": "Amazing festival experience!"},
            {"stars": 4.7, "username": "musicfanaticHU"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[15], "day": "2024-08-07"},
            {"artistId": artists_result.inserted_ids[16], "day": "2024-08-08"},
            {"artistId": artists_result.inserted_ids[17], "day": "2024-08-09"},
            {"artistId": artists_result.inserted_ids[18], "day": "2024-08-10"},
            {"artistId": artists_result.inserted_ids[19], "day": "2024-08-11"},
            {"artistId": artists_result.inserted_ids[0], "day": "2024-08-08"},
            {"artistId": artists_result.inserted_ids[1], "day": "2024-08-09"}
        ]
    },
    {
        "name": "Electric Daisy Carnival (EDC)",
        "country": "US",
        "genre": "electronic",
        "date": {"start": "2024-05-17", "end": "2024-05-19"},
        "prices": [
            {"name": "GA Ticket", "price": 350},
            {"name": "VIP Pass", "price": 800},
            {"name": "SkyDeck Experience", "price": 2000}
        ],
        "ratings": [
            {"stars": 4.9, "username": "edcfanatic", "comment": "Mind-blowing production and energy!"},
            {"stars": 4.7, "username": "raveking"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[20], "day": "2024-05-17"},
            {"artistId": artists_result.inserted_ids[21], "day": "2024-05-18"},
            {"artistId": artists_result.inserted_ids[22], "day": "2024-05-19"},
            {"artistId": artists_result.inserted_ids[23], "day": "2024-05-17"},
            {"artistId": artists_result.inserted_ids[24], "day": "2024-05-18"}
        ]
    },
    {
        "name": "Electric Zoo",
        "country": "US",
        "genre": "electronic",
        "date": {"start": "2024-08-30", "end": "2024-09-01"},
        "prices": [
            {"name": "3-Day Pass", "price": 350},
            {"name": "VIP Experience", "price": 800},
            {"name": "Platinum Experience", "price": 2000}
        ],
        "ratings": [
            {"stars": 4.8, "username": "zoofanatic", "comment": "Unforgettable experience!"},
            {"stars": 4.6, "username": "edmaddict"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[25], "day": "2024-08-30"},
            {"artistId": artists_result.inserted_ids[26], "day": "2024-08-31"},
            {"artistId": artists_result.inserted_ids[27], "day": "2024-09-01"},
            {"artistId": artists_result.inserted_ids[28], "day": "2024-08-30"},
            {"artistId": artists_result.inserted_ids[29], "day": "2024-08-31"}
        ]
    },
    {
        "name": "Summer Sonic",
        "country": "JP",
        "genre": "mixed",
        "date": {"start": "2024-08-16", "end": "2024-08-18"},
        "prices": [
            {"name": "1-Day Ticket", "price": 150},
            {"name": "2-Day Pass", "price": 250},
            {"name": "3-Day Pass", "price": 350}
        ],
        "ratings": [
            {"stars": 4.7, "username": "sonicfanatic", "comment": "Incredible lineup and vibes!"},
            {"stars": 4.5, "username": "musicloverJP"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[1], "day": "2024-08-16"},
            {"artistId": artists_result.inserted_ids[19], "day": "2024-08-17"},
            {"artistId": artists_result.inserted_ids[20], "day": "2024-08-18"},
            {"artistId": artists_result.inserted_ids[26], "day": "2024-08-16"},
            {"artistId": artists_result.inserted_ids[27], "day": "2024-08-17"}
        ]
    },
    {
        "name": "Austin City Limits Music Festival",
        "country": "US",
        "genre": "mixed",
        "date": {"start": "2024-10-04", "end": "2024-10-06"},
        "prices": [
            {"name": "GA 3-Day Ticket", "price": 300},
            {"name": "VIP 3-Day Ticket", "price": 1000},
            {"name": "Platinum 3-Day Ticket", "price": 2500}
        ],
        "ratings": [
            {"stars": 4.8, "username": "aclfanatic", "comment": "Amazing music and atmosphere!"},
            {"stars": 4.7, "username": "austinmusiclover"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[9], "day": "2024-10-04"},
            {"artistId": artists_result.inserted_ids[11], "day": "2024-10-05"},
            {"artistId": artists_result.inserted_ids[19], "day": "2024-10-06"},
            {"artistId": artists_result.inserted_ids[22], "day": "2024-10-04"},
            {"artistId": artists_result.inserted_ids[28], "day": "2024-10-05"}
        ]
    },
    {
        "name": "Osheaga Festival",
        "country": "CA",
        "genre": "mixed",
        "date": {"start": "2024-08-02", "end": "2024-08-04"},
        "prices": [
            {"name": "General Admission", "price": 350},
            {"name": "Gold Pass", "price": 800},
            {"name": "Platinum Pass", "price": 1500}
        ],
        "ratings": [
            {"stars": 4.7, "username": "osheagafanatic", "comment": "Fantastic lineup and organization!"},
            {"stars": 4.6, "username": "musicloverCA"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[1], "day": "2024-08-02"},
            {"artistId": artists_result.inserted_ids[9], "day": "2024-08-03"},
            {"artistId": artists_result.inserted_ids[29], "day": "2024-08-04"},
            {"artistId": artists_result.inserted_ids[4], "day": "2024-08-02"},
            {"artistId": artists_result.inserted_ids[28], "day": "2024-08-03"}
        ]
    },
    {
        "name": "Rock en Seine",
        "country": "FR",
        "genre": "rock",
        "date": {"start": "2024-08-23", "end": "2024-08-25"},
        "prices": [
            {"name": "3-Day Pass", "price": 250},
            {"name": "VIP Pass", "price": 600},
            {"name": "Camping Pass", "price": 100}
        ],
        "ratings": [
            {"stars": 4.6, "username": "rockenseinefanatic", "comment": "Great atmosphere and lineup!"},
            {"stars": 4.5, "username": "musicloverFR"}
        ],
        "artists": [
            {"artistId": artists_result.inserted_ids[9], "day": "2024-08-23"},
            {"artistId": artists_result.inserted_ids[21], "day": "2024-08-24"},
            {"artistId": artists_result.inserted_ids[11], "day": "2024-08-25"},
            {"artistId": artists_result.inserted_ids[26], "day": "2024-08-23"},
            {"artistId": artists_result.inserted_ids[12], "day": "2024-08-24"}
        ]
    }
]


festivals_collection = db['Festivals']
festival_result = festivals_collection.insert_many(festivals)
print(f"Erfolgreich {len(festival_result.inserted_ids)} Festivals eingefügt")

client.close()
