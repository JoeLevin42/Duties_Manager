"""
This is the logistical functions to manage 
the data of soldiers 
"""
import data
import utils

def add_soldier(soldier_id: int , name: str) -> None:

    if utils.is_id_exist():
        raise ValueError("The soldier is already exist!")

    if utils.is_valid_name():
        soldier_dict = {"id": soldier_id ,"name": name, "duties" : []}
        data.data.append(soldier_dict)
    else:
        raise ValueError("The name for the soldier is Invalid")
    

def remove_soldier(soldier_id: int) -> None:
    
    if not utils.is_id_exist():
        raise KeyError("The soldier ID not in the system!")
    else:
        for index , d in enumerate(data.data):
            if d["id"] == soldier_id:
                del data.data[index]
                break

    
def get_all_soldiers()-> list:

    return data.data



