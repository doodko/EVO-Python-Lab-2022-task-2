from pymongo import MongoClient
from datetime import datetime


client = MongoClient()
db = client['PyLab']
friends = db['friends']


def add_new_friend(name):
    friend = {'name': name, 'date': datetime.now()}
    return friends.insert_one(friend).inserted_id


def check_if_met_before(name):
    if friends.find_one({'name': name}) is None:
        friend = {'name': name, 'date': datetime.now()}
        friends.insert_one(friend)
        return f"Приємно познайомитись, {name}."
    return f"Здається, ми вже бачились, {name}."


def find_all_friends():
    return [fr["name"] for fr in friends.find()]
