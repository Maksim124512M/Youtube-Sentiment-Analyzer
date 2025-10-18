import os
import pandas as pd

from googleapiclient.discovery import build

from dotenv import load_dotenv

load_dotenv()  # Loading the .env

API_KEY = os.getenv('YOUTUBE_API_KEY')  # Getting the Youtube API KEY

youtube = build('youtube', 'v3', developerKey=API_KEY)  # Building the youtube API


# Getting comment from video
def get_comments(videoId):
    '''Get comments from a Youtube video by its ID.'''

    comments = []
    next_page_token = None

    while True:
        # Finding the video
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=videoId,
            maxResults=100,
            textFormat='plainText',
            pageToken=next_page_token
        ).execute()

        # Appending the new comment to the comments list
        for item in response['items']:
            snippet = item['snippet']['topLevelComment']['snippet']
            comments.append({
                'author': snippet['authorDisplayName'],
                'comment': snippet['textDisplay'],
                'likes': snippet['likeCount'],
                'published': snippet['publishedAt']
            })

        next_page_token = response.get('nextPageToken')  # Getting the next page token
        if not next_page_token:
            break

    df = pd.DataFrame(comments)  # Creating a DataFrame from the comments list

    return df