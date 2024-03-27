from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true')

admin_db = client.admin

users = [
    {"username": "tomUser", "password": "tomPassword", "roles": ["adminRole"]},
    {"username": "jeremiasUser", "password": "jeremiasPassword", "roles": ["dbManagerRole", "readerRole", "writerRole"]},
    {"username": "guestUser", "password": "guestPassword", "roles": ["readerRole"]},
    {"username": "backendUser", "password": "backendPassword", "roles": ["readerRole", "writerRole"]}
]

roles = [
    {"role": "adminRole", "privileges": [{"resource": {"anyResource": True}, "actions": ["anyAction"]}]},
    {"role": "dbManagerRole", "privileges": [{"resource": {"db": "FestivalTracker", "collection": ""}, "actions": ["find", "listCollections", "createCollection", "dropCollection", "createIndex", "dropIndex"]}]},
    {"role": "readerRole", "privileges": [{"resource": {"db": "FestivalTracker", "collection": ""}, "actions": ["find"]}]},
    {"role": "writerRole", "privileges": [{"resource": {"db": "FestivalTracker", "collection": ""}, "actions": ["insert", "update", "remove"]}]}
]

def create_roles_and_users():
    for role in roles:
        admin_db.command("createRole", role["role"], privileges=role["privileges"], roles=[])

    for user in users:
        admin_db.command("createUser", user["username"], pwd=user["password"], roles=user["roles"])

if __name__ == "__main__":
    create_roles_and_users()
    print("Rollen und Benutzer erfolgreich erstellt.")
