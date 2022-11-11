import os
from telegram import *
from telegram.ext import *


async def down(vid=None, aid=None, url=None, uid=None, v=None, a=None, isEdmx = False):
    if not isEdmx:
        try:
            print(vid, aid)
            try:
                working_dir = os.getcwd() + "\working_dir"
                os.chdir(working_dir)
            except:
                pass
            evideo = os.system(f"yt-dlp -f {vid} --allow-unplayable-formats {url} -o evideo.mp4")
            eaudio = os.system(f"yt-dlp -f {aid} --allow-unplayable-formats {url} -o eaudio.mp4")
            return 'OK'
        except Exception as e:
            return
    else:
        try:
            try:
                working_dir = os.getcwd() + "\working_dir"
                os.chdir(working_dir)
            except:
                pass
            evideo = os.system(f"yt-dlp {v} -o evideo.mp4")
            eaudio = os.system(f"yt-dlp {a} -o eaudio.mp4")
            return 'OK'
        except Exception as e:
            return

async def decr(keys):
    try:
        try:
            working_dir = os.getcwd() + "\working_dir"
            os.chdir(working_dir)
        except:
            pass
        os.system(f"mp4decrypt --key {keys} evideo.mp4 dvideo.mp4")
        os.system(f"mp4decrypt --key {keys} eaudio.mp4 daudio.mp4")
        os.system("ffmpeg -y -i daudio.mp4 -i dvideo.mp4 -acodec copy -vcodec copy -fflags +bitexact final.mp4")
        return "OK"
    except:
        return