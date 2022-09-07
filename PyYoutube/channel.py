from googleapiclient.discovery import build
from decouple import config

YOUTUBE_API_KEY = config("API_KEY")



class PyYoutubeChannel:
    def __init__(self,youtube_api_key:str):
        self.YOUTUBE = build('youtube', 'v3', developerKey=youtube_api_key)


    def get_channel_by_id(self, categoryId:str):

        response = self.YOUTUBE.channels().list(id=categoryId, part=['snippet','contentDetails'
        ,'contentOwnerDetails','localizations',
         'statistics','status','topicDetails'],).execute()
        return response

    def get_channel_by_name(self, channelname:str):
        response = self.YOUTUBE.channels().list(forUsername=channelname, part=['snippet','contentDetails'
        ,'contentOwnerDetails','localizations',
         'statistics','status','topicDetails']).execute()
        return response


