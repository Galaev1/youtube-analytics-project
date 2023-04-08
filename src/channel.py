import json
import os

from googleapiclient.discovery import build



class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title: int = self.channel['items'][0]['snippet']['title']
        # self.description: str = self.channel['items'][0]['snippet']['description']
        self.url: str = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        # self.subscriberCount: str = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count: str = self.channel['items'][0]['statistics']['videoCount']
        # self.viewCount: str = self.channel['items'][0]['statistics']['viewCount']


        self.youtube = build('youtube', 'v3', developerKey=self.api_key)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
    @classmethod
    def get_service(self):
        return self.youtube

    def to_json(self,json_to):
        print(json.dumps(json_to, indent=2, ensure_ascii=False))





