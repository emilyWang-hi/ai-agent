from core.state import STATE

def task_add(name: str, date: str, time: str):
    STATE["schedule"].append({
        "name": name,
        "date": date,
        "time": time,
        "priority": 0.5
    })
    return f"Added {name} for {time} on {date}"

def add_priority(user: float, name: str):
    for task in STATE["schedule"]:
        if name == task["name"]:
            task["priority"] = user
            return f"successfully added priority of {user} to event {name}"
    return "Unable to find specified task"

def prioritize():
    STATE["schedule"].sort(key=lambda task: task.get("priority", 0), reverse=True)
    return STATE["schedule"]

def show():
    return STATE["schedule"]