#!/usr/bin/env python
import argparse
import os
import sys
import logging
from datetime import time
from django.conf import settings
from moviepy.editor import *

sys.path.append("../")
from videoupload.models import VideoFragment

def process_videos(vid_out, text_out):
    vtt = open(text_out, "w")
    vtt.write("WEBVTT\n\n")

    clips = []
    starts = VideoFragment.objects.filter(prev_video=None)
    if len(starts) > 1:
        raise Exception("There shouldn't be more than 1 video with a null \
                        prev_video")

    start = starts.get()
    timestamp = 0.0

    while True:
        logging.debug("Cating file %s", os.path.join(settings.MEDIA_ROOT,
                                                start.vidfile.name))
        clip = VideoFileClip(os.path.join(settings.MEDIA_ROOT,
                                                start.vidfile.name))
        clips.append(clip)

        vtt.write("%02d:%06.3f --> %02d:%06.3f\n" % (timestamp / 60,
                                                   timestamp % 60,
                                                   (timestamp + clip.duration) / 60,
                                                   (timestamp + clip.duration) % 60))
        vtt.write("%s|%s\n\n" % (start.id, start.link))


        timestamp += clip.duration
        start = start.next_video
        if not start:
            break

    vtt.close()

    output = concatenate(clips).fx(vfx.resize, width=800, height=600)
    output.write_videofile(vid_out)



def main():
    parser = argparse.ArgumentParser(description="Convert the video fragments \
                                     into the final video. Also output the vtt \
                                     file while we're at it")
    parser.add_argument('-d', '--debug', help="Turn debug on",
                        action='store_true')
    parser.add_argument('-vo', '--video-output',
                        help="Where to output the video",
                        required=True, dest="vo")
    parser.add_argument('-to', '--text-output',
                        help="Where to output the vtt file",
                        required=True, dest="to")
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    process_videos(args.vo, args.to)


if __name__ == "__main__":
    main()
