from fastapi import FastAPI, Request
from transformers import pipeline
import torch
from pydantic import BaseModel

app = FastAPI()

# Device detection
device = 0 if torch.cuda.is_available() else -1
print(f"Using device: {'GPU' if device == 0 else 'CPU'}")

# Load sentiment analyzer
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    tokenizer="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    device=device
)

class TextInput(BaseModel):
    text: str

# Test endpoint
@app.get("/")
async def root():
    return {"message": "API is running"}

# Sentiment analysis endpoint with emoji output
@app.post("/analyze")
async def analyze_sentiment(request: Request, input: TextInput):
    result = sentiment_analyzer(input.text)[0]
    label = result['label']
    score = result['score']
    
    # Calculate confidence as a percentage
    confidence = round(score * 100)
    
    # Map label to emoji face, hand, and ratings
    if label == "negative":
        emoji_face = "😞"
        emoji_hand = "👎"
        stars = 1 if confidence > 80 else 2
    elif label == "neutral":
        emoji_face = "😐"
        emoji_hand = "👌"
        stars = 3
    elif label == "positive":
        emoji_face = "😊"
        emoji_hand = "👍"
        stars = 5 if confidence > 80 else 4
    
    # Generate star rating string
    star_rating = "★" * stars + "☆" * (5 - stars)
    
    # Generate numeric rating
    numeric_rating = f"{stars}/5"
    
    # Construct response
    response = {
        "label": label,
        "confidence": confidence,
        "emoji_face": emoji_face,
        "emoji_hand": emoji_hand,
        "star_rating": star_rating,
        "numeric_rating": numeric_rating
    }
    
    return response
