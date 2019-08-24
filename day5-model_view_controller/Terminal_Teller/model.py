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

def create_acct(account, first_name, last_name, create_pin):
        data[account] = {}  
        data[account]["first name"] = first_name
        data[account]['last name'] = last_name
        data[account]['pin'] = create_pin
        data[account]['balance'] = 0
        return data[account]

if __name__ == "__main__":
    load()
    create_acct(1,1,1,1)
    print(data)
    save()

   
   