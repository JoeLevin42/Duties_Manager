"""
The main function that handles all
"""
import utils
import soldier_manager
import duty_manager
def shown_menu():
    print("Hello welcome tho this amazing system!\n"\
          "Please Choose on of the option\n" \
          "1. Add soldier\n" \
          "2. Remove soldier\n" \
          "3. View soldier\n" \
          "4. Add duty to soldier\n" \
          "5. Update Duty status to soldier\n" \
          "6. See the soldier duties\n"
          )
    

def get_user_choice():
    user_choice = input("Please enter your choice")
    if len(user_choice) == 1 and int(user_choice) in range(1,7):
        return user_choice
    else:
        print("Not valid input")
    
    pass

def handle_add_solider():
    get_soldier_id = input("Enter soldier ID:  ")
    get_soldier_name = input("Enter soldier name:  ")
    try:
        soldier_manager.add_soldier(soldier_id=get_soldier_id,  name=get_soldier_name)
        print("The soldier added!")
    
    except utils.SoldierIdNotExist:
        print("The soldier is already exist!")
    

def handle_remove_solider():

    get_soldier_id = input("Enter soldier ID:  ")
    try:
        soldier_manager.remove_soldier(get_soldier_id)
        print("The soldier removed!")
    except utils.SoldierIdNotExist:
            print("The soldier ID not in the system!")



def handle_view_solider():

    try:
        list_of_all = soldier_manager.get_all_soldiers()
        print(list_of_all)
    except:
        print("Something went wrong")

def handle_add_duty():
    
    get_soldier_id = input("Enetr ID")
    get_duty_name = input("Please Enter duty name")
    get_day = input("Please Input Day")
    try:
        duty_manager.add_duty_to_solider(get_soldier_id , get_duty_name, get_day)
        print("Duty Added!")
    except utils.SoldierIdNotExist:
        print("The soldier id doesnt exist in the system!")
    except utils.DutyAlreadyExist:
        print("The duty is already exist for this solider")
    except utils.DutyNotFound:
        print("Day Invalid choose day = sunday - thursday")

def handle_update_duty():

    get_soldier_id = input("Enter soldier ID  :")
    get_duty_name = input("enter duty name  :")
    get_duty_new_status = input("PLease enter new status")
    try:
        duty_manager.update_duty_status(get_soldier_id, get_duty_name, get_duty_new_status)
    except utils.SoldierIdNotExist:
        print("Soldier ID not in the system")
    except utils.NotValidStatus:
        print("Invalid status choose  - completed or missed or pending")


def handle_view_solider_duties():

    get_soldier_id = input("Enter soldier ID    :")
    try:
        print(duty_manager.get_soliders_duties(get_soldier_id))
    except utils.NotValidStatus:
        print("NO ID in the system")


def main():


    flag = True
    while flag:
        shown_menu()
        user_choice = get_user_choice()
        match user_choice:
            case "1":
                handle_add_solider()
            case "2":
                handle_remove_solider()
            case "3":
                handle_view_solider()
            case "4":
                handle_add_duty()
            case "5":
                handle_update_duty()
            case "6":
                handle_view_solider_duties()


main()



    
