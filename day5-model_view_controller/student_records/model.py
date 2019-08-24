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

def save():
    with open(DATAPATH, 'w') as json_file:
        json.dump(data, json_file, indent=3)

def add_grade(student, grade):
    data[student]["grades"].append(int(grade))
    print(data[student])

def add_student(student):
    data[student] = {"grades" : []}

def get_gpa(student):
    grades = data[student]["grades"]
    return sum(grades)/len(grades)

if __name__ == "__main__":
    load()
    add_grade("Carter Adams", 100)