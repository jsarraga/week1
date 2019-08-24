import view
import model

def run():
    model.load() 
    account = view.get_acct()
    pin = view.get_pin()
    if pin == model.pin_check(account, pin):
        mainmenu(account)
    else:
        view.bad_input()    

def mainmenu(account):
    while True:
        view.show_menu(account)
        selection = view.get_input()
        if selection == '4':
            answer = view.quit_input()
            if answer =="y":
                model.save() 
            if answer == "n":
                view.show_menu(account)
            return
        elif selection == '1':
            balance = model.check_balance(account) 
            view.show_balance(balance)
        elif selection == '2':
            depbalance = float(view.get_amount_input())
            model.deposit(account, depbalance) 
            balance = model.check_balance(account)
            view.show_balance(balance)
        elif selection =='3':
            wdbalance = float(view.get_amount_input())
            model.withdraw(account, wdbalance) 
            balance = model.check_balance(account)
            view.show_balance(balance)
        else:
            view.bad_input()




if __name__ == "__main__":
    run()
    # print("Current __name__: ", __name__)