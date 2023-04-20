import datetime
import os

import isodate
from googleapiclient.discovery import build



class PlayList:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
        self.playlist_videos = self.youtube.playlists().list(id=self.playlist_id,
                                                       part='contentDetails,snippet',
                                                       maxResults=50, ).execute()
        self.title = self.playlist_videos['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def get_video(self):
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    def get_statistic(self):
        videos = []
        for video in self.get_video():
            video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                        id=video).execute()

            iso_8601_duration = video_response["items"][0]['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            video_url = f"https://youtu.be/{video}"
            videos.append([duration, like_count, video_url])

        return videos

    @property
    def total_duration(self):
        total = datetime.timedelta()
        for i in self.get_statistic():
            total += i[0]
        return total

    def show_best_video(self):
        url_video = None
        like = 0
        for i in self.get_statistic():
            if int(i[1]) >= like:
                like = int(i[1])
                url_video = str(i[2])
        return url_video



