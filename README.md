# chatYTB
a simple command line chatbot for interacting with transcripts of youtube videos using ChatGPT

# dependencies
The program is written for Python3 and has two other major dependencies: the OpenAI API and an open-source library for accessing transcripts of YouTube videos. Both libraries are available through pip and can be installed using the following command in your terminal from inside the chatYTB directory: `pip install -r requirements.txt`.

* https://platform.openai.com/docs/api-reference/introduction
* https://pypi.org/project/youtube-transcript-api/

# usage
`./python chatYTB.py`
`./python3 chatYTB.py`

Upon running, the program will request a YouTube URL or video ID. Copy and paste will work for this, but ensure that any URL you submit does not include a start time. This will interfere with the transcript fetch.

NOTE: In order for the program to work properly, you must have a functioning OpenAI API key assigned to the correct environment variable for your operating system. See more information here: https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key

# how does it work?
Quite simply! The program downloads the indicated YT video's transcript (defaulting to manually-entered transcripts and falling back on automatically generated transcripts). It then feeds this transcript, along with a clear prompt, to OpenAI's ChatGPT 4 Turbo model. 
