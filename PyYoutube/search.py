from base import YOUTUBE
from pprint import PrettyPrinter
pp = PrettyPrinter()

class PyYoutubeSearch:
    def __init__(self,query:str,
                order:str=None,
                


                ):
        self.query = query # search quary
         
        self.order = order # order of search results
        
        

    
    def get_all(self):
        search = YOUTUBE.search().list(q=self.query, part='snippet', type=['channel','video','playlist'])
        response = search.execute()
        return response

    def get_custom(self, search_type:list):
        search = YOUTUBE.search().list(q=self.query, part='snippet', type=search_type)
        response = search.execute()
        return response

    def get_channel(self, channelType:str='any'):
        # The channelType parameter lets you restrict a search to a particular type of channel.

        #     Acceptable values are:
        #     any – Return all channels.
        #     show – Only retrieve shows.
        search = YOUTUBE.search().list(q=self.query,
                    part='snippet',
                    type='channel',
                    channelType=channelType,
                    )
        response = search.execute()
        return response

    def get_video(self,
                videoCaption:str= 'any', # filter videos based on if the have caption or not 
                videoType:str='any',
                videoDuration:str='any', # video search results based on their duration
                max_Result:int=2, # max result returned with a minimum of 5 results and a maximum of 50 results
                order:str='relevance' # order of search results
    
    	        ):

        # videoCaption  filter videos based on if the have caption or not 
                # Acceptable values are:
                #       any – Do not filter results based on caption availability.
                #       closedCaption – Only include videos that have captions.
                #       none – Only include videos that do not have captions.


#       videoDuration Acceptable values are:
                # any – Do not filter video search results based on their duration. This is the default value.
                # long – Only include videos longer than 20 minutes.
                # medium – Only include videos that are between four and 20 minutes long (inclusive).
                # short – Only include videos that are less than four minutes long.

        # order Acceptable values are:
        #     date: – Resources are sorted in reverse chronological order based on the date they were created.
        #     rating: – Resources are sorted from highest to lowest rating.
        #     relevance: – Resources are sorted based on their relevance to the search query.
        #                 This is the default value for this parameter.
        #     title: – Resources are sorted alphabetically by title.
        #     videoCount: – Channels are sorted in descending order of their number of uploaded videos.
        #     viewCount: – Resources are sorted from highest to lowest number of views. For live broadcasts,
        #                videos are sorted by number of concurrent viewers while the broadcasts are ongoing.

        search = YOUTUBE.search().list(q=self.query,
                    part='snippet',
                    type='video',
                    maxResults=max_Result,
                    order=order,
                    videoCaption=videoCaption,
                    videoType=videoType,
                    videoDuration=videoDuration
                    )
        response = search.execute()
        return response

    def get_playlist(self):
        search = YOUTUBE.search().list(q=self.query, part='snippet', type='playlist')
        response = search.execute()
        return response

    def download(self):
        pass

tub = PyYoutubeSearch('python')
pp.pprint(tub.get_video())

