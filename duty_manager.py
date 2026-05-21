"""
This functions is in charge for
the duty manager 
"""
import data
import utils

def add_duty_to_solider(soldier_id: int ,duty_name: str ,day: str)-> None : 

    soldier_dict = utils.find_solider_by_id(soldier_id)
    if type(soldier_id) == None:
        raise KeyError("The soldier id doesnt exist in the system!")
    
    if utils.solider_has_duty(soldier_dict, duty_name):
        raise ValueError("The duty is already exist for this solider")
    
    if not utils.is_valid_day(day):
        raise ValueError("Day Invalid choose day = sunday - thursday")
    
    duty_dict = {"name": duty_name, "day": day,"status": "pending"}

    soldier_dict["duties"].append(duty_dict)    

def update_duty_status(solider_id: int, duty_name: int ,new_status: str) -> None:
    
    soldier_dict = utils.find_solider_by_id(solider_id)
    if soldier_dict == None:
        raise KeyError("The id not in the system!")
    
    soldier_duty_dict = utils.find_duty_by_name(soldier_dict["duties"] ,duty_name)
    if soldier_duty_dict == None:
        raise KeyError("NO duty in this name to the soldier")
    
    if utils.is_valid_status(new_status):
        soldier_duty_dict["status"] = new_status
    else:
        raise ValueError
        
    

def get_soliders_duties(solider_id: int) -> list:
    
    soldier_dict = utils.find_solider_by_id(solider_id)
    if soldier_dict == None:
        raise KeyError("NO id in the system")
    
    return soldier_dict["duties"] 
    

if __name__ == "__main__":

    add_duty_to_solider(1234, "guard duty", "sunday")
    add_duty_to_solider(1234, "guard duty", "sunday")
    print(data.data)