"""
The main function that handles all
"""
import utils
import soldier_manager
import duty_manager
def shown_menu():
    print("Hello welcome tho this amazing system!"\
          "Please Choose on of the option" \
          "1. Add soldier" \
          "2. Remove soldier" \
          "3. View soldier" \
          "4. Add duty to soldier" \
          "5. Update Duty status to soldier" \
          "6. See the soldier duties"
          )
    

def get_user_choice():
    
    pass

def handle_add_solider():
    get_soldier_id = input("Enter soldier ID:  ")
    get_soldier_name = input("Enter soldier name:  ")
    try:
        soldier_manager.add_soldier(soldier_id=get_soldier_id,  name=get_soldier_name)
        print("The soldier added!")
    
    except ValueError:
        print("The soldier not ")
    

def handle_remove_solider():

    get_soldier_id = input("Enter soldier ID:  ")
    try:
        soldier_manager.remove_soldier(get_soldier_id)
        print("The soldier removed!")
    except KeyError:
            print("The soldier ID not in the system!")



def handle_view_solider():

    try:
        soldier_manager.get_all_soldiers()
    except:
        print("Something went wrong")

def handle_add_duty():
    
    get_soldier_id = input("Enetr ID")
    get_duty_name = input("Please Enter duty name")
    get_day = ("Please Input Day")
    try:
        duty_manager.add_duty_to_solider(get_soldier_id , get_duty_name, get_day)
        print("Duty Added!")
    except KeyError:
        print("The soldier id doesnt exist in the system!")
    except ValueError:
        print("The duty is already exist for this solider")
    except ValueError:
        print("Day Invalid choose day = sunday - thursday")

def handle_update_duty():
    

    pass

def handle_view_solider_duties():

    pass

def main():

    pass