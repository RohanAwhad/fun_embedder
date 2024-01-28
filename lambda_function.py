import json
from src import text_vectorization

def lambda_handler(event, context):
  text_list = event['text']
  if isinstance(text_list, str):
    text_list = [text_list]
  
  if not isinstance(text_list, list):
    raise ValueError('text must be a string or a list of strings')

  embeddings = text_vectorization.vectorize_batch(text_list).tolist()
  return {
    'statusCode': 200,
    'body': json.dumps({'embeddings': embeddings})
  }