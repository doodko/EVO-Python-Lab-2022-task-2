from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb+srv://doodko:fyyeirf1008@evo-python-lab-2022.iow5y.mongodb.net/PyLab?retryWrites=true&w=majority")
db = client['PyLab']
friends = db['friends']



cache = True # False to disable caching db
if cache:
    friends_list = [fr["name"] for fr in friends.find()]
else:
    friends_list = []


def add_new_friend(name):
    friend = {'name': name, 'date': datetime.now()}
    friends.insert_one(friend)
    update_cache()


def check_if_met_before(name):
    if friends.find_one({'name': name}) is None:
        add_new_friend(name)
        return f"Приємно познайомитись, {name}."
    return f"Здається, ми вже бачились, {name}."


def find_all_friends():
    global friends_list
    if not cache:
        update_cache()
    return friends_list  


def update_cache():
    global friends_list
    friends_list = [fr["name"] for fr in friends.find()]

