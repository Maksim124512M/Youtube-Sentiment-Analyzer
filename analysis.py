from transformers import pipeline

from youtube_parser import get_comments

classifier = pipeline('sentiment-analysis')  

def comments_analysis(videoId):
    '''Analyze comments from a Youtube video by its ID.'''

    df = get_comments(videoId)  # Getting comments DataFrame

    comments = df['comment'].astype(str).tolist()  # Converting comments to list of strings

    result = classifier(comments)

    return result  # Returning average score