from googleapiclient.discovery import build
from decouple import config

YOUTUBE = build(config("SERVICE"), config("VERSION"), developerKey=config("API_KEY"))


