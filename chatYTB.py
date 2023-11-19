from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

# boilerplate
WELCOME_PROMPT = 'WELCOME to ChatYTB. This program uses YouTube transcripts and OpenAI\'s ChatGPT 4 Turbo model to help you understand YT video content.\n\n>>> Please paste a raw YouTube URL (no start time) or YT Video ID to get started: '
FOLLOW_UP_PROMPT = '>>> Input a follow-up demand (or \'exit\'): '

# GPT assistant initialization
MODEL = "gpt-4-1106-preview"
# MODEL = "gpt-3.5-turbo"
SYSTEM_MESSAGE = "You are an analyst who reviews \
    transcripts of YouTube videos in order to provide summaries and answer questions. \
    You are adept at reviewing transcripts which do not contain punctuation or \
    identify speakers. The videos for which you are reviewing transcripts may \
    contain multiple speakers; please offer disclaimers if there is any possibility that you \
    are not properly identifying speakers."
FIRST_USER_MESSAGE = "Let's begin with a short summary of a video. The summary \
    should have a short introductory paragraph and then contain bullet points \
    outlining the video's highlights. After you provide this summary, I would \
    like to ask you questions about the video. Please only respond to my most \
    recent question when you write a response. Here is a transcript of the video \
    I would like for you to work on: "

# test video refs
# VIDEO_ID_1 = "4qb-_hw7ZqY" # matt walsh responding to tiktok videos
# VIDEO_ID_2 = "RBzij-MA6A8" # bill maher monologue
# VIDEO_ID_3 = "Q9qSwDxF6YI" # f1 las vegas highlights
# VIDEO_ID_4 = "dJZeAAs2V2c" # gordon ramsay making thanksgiving dinner

def main():

    yt_input = input(WELCOME_PROMPT)
    if yt_input == 'exit':
         return
    assert len(yt_input) >= 11, "YouTube video IDs are 11 characters long; you entered a shorter string"
    video_handle = yt_input[-11:] # VIDEO_ID_X

    # fetch transcript object and unpack into one long string
    transcript_returned = YouTubeTranscriptApi.get_transcript(video_handle)
    transcript_list = []
    for phrase_dict in transcript_returned:
        transcript_list.append(phrase_dict['text'])
    transcript = ' '.join(transcript_list)

    # build first message to Chat-GPT
    message_list = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": ''.join([FIRST_USER_MESSAGE, transcript])}
    ]

    # init client and make request
    client = OpenAI()
    completion = client.chat.completions.create(
        model=MODEL,
        messages=message_list
    )

    # print first result from chatgpt
    print('\n' + completion.choices[0].message.content + '\n')

    # get input for follow-up
    user_input = input(FOLLOW_UP_PROMPT)

    # fetch chat-gpt responses and query user until user exits
    while user_input != "exit":
        message_list.append(
             {"role": "user", "content": user_input}
        )

        completion = client.chat.completions.create(
            model=MODEL,
            messages=message_list
        )

        print('\n' + completion.choices[0].message.content + '\n')
        user_input = input(FOLLOW_UP_PROMPT)

    return

if __name__ == "__main__":
        main()
