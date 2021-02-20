import urllib.request, json 
import subprocess
from os.path import basename
import re
import glob

## STREAM GATEWAY 
## Receives JSON via AWS user data and launches FFMpeg to stream SRT to multiple RTMP destinations
## Designed to run inside the StreamGateway docker container with FFMpeg pre-built, including the SRT library 
## Author: George French 

ffmpeg = "ffmpeg -re -i srt://0.0.0.0?pkt_size=1316&mode=listener -strict -2 -y "

with urllib.request.urlopen("http://169.254.169.254/latest/user-data") as userdata:
    userdata = json.loads(userdata)
    for destination in userdata.values():
        ffmpeg = ffmpeg + "-f fifo -fifo_format flv -map 0:0 -map 0:1? -c copy -vtag 7 -atag 10 -drop_pkts_on_overflow 1 -attempt_recovery 1 -recovery_wait_time 1 %s " % (destination)
    print(ffmpeg)


p1 = subprocess.Popen(ffmpeg.split())
output,err = p1.communicate()
