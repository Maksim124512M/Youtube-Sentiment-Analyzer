# YouTube Comment Sentiment Analysis with FastAPI & MLflow
## Description
 API for analyzing the sentiment of YouTube video comments.
Uses <b> Hugging Face Transformers </b> for comment classification and <b> MLflow </b> for logging experiments and metrics.

Features:

- Analyzes comments and returns:

  - Overall sentiment (POSITIVE, NEGATIVE)

  - Average score (average_score)

  - Histogram of positive vs negative comments as an image

- Logs results to MLflow:

    - Parameters: video_id, label

    - Metrics: average_score, num_positive, num_negative

- View all experiments via MLflow UI (http://127.0.0.1:5000)

## Technologies
  - Python 3.12
  - FastAPI
  - Transformers (Hugging Face)
  - Matplotlib
  - MLflow
  - Docker
