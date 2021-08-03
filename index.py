from datetime import date, datetime
import json
import requests

# package imports
from config import ENV

# Global constans to be declared here

DATABASE_LOCATION = "./data"
TIMESLOTS_LOCATION = DATABASE_LOCATION + "/timeslots.json"
EVENT_SLOTS = json.load(open(TIMESLOTS_LOCATION, "r"))

TOP_LEVEL_SECTIONS = ["IT_A", "IT_B"]
CURR_TIME = datetime.now()
CURR_DAY = CURR_TIME.strftime("%A")  # current day
CURR_DATE = CURR_TIME.strftime("%d-%m-%Y")
CURR_HOUR = CURR_TIME.strftime("%H")  # current hour
CURR_MIN = CURR_TIME.strftime("%M")  # current min

# Code starts here


def get_daily_schedule(section):
    daily_schedule_filename = "{db_location}/{section}/{day}.json".format(
        db_location=DATABASE_LOCATION, section=section, day=CURR_DAY
    )
    daily_schedule_file = open(daily_schedule_filename, "r")
    return json.load(daily_schedule_file)


def prepare_payload(event, section_index):
    role_tag = "ROLE_{section}".format(section=event["sections"][section_index])
    section_role_tag = ENV[role_tag]
    event_name = " **{event_short_name}** ".format(event_short_name=event["short_name"])
    links = ""
    for index in range(len(event["faculty_names"])):
        links += "{faculty_name} : <{meet_link}>\n".format(
            faculty_name=event["faculty_names"][index],
            meet_link=event["meet_links"][index],
        )
    return "".join((section_role_tag, event_name, "\n", links))


def send_alert(event):
    for section_index in range(len(event["sections"])):
        payload = prepare_payload(event, section_index)
        webhook_name = "WEBHOOK_{section}".format(
            section=event["sections"][section_index]
        )
        webhook_url = ENV[webhook_name]
        requests.post(webhook_url, data={"content": payload})


def is_event_close(event):
    start_time = EVENT_SLOTS[event["start_time"]]["start_time"]
    event_start_time = datetime.strptime(CURR_DATE + " " + start_time, "%d-%m-%Y %H:%M")
    time_diff = event_start_time - CURR_TIME
    return 0 <= time_diff.total_seconds() <= 300


def event_handler(event):
    if is_event_close(event):
        send_alert(event)
    return None


def main():
    for section in TOP_LEVEL_SECTIONS:
        # Don't process IT_A for now
        if section == "IT_A":
            continue

        daily_schedule = get_daily_schedule(section)

        # wrapping list() is useless, just for supporting map's basic functionality
        list(map(event_handler, daily_schedule))


main()
