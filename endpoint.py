import logging
import base64
import matplotlib.pyplot as plt

from fastapi import FastAPI
from fastapi.responses import Response

from io import BytesIO

from analysis import comments_analysis

plt.style.use('ggplot')  # Setting the plot style
app = FastAPI(title='Youtube comments sentiment analyzer')  # Creating FastAPI app

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a')

logger = logging.getLogger(__name__)

mlflow.set_experiment('youtube_comments_analysis')


@app.get('/')
async def home():
    return {'message': 'Welcome to sentiment analyzer'}


@app.get('/analyze/{videoId}/')
async def analyze_video(videoId: str):
    analysis = comments_analysis(videoId)  # Analyzing comments sentiment
    average_score = sum([item['score'] for item in analysis]) / len(analysis)  # Calculating average score

    num_positive = sum(1 for r in analysis if r['label'] == 'POSITIVE')  # Counting positive comments
    num_negative = sum(1 for r in analysis if r['label'] == 'NEGATIVE')  # Counting negative comments

    X = ['POSITIVE', 'NEGATIVE']  # X-axis labels
    y = [num_positive, num_negative]  # Y-axis values

    plt.bar(X, y)  # Creating bar plot
    plt.xlabel('Label')
    plt.ylabel('Count')

    if average_score > 0.6:
        label = 'POSITIVE'
    if average_score < 0.4:
        label = 'NEGATIVE'

    plt.figure(figsize=(8,5))
    plt.bar(X, y)
    plt.title(f'Comment is {label} with score {average_score:.2f}')
    plt.xlabel('Label')
    plt.ylabel('Count')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    with mlflow.start_run():
        mlflow.log_param('video_id', videoId)
        mlflow.log_metric('average_score', average_score)
        mlflow.log_metric('num_positive', num_positive)
        mlflow.log_metric('num_negative', num_negative)
        mlflow.log_param('label', label)


    logger.info(f'Video ID: {videoId}, Average Score: {average_score:.2f}, Label: {label}')

    return Response(content=buf.getvalue(), media_type='image/png')