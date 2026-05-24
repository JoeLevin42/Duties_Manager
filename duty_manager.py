"""
This functions is in charge for
the duty manager 
"""
import data
import utils

def add_duty_to_solider(soldier_id: int ,duty_name: str ,day: str)-> None : 
    """Adding duty to exist soldier

    This function is adding duty to an existing soldier
    the duty name and day have to be valid or will cause error

    Args:
        soldier_id = the soldier id (have to be uniq)
        duty_name = the duty name if not exist already to this soldier
        day = day between sunday to thursday else will cause error

    Returns:
        None but if worked updating the data base by param    
    """
    soldier_dict = utils.find_solider_by_id(soldier_id)
    if soldier_dict == None:
        raise utils.SoldierIdNotExist("The soldier id doesnt exist in the system!")
    
    if utils.solider_has_duty(soldier_dict, duty_name):
        raise utils.DutyAlreadyExist
    
    if not utils.is_valid_day(day):
        raise utils.DutyNotFound
    duty_dict = {"name": duty_name, "day": day,"status": "pending"}

    soldier_dict["duties"].append(duty_dict)    

def update_duty_status(solider_id: int, duty_name: int ,new_status: str) -> None:
    """Updating the duty status

    This function is updating the duty status to exist duty to exist soldier 
    if the duty doenst exist to this soldier its will raise error

    Args:
        soldier_id = the soldier id 
        duty_name = name of the duty (have to be exist)
        new_status = can be one of the three legal status like "completed"/"missed"

    Returns:
        None but uptdating the status in the data base throght the soldier dict
    
    """    
    soldier_dict = utils.find_solider_by_id(solider_id)
    if soldier_dict == None:
        raise utils.SoldierIdNotExist("The id not in the system!")
    
    soldier_duty_dict = utils.find_duty_by_name(soldier_dict["duties"] ,duty_name)
    if soldier_duty_dict == None:
        raise utils.DutyNotFound("NO duty in this name to the soldier")
    
    if utils.is_valid_status(new_status):
        soldier_duty_dict["status"] = new_status
    else:
        raise utils.NotValidStatus
            

def get_soliders_duties(solider_id: int) -> list:
    """Returns the all duties to one soldier

    This function going to the data base and taking the list of the duties
    of the soldier by id , if id not exist rasing a error

    Args:
        soldier_id = the soldier id

    Returns:
        list of the duties of this soldier    
    """
    soldier_dict = utils.find_solider_by_id(solider_id)
    if soldier_dict == None:
        raise utils.SoldierIdNotExist("NO id in the system")
    
    return soldier_dict["duties"] 
    



 