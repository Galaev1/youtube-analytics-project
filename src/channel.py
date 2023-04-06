import json
import os
from distutils.command.build import build

from helper.youtube_api_manual import youtube

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    service = []

    def __init__(self, channel_id: str, title: str, description: str,url,subscriberCount: int,videoCount: int,viewCount: int) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = self.channel_id['items'][0]['snippet']['title']
        self.description = self.channel_id['items'][0]['snippet']['description']
        self.url = self.channel_id['items'][0]['thumbnails']['url']
        self.subscriberCount = self.channel_id['items'][0]['statistics']['subscriberCount']
        self.videoCount = self.channel_id['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel_id['items'][0]['statistics']['viewCount']
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        Channel.service.append(self)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def get_service(self) -> None:
        return self.service

    def to_json(self,json_to):
        print(json.dumps(json_to, indent=2, ensure_ascii=False))




