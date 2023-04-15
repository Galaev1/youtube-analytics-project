import json
import os

from googleapiclient.discovery import build



class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.__video_id
                                               ).execute()
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = self.video_response['items'][0]['statistics']['commentCount']

class PLVideo(Video):
    def __init__(self, video_id: str, playlist_ids: str):
        super().__init__(video_id)
        self.playlist_ids = playlist_ids