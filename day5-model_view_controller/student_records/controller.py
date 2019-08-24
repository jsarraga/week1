import view
import model


def run():
    model.load()
    student = view.get_student()
    mainmenu(student)


def mainmenu(student):
    while True:
        view.show_menu(student)
        selection = view.get_input()
        # print(selection)
        if selection == '3':
            model.save()
            return
        elif selection == '1':
            newgrade = view.get_input()
            model.add_grade(student, newgrade)
        elif selection == '2':
            gpa = model.get_gpa(student)
            view.show_gpa(gpa)
        else:
            view.bad_input()


if __name__ == "__main__":
    run()
    # print("Current __name__: ", __name__)

