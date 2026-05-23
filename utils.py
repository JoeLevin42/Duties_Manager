"""
This is conatins utils funcitons to support the program
"""
import data

class SoldierIdNotExist(Exception):
    pass

class NameError(Exception):
    pass

class DutyNotFound(Exception):
    pass

class NotValidStatus(Exception):
    pass

class DutyAlreadyExist(Exception):
    pass

def find_solider_by_id(solider_id: int) -> dict | None:

    for index , d in enumerate(data.data):
        if d["id"] == int(solider_id):
            return data.data[index]

def find_duty_by_name(duties: list, duty_name: str) -> dict | None:

    for d in duties:
        if d.get("name") == duty_name:
            return d

def is_valid_status(status: str) -> bool:

    STATUS_LIST = ["pending" ,"completed", "missed"]
    if status in STATUS_LIST:
        return True
    return False

def is_valid_name(name: str) -> bool:
    
    if len(name.strip()) < 1:
        return False
    return True
        

def solider_has_duty(soldier: dict ,duty_name: str) -> bool:

    duties_names = [duty["name"] for duty in soldier["duties"]]
    if duty_name in duties_names:
        return True
    return False


def is_valid_day(day: str) -> bool:

    DAYS = ["sunday" ,"monday" ,"tuseday" ,"wednesday" ,"thursday"]
    if day in DAYS:
        return True
    else:
        return False

def is_id_exist(soldier_id: int,my_data: list) -> bool:
    
    for sid in my_data:
        if sid.get("id") == int(soldier_id):
            return True
        return False
   