from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

youtube_video = "https://www.youtube.com/watch?v=ry9SYnV3svc&ab_channel=LearnEnglishbyPocketPassport"
video_id = youtube_video.split("=")[1]

print("\n The ID of the video to be Summarized => ", video_id, "\n")
YouTubeVideo(video_id)
YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)

transcript[0:5]

result = ""
for i in transcript:
    result += ' ' + i['text']
# print(result)
print(len(result))

summarizer = pipeline('summarization')

num_iters = int(len(result))
summarized_text = []

for i in range(0, num_iters + 1):
    start = 0
    start = i * 1
    end = (i + 1) * 10000
    print("\n Input Text:- \n -----------\n" + result[start:end])
    out = summarizer(result[start:end])
    out = out[0]
    out = out['summary_text']
    print("\n Summarized text \n -----------\n" + out)
    summarized_text.append(out)

# print(summarized_text)
len(str(summarized_text))
str(summarized_text)
