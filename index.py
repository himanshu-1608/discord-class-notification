from datetime import date, datetime
import json


# Global constans to be declared here

DATABASE_FOLDER = "./data"
TOP_LEVEL_SECTIONS = ["IT_A", "IT_B"]
CURR_TIME = datetime.now()
CURR_DAY = CURR_TIME.strftime("%A")  # current day
CURR_HOUR = CURR_TIME.strftime("%H")  # current hour
CURR_MIN = CURR_TIME.strftime("%M")  # current min
