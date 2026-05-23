"""
This is the logistical functions to manage 
the data of soldiers 
"""

import data
import utils

def add_soldier(soldier_id: int , name: str,my_data=data.data) -> None:
    """Adding soldier

    This function is adding soldier to the data base , checking if the soldier id
    not already exist in the system and if the name is valid

    Args:
        soldier_id = the id of the soldier
        name = the soldier name hava to be valid!
        my_data = the data base param
    
    Returns:
        None = Updating the data base
    """
    if utils.is_id_exist(soldier_id,my_data):
        raise utils.SoldierIdNotExist("The soldier is already exist!")

    if utils.is_valid_name(name):
        soldier_dict = {"id": soldier_id ,"name": name, "duties" : []}
        my_data.append(soldier_dict)

    else:
        raise NameError("The name for the soldier is Invalid")


def remove_soldier(soldier_id: int, my_data=data.data) -> None:
    """Removing soldier from DB

    This function is removing the soldier from the data base by the soldier id
    if wrong if its will cause error

    Args:
        soldier_id = the id if the soldier 
        my_data = the data base as param

    Returns:
        None but updating and removing the soldier from DB
    """   
    if not utils.is_id_exist(soldier_id ,my_data):
        raise utils.SoldierIdNotExist("The soldier ID not in the system!")
    else:
        for index , d in enumerate(data.data):
            if d["id"] == soldier_id:
                del my_data[index]
                break

    
def get_all_soldiers(my_data: list =data.data) -> list:
    """
    Retunrn the Data base list
    """

    return my_data

if __name__ == "__main__":
    pass