from tools.tools import *

TOOLS = {
    "task_add": task_add,
    "add_priority": add_priority,
    "prioritize": prioritize,
    "show": show,
}

TOOL_DESCRIPTIONS = {
    "task_add": "Add an event to the calendar. args: name:str, date:str, time:str",
    "add_priority": "Adds a priority tag to the specified name. args: user:float, name:str",
    "prioritize" : "Makes a priority list based on the names of the events and what the user themselves wants to prioritize, organized by highest to lowest priority. args: none",
    "show": "Return all events in caldenar in different formats, based on the following day, week, or month. args: none",
}