from urllib import response
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

    def get_channel_videos(self, channelId:str):
        response = self.YOUTUBE.channels().list(id=channelId, part=['contentDetails'],)
        play_list_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        videos = []
        next_page_token = None
        
        while True:
            res = self.YOUTUBE.playlistItems().list(part='snippet', playlistId=play_list_id,
                pageToken=next_page_token, maxResults=50)

            videos += res['items']
            next_page_token = res['nextPageToken']
            if next_page_token == None:
                break

            return videos


tub = PyYoutubeChannel(youtube_api_key=config("API_KEY"))

