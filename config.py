import os
from dotenv import load_dotenv

load_dotenv()


class ENV:
    CHANNEL_IT_A = os.getenv("CHANNEL_IT_A")
    CHANNEL_IT_B = os.getenv("CHANNEL_IT_B")
    CHANNEL_IT_1 = os.getenv("CHANNEL_IT_1")
    CHANNEL_IT_2 = os.getenv("CHANNEL_IT_2")
    CHANNEL_IT_3 = os.getenv("CHANNEL_IT_3")
    CHANNEL_IT_4 = os.getenv("CHANNEL_IT_4")
    CHANNEL_IT_5 = os.getenv("CHANNEL_IT_5")
    CHANNEL_IT_6 = os.getenv("CHANNEL_IT_6")

    ROLE_IT_A = os.getenv("ROLE_IT_A")
    ROLE_IT_B = os.getenv("ROLE_IT_B")
    ROLE_IT_1 = os.getenv("ROLE_IT_1")
    ROLE_IT_2 = os.getenv("ROLE_IT_2")
    ROLE_IT_3 = os.getenv("ROLE_IT_3")
    ROLE_IT_4 = os.getenv("ROLE_IT_4")
    ROLE_IT_5 = os.getenv("ROLE_IT_5")
    ROLE_IT_6 = os.getenv("ROLE_IT_6")

    WEBHOOK_IT_A = os.getenv("WEBHOOK_IT_A")
    WEBHOOK_IT_B = os.getenv("WEBHOOK_IT_B")
    WEBHOOK_IT_1 = os.getenv("WEBHOOK_IT_1")
    WEBHOOK_IT_2 = os.getenv("WEBHOOK_IT_2")
    WEBHOOK_IT_3 = os.getenv("WEBHOOK_IT_3")
    WEBHOOK_IT_4 = os.getenv("WEBHOOK_IT_4")
    WEBHOOK_IT_5 = os.getenv("WEBHOOK_IT_5")
    WEBHOOK_IT_6 = os.getenv("WEBHOOK_IT_6")
