#Signoture of functions
def shown_menu():
    """Showing the menu

    This function is printing the menu the the choice 
    option to the user
    """
    pass

def solider_exit_valid(id:int):
    """Checing of solider in DB

    This fucntion cheking if the solider is exist in the
    DB

    Args:
        id = The id of the solider

    Returns:
        bool - if exits True / not exist False
    """
    pass

def add_solider(id:int , name:str):
    """Adding solider to DB

    This function is adding the solider to the DB
    after call the check exist in DB fucntion to the soldier

    Args:
        id = the id of the solider
        name = the name of the solider
    """
    pass

def remove_solider(id: int):
    """Removing solider from DB

    This function is deleting the solider from the DB

    Args:
        id = the id of the solider

    """
    pass

def view_soliders():
    """Showing list of the soliders

    This function is going to the DB and printing
    the list of all the soliders
    """
    pass

def add_duty_to_solider(duty:dict , id:int):
    """Adding duty to the solider duty list

    This function in adding the duty : dict
    to the solider duties dicts

    Args:
        duty = dict of the duty
        id = id of the solider
    
    """
    pass

def update_duty(duty : dict , id: int , update :str):
    """Updating the duty status

    This function is taking the update :str one from 
    three option and updating the status of the duty

    Args:
        duty = dict of the dudty
        id = id of the solider
        update = the update for the status

    """
    pass

def get_duties_solider(id:int):
    """Print the solider duty list

    This function is taking the duties list of the 
    solider and return the list , by searching the solider

    Args:
        id = id of the solier
    
    Returns:
        list of the duties
    """
    pass

def search_solider(id:int):
    """Search the solider by the if

    This function is searching if the solifer is exist 
    in the data base 

    Args:
        id = id of the solider
    
    Returns:
        The solider data : dict
    
    """
    pass