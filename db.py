from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb+srv://doodko:fyyeirf1008@evo-python-lab-2022.iow5y.mongodb.net/PyLab?retryWrites=true&w=majority")
db = client['PyLab']
friends = db['friends']



def add_new_friend(name):
    friend = {'name': name, 'date': datetime.now()}
    friends.insert_one(friend)


def check_if_met_before(name):
    if friends.find_one({'name': name}) is None:
        add_new_friend(name)
        return f"Приємно познайомитись, {name}."
    return f"Здається, ми вже бачились, {name}."


def find_all_friends():
    friends_list = [fr["name"] for fr in friends.find()]
    return friends_list  
