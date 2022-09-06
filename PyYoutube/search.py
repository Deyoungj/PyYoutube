from base import YOUTUBE
from pprint import PrettyPrinter
pp = PrettyPrinter()

class PyYoutubeSearch:
    def __init__(self,query:str):
        self.query = query # search quary
        
    def get_all(self,
                max_Result:int=5, # max result returned with a minimum of 5 results and a maximum of 50 results
                ):

        search = YOUTUBE.search().list(q=self.query, part='snippet',
         type=['channel','video','playlist'],
          maxResults=max_Result)

        response = search.execute()
        return response

    def get_custom(self, 
                    search_type:list,
                    max_Result:int=5, # max result returned with a minimum of 5 results and a maximum of 50 results
                    ):
        # search_type is a list of strings eg. ['channel', 'video', 'playlist]
        search = YOUTUBE.search().list(q=self.query, part='snippet', type=search_type, maxResults=max_Result)
        response = search.execute()
        return response

    def get_channel(self, 
                    channelType:str='any',# channelType parameter lets you restrict a search to a particular type of channel.
                    max_Result:int=5, # max result returned with a minimum of 5 results and a maximum of 50 results
    	            ):


        #  channelType   Acceptable values are:
        #     any – Return all channels.
        #     show – Only retrieve shows.
        search = YOUTUBE.search().list(q=self.query,
                    part='snippet',
                    type='channel',
                    channelType=channelType,
                    maxResults= max_Result,
                    
                    )
        response = search.execute()
        return response


    def get_video(self,
                videoCaption:str= 'any', # filter videos based on if the have caption or not 
                videoType:str='any', # The videoType parameter lets you restrict a search to a particular type of videos. 
                videoDuration:str='any', # video search results based on their duration
                videoSyndicated:str='any', # The videoSyndicated parameter  lets you to restrict a search to only videos that can be played outside youtube.com.
                videoDimension:str='any', # The videoDimension lets you restrict a search to only retrieve 2D or 3D videos.
                safeSearch:str='none', # The safeSearch parameter indicates whether the search results should include restricted content as well as standard content.
                videoEmbeddable:str='any', # The videoEmbeddable parameter lets you to restrict a search to only videos that can be embedded into a webpage.
                videoDefinition:str='any', # The videoDefinition parameter lets you restrict to only include either high definition (HD) or standard definition (SD) videos. HD videos are available for playback in at least 720p,
                #  though higher resolutions, like 1080p, might also be available. If you specify a value for this parameter,
                videoLicense:str= 'any', # The videoLicense parameter filters search results to only include videos with a particular license.
                max_Result:int=5, # max result returned with a minimum of 5 results and a maximum of 50 results
                order:str='relevance' # order of search results
    
    	        ):

        # videoCaption  filter videos based on if the have caption or not 
                # Acceptable values are:
                #       any – Do not filter results based on caption availability.
                #       closedCaption – Only include videos that have captions.
                #       none – Only include videos that do not have captions.

#       channelType  Acceptable values are:
                # any – Return all channels.
                # show – Only retrieve shows.

#       safeSearch  Acceptable values are:
                # moderate – YouTube will filter some content from search results and, at the least, will filter content that is restricted in your locale. Based on their content, search results could be removed from search results or demoted in search results. This is the default parameter value.
                # none – YouTube will not filter the search result set.
                # strict – YouTube will try to exclude all restricted content from the search result set. Based on their content, search results could be removed from search results or demoted in search results.


#       videoDuration Acceptable values are:
                # any – Do not filter video search results based on their duration. This is the default value.
                # long – Only include videos longer than 20 minutes.
                # medium – Only include videos that are between four and 20 minutes long (inclusive).
                # short – Only include videos that are less than four minutes long.

#       videoSyndicated Acceptable values are:
                # any – Return all videos, syndicated or not.
                # true – Only retrieve syndicated videos.

#      videoType Acceptable values are:
                # any – Return all videos.
                # episode – Only retrieve episodes of shows.
                # movie – Only retrieve movies.

#       videoEmbeddable Acceptable values are:
                # any – Return all videos, embeddable or not.
                # true – Only retrieve embeddable videos.

#     videoLicense  Acceptable values are:
                # any – Return all videos, regardless of which license they have, that match the query parameters.
                # creativeCommon – Only return videos that have a Creative Commons license. Users can reuse videos with this license in other videos that they create. Learn more.
                # youtube – Only return videos that have the standard YouTube license.

#    videoDefinition Acceptable values are:
                # any – Return all videos, regardless of their resolution.
                # high – Only retrieve HD videos.
                # standard – Only retrieve videos in standard definition.

#    videoDimension Acceptable values are:
                # 2d – Restrict search results to exclude 3D videos.
                # 3d – Restrict search results to only include 3D videos.
                # any – Include both 3D and non-3D videos in returned results. This is the default value.


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
                    videoDuration=videoDuration,
                    videoLicense=videoLicense,
                    videoDefinition=videoDefinition,
                    videoEmbeddable=videoEmbeddable,
                    videoSyndicated=videoSyndicated,
                    safeSearch=safeSearch,
                    videoDimension=videoDimension,
                    
                    )
        response = search.execute()
        return response

    def get_playlist(self, max_Result:int=5):
        search = YOUTUBE.search().list(q=self.query, part='snippet', type='playlist',maxResults= max_Result,)
        response = search.execute()
        return response

    def download(self):
        pass

tub = PyYoutubeSearch('python')
pp.pprint(tub.get_playlist())

