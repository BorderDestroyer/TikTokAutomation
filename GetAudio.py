from resemble import Resemble
from Secrets import *
import sys
import time

recordingText = open("Responses.txt", "r")
Resemble.api_key('QsfSfccI45rHerT8cRY7QQtt')

callback_uri = 'https://example.com/callback/resemble-clip'

for i in range(1):
    body = recordingText.readline()
    
    print(body)
    if body == "" or body == "\n":
        continue
    
    response = Resemble.v2.clips.create_async(
    project_uuid,
    voice_uuid,
    callback_uri,
    body,
    title=None,
    sample_rate=None,
    output_format=None,
    precision=None,
    include_timestamps=None,
    is_public=None,
    is_archived=None
    )
    
    clip = response['item']
    
    time.sleep(30)