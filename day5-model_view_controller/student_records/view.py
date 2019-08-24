
def get_student():
    return input("Student Name: ")


def show_menu(student):
    print()
    print("Working on student {}".format(student))
    print()
    print("Options:")
    print("1 add grade")
    print("2 show gpa")
    print("3 quit")

def get_input():
    print()
    print("Your choice: ", end="")
    return input()

def show_gpa(gpa):
    print()
    print("Student's gpa is {}.".format(gpa))

def bad_input():
    print()
    print("Bad input")
    print()


if __name__ == "__main__":
    show_menu("Greg")