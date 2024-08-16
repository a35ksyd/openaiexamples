import os
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

# Initial the api call
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

# YouTubeTranscriptApi to download the video transcript
transcripts = YouTubeTranscriptApi.get_transcript("CMsuDp_DER4")

# filter the content 
content = " ".join([segment['text'] for segment in transcripts  if '[Music]' not in segment['text']] )

# Calling openAI to summary the transcript
# using model gpt-3.5-turbo
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Summarize the video ranscript:\n{content}"}]
)

print(response)