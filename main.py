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
    
    except ValueError:
        print("The soldier not ")
    finally:
        print("The soldier added!")

def handle_remove_solider():
    


    pass

def handle_view_solider():

    pass

def handle_add_duty():

    pass

def handle_update_duty():

    pass

def handle_view_solider_duties():

    pass

def main():

    pass