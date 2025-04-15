FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

WORKDIR /app

COPY . .

RUN pip install transformers==4.20.1 fastapi uvicorn pytz protobuf==3.20.0 tiktoken sentencepiece

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
