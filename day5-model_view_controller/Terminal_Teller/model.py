import json
import os


PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, 'r') as file_object:
        data = json.load(file_object)

def pin_check(account, pin): 
    pin = data[account]["pin"]
    return pin

def save():
    with open(DATAPATH, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def deposit(account, depbalance):
    newbalance = data[account]["balance"] + depbalance
    data[account]["balance"] = newbalance
    return data[account]["balance"]

def withdraw(account, wdbalance):
    newbalance = data[account]["balance"] - wdbalance
    data[account]["balance"] = newbalance
    return data[account]["balance"]

def check_balance(account):
    balance = data[account]["balance"]
    return balance

if __name__ == "__main__":
    load()
    deposit("1", 100)
   
   