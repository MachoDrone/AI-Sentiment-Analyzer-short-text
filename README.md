# Sentiment Analysis API

## Introduction
This project is a sentiment analysis API that analyzes text to determine its sentiment. It provides outputs including sentiment labels (positive, negative, neutral), confidence scores, emoji faces, emoji hands, star ratings, and numeric ratings. The API is built using FastAPI and leverages the Hugging Face Transformers library for sentiment analysis. It is containerized with Docker for easy deployment.

## Technologies Used
- **FastAPI**: A modern web framework for building APIs with Python.
- **Hugging Face Transformers**: A library for natural language processing tasks, including sentiment analysis.
- **Docker**: A platform for developing, shipping, and running applications in containers.

## Installation
To set up and run the API locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-api.git
   cd sentiment-analysis-api
2. **Build the Docker Image**:
   ```bash
   docker build -t sentiment-analysis-multilingual:0.0.3 .
3. **Paste the job-def.json contents into Nosana**
   ```https://dashboard.nosana.com/deploy/
   Choose Advanced Builder, paste the job definition, select a GPU with 8GB or more, and click Create Deployment.
4. **Deplyment Page**:
   ```Logs Tab
   Make note of the address that is eventually listed:
   e.g. https://538qBxRN1EMmB3YAt35tvmPe8JfEZx4n1unrfRtMQCjq.node.k8s.prd.nos.ci
5. **Send a test message**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "I love Nosana!"}' http://localhost:8000/analyze

   you will receive a response with a variety of sentiments to draw from with a confidence score between 0-100 which shows the confidence level of how AI interpreted the text.
6. **Response**:
7. ## bash: 
   "label": "positive",
  "confidence": 93,
  "emoji_face": "😊",
  "emoji_hand": "👍",
  "star_rating": "★★★★★",
  "numeric_rating": "5/5"
8. **After your custom processing**:
   ```Processed response samples
   I love Nosana! 5/5
   ★★★★★ "I love Nosana!" --actual client
   I can't curse in the store, but I get it. 👌
   The Movie was cancelled. Unfiar 😞

License
This project is licensed under the MIT License. See the LICENSE file for details.
```
