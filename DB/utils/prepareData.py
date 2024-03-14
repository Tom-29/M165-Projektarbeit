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

# Festivalsdaten erweitern
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
]


festivals_collection = db['Festivals']
festival_result = festivals_collection.insert_many(festivals)
print(f"Erfolgreich {len(festival_result.inserted_ids)} Festivals eingefügt")

client.close()
