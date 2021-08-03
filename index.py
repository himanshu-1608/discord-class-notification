from datetime import date, datetime
import json


# Global constans to be declared here

DATABASE_LOCATION = "./data"
TOP_LEVEL_SECTIONS = ["IT_A", "IT_B"]
CURR_TIME = datetime.now()
CURR_DAY = CURR_TIME.strftime("%A")  # current day
CURR_HOUR = CURR_TIME.strftime("%H")  # current hour
CURR_MIN = CURR_TIME.strftime("%M")  # current min

# Code starts here

for section in TOP_LEVEL_SECTIONS:
    # Don't process IT_A for now
    if section == "IT_A":
        continue

    daily_schedule_filename = "{db_location}/{section}/{day}.json".format(
        db_location=DATABASE_LOCATION, section=section, day=CURR_DAY
    )
    daily_schedule_file = open(daily_schedule_filename, "r")
    daily_schedule = json.load(daily_schedule_file)
    for event in daily_schedule:
        print(event["type"])
